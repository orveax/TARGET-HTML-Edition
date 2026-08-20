#!/usr/bin/env python3
"""ORIGEX PG30 Privacy QA V2 — legal-demo/source/rendered/accessibility gate."""
from pathlib import Path
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import json
import re
import subprocess
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

R = Path(__file__).resolve().parents[2]
O = R / "qa/pg30-privacy"
O.mkdir(parents=True, exist_ok=True)
SECTIONS = ["information-collected", "use", "cookies", "third-parties", "retention", "rights", "contact", "update-date"]


def source_qa():
    report = {"failures": [], "pages": {}, "css": {"failures": []}}
    css = (R / "assets/css/origex-legal.css").read_text(encoding="utf-8")
    for marker in (".orx-legal-shell", ".orx-legal-toc", "position: sticky", "max-width: 991.98px", "max-width: 767.98px"):
        if marker not in css:
            report["css"]["failures"].append("missing:" + marker)
    report["failures"].extend(report["css"]["failures"])

    sprite = (R / "assets/icons/sprite.svg").read_text(encoding="utf-8")
    sprite_ids = set(re.findall(r'<symbol[^>]+id="([^"]+)"', sprite))
    specs = {
        "ar": {
            "dir": "rtl",
            "h1": "سياسة الخصوصية — نموذج توضيحي قابل للتخصيص.",
            "intro": "هذا نص نموذجي يوضح هيكل صفحة سياسة الخصوصية داخل القالب. يجب مراجعته وتعديله بواسطة صاحب الموقع أو مستشاره القانوني وفقًا لطريقة جمع البيانات والقوانين المطبقة قبل النشر.",
            "updated": "يُستبدل قبل النشر",
            "other": "../en/privacy.html",
        },
        "en": {
            "dir": "ltr",
            "h1": "Privacy policy — a customization-ready Demo structure.",
            "intro": "Sample privacy structure only; buyer/legal adviser must adapt to actual data practices and applicable law.",
            "updated": "Replace before production",
            "other": "../ar/privacy.html",
        },
    }

    for lang, spec in specs.items():
        text = (R / lang / "privacy.html").read_text(encoding="utf-8")
        soup = BeautifulSoup(text, "html.parser")
        failures = []
        if soup.html.get("lang") != lang or soup.html.get("dir") != spec["dir"]: failures.append("lang-dir")
        h1s = soup.find_all("h1")
        if len(h1s) != 1 or h1s[0].get_text(" ", strip=True) != spec["h1"]: failures.append("h1")
        if spec["intro"] not in text: failures.append("canonical-intro")

        robots = soup.find("meta", attrs={"name": "robots"})
        if not robots or robots.get("content", "").replace(" ", "").lower() != "noindex,follow": failures.append("robots")
        if soup.find("link", rel="canonical"): failures.append("canonical-present")
        if soup.find("link", rel="alternate"): failures.append("hreflang-present")
        if soup.find("script", attrs={"type": "application/ld+json"}): failures.append("structured-data-present")
        for prop in ("og:type", "og:title", "og:description", "og:image"):
            if not soup.find("meta", attrs={"property": prop}): failures.append("missing-" + prop)

        toc = soup.select_one(".orx-legal-toc")
        toc_links = [a.get("href") for a in toc.select("a[href^='#']")] if toc else []
        if toc_links != ["#" + s for s in SECTIONS]: failures.append("toc-order")
        for sid in SECTIONS:
            section = soup.find("section", id=sid)
            if not section: failures.append("section:" + sid); continue
            heading = section.find(["h2", "h3"])
            if not heading or not heading.get("id"): failures.append("section-heading:" + sid)

        updated = soup.select_one("[data-pg30-updated]")
        if not updated or updated.get_text(" ", strip=True) != spec["updated"]: failures.append("updated-placeholder")
        if re.search(r"\b20\d{2}[-/]\d{1,2}[-/]\d{1,2}\b", text): failures.append("fabricated-policy-date")
        if not soup.select_one('[data-orx-email="trade"][href^="mailto:"]'): failures.append("contact-config")
        if not soup.select_one('a[href="contact.html"]'): failures.append("contact-route")

        lowered = text.lower()
        for banned in ("gdpr", "ccpa", "qatar pdpl", "saudi pdpl", "uae pdpl"):
            if banned in lowered: failures.append("named-law:" + banned)
        for marker in ("data-cookie-consent", "localstorage", "sessionstorage"):
            if marker in lowered: failures.append("fake-consent-tech:" + marker)
        if "cookie consent banner" not in text and "Cookie Consent Banner" not in text:
            # The page must explicitly explain why a banner is not assumed.
            failures.append("cookie-boundary-copy")

        if not soup.select_one('[data-orx-mega-trigger][aria-current="page"]'): failures.append("explore-current")
        if soup.select_one('.orx-mega-menu [aria-current="page"]'): failures.append("mega-child-current")
        if soup.select_one('.orx-mobile-nav [aria-current="page"]'): failures.append("mobile-child-current")
        if not soup.find("a", class_="orx-lang-switch", href=spec["other"]): failures.append("language-switch-source")
        if len(soup.select('footer[data-orx-global-footer="v1"]')) != 1: failures.append("footer")
        if soup.find("script", src="../assets/js/origex-privacy.js"): failures.append("unnecessary-page-js")
        if "TARGET" in text or "targetft" in lowered: failures.append("client-leak")

        icons = set(re.findall(r"sprite\.svg#([a-z0-9-]+)", text))
        missing = sorted(icons - sprite_ids)
        if missing: failures.append("icons:" + str(missing))
        report["pages"][lang] = {"failures": failures, "sections": len([s for s in SECTIONS if soup.find("section", id=s)]), "tocLinks": len(toc_links), "iconCount": len(icons)}
        report["failures"].extend([lang + ":" + f for f in failures])

    for script, label in ((".github/scripts/normalize_global_navigation.py", "nav-drift"), (".github/scripts/normalize_global_footer.py", "footer-drift")):
        run = subprocess.run(["python", script, "--check"], cwd=R, capture_output=True, text=True)
        if run.returncode:
            report["failures"].append(label)
            report[label] = run.stdout + run.stderr

    (O / "source-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def rendered_qa():
    report = {"failures": [], "cases": [], "interaction": {}}
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=820,1900")
    server = subprocess.Popen(["python", "-m", "http.server", "8767"], cwd=R, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    try:
        for lang in ("ar", "en"):
            driver = webdriver.Chrome(options=options)
            try:
                for width in (390, 820, 1366, 1536):
                    failures = []
                    try:
                        driver.set_window_size(width, 1900)
                        driver.get(f"http://127.0.0.1:8767/{lang}/privacy.html")
                        time.sleep(.15)
                        if driver.find_element(By.TAG_NAME, "html").get_attribute("dir") != ("rtl" if lang == "ar" else "ltr"): failures.append("direction")
                        if driver.execute_script("return document.documentElement.scrollWidth") > driver.execute_script("return document.documentElement.clientWidth") + 1: failures.append("overflow")
                        if len(driver.find_elements(By.TAG_NAME, "h1")) != 1: failures.append("h1-count")
                        if not driver.find_element(By.CSS_SELECTOR, ".orx-legal-disclaimer").is_displayed(): failures.append("disclaimer")
                        toc = driver.find_element(By.CSS_SELECTOR, ".orx-legal-toc")
                        if not toc.is_displayed(): failures.append("toc-hidden")
                        position = driver.execute_script("return getComputedStyle(arguments[0]).position", toc)
                        if width >= 992 and position != "sticky": failures.append("toc-not-sticky")
                        if width < 992 and position != "static": failures.append("toc-not-static")
                        if len(driver.find_elements(By.CSS_SELECTOR, ".orx-legal-section")) != 8: failures.append("section-count")
                        if driver.find_element(By.CSS_SELECTOR, '[data-pg30-updated]').text.strip() not in ("Replace before production", "يُستبدل قبل النشر"): failures.append("updated")
                        if driver.find_element(By.CSS_SELECTOR, '[data-orx-email="trade"]').get_attribute("href") != "mailto:trade@example.com": failures.append("contact-config")

                        # Touch-target QA applies to controls and navigation targets, not normal inline prose links.
                        controls = "button,.orx-btn,.orx-lang-switch,.orx-legal-toc a,[data-orx-drawer-open],[data-orx-drawer-close]"
                        small = []
                        for el in driver.find_elements(By.CSS_SELECTOR, controls):
                            if el.is_displayed() and el.rect["width"] and el.rect["height"] and (el.rect["width"] < 24 or el.rect["height"] < 24):
                                small.append({"tag": el.tag_name, "w": round(el.rect["width"], 1), "h": round(el.rect["height"], 1), "text": el.text[:20]})
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
                        failures.append(type(exc).__name__ + ":" + str(exc)[:220])
                    report["cases"].append({"lang": lang, "width": width, "failures": failures})
                    report["failures"].extend([f"{lang}-{width}:{f}" for f in failures])

                failures = []
                try:
                    driver.set_window_size(1366, 1900)
                    driver.get(f"http://127.0.0.1:8767/{lang}/privacy.html")
                    time.sleep(.1)
                    first = driver.find_element(By.CSS_SELECTOR, '.orx-legal-toc a[href="#information-collected"]')
                    driver.execute_script("arguments[0].click()", first); time.sleep(.08)
                    if driver.execute_script("return location.hash") != "#information-collected": failures.append("toc-hash")
                    switch_href = driver.find_element(By.CSS_SELECTOR, ".orx-lang-switch").get_attribute("href")
                    expected_path = "/en/privacy.html" if lang == "ar" else "/ar/privacy.html"
                    if not urlparse(switch_href).path.endswith(expected_path): failures.append("language-switch")
                except Exception as exc:
                    failures.append(type(exc).__name__ + ":" + str(exc)[:220])
                report["interaction"][lang + "-toc-language"] = failures
                report["failures"].extend([lang + "-toc-language:" + f for f in failures])
            finally:
                driver.quit()
    finally:
        server.terminate()
        try: server.wait(timeout=2)
        except Exception: server.kill()

    (O / "rendered-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def main():
    source = source_qa()
    rendered = rendered_qa()
    failures = source["failures"] + rendered["failures"]
    (O / "run-status.txt").write_text(("PASS" if not failures else "FAIL") + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS" if not failures else "FAIL", "failures": failures}, ensure_ascii=False, indent=2))
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
