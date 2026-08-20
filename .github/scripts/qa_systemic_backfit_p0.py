#!/usr/bin/env python3
"""ORIGEX systemic backfit P0 QA.

Validates SYS-01..SYS-04 at their shared ownership layers before the full global
AR/EN regression. This is intentionally a small reusable gate, not a page patcher.
"""
from pathlib import Path
import json
import re
import subprocess
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

R = Path(__file__).resolve().parents[2]
O = R / "qa" / "systemic-backfit-p0"
O.mkdir(parents=True, exist_ok=True)


def read(path):
    return (R / path).read_text(encoding="utf-8")


def hex_rgb(value):
    value = value.strip().lstrip("#")
    return tuple(int(value[i:i+2], 16) / 255 for i in (0, 2, 4))


def linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(value):
    r, g, b = map(linear, hex_rgb(value))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def token(css, name):
    match = re.search(rf"--{re.escape(name)}:\s*(#[0-9A-Fa-f]{{6}})", css)
    return match.group(1).upper() if match else None


def source_qa():
    tokens = read("assets/css/origex-tokens.css")
    foundation = read("assets/css/origex-foundation.css")
    components = read("assets/css/origex-components.css")
    shell = read("assets/css/origex-shell.css")
    ui = read("assets/js/origex-ui.js")
    failures = []

    semantic_required = [
        "--orx-surface-base", "--orx-surface-raised", "--orx-surface-subtle",
        "--orx-surface-brand", "--orx-surface-brand-strong", "--orx-surface-accent",
        "--orx-on-light-primary", "--orx-on-light-body", "--orx-on-light-muted",
        "--orx-on-dark-primary", "--orx-on-dark-muted", "--orx-on-accent",
    ]
    dimension_required = [
        "--orx-control-s: 40px", "--orx-control-m: 48px", "--orx-control-l: 56px",
        "--orx-touch-target: 48px", "--orx-textarea-min: 144px",
        "--orx-check-size: 20px", "--orx-upload-min: 144px",
    ]
    for item in semantic_required + dimension_required:
        if item not in tokens:
            failures.append("tokens:missing:" + item)

    soft = token(tokens, "orx-surface-soft")
    accent = token(tokens, "orx-accent")
    deep = token(tokens, "orx-primary-strong")
    muted = token(tokens, "orx-on-light-muted")
    contrast_report = {}
    if all((soft, accent, deep, muted)):
        contrast_report["mutedOnSoft"] = round(contrast(muted, soft), 2)
        contrast_report["deepOnAccent"] = round(contrast(deep, accent), 2)
        if contrast_report["mutedOnSoft"] < 4.5:
            failures.append("contrast:muted-on-soft")
        if contrast_report["deepOnAccent"] < 4.5:
            failures.append("contrast:on-accent")
    else:
        failures.append("contrast:token-resolution")

    expected_component_fragments = [
        "min-block-size:var(--orx-control-m)",
        "min-block-size:var(--orx-control-l)",
        "inline-size:var(--orx-touch-target);block-size:var(--orx-touch-target)",
        "block-size:var(--orx-control-m);min-block-size:var(--orx-control-m)",
        "min-block-size:var(--orx-textarea-min)",
        "inline-size:var(--orx-check-size);block-size:var(--orx-check-size)",
        "min-height:var(--orx-upload-min)",
        "min-inline-size:var(--orx-control-m);block-size:var(--orx-control-m)",
        "color:var(--orx-on-accent)",
    ]
    for item in expected_component_fragments:
        if item not in components:
            failures.append("components:missing:" + item)

    forbidden_dimension_fragments = [
        "min-block-size:46px", "min-block-size:52px", "inline-size:44px;block-size:44px",
        "min-inline-size:42px;block-size:42px", "inline-size:38px;block-size:38px",
        "min-block-size:132px", "min-height:140px",
    ]
    for item in forbidden_dimension_fragments:
        if item in components:
            failures.append("components:off-tier:" + item)

    if ".orx-floating>a,.orx-floating>button{inline-size:44px" in shell or ".orx-whatsapp,.orx-back-to-top{inset-inline-end:.75rem;inline-size:44px" in shell:
        failures.append("shell:mobile-44px-downgrade")
    for item in [
        ".orx-socials a{display:grid;place-items:center;min-width:var(--orx-touch-target);height:var(--orx-touch-target)",
        ".orx-lang-switch{display:inline-flex;align-items:center;justify-content:center;min-block-size:var(--orx-control-m);min-inline-size:var(--orx-control-m)",
        ".orx-mobile-nav a{display:flex;align-items:center;min-block-size:var(--orx-touch-target)",
    ]:
        if item not in shell:
            failures.append("shell:missing:" + item)

    for item in ["const trapDrawerFocus", "event.key !== 'Tab'", "drawer.contains(active)", "event.shiftKey && active === first", "!event.shiftKey && active === last"]:
        if item not in ui:
            failures.append("ui:focus-trap:" + item)

    if "var(--orx-on-light-muted)" not in foundation:
        failures.append("foundation:semantic-muted-not-adopted")
    if "var(--orx-surface-base)" not in foundation:
        failures.append("foundation:semantic-surface-not-adopted")

    report = {
        "failures": failures,
        "contrast": contrast_report,
        "systems": {
            "SYS-01": "PASS" if not any(x.startswith("contrast:") or x.startswith("tokens:") or x.startswith("foundation:") for x in failures) else "FAIL",
            "SYS-02": "PASS" if not any(x.startswith("components:") for x in failures) else "FAIL",
            "SYS-03": "PASS" if not any(x.startswith("shell:") for x in failures) else "FAIL",
            "SYS-04": "PASS" if not any(x.startswith("ui:") for x in failures) else "FAIL",
        },
    }
    (O / "source-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


def browser_qa():
    failures = []
    cases = []
    diagnostics = {}
    drawer_results = {}
    pages = ["components.html", "index.html", "products.html", "contact.html"]

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1366,2200")

    server = subprocess.Popen(
        ["python", "-m", "http.server", "8780"], cwd=R,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    time.sleep(1)
    try:
        driver = webdriver.Chrome(options=options)
        try:
            for lang in ("ar", "en"):
                for page in pages:
                    for width in (390, 1366):
                        local = []
                        driver.set_window_size(width, 2200)
                        driver.get(f"http://127.0.0.1:8780/{lang}/{page}")
                        time.sleep(0.25)
                        sw = driver.execute_script("return document.documentElement.scrollWidth")
                        cw = driver.execute_script("return document.documentElement.clientWidth")
                        if sw > cw + 1:
                            local.append(f"document-overflow:{sw}>{cw}")
                        expected_dir = "rtl" if lang == "ar" else "ltr"
                        if driver.find_element(By.TAG_NAME, "html").get_attribute("dir") != expected_dir:
                            local.append("direction")
                        cases.append({"lang": lang, "page": page, "width": width, "scrollWidth": sw, "clientWidth": cw, "failures": local})
                        failures += [f"{lang}:{page}:{width}:{item}" for item in local]

                # PG32 must show the systemic P0 dimensions as aligned after the shared backfit.
                driver.set_window_size(1366, 2200)
                driver.get(f"http://127.0.0.1:8780/{lang}/components.html")
                time.sleep(0.4)
                rows = driver.find_elements(By.CSS_SELECTOR, "[data-lab-diagnostic-row]")
                state_map = {r.get_attribute("data-lab-diagnostic-row"): r.get_attribute("data-state") for r in rows}
                diagnostics[lang] = state_map
                expected = {"button-default", "button-large", "icon-button", "input", "select", "textarea", "checkbox", "upload", "pagination"}
                if set(state_map) != expected:
                    failures.append(f"{lang}:diagnostics-key-set")
                for key in expected:
                    if state_map.get(key) != "aligned":
                        failures.append(f"{lang}:diagnostic:{key}:{state_map.get(key)}")

                # N03 focus containment: forward cycle, reverse cycle, Escape and focus return.
                driver.set_window_size(390, 1800)
                driver.get(f"http://127.0.0.1:8780/{lang}/components.html")
                time.sleep(0.25)
                local = []
                opener = driver.find_element(By.CSS_SELECTOR, "[data-orx-drawer-open]")
                opener.click()
                time.sleep(0.08)
                drawer = driver.find_element(By.CSS_SELECTOR, "[data-orx-mobile-drawer]")
                if drawer.get_attribute("aria-hidden") != "false":
                    local.append("open")
                focusables = driver.find_elements(By.CSS_SELECTOR, "[data-orx-mobile-drawer] a[href], [data-orx-mobile-drawer] button:not([disabled]), [data-orx-mobile-drawer] input:not([disabled]), [data-orx-mobile-drawer] select:not([disabled]), [data-orx-mobile-drawer] textarea:not([disabled]), [data-orx-mobile-drawer] [tabindex]:not([tabindex='-1'])")
                if not focusables:
                    local.append("no-focusables")
                else:
                    first, last = focusables[0], focusables[-1]
                    driver.execute_script("arguments[0].focus()", last)
                    last.send_keys(Keys.TAB)
                    time.sleep(0.05)
                    if driver.switch_to.active_element != first:
                        local.append("forward-trap")
                    driver.execute_script("arguments[0].focus()", first)
                    ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
                    time.sleep(0.05)
                    if driver.switch_to.active_element != last:
                        local.append("reverse-trap")
                    driver.switch_to.active_element.send_keys(Keys.ESCAPE)
                    time.sleep(0.06)
                    if drawer.get_attribute("aria-hidden") != "true":
                        local.append("escape-close")
                    if driver.switch_to.active_element != opener:
                        local.append("focus-return")
                    if "orx-nav-open" in (driver.find_element(By.TAG_NAME, "body").get_attribute("class") or ""):
                        local.append("body-scroll-lock-release")
                drawer_results[lang] = local
                failures += [f"{lang}:drawer:{item}" for item in local]
        finally:
            driver.quit()
    finally:
        server.terminate()
        try:
            server.wait(timeout=2)
        except Exception:
            server.kill()

    report = {"failures": failures, "cases": cases, "diagnostics": diagnostics, "drawerFocusTrap": drawer_results}
    (O / "browser-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


def main():
    source = source_qa()
    browser = browser_qa()
    failures = source["failures"] + browser["failures"]
    status = "PASS" if not failures else "FAIL"
    (O / "run-status.txt").write_text(status + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "failures": failures}, indent=2))
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
