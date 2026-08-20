#!/usr/bin/env python3
"""ORIGEX PG32 Components / Elements — source, registry, diagnostic, rendered and interaction QA."""
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
O = R / "qa/pg32-components"
O.mkdir(parents=True, exist_ok=True)

CARD_CLASSES = [
    "orx-feature-card", "orx-product-card", "orx-supplier-card", "orx-market-card",
    "orx-process-card", "orx-metric-card", "orx-certification-card", "orx-resource-card",
    "orx-case-study-card", "orx-contact-card", "orx-cta-card"
]
COMPONENT_SELECTORS = {
    "C12": ".orx-breadcrumb", "C13": ".orx-tabs", "C14": ".orx-accordion",
    "C15": ".orx-pagination", "C16": ".orx-search", "C17": ".orx-filter-group",
    "C18": ".orx-spec", "C19": ".orx-stat-strip", "C20": ".orx-trust-item",
    "C21": ".orx-empty-state", "C22": ".orx-alert", "C23": ".orx-field",
    "C24": ".orx-upload", "C25": ".orx-form-status", "C26": ".orx-product-media",
    "C27": ".orx-logo-frame", "C28": ".orx-editorial-media"
}
PRIMITIVE_SELECTORS = {
    "P01": ".orx-btn--primary", "P02": ".orx-btn--secondary", "P03": ".orx-text-action",
    "P04": ".orx-icon-btn", "P05": ".orx-badge", "P06": ".orx-input",
    "P07": ".orx-select", "P08": ".orx-textarea", "P09": ".orx-check",
    "P10": ".orx-divider", "P11": ".orx-icon-box"
}


def source_qa():
    report = {"failures": [], "pages": {}, "labCss": {"failures": []}, "labJs": {"failures": []}}
    css = (R / "assets/css/origex-components-lab.css").read_text(encoding="utf-8")
    js = (R / "assets/js/origex-components-lab.js").read_text(encoding="utf-8")
    global_css = (R / "assets/css/origex-components.css").read_text(encoding="utf-8")

    # PG32 CSS may compose specimens but must not redefine registered component roots.
    forbidden_css = [r"(?:^|\})\s*\.orx-btn\s*\{", r"(?:^|\})\s*\.orx-input\s*\{",
                     r"(?:^|\})\s*\.orx-card\s*\{", r"(?:^|\})\s*\.orx-icon-btn\s*\{"]
    for pattern in forbidden_css:
        if re.search(pattern, css): report["labCss"]["failures"].append("registered-root-override:" + pattern)
    for marker in (".orx-lab-table-wrap", ".orx-lab-diagnostic-row", ".orx-lab-swatch", ".orx-lab-modal", "max-width: 767.98px"):
        if marker not in css: report["labCss"]["failures"].append("missing:" + marker)
    report["failures"].extend(report["labCss"]["failures"])

    lowered_js = js.lower()
    for banned in ("fetch(", "xmlhttprequest", "localstorage", "sessionstorage", "navigator.sendbeacon"):
        if banned in lowered_js: report["labJs"]["failures"].append("network-storage:" + banned)
    for marker in ("getboundingclientrect", "data-pg32-diagnostics", "data-lab-demo-form", "preventdefault"):
        if marker not in lowered_js: report["labJs"]["failures"].append("missing:" + marker)
    if ".style." in lowered_js or "style.setproperty" in lowered_js:
        report["labJs"]["failures"].append("runtime-style-mutation")
    report["failures"].extend(report["labJs"]["failures"])

    # Known source values must remain visible to diagnostics, not silently fixed by PG32 page CSS.
    known_current = ("min-block-size:46px", "min-block-size:52px", "inline-size:44px", "block-size:44px",
                     "min-block-size:132px", "block-size:42px", "min-height:140px")
    missing_known = [value for value in known_current if value not in global_css]
    if missing_known:
        report["knownCurrentChanged"] = missing_known
        # Not a page failure by itself: a central fix may have landed. Rendered diagnostics become authority.

    specs = {
        "ar": {
            "dir": "rtl",
            "h1": "مكونات ORIGEX بمحتوى واقعي جاهز للاختبار والتخصيص.",
            "support": "استعرض الأزرار، الكروت، النماذج، الجداول، الحالات، والأنماط باستخدام أمثلة تجارية من نفس تجربة القالب.",
            "other": "../en/components.html",
            "canonical": "https://example.com/ar/components.html",
            "bootstrap": "../assets/vendor/bootstrap/css/bootstrap.rtl.min.css",
        },
        "en": {
            "dir": "ltr",
            "h1": "ORIGEX components demonstrated with realistic, customization-ready content.",
            "support": "Explore buttons, cards, forms, tables, states and patterns using commercial examples from the same ORIGEX template experience.",
            "other": "../ar/components.html",
            "canonical": "https://example.com/en/components.html",
            "bootstrap": "../assets/vendor/bootstrap/css/bootstrap.min.css",
        },
    }

    sprite = (R / "assets/icons/sprite.svg").read_text(encoding="utf-8")
    sprite_ids = set(re.findall(r'<symbol[^>]+id="([^"]+)"', sprite))

    for lang, spec in specs.items():
        path = R / lang / "components.html"
        text = path.read_text(encoding="utf-8")
        soup = BeautifulSoup(text, "html.parser")
        failures = []
        if soup.html.get("lang") != lang or soup.html.get("dir") != spec["dir"]: failures.append("lang-dir")
        h1s = soup.find_all("h1")
        if len(h1s) != 1 or h1s[0].get_text(" ", strip=True) != spec["h1"]: failures.append("canonical-h1")
        if spec["support"] not in soup.get_text(" ", strip=True): failures.append("canonical-support")
        if not soup.find("link", rel="stylesheet", href=spec["bootstrap"]): failures.append("bootstrap-direction")
        canonical = soup.find("link", rel="canonical")
        if not canonical or canonical.get("href") != spec["canonical"]: failures.append("canonical")
        alternates = {(a.get("hreflang"), a.get("href")) for a in soup.find_all("link", rel="alternate")}
        expected_alts = {
            ("ar", "https://example.com/ar/components.html"),
            ("en", "https://example.com/en/components.html"),
            ("x-default", "https://example.com/en/components.html"),
        }
        if not expected_alts.issubset(alternates): failures.append("hreflang")
        if not soup.find("a", class_="orx-lang-switch", href=spec["other"]): failures.append("language-switch")

        ld = " ".join(s.get_text() for s in soup.find_all("script", attrs={"type": "application/ld+json"}))
        if '"WebPage"' not in ld or '"BreadcrumbList"' not in ld: failures.append("structured-data")
        for banned_type in ('"Product"', '"Offer"', '"Review"'):
            if banned_type in ld: failures.append("forbidden-schema:" + banned_type)

        if not soup.select_one("[data-pg32-root]"): failures.append("root")
        if "BACKFIT" not in text or "Demo" not in text: failures.append("qa-demo-boundary")
        if "TARGET" in text or "targetft" in text.lower(): failures.append("client-leak")
        if not soup.find("link", rel="stylesheet", href="../assets/css/origex-components-lab.css"): failures.append("lab-css")
        if not soup.find("script", src="../assets/js/origex-components-lab.js"): failures.append("lab-js")

        # Frozen scope / sample families.
        required_text = ["Product", "Supplier", "Market", "Certification", "Resource", "RFQ", "Alert"] if lang == "en" else ["Product", "المورد", "السوق", "Certification", "Resource", "RFQ", "Alert"]
        page_text = soup.get_text(" ", strip=True)
        for item in required_text:
            if item not in page_text: failures.append("sample:" + item)
        for klass in CARD_CLASSES:
            if not soup.select_one("." + klass): failures.append("card:" + klass)
        for cid, selector in COMPONENT_SELECTORS.items():
            if not soup.select_one(selector): failures.append("component:" + cid)
        for pid, selector in PRIMITIVE_SELECTORS.items():
            if not soup.select_one(selector): failures.append("primitive:" + pid)
        for family in ("F01–07", "P01–11", "C01–28", "S01–06", "N01–04"):
            if family not in page_text: failures.append("registry-family:" + family)

        # Required states and buyer/productization reference.
        for selector, label in (("[data-lab-demo-form]", "demo-form"), ("[data-lab-error-input]", "error-state"),
                                ("[data-bs-toggle='modal']", "overlay"), (".orx-lab-do-dont", "do-dont"),
                                (".orx-lab-table-wrap", "reference-table"), ("[data-lab-probe]", "diagnostics"),
                                (".orx-lab-social-slots", "social-state")):
            if not soup.select_one(selector): failures.append(label)
        if len(soup.select("[data-lab-diagnostic-row]")) != 9: failures.append("diagnostic-row-count")
        if not soup.select_one("select.orx-select"): failures.append("market-selector")
        if not soup.select_one(".orx-lang-switch"): failures.append("language-selector")
        if not soup.select_one(".orx-final-cta"): failures.append("final-cta")
        if not soup.select_one("header[data-orx-global-nav='v1']"): failures.append("global-nav")
        if not soup.select_one("footer[data-orx-global-footer='v1']"): failures.append("global-footer")

        # Form must have no action endpoint and page runtime must remain local.
        form = soup.select_one("[data-lab-demo-form]")
        if form and form.get("action"): failures.append("form-action")
        lowered = text.lower()
        for banned in ("fetch(", "xmlhttprequest", "localstorage", "sessionstorage"):
            if banned in lowered: failures.append("network-storage:" + banned)

        icons = set(re.findall(r"sprite\.svg#([a-z0-9-]+)", text))
        missing = sorted(icons - sprite_ids)
        if missing: failures.append("icons:" + str(missing))

        report["pages"][lang] = {
            "failures": failures,
            "cards": len([k for k in CARD_CLASSES if soup.select_one("." + k)]),
            "coreComponents": len([cid for cid, sel in COMPONENT_SELECTORS.items() if soup.select_one(sel)]),
            "primitives": len([pid for pid, sel in PRIMITIVE_SELECTORS.items() if soup.select_one(sel)]),
            "diagnosticRows": len(soup.select("[data-lab-diagnostic-row]")),
            "iconCount": len(icons),
        }
        report["failures"].extend([lang + ":" + f for f in failures])

    for script, label in ((".github/scripts/normalize_global_navigation.py", "nav-drift"),
                          (".github/scripts/normalize_global_footer.py", "footer-drift")):
        run = subprocess.run(["python", script, "--check"], cwd=R, capture_output=True, text=True)
        if run.returncode:
            report["failures"].append(label)
            report[label] = run.stdout + run.stderr

    (O / "source-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def rendered_qa():
    report = {"failures": [], "cases": [], "interaction": {}, "diagnostics": {}}
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1366,2200")
    server = subprocess.Popen(["python", "-m", "http.server", "8772"], cwd=R, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    try:
        for lang in ("ar", "en"):
            driver = webdriver.Chrome(options=options)
            try:
                for width in (390, 820, 1366, 1536):
                    failures = []
                    try:
                        driver.set_window_size(width, 2200)
                        driver.get(f"http://127.0.0.1:8772/{lang}/components.html")
                        time.sleep(.3)
                        if driver.find_element(By.TAG_NAME, "html").get_attribute("dir") != ("rtl" if lang == "ar" else "ltr"): failures.append("direction")
                        if driver.execute_script("return document.documentElement.scrollWidth") > driver.execute_script("return document.documentElement.clientWidth") + 1: failures.append("document-overflow")
                        if len(driver.find_elements(By.TAG_NAME, "h1")) != 1: failures.append("h1-count")
                        if driver.find_element(By.TAG_NAME, "html").get_attribute("data-pg32-diagnostics") != "ready": failures.append("diagnostics-not-ready")
                        rows = driver.find_elements(By.CSS_SELECTOR, "[data-lab-diagnostic-row]")
                        if len(rows) != 9: failures.append("diagnostic-count")
                        waiting = [r.get_attribute("data-lab-diagnostic-row") for r in rows if r.get_attribute("data-state") not in ("aligned", "backfit")]
                        if waiting: failures.append("diagnostic-wait:" + str(waiting))
                        if not driver.find_element(By.CSS_SELECTOR, ".orx-lab-boundary").is_displayed(): failures.append("boundary")
                        if len(driver.find_elements(By.CSS_SELECTOR, ".orx-product-card")) < 1: failures.append("product-card")
                        if len(driver.find_elements(By.CSS_SELECTOR, ".orx-supplier-card")) < 1: failures.append("supplier-card")
                        if len(driver.find_elements(By.CSS_SELECTOR, ".orx-market-card")) < 1: failures.append("market-card")
                        # Reference table wrappers may scroll internally; page itself must not.
                        for wrap in driver.find_elements(By.CSS_SELECTOR, ".orx-lab-table-wrap"):
                            if not wrap.is_displayed(): failures.append("table-hidden")
                    except Exception as exc:
                        failures.append(type(exc).__name__ + ":" + str(exc)[:220])
                    report["cases"].append({"lang": lang, "width": width, "failures": failures})
                    report["failures"].extend([f"{lang}-{width}:{f}" for f in failures])

                # Full interaction suite at desktop.
                failures = []
                try:
                    driver.set_window_size(1366, 2200)
                    driver.get(f"http://127.0.0.1:8772/{lang}/components.html")
                    time.sleep(.25)
                    # Diagnostics: at least one current mismatch and no WAIT states.
                    states = {r.get_attribute("data-lab-diagnostic-row"): r.get_attribute("data-state") for r in driver.find_elements(By.CSS_SELECTOR, "[data-lab-diagnostic-row]")}
                    report["diagnostics"][lang] = states
                    if "backfit" not in states.values(): failures.append("no-backfit-detected")
                    if states.get("input") not in ("aligned", "backfit") or states.get("select") not in ("aligned", "backfit"): failures.append("input-select-state")

                    # Mega menu / Escape.
                    trigger = driver.find_element(By.CSS_SELECTOR, "[data-orx-mega-trigger]")
                    trigger.click(); time.sleep(.05)
                    if trigger.get_attribute("aria-expanded") != "true": failures.append("mega-open")
                    trigger.send_keys(Keys.ESCAPE); time.sleep(.05)
                    if trigger.get_attribute("aria-expanded") != "false": failures.append("mega-escape")

                    # Tabs keyboard.
                    tabs = driver.find_elements(By.CSS_SELECTOR, "[data-orx-tabs] [role='tab']")
                    tabs[0].click(); tabs[0].send_keys(Keys.ARROW_RIGHT); time.sleep(.08)
                    if not any(t.get_attribute("aria-selected") == "true" and t != tabs[0] for t in tabs): failures.append("tabs-keyboard")

                    # Accordion disclosure.
                    acc = driver.find_elements(By.CSS_SELECTOR, "[data-orx-accordion-trigger]")[1]
                    before = acc.get_attribute("aria-expanded")
                    acc.click(); time.sleep(.05)
                    if acc.get_attribute("aria-expanded") == before: failures.append("accordion-toggle")

                    # Demo form local success.
                    form = driver.find_element(By.CSS_SELECTOR, "[data-lab-demo-form]")
                    form.find_element(By.CSS_SELECTOR, "button[type='submit']").click(); time.sleep(.08)
                    success = form.find_element(By.CSS_SELECTOR, "[data-lab-form-success]")
                    if not success.is_displayed(): failures.append("form-success")

                    # Bootstrap modal open/close and return.
                    modal_trigger = driver.find_element(By.CSS_SELECTOR, "[data-bs-toggle='modal']")
                    driver.execute_script("arguments[0].scrollIntoView({block:'center'})", modal_trigger)
                    modal_trigger.click(); time.sleep(.2)
                    modal = driver.find_element(By.CSS_SELECTOR, ".orx-lab-modal")
                    if "show" not in (modal.get_attribute("class") or ""): failures.append("modal-open")
                    close = modal.find_element(By.CSS_SELECTOR, "[data-bs-dismiss='modal']")
                    close.click(); time.sleep(.2)
                    if "show" in (modal.get_attribute("class") or ""): failures.append("modal-close")

                    # Language counterpart.
                    href = driver.find_element(By.CSS_SELECTOR, ".orx-lang-switch").get_attribute("href")
                    expected = "/en/components.html" if lang == "ar" else "/ar/components.html"
                    if not urlparse(href).path.endswith(expected): failures.append("language-counterpart")
                except Exception as exc:
                    failures.append(type(exc).__name__ + ":" + str(exc)[:240])
                report["interaction"][lang + "-desktop"] = failures
                report["failures"].extend([lang + "-desktop:" + f for f in failures])

                # Mobile drawer separately.
                failures = []
                try:
                    driver.set_window_size(390, 1800)
                    driver.get(f"http://127.0.0.1:8772/{lang}/components.html")
                    time.sleep(.18)
                    opener = driver.find_element(By.CSS_SELECTOR, "[data-orx-drawer-open]")
                    opener.click(); time.sleep(.08)
                    drawer = driver.find_element(By.CSS_SELECTOR, "[data-orx-mobile-drawer]")
                    if drawer.get_attribute("aria-hidden") != "false": failures.append("drawer-open")
                    driver.find_element(By.CSS_SELECTOR, "[data-orx-drawer-close]").click(); time.sleep(.08)
                    if drawer.get_attribute("aria-hidden") != "true": failures.append("drawer-close")
                except Exception as exc:
                    failures.append(type(exc).__name__ + ":" + str(exc)[:220])
                report["interaction"][lang + "-mobile"] = failures
                report["failures"].extend([lang + "-mobile:" + f for f in failures])
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
