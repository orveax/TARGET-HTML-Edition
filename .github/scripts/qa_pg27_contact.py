#!/usr/bin/env python3
"""ORIGEX PG27 Contact QA — source, config, rendered and interaction gate."""
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
O = R / "qa/pg27-contact"
O.mkdir(parents=True, exist_ok=True)


def source_qa():
    source = {"failures": [], "pages": {}, "runtime": {}, "config": {}}

    js = (R / "assets/js/origex-contact.js").read_text(encoding="utf-8")
    runtime_failures = []
    for bad in ("fetch(", "XMLHttpRequest", "localStorage", "sessionStorage"):
        if bad in js:
            runtime_failures.append("forbidden-runtime:" + bad)
    for required in (
        "'general'", "'rfq'", "'supplier'", "'partner'",
        "history.replaceState", "data-pg27-route", "data-pg27-topic-select",
        "data-pg27-ready", "orx-mobile-nav a[lang]", "preventDefault",
    ):
        if required not in js:
            runtime_failures.append("runtime-missing:" + required)
    source["runtime"] = {"failures": runtime_failures}
    source["failures"] += runtime_failures

    config = (R / "assets/js/config.js").read_text(encoding="utf-8")
    config_failures = []
    for required in (
        "email:", "rfqEmail:", "suppliersEmail:", "partnersEmail:",
        "phone:", "addressAr:", "addressEn:", "social:", "businessHours:",
    ):
        if required not in config:
            config_failures.append("config-missing:" + required)
    source["config"] = {"failures": config_failures}
    source["failures"] += config_failures

    sprite = (R / "assets/icons/sprite.svg").read_text(encoding="utf-8")
    sprite_ids = set(re.findall(r'<symbol[^>]+id="([^"]+)"', sprite))
    specs = {
        "ar": {
            "dir": "rtl",
            "h1": "اختر قناة التواصل المناسبة لطلبك.",
            "canonical": "https://example.com/ar/contact.html",
            "other": "../en/contact.html",
            "support": "للمنتجات، الموردين، طلبات الأسعار أو الشراكات، شارك نوع الطلب والمعلومات الأساسية حتى يصل إلى المسار الصحيح.",
        },
        "en": {
            "dir": "ltr",
            "h1": "Choose the right contact route for your enquiry.",
            "canonical": "https://example.com/en/contact.html",
            "other": "../ar/contact.html",
        },
    }
    expected_routes = ["general", "rfq", "supplier", "partner"]
    required_names = {"topic", "contactName", "email", "message", "consent"}
    optional_names = {"company", "phone"}

    for lang, spec in specs.items():
        p = R / lang / "contact.html"
        text = p.read_text(encoding="utf-8")
        soup = BeautifulSoup(text, "html.parser")
        failures = []

        if soup.html.get("lang") != lang or soup.html.get("dir") != spec["dir"]:
            failures.append("lang-dir")
        h1s = soup.find_all("h1")
        if len(h1s) != 1 or h1s[0].get_text(" ", strip=True) != spec["h1"]:
            failures.append("h1")
        if lang == "ar" and spec["support"] not in text:
            failures.append("canonical-support")

        cards = soup.select("[data-pg27-route-card]")
        routes = [x.get("data-pg27-route-card") for x in cards]
        if routes != expected_routes:
            failures.append("route-cards:" + str(routes))
        buttons = soup.select("[data-pg27-route]")
        if [x.get("data-pg27-route") for x in buttons] != expected_routes:
            failures.append("route-buttons")

        email_hooks = {
            "general": ("trade", "general"),
            "rfq": ("rfq", "rfq"),
            "supplier": ("suppliers", "supplier"),
            "partner": ("partners", "partner"),
        }
        for route, (hook, local) in email_hooks.items():
            if not soup.select_one(f'[data-pg27-email="{local}"][data-orx-email="{hook}"]'):
                failures.append("email-hook:" + route)

        if not soup.select_one("[data-orx-phone]"):
            failures.append("phone-hook")
        if len(soup.select("[data-orx-address]")) < 2:
            failures.append("address-hooks")
        if len(soup.select("[data-orx-business-hours]")) < 2:
            failures.append("business-hours-hooks")
        if len(soup.select("[data-pg27-social] [data-orx-social-link]")) != 6:
            failures.append("social-hooks")

        form = soup.select_one("form[data-pg27-form]")
        if not form:
            failures.append("form")
            fields = {}
        else:
            if form.get("action") or form.get("method"):
                failures.append("form-network-attributes")
            fields = {x.get("name"): x for x in form.select("[name]")}
            if not required_names.issubset(fields):
                failures.append("required-field-set:" + str(sorted(fields)))
            if not optional_names.issubset(fields):
                failures.append("optional-field-set")
            for name in required_names:
                if name in fields and not fields[name].has_attr("required"):
                    failures.append("required-missing:" + name)
            if not form.has_attr("novalidate"):
                failures.append("novalidate-contract")
            topic = form.select_one("[data-pg27-topic-select]")
            if not topic or [o.get("value") for o in topic.find_all("option")] != expected_routes:
                failures.append("topic-options")

        if not soup.select_one('[data-pg27-error][role="alert"][hidden]'):
            failures.append("error-state")
        if not soup.select_one('[data-pg27-success][role="status"][hidden]'):
            failures.append("success-state")
        if lang == "en" and "no message was transmitted" not in text.lower():
            failures.append("demo-success-disclosure")
        if lang == "ar" and "لم يتم إرسال أي رسالة" not in text:
            failures.append("demo-success-disclosure")

        if soup.find("iframe") or "maps.googleapis.com" in text or "mapbox" in text.lower():
            failures.append("map-provider")
        if not soup.select_one(".orx-contact-map [data-orx-address]"):
            failures.append("map-placeholder")
        if not soup.select_one('[data-orx-mega-trigger][aria-current="page"]'):
            failures.append("explore-current")
        if not soup.select_one('.orx-mega-menu a[href="contact.html"][aria-current="page"]'):
            failures.append("mega-contact-current")
        if not soup.select_one('.orx-mobile-nav a[href="contact.html"][aria-current="page"]'):
            failures.append("mobile-contact-current")
        if not soup.find("a", class_="orx-lang-switch", href=lambda x: x and spec["other"] in x):
            failures.append("language-switch")

        footer = soup.select('footer[data-orx-global-footer="v1"]')
        if len(footer) != 1 or not footer[0].select_one("[data-orx-business-hours]"):
            failures.append("footer")
        canonical = soup.find("link", rel="canonical")
        if not canonical or canonical.get("href") != spec["canonical"]:
            failures.append("canonical")
        hreflangs = {x.get("hreflang") for x in soup.find_all("link", rel="alternate")}
        if not {"ar", "en", "x-default"}.issubset(hreflangs):
            failures.append("hreflang")

        try:
            data = json.loads(soup.find("script", attrs={"type": "application/ld+json"}).string)
            types = {x.get("@type") for x in data.get("@graph", [])}
            if not {"WebPage", "BreadcrumbList"}.issubset(types):
                failures.append("schema")
            prohibited = {"LocalBusiness", "Organization", "ContactPoint", "Product", "Offer", "Review", "Rating", "AggregateRating"}
            if types & prohibited:
                failures.append("prohibited-schema:" + str(sorted(types & prohibited)))
        except Exception:
            failures.append("schema-json")

        combined = soup.get_text(" ", strip=True).lower()
        if "demo" not in combined:
            failures.append("demo-boundary")
        if re.search(r"(?<!no )guaranteed response", combined) or any(
            x in combined for x in ("24/7 support", "instant response", "رد مضمون", "دعم 24/7")
        ):
            failures.append("response-claim")
        if "TARGET" in text or "targetft" in text.lower():
            failures.append("client-leak")

        icons = set(re.findall(r"sprite\.svg#([a-z0-9-]+)", text))
        missing = sorted(icons - sprite_ids)
        if missing:
            failures.append("icons:" + str(missing))

        source["pages"][lang] = {
            "failures": failures,
            "routes": routes,
            "formFields": sorted(x for x in fields if x),
        }
        source["failures"] += [lang + ":" + x for x in failures]

    for script, label in [
        (".github/scripts/normalize_global_navigation.py", "nav-drift"),
        (".github/scripts/normalize_global_footer.py", "footer-drift"),
    ]:
        run = subprocess.run(["python", script, "--check"], cwd=R, capture_output=True, text=True)
        if run.returncode:
            source["failures"].append(label)
            source[label] = run.stdout + run.stderr

    (O / "source-report.json").write_text(json.dumps(source, ensure_ascii=False, indent=2), encoding="utf-8")
    return source


def ready(driver):
    WebDriverWait(driver, 8).until(
        lambda x: x.find_element(By.CSS_SELECTOR, "[data-pg27-root]").get_attribute("data-pg27-ready") == "true"
    )


def rendered_qa():
    rendered = {"failures": [], "cases": [], "interaction": {}}
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=820,1900")
    server = subprocess.Popen(
        ["python", "-m", "http.server", "8765"],
        cwd=R,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(1)
    try:
        for lang in ("ar", "en"):
            driver = webdriver.Chrome(options=opts)
            try:
                for width in (390, 820, 1366, 1536):
                    failures = []
                    try:
                        driver.set_window_size(width, 1900)
                        driver.get(f"http://127.0.0.1:8765/{lang}/contact.html")
                        ready(driver)
                        root = driver.find_element(By.CSS_SELECTOR, "[data-pg27-root]")
                        if root.get_attribute("data-pg27-topic") != "general":
                            failures.append("initial-topic")
                        if root.get_attribute("data-pg27-form-state") != "idle":
                            failures.append("initial-form-state")
                        if len([x for x in driver.find_elements(By.CSS_SELECTOR, "[data-pg27-route-card]") if x.is_displayed()]) != 4:
                            failures.append("route-cards")
                        if driver.execute_script("return document.documentElement.scrollWidth") > driver.execute_script("return document.documentElement.clientWidth") + 1:
                            failures.append("overflow")
                        if driver.find_element(By.TAG_NAME, "html").get_attribute("dir") != ("rtl" if lang == "ar" else "ltr"):
                            failures.append("direction")
                        if driver.find_element(By.CSS_SELECTOR, "[data-orx-phone]").text.strip() != "+974 0000 0000":
                            failures.append("config-phone")
                        first_address = driver.find_elements(By.CSS_SELECTOR, "[data-orx-address]")[0].text
                        if lang == "en" and "Doha" not in first_address:
                            failures.append("config-address")
                        if lang == "ar" and "الدوحة" not in first_address:
                            failures.append("config-address")
                        if not driver.find_element(By.CSS_SELECTOR, "[data-pg27-social]").get_attribute("hidden"):
                            failures.append("social-default-hidden")

                        small = []
                        for element in driver.find_elements(By.CSS_SELECTOR, "a,button,input,select,textarea"):
                            if element.is_displayed() and element.rect["width"] and element.rect["height"] and (
                                element.rect["width"] < 24 or element.rect["height"] < 24
                            ):
                                small.append({
                                    "tag": element.tag_name,
                                    "w": round(element.rect["width"], 1),
                                    "h": round(element.rect["height"], 1),
                                    "text": element.text[:18],
                                })
                        if small:
                            failures.append("touch:" + json.dumps(small, ensure_ascii=False))

                        if width >= 1051:
                            trigger = driver.find_element(By.CSS_SELECTOR, "[data-orx-mega-trigger]")
                            trigger.click(); time.sleep(.04)
                            if trigger.get_attribute("aria-expanded") != "true":
                                failures.append("mega-open")
                            trigger.send_keys(Keys.ESCAPE); time.sleep(.04)
                            if trigger.get_attribute("aria-expanded") != "false":
                                failures.append("mega-escape")
                        else:
                            opener = driver.find_element(By.CSS_SELECTOR, "[data-orx-drawer-open]")
                            opener.click(); time.sleep(.04)
                            drawer = driver.find_element(By.CSS_SELECTOR, "[data-orx-mobile-drawer]")
                            if drawer.get_attribute("aria-hidden") != "false":
                                failures.append("drawer-open")
                            driver.find_element(By.CSS_SELECTOR, "[data-orx-drawer-close]").click(); time.sleep(.04)
                            if drawer.get_attribute("aria-hidden") != "true":
                                failures.append("drawer-close")
                    except Exception as exc:
                        failures.append(type(exc).__name__ + ":" + str(exc)[:260])
                    rendered["cases"].append({"lang": lang, "width": width, "failures": failures})
                    rendered["failures"] += [f"{lang}-{width}:{x}" for x in failures]

                failures = []
                try:
                    driver.get(f"http://127.0.0.1:8765/{lang}/contact.html")
                    ready(driver)
                    driver.find_element(By.CSS_SELECTOR, '[data-pg27-route="rfq"]').click(); time.sleep(.12)
                    root = driver.find_element(By.CSS_SELECTOR, "[data-pg27-root]")
                    if root.get_attribute("data-pg27-topic") != "rfq": failures.append("root-topic")
                    if driver.find_element(By.CSS_SELECTOR, "[data-pg27-topic-select]").get_attribute("value") != "rfq": failures.append("select-topic")
                    if "topic=rfq" not in driver.current_url: failures.append("url-topic")
                    if driver.find_element(By.CSS_SELECTOR, '[data-pg27-route-card="rfq"]').get_attribute("data-active") != "true": failures.append("active-card")
                    if driver.find_element(By.CSS_SELECTOR, "[data-pg27-route-email]").text.strip() != "rfq@example.com": failures.append("summary-email")
                except Exception as exc:
                    failures.append(type(exc).__name__ + ":" + str(exc)[:260])
                rendered["interaction"][lang + "-route"] = failures
                rendered["failures"] += [lang + "-route:" + x for x in failures]

                failures = []
                try:
                    driver.get(f"http://127.0.0.1:8765/{lang}/contact.html?topic=supplier")
                    ready(driver)
                    root = driver.find_element(By.CSS_SELECTOR, "[data-pg27-root]")
                    if root.get_attribute("data-pg27-topic") != "supplier": failures.append("query-hydration")
                    links = driver.find_elements(By.CSS_SELECTOR, ".orx-lang-switch,.orx-mobile-nav a[lang]")
                    if len(links) < 2: failures.append("language-links")
                    if any("topic=supplier" not in a.get_attribute("href") for a in links): failures.append("language-topic")
                except Exception as exc:
                    failures.append(type(exc).__name__ + ":" + str(exc)[:260])
                rendered["interaction"][lang + "-query-language"] = failures
                rendered["failures"] += [lang + "-query-language:" + x for x in failures]

                failures = []
                try:
                    driver.get(f"http://127.0.0.1:8765/{lang}/contact.html?topic=unknown")
                    ready(driver)
                    root = driver.find_element(By.CSS_SELECTOR, "[data-pg27-root]")
                    if root.get_attribute("data-pg27-topic") != "general": failures.append("invalid-fallback")
                    if "topic=general" not in driver.current_url: failures.append("invalid-url-normalize")
                except Exception as exc:
                    failures.append(type(exc).__name__ + ":" + str(exc)[:260])
                rendered["interaction"][lang + "-invalid-topic"] = failures
                rendered["failures"] += [lang + "-invalid-topic:" + x for x in failures]

                failures = []
                try:
                    driver.get(f"http://127.0.0.1:8765/{lang}/contact.html?topic=partner")
                    ready(driver)
                    form = driver.find_element(By.CSS_SELECTOR, "[data-pg27-form]")
                    root = driver.find_element(By.CSS_SELECTOR, "[data-pg27-root]")

                    # Trigger the real submit event without coupling the form-state test to viewport pointer scrolling.
                    driver.execute_script("arguments[0].requestSubmit()", form); time.sleep(.08)
                    if root.get_attribute("data-pg27-form-state") != "invalid": failures.append("invalid-state")
                    if not driver.find_element(By.CSS_SELECTOR, "[data-pg27-error]").is_displayed(): failures.append("error-visible")

                    name = driver.find_element(By.NAME, "contactName")
                    email = driver.find_element(By.NAME, "email")
                    message = driver.find_element(By.NAME, "message")
                    consent = driver.find_element(By.NAME, "consent")
                    name.send_keys("Demo Contact")
                    email.send_keys("buyer@example.com")
                    message.send_keys("Demo commercial enquiry for validation only.")

                    # Keyboard interaction verifies the checkbox can be operated without a pointer.
                    consent.send_keys(Keys.SPACE); time.sleep(.04)
                    if not consent.is_selected(): failures.append("consent-keyboard")

                    driver.execute_script("arguments[0].requestSubmit()", form); time.sleep(.08)
                    if root.get_attribute("data-pg27-form-state") != "demo-confirmed": failures.append("success-state")
                    if not driver.find_element(By.CSS_SELECTOR, "[data-pg27-success]").is_displayed(): failures.append("success-visible")
                    if name.get_attribute("value") != "Demo Contact": failures.append("form-cleared")

                    # Native reset button remains a real click target and validates the public interaction path.
                    reset = driver.find_element(By.CSS_SELECTOR, '[data-pg27-form] button[type="reset"]')
                    driver.execute_script("arguments[0].scrollIntoView({block:'center'})", reset); time.sleep(.04)
                    reset.click(); time.sleep(.08)
                    if root.get_attribute("data-pg27-form-state") != "idle": failures.append("reset-state")
                    if root.get_attribute("data-pg27-topic") != "general": failures.append("reset-topic")
                    if name.get_attribute("value") != "": failures.append("reset-fields")
                except Exception as exc:
                    failures.append(type(exc).__name__ + ":" + str(exc)[:260])
                rendered["interaction"][lang + "-form"] = failures
                rendered["failures"] += [lang + "-form:" + x for x in failures]
            finally:
                driver.quit()
    finally:
        server.terminate()
        server.wait(timeout=5)

    (O / "rendered-report.json").write_text(json.dumps(rendered, ensure_ascii=False, indent=2), encoding="utf-8")
    return rendered


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
