#!/usr/bin/env python3
"""ORIGEX PG29 Coming Soon QA — source, noindex, config, countdown, subscribe, social, rendered and interaction gate."""
from pathlib import Path
from bs4 import BeautifulSoup
import json
import re
import subprocess
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

R = Path(__file__).resolve().parents[2]
O = R / "qa/pg29-coming-soon"
O.mkdir(parents=True, exist_ok=True)


def source_qa():
    report = {"failures": [], "pages": {}, "runtime": {}, "config": {}}
    runtime = (R / "assets/js/origex-coming-soon.js").read_text(encoding="utf-8")
    config_text = (R / "assets/js/config.js").read_text(encoding="utf-8")

    runtime_failures = []
    for bad in ("fetch(", "XMLHttpRequest", "localStorage", "sessionStorage"):
        if bad in runtime:
            runtime_failures.append("forbidden-runtime:" + bad)
    for required in (
        "data-pg29-root", "data-pg29-countdown", "data-pg29-date-empty", "data-pg29-form",
        "data-pg29-social", "data-pg29-email", "pg29Ready", "ORIGEXComingSoon", "launchDate"
    ):
        if required not in runtime:
            runtime_failures.append("runtime-missing:" + required)
    report["runtime"] = {"failures": runtime_failures}
    report["failures"] += runtime_failures

    config_failures = []
    if "comingSoon" not in config_text or "launchDate" not in config_text:
        config_failures.append("coming-soon-config")
    if not re.search(r'launchDate:\s*""', config_text):
        config_failures.append("default-launch-date-not-empty")
    report["config"] = {"failures": config_failures}
    report["failures"] += config_failures

    sprite = (R / "assets/icons/sprite.svg").read_text(encoding="utf-8")
    sprite_ids = set(re.findall(r'<symbol[^>]+id="([^"]+)"', sprite))

    specs = {
        "ar": {
            "dir": "rtl",
            "h1": "نجهز هذه الصفحة بمعلوماتها التجارية الكاملة.",
            "support": "استخدم بيانات التواصل الحالية إذا كان لديك طلب عاجل، أو عد لاحقًا بعد اكتمال التحديث.",
            "cta": "تواصل معنا",
            "other": "../en/coming-soon.html",
        },
        "en": {
            "dir": "ltr",
            "h1": "We’re preparing this page with its complete commercial information.",
            "other": "../ar/coming-soon.html",
        },
    }

    for lang, spec in specs.items():
        path = R / lang / "coming-soon.html"
        text = path.read_text(encoding="utf-8")
        soup = BeautifulSoup(text, "html.parser")
        failures = []

        if soup.html.get("lang") != lang or soup.html.get("dir") != spec["dir"]:
            failures.append("lang-dir")
        h1s = soup.find_all("h1")
        if len(h1s) != 1 or h1s[0].get_text(" ", strip=True) != spec["h1"]:
            failures.append("h1")
        if lang == "ar":
            if spec["support"] not in text: failures.append("canonical-support")
            hero = soup.select_one(".orx-coming-hero")
            if not hero or spec["cta"] not in hero.get_text(" ", strip=True): failures.append("canonical-cta")

        robots = soup.find("meta", attrs={"name": "robots"})
        if not robots or robots.get("content", "").replace(" ", "").lower() != "noindex,follow":
            failures.append("robots-noindex")
        if soup.find("link", rel="canonical"): failures.append("unexpected-canonical")
        if soup.find("link", rel="alternate"): failures.append("unexpected-hreflang")
        if soup.find("script", attrs={"type": "application/ld+json"}): failures.append("unexpected-structured-data")
        for prop in ("og:type", "og:title", "og:description", "og:url", "og:image"):
            if not soup.find("meta", attrs={"property": prop}): failures.append("missing-" + prop)

        if not soup.select_one("[data-pg29-date-empty]"): failures.append("date-empty")
        if not soup.select_one("[data-pg29-countdown][hidden]"): failures.append("default-countdown-hidden")
        if len(soup.select("[data-pg29-days],[data-pg29-hours],[data-pg29-minutes],[data-pg29-seconds]")) != 4:
            failures.append("countdown-units")
        form = soup.select_one("form[data-pg29-form]")
        if not form: failures.append("subscribe-form")
        else:
            if form.get("action"): failures.append("form-action")
            email = form.select_one('input[type="email"][required]')
            if not email: failures.append("email-field")
            if not form.select_one("[data-pg29-form-error][hidden]"): failures.append("form-error")
            if not form.select_one("[data-pg29-form-success][hidden]"): failures.append("form-success")

        social = soup.select_one("[data-pg29-social][hidden]")
        if not social: failures.append("social-default-hidden")
        if len(soup.select("[data-pg29-social-link]")) != 6: failures.append("social-link-count")
        if not soup.select_one('a[href="contact.html"]'): failures.append("contact-link")
        if not soup.select_one("[data-pg29-email]"): failures.append("email-fallback")
        if not soup.select_one('[data-orx-mega-trigger][aria-current="page"]'): failures.append("explore-current")
        if soup.select_one('.orx-mega-menu [aria-current="page"]'): failures.append("unexpected-mega-current")
        if soup.select_one('.orx-mobile-nav [aria-current="page"]'): failures.append("unexpected-mobile-current")
        if not soup.find("a", class_="orx-lang-switch", href=lambda x: x and spec["other"] in x): failures.append("language-switch")
        if len(soup.select('footer[data-orx-global-footer="v1"]')) != 1: failures.append("footer")
        if "TARGET" in text or "targetft" in text.lower(): failures.append("client-leak")

        scripts = [s.get("src", "") for s in soup.find_all("script") if s.get("src")]
        if not scripts or scripts[-1] != "../assets/js/origex-coming-soon.js": failures.append("runtime-order")

        icons = set(re.findall(r"sprite\.svg#([a-z0-9-]+)", text))
        missing = sorted(icons - sprite_ids)
        if missing: failures.append("icons:" + str(missing))

        report["pages"][lang] = {"failures": failures, "iconCount": len(icons)}
        report["failures"] += [lang + ":" + failure for failure in failures]

    for script, label in [
        (".github/scripts/normalize_global_navigation.py", "nav-drift"),
        (".github/scripts/normalize_global_footer.py", "footer-drift"),
    ]:
        run = subprocess.run(["python", script, "--check"], cwd=R, capture_output=True, text=True)
        if run.returncode:
            report["failures"].append(label)
            report[label] = run.stdout + run.stderr

    (O / "source-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def wait_ready(driver):
    WebDriverWait(driver, 8).until(
        lambda current: current.find_element(By.CSS_SELECTOR, "[data-pg29-root]").get_attribute("data-pg29-ready") == "true"
    )


def rendered_qa():
    report = {"failures": [], "cases": [], "interaction": {}}
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=820,1900")

    server = subprocess.Popen(["python", "-m", "http.server", "8766"], cwd=R, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)

    try:
        for lang in ("ar", "en"):
            driver = webdriver.Chrome(options=options)
            try:
                for width in (390, 820, 1366, 1536):
                    failures = []
                    try:
                        driver.set_window_size(width, 1900)
                        driver.get(f"http://127.0.0.1:8766/{lang}/coming-soon.html")
                        wait_ready(driver)
                        root = driver.find_element(By.CSS_SELECTOR, "[data-pg29-root]")
                        if root.get_attribute("data-pg29-launch-state") != "not-configured": failures.append("default-launch-state")
                        if driver.find_element(By.CSS_SELECTOR, "[data-pg29-countdown]").is_displayed(): failures.append("default-countdown-visible")
                        if not driver.find_element(By.CSS_SELECTOR, "[data-pg29-date-empty]").is_displayed(): failures.append("default-date-empty-hidden")
                        if driver.find_element(By.CSS_SELECTOR, "[data-pg29-social]").is_displayed(): failures.append("default-social-visible")
                        if driver.execute_script("return document.documentElement.scrollWidth") > driver.execute_script("return document.documentElement.clientWidth") + 1:
                            failures.append("overflow")
                        if driver.find_element(By.TAG_NAME, "html").get_attribute("dir") != ("rtl" if lang == "ar" else "ltr"): failures.append("direction")
                        if driver.find_element(By.CSS_SELECTOR, 'meta[name="robots"]').get_attribute("content").replace(" ", "").lower() != "noindex,follow": failures.append("robots")

                        small = []
                        for element in driver.find_elements(By.CSS_SELECTOR, "a,button,input"):
                            if element.is_displayed() and element.rect["width"] and element.rect["height"] and (element.rect["width"] < 24 or element.rect["height"] < 24):
                                small.append({"tag": element.tag_name, "w": round(element.rect["width"],1), "h": round(element.rect["height"],1), "text": element.text[:20]})
                        if small: failures.append("touch:" + json.dumps(small, ensure_ascii=False))

                        if width >= 1051:
                            trigger = driver.find_element(By.CSS_SELECTOR, "[data-orx-mega-trigger]")
                            trigger.click(); time.sleep(.04)
                            if trigger.get_attribute("aria-expanded") != "true": failures.append("mega-open")
                            trigger.send_keys(Keys.ESCAPE); time.sleep(.04)
                            if trigger.get_attribute("aria-expanded") != "false": failures.append("mega-escape")
                        else:
                            opener = driver.find_element(By.CSS_SELECTOR, "[data-orx-drawer-open]")
                            opener.click(); time.sleep(.04)
                            drawer = driver.find_element(By.CSS_SELECTOR, "[data-orx-mobile-drawer]")
                            if drawer.get_attribute("aria-hidden") != "false": failures.append("drawer-open")
                            driver.find_element(By.CSS_SELECTOR, "[data-orx-drawer-close]").click(); time.sleep(.04)
                            if drawer.get_attribute("aria-hidden") != "true": failures.append("drawer-close")
                    except Exception as exc:
                        failures.append(type(exc).__name__ + ":" + str(exc)[:240])
                    report["cases"].append({"lang": lang, "width": width, "failures": failures})
                    report["failures"] += [f"{lang}-{width}:{failure}" for failure in failures]

                # Future countdown + past fallback.
                failures = []
                try:
                    driver.get(f"http://127.0.0.1:8766/{lang}/coming-soon.html")
                    wait_ready(driver)
                    root = driver.find_element(By.CSS_SELECTOR, "[data-pg29-root]")
                    driver.execute_script("window.ORIGEX_CONFIG.comingSoon.launchDate = new Date(Date.now()+172800000).toISOString(); window.ORIGEXComingSoon.refresh();")
                    time.sleep(.08)
                    if root.get_attribute("data-pg29-launch-state") != "future": failures.append("future-state")
                    if not driver.find_element(By.CSS_SELECTOR, "[data-pg29-countdown]").is_displayed(): failures.append("future-countdown")
                    if driver.find_element(By.CSS_SELECTOR, "[data-pg29-date-value]").text.strip() == "": failures.append("future-date-label")
                    values = [driver.find_element(By.CSS_SELECTOR, selector).text for selector in ("[data-pg29-days]","[data-pg29-hours]","[data-pg29-minutes]","[data-pg29-seconds]")]
                    if any(not re.fullmatch(r"\d+", value) for value in values): failures.append("future-values")
                    driver.execute_script("window.ORIGEX_CONFIG.comingSoon.launchDate = new Date(Date.now()-60000).toISOString(); window.ORIGEXComingSoon.refresh();")
                    time.sleep(.08)
                    if root.get_attribute("data-pg29-launch-state") != "past": failures.append("past-state")
                    if driver.find_element(By.CSS_SELECTOR, "[data-pg29-countdown]").is_displayed(): failures.append("past-countdown")
                    if not driver.find_element(By.CSS_SELECTOR, "[data-pg29-date-empty]").is_displayed(): failures.append("past-empty")
                except Exception as exc:
                    failures.append(type(exc).__name__ + ":" + str(exc)[:240])
                report["interaction"][lang + "-countdown"] = failures
                report["failures"] += [lang + "-countdown:" + failure for failure in failures]

                # Subscribe validation + reset.
                failures = []
                try:
                    driver.get(f"http://127.0.0.1:8766/{lang}/coming-soon.html")
                    wait_ready(driver)
                    root = driver.find_element(By.CSS_SELECTOR, "[data-pg29-root]")
                    email = driver.find_element(By.CSS_SELECTOR, '[data-pg29-form] input[type="email"]')
                    submit = driver.find_element(By.CSS_SELECTOR, '[data-pg29-form] button[type="submit"]')
                    email.send_keys("not-an-email"); submit.click(); time.sleep(.05)
                    if root.get_attribute("data-pg29-form-state") != "error": failures.append("invalid-state")
                    if not driver.find_element(By.CSS_SELECTOR, "[data-pg29-form-error]").is_displayed(): failures.append("invalid-error")
                    email.clear(); email.send_keys("buyer@example.com"); submit.click(); time.sleep(.05)
                    if root.get_attribute("data-pg29-form-state") != "validated": failures.append("valid-state")
                    if not driver.find_element(By.CSS_SELECTOR, "[data-pg29-form-success]").is_displayed(): failures.append("valid-success")
                    driver.find_element(By.CSS_SELECTOR, '[data-pg29-form] button[type="reset"]').click(); time.sleep(.08)
                    if root.get_attribute("data-pg29-form-state") != "idle": failures.append("reset-state")
                    if email.get_attribute("value") != "": failures.append("reset-email")
                except Exception as exc:
                    failures.append(type(exc).__name__ + ":" + str(exc)[:240])
                report["interaction"][lang + "-subscribe"] = failures
                report["failures"] += [lang + "-subscribe:" + failure for failure in failures]

                # Social config visibility.
                failures = []
                try:
                    driver.get(f"http://127.0.0.1:8766/{lang}/coming-soon.html")
                    wait_ready(driver)
                    root = driver.find_element(By.CSS_SELECTOR, "[data-pg29-root]")
                    driver.execute_script("window.ORIGEX_CONFIG.social.linkedin='https://example.com/company'; window.ORIGEXComingSoon.refresh();")
                    time.sleep(.05)
                    if root.get_attribute("data-pg29-social-count") != "1": failures.append("social-count")
                    wrap = driver.find_element(By.CSS_SELECTOR, "[data-pg29-social]")
                    if not wrap.is_displayed(): failures.append("social-wrap")
                    link = driver.find_element(By.CSS_SELECTOR, '[data-pg29-social-link="linkedin"]')
                    if not link.is_displayed() or not link.get_attribute("href").startswith("https://example.com/company"): failures.append("social-link")
                    driver.execute_script("window.ORIGEX_CONFIG.social.linkedin='#'; window.ORIGEXComingSoon.refresh();")
                    time.sleep(.05)
                    if wrap.is_displayed(): failures.append("social-placeholder-hide")
                except Exception as exc:
                    failures.append(type(exc).__name__ + ":" + str(exc)[:240])
                report["interaction"][lang + "-social"] = failures
                report["failures"] += [lang + "-social:" + failure for failure in failures]
            finally:
                driver.quit()
    finally:
        server.terminate(); server.wait(timeout=5)

    (O / "rendered-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def main():
    source = source_qa()
    rendered = rendered_qa()
    failures = source["failures"] + rendered["failures"]
    status = "PASS" if not failures else "FAIL"
    (O / "run-status.txt").write_text(status + "\n", encoding="utf-8")
    print(status, "source", len(source["failures"]), "rendered", len(rendered["failures"]))
    if failures:
        print("\n".join(failures))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
