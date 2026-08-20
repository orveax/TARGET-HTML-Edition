#!/usr/bin/env python3
"""ORIGEX PG31 Terms QA — legal-demo, frozen-standards, source, rendered and accessibility gate."""
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
O = R / "qa/pg31-terms"
O.mkdir(parents=True, exist_ok=True)
SECTIONS = [
    "site-use", "information-accuracy", "enquiries", "intellectual-property",
    "external-links", "liability", "governing-law", "contact"
]


def source_qa():
    report = {"failures": [], "pages": {}, "css": {"failures": []}}
    css = (R / "assets/css/origex-legal.css").read_text(encoding="utf-8")
    css_required = (
        ".orx-legal-shell", ".orx-legal-toc", ".orx-legal-context-nav",
        ".orx-legal-table-wrap", ".orx-legal-table", "overflow-x: auto",
        "min-height: 48px", "position: sticky", "max-width: 991.98px",
        "max-width: 767.98px"
    )
    for marker in css_required:
        if marker not in css:
            report["css"]["failures"].append("missing:" + marker)
    report["failures"].extend(report["css"]["failures"])

    sprite = (R / "assets/icons/sprite.svg").read_text(encoding="utf-8")
    sprite_ids = set(re.findall(r'<symbol[^>]+id="([^"]+)"', sprite))
    specs = {
        "ar": {
            "dir": "rtl",
            "h1": "شروط الاستخدام — نموذج توضيحي قابل للتخصيص.",
            "intro": "هذه شروط نموذجية لأغراض تصميم القالب فقط ولا تمثل شروط استخدام جاهزة لأي نشاط تجاري. استبدلها بنص قانوني مناسب لنشاطك ودولتك قبل النشر.",
            "updated": "يُستبدل قبل النشر",
            "other": "../en/terms.html",
            "liability_boundary": "ORIGEX لا يضع حد مسؤولية افتراضيًا ولا استبعاد ضمان عامًا.",
            "law_boundary": "لا تنشر دولة أو ولاية أو محكمة أو جهة تحكيم أو آلية نزاع لمجرد أنها ظهرت في قالب عام.",
        },
        "en": {
            "dir": "ltr",
            "h1": "Terms of use — a customization-ready Demo structure.",
            "intro": "Sample terms for template demonstration only; not ready-to-publish legal terms.",
            "updated": "Replace before production",
            "other": "../ar/terms.html",
            "liability_boundary": "ORIGEX does not supply a default liability cap or universal warranty exclusion.",
            "law_boundary": "Do not publish a country, state, court, arbitration forum or dispute procedure simply because it appears in a generic template.",
        },
    }

    for lang, spec in specs.items():
        path = R / lang / "terms.html"
        text = path.read_text(encoding="utf-8")
        soup = BeautifulSoup(text, "html.parser")
        failures = []
        main = soup.find("main")
        main_text = main.get_text(" ", strip=True) if main else ""

        if soup.html.get("lang") != lang or soup.html.get("dir") != spec["dir"]:
            failures.append("lang-dir")
        h1s = soup.find_all("h1")
        if len(h1s) != 1 or h1s[0].get_text(" ", strip=True) != spec["h1"]:
            failures.append("h1")
        if spec["intro"] not in text:
            failures.append("canonical-intro")

        robots = soup.find("meta", attrs={"name": "robots"})
        if not robots or robots.get("content", "").replace(" ", "").lower() != "noindex,follow":
            failures.append("robots")
        if soup.find("link", rel="canonical"):
            failures.append("canonical-present")
        if soup.find("link", rel="alternate"):
            failures.append("hreflang-present")
        if soup.find("script", attrs={"type": "application/ld+json"}):
            failures.append("structured-data-present")
        for prop in ("og:type", "og:title", "og:description", "og:image"):
            if not soup.find("meta", attrs={"property": prop}):
                failures.append("missing-" + prop)

        toc = soup.select_one(".orx-legal-toc")
        toc_links = [a.get("href") for a in toc.select("a[href^='#']")] if toc else []
        if toc_links != ["#" + s for s in SECTIONS]:
            failures.append("toc-order")
        for index, sid in enumerate(SECTIONS, 1):
            section = soup.find("section", id=sid)
            if not section:
                failures.append("section:" + sid)
                continue
            heading = section.find(["h2", "h3"])
            if not heading or not heading.get("id"):
                failures.append("section-heading:" + sid)
            marker = section.select_one(".orx-legal-section__index")
            if not marker or marker.get_text(strip=True) != f"{index:02d}":
                failures.append("section-number:" + sid)

        context = soup.select_one(".orx-legal-context-nav")
        if not context:
            failures.append("context-nav")
        else:
            privacy = context.find("a", href="privacy.html")
            terms = context.find("a", href="terms.html")
            if not privacy:
                failures.append("context-privacy")
            if not terms or terms.get("aria-current") != "page":
                failures.append("context-terms-current")

        updated = soup.select_one("[data-pg31-updated]")
        if not updated or updated.get_text(" ", strip=True) != spec["updated"]:
            failures.append("updated-placeholder")
        if re.search(r"\b20\d{2}[-/]\d{1,2}[-/]\d{1,2}\b", main_text):
            failures.append("fabricated-effective-date")
        if not soup.select_one('[data-orx-email="trade"][href^="mailto:"]'):
            failures.append("contact-config")
        if not soup.select_one('a[href="contact.html"]'):
            failures.append("contact-route")
        if lang == "ar" and not soup.select_one('#contact bdi[dir="ltr"]'):
            failures.append("rtl-mixed-email")

        if spec["liability_boundary"] not in text:
            failures.append("liability-boundary")
        if spec["law_boundary"] not in text:
            failures.append("governing-law-boundary")
        for named in ("United Kingdom", "United States", "Saudi Arabia", "United Arab Emirates", "State of Qatar", "England and Wales"):
            if named.lower() in main_text.lower():
                failures.append("named-jurisdiction:" + named)
        if re.search(r"\b(?:QAR|USD|EUR|GBP)\s*\d", main_text, re.I):
            failures.append("fabricated-liability-amount")

        legal_lists = soup.select(".orx-legal-content .orx-legal-section ul, .orx-legal-content .orx-legal-section ol")
        if len(legal_lists) < 2:
            failures.append("long-form-lists")
        wrapper = soup.select_one(".orx-legal-table-wrap")
        table = soup.select_one("table.orx-legal-table")
        if not wrapper or wrapper.get("tabindex") != "0" or wrapper.get("role") != "region":
            failures.append("table-wrapper")
        if not table:
            failures.append("semantic-table")
        else:
            if not table.find("caption") or not table.find("thead") or not table.find("tbody"):
                failures.append("table-anatomy")
            if len(table.select('thead th[scope="col"]')) != 3:
                failures.append("table-col-headers")
            if len(table.select('tbody th[scope="row"]')) != 4:
                failures.append("table-row-headers")

        if not soup.select_one('[data-orx-mega-trigger][aria-current="page"]'):
            failures.append("explore-current")
        if soup.select_one('.orx-mega-menu [aria-current="page"]'):
            failures.append("mega-child-current")
        if soup.select_one('.orx-mobile-nav [aria-current="page"]'):
            failures.append("mobile-child-current")
        if not soup.find("a", class_="orx-lang-switch", href=spec["other"]):
            failures.append("language-switch-source")
        if len(soup.select('footer[data-orx-global-footer="v1"]')) != 1:
            failures.append("footer")
        if soup.find("script", src="../assets/js/origex-terms.js"):
            failures.append("unnecessary-page-js")
        if "TARGET" in text or "targetft" in text.lower():
            failures.append("client-leak")

        icons = set(re.findall(r"sprite\.svg#([a-z0-9-]+)", text))
        missing = sorted(icons - sprite_ids)
        if missing:
            failures.append("icons:" + str(missing))

        report["pages"][lang] = {
            "failures": failures,
            "sections": len([s for s in SECTIONS if soup.find("section", id=s)]),
            "tocLinks": len(toc_links),
            "legalLists": len(legal_lists),
            "tableRows": len(table.select("tbody tr")) if table else 0,
            "iconCount": len(icons),
        }
        report["failures"].extend([lang + ":" + f for f in failures])

    for script, label in (
        (".github/scripts/normalize_global_navigation.py", "nav-drift"),
        (".github/scripts/normalize_global_footer.py", "footer-drift"),
    ):
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
    server = subprocess.Popen(["python", "-m", "http.server", "8768"], cwd=R, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    try:
        for lang in ("ar", "en"):
            driver = webdriver.Chrome(options=options)
            try:
                for width in (390, 820, 1366, 1536):
                    failures = []
                    try:
                        driver.set_window_size(width, 1900)
                        driver.get(f"http://127.0.0.1:8768/{lang}/terms.html")
                        time.sleep(.15)
                        if driver.find_element(By.TAG_NAME, "html").get_attribute("dir") != ("rtl" if lang == "ar" else "ltr"):
                            failures.append("direction")
                        if driver.execute_script("return document.documentElement.scrollWidth") > driver.execute_script("return document.documentElement.clientWidth") + 1:
                            failures.append("document-overflow")
                        if len(driver.find_elements(By.TAG_NAME, "h1")) != 1:
                            failures.append("h1-count")
                        if not driver.find_element(By.CSS_SELECTOR, ".orx-legal-disclaimer").is_displayed():
                            failures.append("disclaimer")
                        toc = driver.find_element(By.CSS_SELECTOR, ".orx-legal-toc")
                        position = driver.execute_script("return getComputedStyle(arguments[0]).position", toc)
                        if width >= 992 and position != "sticky": failures.append("toc-not-sticky")
                        if width < 992 and position != "static": failures.append("toc-not-static")
                        if len(driver.find_elements(By.CSS_SELECTOR, ".orx-legal-section")) != 8:
                            failures.append("section-count")
                        if driver.find_element(By.CSS_SELECTOR, '[data-pg31-updated]').text.strip() not in ("Replace before production", "يُستبدل قبل النشر"):
                            failures.append("updated")
                        if driver.find_element(By.CSS_SELECTOR, '[data-orx-email="trade"]').get_attribute("href") != "mailto:trade@example.com":
                            failures.append("contact-config")

                        for selector, label in ((".orx-legal-toc a", "toc-target"), (".orx-legal-context-nav a", "context-target")):
                            for el in driver.find_elements(By.CSS_SELECTOR, selector):
                                if el.is_displayed() and el.rect["height"] < 47.5:
                                    failures.append(f"{label}:{round(el.rect['height'], 1)}")

                        table_wrap = driver.find_element(By.CSS_SELECTOR, ".orx-legal-table-wrap")
                        if not table_wrap.is_displayed(): failures.append("table-hidden")
                        if width == 390:
                            sw = driver.execute_script("return arguments[0].scrollWidth", table_wrap)
                            cw = driver.execute_script("return arguments[0].clientWidth", table_wrap)
                            if sw <= cw: failures.append("mobile-table-not-scrollable")

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
                    driver.get(f"http://127.0.0.1:8768/{lang}/terms.html")
                    time.sleep(.1)
                    first = driver.find_element(By.CSS_SELECTOR, '.orx-legal-toc a[href="#site-use"]')
                    driver.execute_script("arguments[0].click()", first); time.sleep(.08)
                    if driver.execute_script("return location.hash") != "#site-use": failures.append("toc-hash")
                    switch_href = driver.find_element(By.CSS_SELECTOR, ".orx-lang-switch").get_attribute("href")
                    expected_path = "/en/terms.html" if lang == "ar" else "/ar/terms.html"
                    if not urlparse(switch_href).path.endswith(expected_path): failures.append("language-switch")
                    privacy_href = driver.find_element(By.CSS_SELECTOR, '.orx-legal-context-nav a[href="privacy.html"]').get_attribute("href")
                    if not urlparse(privacy_href).path.endswith(f"/{lang}/privacy.html"): failures.append("privacy-context")
                    current = driver.find_element(By.CSS_SELECTOR, '.orx-legal-context-nav a[href="terms.html"]')
                    if current.get_attribute("aria-current") != "page": failures.append("terms-current")
                    table_wrap = driver.find_element(By.CSS_SELECTOR, ".orx-legal-table-wrap")
                    driver.execute_script("arguments[0].focus()", table_wrap)
                    if driver.execute_script("return document.activeElement === arguments[0]", table_wrap) is not True:
                        failures.append("table-focus")
                except Exception as exc:
                    failures.append(type(exc).__name__ + ":" + str(exc)[:220])
                report["interaction"][lang + "-toc-context-language-table"] = failures
                report["failures"].extend([lang + "-interaction:" + f for f in failures])
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
    status = "PASS" if not failures else "FAIL"
    (O / "run-status.txt").write_text(status + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "failures": failures}, ensure_ascii=False, indent=2))
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
