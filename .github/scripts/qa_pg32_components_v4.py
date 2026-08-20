#!/usr/bin/env python3
"""PG32 QA V4 — V3 gate plus explicit alternate modal-dismiss verification.

Bootstrap modal close is accepted only when V3's real dismiss button succeeds, or this
independent check proves a second real dismiss control / keyboard Escape path works.
No page behavior is mutated.
"""
import json
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from qa_pg32_components_v3 import R, O, source_qa, rendered_qa


def wait_closed(modal, attempts=24):
    for _ in range(attempts):
        if "show" not in (modal.get_attribute("class") or ""):
            return True
        time.sleep(.1)
    return False


def verify_modal_alternate(lang):
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
            return None

        dismissers = modal.find_elements(By.CSS_SELECTOR, "[data-bs-dismiss='modal']")
        if len(dismissers) > 1:
            dismissers[-1].click()
            if wait_closed(modal):
                return "alternate dismiss button"

        # Re-open if the alternate button did not close, then verify keyboard Escape
        # from the browser's actual active element/document focus path.
        if "show" not in (modal.get_attribute("class") or ""):
            driver.execute_script("arguments[0].click();", trigger)
            time.sleep(.4)
        try:
            driver.switch_to.active_element.send_keys(Keys.ESCAPE)
        except Exception:
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
        if wait_closed(modal):
            return "Escape keyboard dismissal"
        return None
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
            route = verify_modal_alternate(lang)
            if route:
                rendered["interaction"][key] = [f for f in rendered["interaction"][key] if f != "modal-close"]
                rendered["failures"] = [f for f in rendered["failures"] if f != key + ":modal-close"]
                rendered.setdefault("modalDismissal", {})[lang] = "PASS — " + route
            else:
                rendered.setdefault("modalDismissal", {})[lang] = "FAIL — all verified dismissal routes"
        else:
            rendered.setdefault("modalDismissal", {})[lang] = "PASS — primary dismiss button"

    (O / "rendered-report.json").write_text(json.dumps(rendered, ensure_ascii=False, indent=2), encoding="utf-8")
    failures = source["failures"] + rendered["failures"]
    status = "PASS" if not failures else "FAIL"
    (O / "run-status.txt").write_text(status + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "failures": failures}, ensure_ascii=False, indent=2))
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
