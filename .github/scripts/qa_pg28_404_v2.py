#!/usr/bin/env python3
"""ORIGEX PG28 404 QA V2 — source, SEO, recovery, rendered and interaction gate."""
from pathlib import Path
from bs4 import BeautifulSoup
import json, re, subprocess, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

R = Path(__file__).resolve().parents[2]
O = R / "qa/pg28-404"
O.mkdir(parents=True, exist_ok=True)
ROUTES = ["index.html", "products.html", "suppliers.html", "resources.html", "faq.html", "contact.html"]


def source_qa():
    out = {"failures": [], "pages": {}, "runtime": {}}
    js = (R / "assets/js/origex-404.js").read_text(encoding="utf-8")
    rf = []
    for bad in ("fetch(", "XMLHttpRequest", "localStorage", "sessionStorage"):
        if bad in js:
            rf.append("forbidden-runtime:" + bad)
    for token in (
        "data-pg28-root", "data-pg28-search", "data-pg28-recovery-card", "data-pg28-count",
        "data-pg28-empty", "data-pg28-reset", "history.replaceState", "orx-lang-switch",
        "orx-mobile-nav a[lang]", "pg28Ready",
    ):
        if token not in js:
            rf.append("runtime-missing:" + token)
    out["runtime"] = {"failures": rf}
    out["failures"] += rf

    sprite = (R / "assets/icons/sprite.svg").read_text(encoding="utf-8")
    sprite_ids = set(re.findall(r'<symbol[^>]+id="([^"]+)"', sprite))
    specs = {
        "ar": {
            "dir": "rtl", "h1": "الصفحة غير موجودة، لكن المسار واضح.",
            "support": "ربما تغير الرابط أو تم نقله. ارجع إلى المنتجات أو الموردين أو تواصل معنا للوصول للمعلومة المطلوبة.",
            "home": "العودة للرئيسية", "products": "استعرض المنتجات", "other": "../en/404.html",
        },
        "en": {
            "dir": "ltr", "h1": "This page is unavailable, but the route is clear.",
            "home": "Back to Home", "products": "Explore Products", "other": "../ar/404.html",
        },
    }

    for lang, spec in specs.items():
        p = R / lang / "404.html"
        text = p.read_text(encoding="utf-8")
        soup = BeautifulSoup(text, "html.parser")
        f = []
        if soup.html.get("lang") != lang or soup.html.get("dir") != spec["dir"]: f.append("lang-dir")
        h1s = soup.find_all("h1")
        if len(h1s) != 1 or h1s[0].get_text(" ", strip=True) != spec["h1"]: f.append("h1")
        if lang == "ar" and spec["support"] not in text: f.append("canonical-support")
        hero = soup.select_one(".orx-error-hero")
        if not hero: f.append("hero")
        else:
            ht = hero.get_text(" ", strip=True)
            if spec["home"] not in ht: f.append("home-cta")
            if spec["products"] not in ht: f.append("products-cta")

        robots = soup.find("meta", attrs={"name": "robots"})
        if not robots or robots.get("content", "").replace(" ", "").lower() != "noindex,follow": f.append("robots-noindex")
        if soup.find("link", rel="canonical"): f.append("unexpected-canonical")
        if soup.find("link", rel="alternate"): f.append("unexpected-hreflang")
        if soup.find("script", attrs={"type": "application/ld+json"}): f.append("unexpected-structured-data")
        for prop in ("og:type", "og:title", "og:description", "og:url", "og:image"):
            if not soup.find("meta", attrs={"property": prop}): f.append("missing-" + prop)

        cards = soup.select("[data-pg28-recovery-card]")
        hrefs = [c.select_one("a[href]").get("href") if c.select_one("a[href]") else "" for c in cards]
        if len(cards) != 6: f.append("recovery-count:" + str(len(cards)))
        if hrefs != ROUTES: f.append("recovery-order:" + str(hrefs))
        if any(c.has_attr("hidden") for c in cards): f.append("progressive-enhancement-hidden-card")
        for href in hrefs:
            if href and not (R / lang / href).exists(): f.append("missing-recovery-target:" + href)

        if not soup.select_one("[data-pg28-search]"): f.append("search-field")
        if not soup.select_one('[data-pg28-count][aria-live="polite"]'): f.append("result-count-live")
        if not soup.select_one('[data-pg28-empty][role="status"][hidden]'): f.append("empty-state")
        if len(soup.select("[data-pg28-reset]")) < 2: f.append("reset-controls")
        empty = soup.select_one("[data-pg28-empty]")
        if not empty or not empty.select_one('a[href="contact.html"]'): f.append("contact-fallback")
        if not soup.select_one('[data-orx-mega-trigger][aria-current="page"]'): f.append("explore-current")
        if soup.select_one('.orx-mega-menu [aria-current="page"]'): f.append("unexpected-mega-current")
        if soup.select_one('.orx-mobile-nav [aria-current="page"]'): f.append("unexpected-mobile-current")
        if not soup.find("a", class_="orx-lang-switch", href=lambda x: x and spec["other"] in x): f.append("language-switch")
        if len(soup.select('footer[data-orx-global-footer="v1"]')) != 1: f.append("footer")
        if soup.find("form"): f.append("unexpected-form")
        if soup.find("iframe") or "maps.googleapis.com" in text or "mapbox" in text.lower(): f.append("unexpected-provider")
        if "HTTP 404" not in text: f.append("deployment-status-note")
        if "TARGET" in text or "targetft" in text.lower(): f.append("client-leak")
        scripts = [s.get("src", "") for s in soup.find_all("script") if s.get("src")]
        if not scripts or scripts[-1] != "../assets/js/origex-404.js": f.append("runtime-order")
        icons = set(re.findall(r"sprite\.svg#([a-z0-9-]+)", text))
        missing = sorted(icons - sprite_ids)
        if missing: f.append("icons:" + str(missing))
        out["pages"][lang] = {"failures": f, "recoveryRoutes": hrefs, "iconCount": len(icons)}
        out["failures"] += [lang + ":" + x for x in f]

    for script, label in [
        (".github/scripts/normalize_global_navigation.py", "nav-drift"),
        (".github/scripts/normalize_global_footer.py", "footer-drift"),
    ]:
        run = subprocess.run(["python", script, "--check"], cwd=R, capture_output=True, text=True)
        if run.returncode:
            out["failures"].append(label)
            out[label] = run.stdout + run.stderr
    (O / "source-report.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    return out


def ready(driver):
    WebDriverWait(driver, 8).until(lambda d: d.find_element(By.CSS_SELECTOR, "[data-pg28-root]").get_attribute("data-pg28-ready") == "true")


def count(driver):
    try:
        return int(driver.find_element(By.CSS_SELECTOR, "[data-pg28-root]").get_attribute("data-pg28-result-count") or "0")
    except ValueError:
        return -1


def rendered_qa():
    out = {"failures": [], "cases": [], "interaction": {}}
    opts = Options()
    for arg in ("--headless=new", "--no-sandbox", "--disable-dev-shm-usage", "--window-size=820,1900"):
        opts.add_argument(arg)
    server = subprocess.Popen(["python", "-m", "http.server", "8765"], cwd=R, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    try:
        for lang in ("ar", "en"):
            d = webdriver.Chrome(options=opts)
            try:
                for width in (390, 820, 1366, 1536):
                    f = []
                    try:
                        d.set_window_size(width, 1900)
                        d.get(f"http://127.0.0.1:8765/{lang}/404.html")
                        ready(d)
                        if count(d) != 6: f.append("initial-count")
                        if len([c for c in d.find_elements(By.CSS_SELECTOR, "[data-pg28-recovery-card]") if c.is_displayed()]) != 6: f.append("initial-cards")
                        if d.execute_script("return document.documentElement.scrollWidth") > d.execute_script("return document.documentElement.clientWidth") + 1: f.append("overflow")
                        if d.find_element(By.TAG_NAME, "html").get_attribute("dir") != ("rtl" if lang == "ar" else "ltr"): f.append("direction")
                        if d.find_element(By.CSS_SELECTOR, 'meta[name="robots"]').get_attribute("content").replace(" ", "").lower() != "noindex,follow": f.append("robots")
                        small = []
                        for e in d.find_elements(By.CSS_SELECTOR, "a,button,input"):
                            if e.is_displayed() and e.rect["width"] and e.rect["height"] and (e.rect["width"] < 24 or e.rect["height"] < 24):
                                small.append({"tag": e.tag_name, "w": round(e.rect["width"], 1), "h": round(e.rect["height"], 1), "text": e.text[:20]})
                        if small: f.append("touch:" + json.dumps(small, ensure_ascii=False))
                        if width >= 1051:
                            t = d.find_element(By.CSS_SELECTOR, "[data-orx-mega-trigger]"); t.click(); time.sleep(.04)
                            if t.get_attribute("aria-expanded") != "true": f.append("mega-open")
                            t.send_keys(Keys.ESCAPE); time.sleep(.04)
                            if t.get_attribute("aria-expanded") != "false": f.append("mega-escape")
                        else:
                            op = d.find_element(By.CSS_SELECTOR, "[data-orx-drawer-open]"); op.click(); time.sleep(.04)
                            drawer = d.find_element(By.CSS_SELECTOR, "[data-orx-mobile-drawer]")
                            if drawer.get_attribute("aria-hidden") != "false": f.append("drawer-open")
                            d.find_element(By.CSS_SELECTOR, "[data-orx-drawer-close]").click(); time.sleep(.04)
                            if drawer.get_attribute("aria-hidden") != "true": f.append("drawer-close")
                    except Exception as exc:
                        f.append(type(exc).__name__ + ":" + str(exc)[:240])
                    out["cases"].append({"lang": lang, "width": width, "failures": f})
                    out["failures"] += [f"{lang}-{width}:{x}" for x in f]

                f = []
                try:
                    d.get(f"http://127.0.0.1:8765/{lang}/404.html"); ready(d)
                    search = d.find_element(By.CSS_SELECTOR, "[data-pg28-search]")
                    search.send_keys("مورد" if lang == "ar" else "supplier"); time.sleep(.1)
                    result_count = count(d)
                    if result_count < 1 or result_count >= 6: f.append("search-count")
                    visible = [c for c in d.find_elements(By.CSS_SELECTOR, "[data-pg28-recovery-card]") if c.is_displayed()]
                    if not any("suppliers.html" in c.find_element(By.CSS_SELECTOR, "a[href]").get_attribute("href") for c in visible): f.append("search-route")
                    if "?q=" not in d.current_url: f.append("search-url")
                    links = d.find_elements(By.CSS_SELECTOR, ".orx-lang-switch,.orx-mobile-nav a[lang]")
                    if len(links) < 2 or any("?q=" not in link.get_attribute("href") for link in links): f.append("language-query")
                except Exception as exc:
                    f.append(type(exc).__name__ + ":" + str(exc)[:240])
                out["interaction"][lang + "-search"] = f; out["failures"] += [lang + "-search:" + x for x in f]

                f = []
                try:
                    d.get(f"http://127.0.0.1:8765/{lang}/404.html"); ready(d)
                    search = d.find_element(By.CSS_SELECTOR, "[data-pg28-search]")
                    search.send_keys("zzzz-no-route"); time.sleep(.08)
                    if count(d) != 0: f.append("empty-count")
                    if not d.find_element(By.CSS_SELECTOR, "[data-pg28-empty]").is_displayed(): f.append("empty-visible")
                    d.find_element(By.CSS_SELECTOR, "[data-pg28-empty] [data-pg28-reset]").send_keys(Keys.ENTER); time.sleep(.08)
                    if count(d) != 6: f.append("reset-count")
                    if search.get_attribute("value") != "": f.append("reset-query")
                    if d.find_element(By.CSS_SELECTOR, "[data-pg28-empty]").is_displayed(): f.append("reset-empty")
                except Exception as exc:
                    f.append(type(exc).__name__ + ":" + str(exc)[:240])
                out["interaction"][lang + "-empty-reset"] = f; out["failures"] += [lang + "-empty-reset:" + x for x in f]

                f = []
                try:
                    d.get(f"http://127.0.0.1:8765/{lang}/404.html?q=supplier"); ready(d)
                    search = d.find_element(By.CSS_SELECTOR, "[data-pg28-search]")
                    if search.get_attribute("value") != "supplier": f.append("query-hydration")
                    result_count = count(d)
                    if result_count < 1 or result_count >= 6: f.append("query-count")
                    visible = [c for c in d.find_elements(By.CSS_SELECTOR, "[data-pg28-recovery-card]") if c.is_displayed()]
                    if not any("suppliers.html" in c.find_element(By.CSS_SELECTOR, "a[href]").get_attribute("href") for c in visible): f.append("query-route")
                    search.send_keys(Keys.ESCAPE); time.sleep(.08)
                    if search.get_attribute("value") != "": f.append("escape-clear")
                    if count(d) != 6: f.append("escape-count")
                    if "?q=" in d.current_url: f.append("escape-url")
                except Exception as exc:
                    f.append(type(exc).__name__ + ":" + str(exc)[:240])
                out["interaction"][lang + "-query-escape"] = f; out["failures"] += [lang + "-query-escape:" + x for x in f]
            finally:
                d.quit()
    finally:
        server.terminate(); server.wait(timeout=5)
    (O / "rendered-report.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    return out


def main():
    source = source_qa(); rendered = rendered_qa()
    failures = source["failures"] + rendered["failures"]
    status = "PASS" if not failures else "FAIL"
    (O / "run-status.txt").write_text(status + "\n", encoding="utf-8")
    print(status, "source", len(source["failures"]), "rendered", len(rendered["failures"]))
    if failures:
        print("\n".join(failures)); raise SystemExit(1)


if __name__ == "__main__":
    main()
