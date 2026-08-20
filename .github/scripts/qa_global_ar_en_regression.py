#!/usr/bin/env python3
"""ORIGEX global AR/EN regression after shared-system backfit.

Runs structural parity, local-route/asset integrity and rendered responsive smoke QA
across every shipped Arabic and English page. Page-specific interaction suites remain
owned by their page gates and the later sequential second pass.
"""
from pathlib import Path
from urllib.parse import urlparse, unquote
import json
import subprocess
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

R = Path(__file__).resolve().parents[2]
O = R / "qa" / "global-ar-en-regression"
O.mkdir(parents=True, exist_ok=True)
WIDTHS = (390, 820, 1366, 1536)
LANGS = {"ar": "rtl", "en": "ltr"}


def html_files(lang):
    return sorted(p.name for p in (R / lang).glob("*.html"))


def local_target(page_path, raw):
    if not raw:
        return None
    raw = raw.strip()
    if raw.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return None
    parsed = urlparse(raw)
    if parsed.scheme or parsed.netloc:
        return None
    path = unquote(parsed.path)
    if not path or path == "/":
        return R / "index.html"
    if path.startswith("/"):
        return R / path.lstrip("/")
    return (page_path.parent / path).resolve()


def static_qa():
    failures = []
    ar = html_files("ar")
    en = html_files("en")
    if len(ar) != 33:
        failures.append(f"ar-count:{len(ar)}")
    if len(en) != 33:
        failures.append(f"en-count:{len(en)}")
    if ar != en:
        failures.append("filename-parity")

    pages = {}
    for lang, direction in LANGS.items():
        for name in html_files(lang):
            path = R / lang / name
            soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
            local = []
            html = soup.find("html")
            if not html or html.get("lang", "").split("-")[0] != lang:
                local.append("lang")
            if not html or html.get("dir") != direction:
                local.append("dir")
            if len(soup.find_all("h1")) != 1:
                local.append("h1-count")

            text = path.read_text(encoding="utf-8")
            for forbidden in ("targetft.com", "TARGET Food Trading", "TARGET — Food"):
                if forbidden.lower() in text.lower():
                    local.append("client-leak:" + forbidden)

            # Reciprocal counterpart exists and the static language switch points to it.
            counterpart = R / ("en" if lang == "ar" else "ar") / name
            if not counterpart.exists():
                local.append("counterpart-missing")
            switch = soup.select_one(".orx-lang-switch")
            if switch:
                target = local_target(path, switch.get("href"))
                if target and target.name != name:
                    local.append("language-switch-filename")

            # Local linked HTML/assets must exist. Skip form placeholder/action anchors.
            checked = set()
            for tag, attr in (("a", "href"), ("link", "href"), ("script", "src"), ("img", "src"), ("source", "src")):
                for node in soup.find_all(tag):
                    raw = node.get(attr)
                    target = local_target(path, raw)
                    if not target:
                        continue
                    key = str(target)
                    if key in checked:
                        continue
                    checked.add(key)
                    if not target.exists():
                        local.append(f"missing-local:{tag}:{raw}")

            pages[f"{lang}/{name}"] = {"failures": local, "localTargetsChecked": len(checked)}
            failures += [f"{lang}/{name}:{item}" for item in local]

    report = {"failures": failures, "arCount": len(ar), "enCount": len(en), "filenameParity": ar == en, "pages": pages}
    (O / "static-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def rendered_qa():
    failures = []
    cases = []
    page_names = html_files("ar")

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1366,1800")
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

    server = subprocess.Popen(["python", "-m", "http.server", "8782"], cwd=R, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    try:
        driver = webdriver.Chrome(options=options)
        try:
            for lang, direction in LANGS.items():
                for name in page_names:
                    for width in WIDTHS:
                        local = []
                        driver.set_window_size(width, 1800)
                        driver.get(f"http://127.0.0.1:8782/{lang}/{name}")
                        time.sleep(0.08)
                        html = driver.find_element(By.TAG_NAME, "html")
                        if html.get_attribute("dir") != direction:
                            local.append("direction")
                        sw = driver.execute_script("return document.documentElement.scrollWidth")
                        cw = driver.execute_script("return document.documentElement.clientWidth")
                        if sw > cw + 1:
                            local.append(f"overflow:{sw}>{cw}")
                        if len(driver.find_elements(By.TAG_NAME, "h1")) != 1:
                            local.append("h1")
                        severe = []
                        try:
                            for entry in driver.get_log("browser"):
                                if entry.get("level") == "SEVERE":
                                    message = entry.get("message", "")
                                    # Chrome can emit benign favicon noise. Keep JS/runtime and resource failures.
                                    if "favicon" not in message.lower():
                                        severe.append(message[:260])
                        except Exception:
                            pass
                        if severe:
                            local.append("console-severe:" + " | ".join(severe[:3]))
                        cases.append({"lang": lang, "page": name, "width": width, "scrollWidth": sw, "clientWidth": cw, "failures": local})
                        failures += [f"{lang}/{name}:{width}:{item}" for item in local]
        finally:
            driver.quit()
    finally:
        server.terminate()
        try:
            server.wait(timeout=2)
        except Exception:
            server.kill()

    report = {"failures": failures, "caseCount": len(cases), "expectedCases": 33 * 2 * len(WIDTHS), "cases": cases}
    (O / "rendered-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def main():
    static = static_qa()
    rendered = rendered_qa()
    failures = static["failures"] + rendered["failures"]
    status = "PASS" if not failures else "FAIL"
    summary = {
        "status": status,
        "failures": failures,
        "arPages": static["arCount"],
        "enPages": static["enCount"],
        "filenameParity": static["filenameParity"],
        "renderedCases": rendered["caseCount"],
    }
    (O / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    (O / "run-status.txt").write_text(status + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
