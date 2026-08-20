#!/usr/bin/env python3
"""ORIGEX PG28 404 QA — source, SEO, recovery-route, rendered and interaction gate."""
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
O = R / "qa/pg28-404"
O.mkdir(parents=True, exist_ok=True)

EXPECTED_ROUTES = ["index.html", "products.html", "suppliers.html", "resources.html", "faq.html", "contact.html"]


def source_qa():
    report = {"failures": [], "pages": {}, "runtime": {}}

    runtime = (R / "assets/js/origex-404.js").read_text(encoding="utf-8")
    runtime_failures = []
    for bad in ("fetch(", "XMLHttpRequest", "localStorage", "sessionStorage"):
        if bad in runtime:
            runtime_failures.append("forbidden-runtime:" + bad)
    for required in (
        "data-pg28-root", "data-pg28-search", "data-pg28-recovery-card", "data-pg28-count",
        "data-pg28-empty", "data-pg28-reset", "history.replaceState", "orx-lang-switch",
        "orx-mobile-nav a[lang]", "data-pg28-ready",
    ):
        if required not in runtime:
            runtime_failures.append("runtime-missing:" + required)
    report["runtime"] = {"failures": runtime_failures}
    report["failures"] += runtime_failures

    sprite = (R / "assets/icons/sprite.svg").read_text(encoding="utf-8")
    sprite_ids = set(re.findall(r'<symbol[^>]+id="([^"]+)"', sprite))

    specs = {
        "ar": {
            "dir": "rtl",
            "h1": "الصفحة غير موجودة، لكن المسار واضح.",
            "support": "ربما تغير الرابط أو تم نقله. ارجع إلى المنتجات أو الموردين أو تواصل معنا للوصول للمعلومة المطلوبة.",
            "cta_home": "العودة للرئيسية",
            "cta_products": "استعرض المنتجات",
            "other": "../en/404.html",
        },
        "en": {
            "dir": "ltr",
            "h1": "This page is unavailable, but the route is clear.",
            "cta_home": "Back to Home",
            "cta_products": "Explore Products",
            "other": "../ar/404.html",
        },
    }

    for lang, spec in specs.items():
        path = R / lang / "404.html"
        text = path.read_text(encoding="utf-8")
        soup = BeautifulSoup(text, "html.parser")
        failures = []

        if soup.html.get("lang") != lang or soup.html.get("dir") != spec["dir"]:
            failures.append("lang-dir")
        h1s = soup.find_all("h1")
        if len(h1s) != 1 or h1s[0].get_text(" ", strip=True) != spec["h1"]:
            failures.append("h1")
        if lang == "ar" and spec["support"] not in text:
            failures.append("canonical-support")

        hero = soup.select_one(".orx-error-hero")
        if not hero:
            failures.append("hero")
        else:
            hero_text = hero.get_text(" ", strip=True)
            if spec["cta_home"] not in hero_text:
                failures.append("home-cta")
            if spec["cta_products"] not in hero_text:
                failures.append("products-cta")

        robots = soup.find("meta", attrs={"name": "robots"})
        if not robots or robots.get("content", "").replace(" ", "").lower() != "noindex,follow":
            failures.append("robots-noindex")
        if soup.find("link", rel="canonical"):
            failures.append("unexpected-canonical")
        if soup.find("link", rel="alternate"):
            failures.append("unexpected-hreflang")
        if soup.find("script", attrs={"type": "application/ld+json"}):
            failures.append("unexpected-structured-data")
        for prop in ("og:type", "og:title", "og:description", "og:url", "og:image"):
            if not soup.find("meta", attrs={"property": prop}):
                failures.append("missing-" + prop)

        cards = soup.select("[data-pg28-recovery-card]")
        hrefs = [c.select_one("a[href]").get("href") if c.select_one("a[href]") else "" for c in cards]
        if len(cards) != 6:
            failures.append("recovery-count:" + str(len(cards)))
        if hrefs != EXPECTED_ROUTES:
            failures.append("recovery-order:" + str(hrefs))
        if any(c.has_attr("hidden") for c in cards):
            failures.append("progressive-enhancement-hidden-card")
        for href in hrefs:
            if href and not (R / lang / href).exists():
                failures.append("missing-recovery-target:" + href)

        if not soup.select_one("[data-pg28-search]"):
            failures.append("search-field")
        if not soup.select_one('[data-pg28-count][aria-live="polite"]'):
            failures.append("result-count-live")
        if not soup.select_one('[data-pg28-empty][role="status"][hidden]'):
            failures.append("empty-state")
        if len(soup.select("[data-pg28-reset]")) < 2:
            failures.append("reset-controls")
        empty = soup.select_one("[data-pg28-empty]")
        if not empty or not empty.select_one('a[href="contact.html"]'):
            failures.append("contact-fallback")

        if not soup.select_one('[data-orx-mega-trigger][aria-current="page"]'):
            failures.append("explore-current")
        if soup.select_one('.orx-mega-menu [aria-current="page"]'):
            failures.append("unexpected-mega-current")
        if soup.select_one('.orx-mobile-nav [aria-current="page"]'):
            failures.append("unexpected-mobile-current")
        lang_switch = soup.find("a", class_="orx-lang-switch", href=lambda x: x and spec["other"] in x)
        if not lang_switch:
            failures.append("language-switch")

        footer = soup.select('footer[data-orx-global-footer="v1"]')
        if len(footer) != 1:
            failures.append("footer")
        if soup.find("form"):
            failures.append("unexpected-form")
        if soup.find("iframe"):
            failures.append("unexpected-iframe")
        if "maps.googleapis.com" in text or "mapbox" in text.lower():
            failures.append("unexpected-map-provider")
        if "HTTP 404" not in text:
            failures.append("deployment-status-note")
        if "TARGET" in text or "targetft" in text.lower():
            failures.append("client-leak")

        scripts = [s.get("src", "") for s in soup.find_all("script") if s.get("src")]
        if not scripts or scripts[-1] != "../assets/js/origex-404.js":
            failures.append("runtime-order")

        icons = set(re.findall(r"sprite\.svg#([a-z0-9-]+)", text))
        missing = sorted(icons - sprite_ids)
        if missing:
            failures.append("icons:" + str(missing))

        report["pages"][lang] = {"failures": failures, "recoveryRoutes": hrefs, "iconCount": len(icons)}
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
        lambda current: current.find_element(By.CSS_SELECTOR, "[data-pg28-root]").get_attribute("data-pg28-ready") == "true"
    )


def rendered_qa():
    report = {"failures": [], "cases": [], "interaction": {}}
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=820,1900")

    server = subprocess.Popen(
        ["python", "-m", "http.server", "8765"],
        cwd=R,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(1)

    try:
        for lang in ("ar", "en"):
            driver = webdriver.Chrome(options=options)
            try:
                for width in (390, 820, 1366, 1536):
                    failures = []
                    try:
                        driver.set_window_size(width, 1900)
                        driver.get(f"http://127.0.0.1:8765/{lang}/404.html")
                        wait_ready(driver)
                        root = driver.find_element(By.CSS_SELECTOR, "[data-pg28-root]")
                        if root.get_attribute("data-pg28-result-count") != "6":
                            failures.append("initial-count")
                        if len([c for c in driver.find_elements(By.CSS_SELECTOR, "[data-pg28-recovery-card]") if c.is_displayed()]) != 6:
                            failures.append("initial-cards")
                        if driver.execute_script("return document.documentElement.scrollWidth") > driver.execute_script("return document.documentElement.clientWidth") + 1:
                            failures.append("overflow")
                        if driver.find_element(By.TAG_NAME, "html").get_attribute("dir") != ("rtl" if lang == "ar" else "ltr"):
                            failures.append("direction")
                        if driver.find_element(By.CSS_SELECTOR, 'meta[name="robots"]').get_attribute("content").replace(" ", "").lower() != "noindex,follow":
                            failures.append("robots")

                        small = []
                        for element in driver.find_elements(By.CSS_SELECTOR, "a,button,input"):
                            if element.is_displayed() and element.rect["width"] and element.rect["height"] and (
                                element.rect["width"] < 24 or element.rect["height"] < 24
                            ):
                                small.append({
                                    "tag": element.tag_name,
                                    "w": round(element.rect["width"], 1),
                                    "h": round(element.rect["height"], 1),
                                    "text": element.text[:20],
                                })
                        if small:
                            failures.append("touch:" + json.dumps(small, ensure_ascii=False))

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

                # Search + language preservation.
                failures = []
                try:
                    driver.get(f"http://127.0.0.1:8765/{lang}/404.html")
                    wait_ready(driver)
                    search = driver.find_element(By.CSS_SELECTOR, "[data-pg28-search]")
                    search.send_keys("مورد" if lang == "ar" else "supplier")
                    time.sleep(.1)
                    root = driver.find_element(By.CSS_SELECTOR, "[data-pg28-root]")
                    if root.get_attribute("data-pg28-result-count") != "1": failures.append("search-count")
                    visible = [c for c in driver.find_elements(By.CSS_SELECTOR, "[data-pg28-recovery-card]") if c.is_displayed()]
                    if len(visible) != 1 or "suppliers.html" not in visible[0].find_element(By.CSS_SELECTOR, "a[href]").get_attribute("href"):
                        failures.append("search-route")
                    if "?q=" not in driver.current_url:
                        failures.append("search-url")
                    language_links = driver.find_elements(By.CSS_SELECTOR, ".orx-lang-switch,.orx-mobile-nav a[lang]")
                    if len(language_links) < 2 or any("?q=" not in link.get_attribute("href") for link in language_links):
                        failures.append("language-query")
                except Exception as exc:
                    failures.append(type(exc).__name__ + ":" + str(exc)[:240])
                report["interaction"][lang + "-search"] = failures
                report["failures"] += [lang + "-search:" + failure for failure in failures]

                # Empty + keyboard reset.
                failures = []
                try:
                    driver.get(f"http://127.0.0.1:8765/{lang}/404.html")
                    wait_ready(driver)
                    search = driver.find_element(By.CSS_SELECTOR, "[data-pg28-search]")
                    search.send_keys("zzzz-no-route")
                    time.sleep(.08)
                    root = driver.find_element(By.CSS_SELECTOR, "[data-pg28-root]")
                    if root.get_attribute("data-pg28-result-count") != "0": failures.append("empty-count")
                    if not driver.find_element(By.CSS_SELECTOR, "[data-pg28-empty]").is_displayed(): failures.append("empty-visible")
                    reset = driver.find_element(By.CSS_SELECTOR, "[data-pg28-empty] [data-pg28-reset]")
                    reset.send_keys(Keys.ENTER); time.sleep(.08)
                    if root.get_attribute("data-pg28-result-count") != "6": failures.append("reset-count")
                    if search.get_attribute("value") != "": failures.append("reset-query")
                    if driver.find_element(By.CSS_SELECTOR, "[data-pg28-empty]").is_displayed(): failures.append("reset-empty")
                except Exception as exc:
                    failures.append(type(exc).__name__ + ":" + str(exc)[:240])
                report["interaction"][lang + "-empty-reset"] = failures
                report["failures"] += [lang + "-empty-reset:" + failure for failure in failures]

                # Query hydration + Escape clear.
                failures = []
                try:
                    driver.get(f"http://127.0.0.1:8765/{lang}/404.html?q=supplier")
                    wait_ready(driver)
                    root = driver.find_element(By.CSS_SELECTOR, "[data-pg28-root]")
                    search = driver.find_element(By.CSS_SELECTOR, "[data-pg28-search]")
                    if search.get_attribute("value") != "supplier": failures.append("query-hydration")
                    if root.get_attribute("data-pg28-result-count") != "1": failures.append("query-count")
                    search.send_keys(Keys.ESCAPE); time.sleep(.08)
                    if search.get_attribute("value") != "": failures.append("escape-clear")
                    if root.get_attribute("data-pg28-result-count") != "6": failures.append("escape-count")
                    if "?q=" in driver.current_url: failures.append("escape-url")
                except Exception as exc:
                    failures.append(type(exc).__name__ + ":" + str(exc)[:240])
                report["interaction"][lang + "-query-escape"] = failures
                report["failures"] += [lang + "-query-escape:" + failure for failure in failures]
            finally:
                driver.quit()
    finally:
        server.terminate()
        server.wait(timeout=5)

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
