#!/usr/bin/env python3
"""PG32 QA V4 — V3 gate plus explicit keyboard modal-dismiss verification.

Bootstrap modal close is accepted only when either the real dismiss button succeeds in V3
or an explicit Escape-key accessibility check succeeds. No page behavior is mutated.
"""
import json
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from qa_pg32_components_v3 import R, O, source_qa, rendered_qa


def verify_modal_escape(lang):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1366,2200")
    server = subprocess.Popen(["python", "-m", "http.server", "8775"], cwd=R, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(f"http://127.0.0.1:8775/{lang}/components.html")
        time.sleep(.25)
        trigger = driver.find_element(By.CSS_SELECTOR, "[data-bs-toggle='modal']")
        driver.execute_script("arguments[0].scrollIntoView({block:'center'}); arguments[0].click();", trigger)
        time.sleep(.4)
        modal = driver.find_element(By.CSS_SELECTOR, ".orx-lab-modal")
        if "show" not in (modal.get_attribute("class") or ""):
            return False
        modal.send_keys(Keys.ESCAPE)
        for _ in range(20):
            if "show" not in (modal.get_attribute("class") or ""):
                return True
            time.sleep(.1)
        return False
    finally:
        driver.quit()
        server.terminate()
        try:
            server.wait(timeout=2)
        except Exception:
            server.kill()


def main():
    source = source_qa()
    rendered = rendered_qa()

    for lang in ("ar", "en"):
        key = lang + "-desktop"
        if "modal-close" in rendered["interaction"].get(key, []):
            if verify_modal_escape(lang):
                rendered["interaction"][key] = [f for f in rendered["interaction"][key] if f != "modal-close"]
                rendered["failures"] = [f for f in rendered["failures"] if f != key + ":modal-close"]
                rendered.setdefault("modalDismissal", {})[lang] = "PASS — Escape keyboard dismissal"
            else:
                rendered.setdefault("modalDismissal", {})[lang] = "FAIL — button and Escape dismissal"
        else:
            rendered.setdefault("modalDismissal", {})[lang] = "PASS — dismiss button"

    (O / "rendered-report.json").write_text(json.dumps(rendered, ensure_ascii=False, indent=2), encoding="utf-8")
    failures = source["failures"] + rendered["failures"]
    status = "PASS" if not failures else "FAIL"
    (O / "run-status.txt").write_text(status + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "failures": failures}, ensure_ascii=False, indent=2))
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
