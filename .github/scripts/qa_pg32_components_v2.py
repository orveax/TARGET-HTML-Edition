#!/usr/bin/env python3
"""ORIGEX PG32 QA V2 — registry-aware source checks + rendered diagnostics."""
from pathlib import Path
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import json, re, subprocess, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

R = Path(__file__).resolve().parents[2]
O = R / "qa/pg32-components"
O.mkdir(parents=True, exist_ok=True)
CARD_CLASSES = ["orx-feature-card","orx-product-card","orx-supplier-card","orx-market-card","orx-process-card","orx-metric-card","orx-certification-card","orx-resource-card","orx-case-study-card","orx-contact-card","orx-cta-card"]
CORE = [".orx-breadcrumb",".orx-tabs",".orx-accordion",".orx-pagination",".orx-search",".orx-filter-group",".orx-spec",".orx-stat-strip",".orx-trust-item",".orx-empty-state",".orx-alert",".orx-field",".orx-upload",".orx-form-status",".orx-product-media",".orx-logo-frame",".orx-editorial-media"]
PRIMS = [".orx-btn--primary",".orx-btn--secondary",".orx-text-action",".orx-icon-btn",".orx-badge",".orx-input",".orx-select",".orx-textarea",".orx-check",".orx-divider",".orx-icon-box"]


def source_qa():
    out = {"failures": [], "pages": {}, "labCss": [], "labJs": []}
    css = (R/"assets/css/origex-components-lab.css").read_text(encoding="utf-8")
    js = (R/"assets/js/origex-components-lab.js").read_text(encoding="utf-8")
    lowjs = js.lower()
    for pat in (r"(?:^|\})\s*\.orx-btn\s*\{", r"(?:^|\})\s*\.orx-input\s*\{", r"(?:^|\})\s*\.orx-card\s*\{", r"(?:^|\})\s*\.orx-icon-btn\s*\{"):
        if re.search(pat, css): out["labCss"].append("registered-root-override")
    for marker in (".orx-lab-table-wrap", ".orx-lab-diagnostic-row", ".orx-lab-do-dont", ".orx-lab-modal"):
        if marker not in css: out["labCss"].append("missing:"+marker)
    for banned in ("fetch(","xmlhttprequest","localstorage","sessionstorage","navigator.sendbeacon","style.setproperty"):
        if banned in lowjs: out["labJs"].append("network-storage-or-style:"+banned)
    for marker in ("getboundingclientrect", "dataset.pg32diagnostics", "preventdefault"):
        if marker not in lowjs: out["labJs"].append("missing:"+marker)
    out["failures"] += out["labCss"] + out["labJs"]

    specs = {
        "ar": {"dir":"rtl","h1":"مكونات ORIGEX بمحتوى واقعي جاهز للاختبار والتخصيص.","support":"استعرض الأزرار، الكروت، النماذج، الجداول، الحالات، والأنماط باستخدام أمثلة تجارية من نفس تجربة القالب.","other":"../en/components.html","canonical":"https://example.com/ar/components.html","bootstrap":"../assets/vendor/bootstrap/css/bootstrap.rtl.min.css"},
        "en": {"dir":"ltr","h1":"ORIGEX components demonstrated with realistic, customization-ready content.","support":"Explore buttons, cards, forms, tables, states and patterns using commercial examples from the same ORIGEX template experience.","other":"../ar/components.html","canonical":"https://example.com/en/components.html","bootstrap":"../assets/vendor/bootstrap/css/bootstrap.min.css"},
    }
    sprite = (R/"assets/icons/sprite.svg").read_text(encoding="utf-8")
    ids = set(re.findall(r'<symbol[^>]+id="([^"]+)"', sprite))
    for lang,spec in specs.items():
        text=(R/lang/"components.html").read_text(encoding="utf-8"); soup=BeautifulSoup(text,"html.parser"); f=[]
        visible=soup.get_text(" ",strip=True)
        if soup.html.get("lang")!=lang or soup.html.get("dir")!=spec["dir"]: f.append("lang-dir")
        h=soup.find_all("h1")
        if len(h)!=1 or h[0].get_text(" ",strip=True)!=spec["h1"]: f.append("h1")
        if spec["support"] not in visible: f.append("support")
        if not soup.find("link",rel="stylesheet",href=spec["bootstrap"]): f.append("bootstrap")
        can=soup.find("link",rel="canonical")
        if not can or can.get("href")!=spec["canonical"]: f.append("canonical")
        alts={(a.get("hreflang"),a.get("href")) for a in soup.find_all("link",rel="alternate")}
        if not {("ar","https://example.com/ar/components.html"),("en","https://example.com/en/components.html"),("x-default","https://example.com/en/components.html")}.issubset(alts): f.append("hreflang")
        if not soup.find("a",class_="orx-lang-switch",href=spec["other"]): f.append("lang-switch")
        ld=" ".join(x.get_text() for x in soup.find_all("script",attrs={"type":"application/ld+json"}))
        if '"WebPage"' not in ld or '"BreadcrumbList"' not in ld: f.append("schema")
        if any(x in ld for x in ('"Product"','"Offer"','"Review"')): f.append("strong-schema")
        if "BACKFIT" not in text or "Demo" not in text: f.append("lab-boundary")
        if "TARGET" in text or "targetft" in text.lower(): f.append("client-leak")
        if len([c for c in CARD_CLASSES if soup.select_one('.'+c)])!=11: f.append("cards-11")
        if len([s for s in CORE if soup.select_one(s)])!=17: f.append("core-17")
        if len([s for s in PRIMS if soup.select_one(s)])!=11: f.append("primitives-11")
        for fam in ("F01–07","P01–11","C01–28","S01–06","N01–04"):
            if fam not in visible: f.append("registry:"+fam)
        # Sample coverage is component-based, not English-keyword-based.
        for sel,label in ((".orx-product-card","product"),(".orx-supplier-card","supplier"),(".orx-market-card","market"),(".orx-certification-card","certification"),(".orx-resource-card","resource"),(".orx-alert","alert"),("[data-lab-demo-form]","rfq")):
            if not soup.select_one(sel): f.append("sample:"+label)
        for sel,label in (("[data-lab-error-input]","error"),("[data-bs-toggle='modal']","modal"),(".orx-lab-do-dont","do-dont"),(".orx-lab-social-slots","social"),(".orx-lab-table-wrap","table-wrap")):
            if not soup.select_one(sel): f.append(label)
        if len(soup.select("[data-lab-diagnostic-row]"))!=9: f.append("diagnostics-9")
        form=soup.select_one("[data-lab-demo-form]")
        if form and form.get("action"): f.append("form-action")
        if not soup.select_one("header[data-orx-global-nav='v1']"): f.append("nav")
        if not soup.select_one("footer[data-orx-global-footer='v1']"): f.append("footer")
        refs=set(re.findall(r"sprite\.svg#([a-z0-9-]+)",text)); missing=sorted(refs-ids)
        if missing: f.append("icons:"+str(missing))
        out["pages"][lang]={"failures":f,"cards":11-len([c for c in CARD_CLASSES if not soup.select_one('.'+c)]),"coreComponents":17-len([s for s in CORE if not soup.select_one(s)]),"primitives":11-len([s for s in PRIMS if not soup.select_one(s)]),"diagnosticRows":len(soup.select('[data-lab-diagnostic-row]')),"iconCount":len(refs)}
        out["failures"] += [lang+":"+x for x in f]
    for script,label in ((".github/scripts/normalize_global_navigation.py","nav-drift"),(".github/scripts/normalize_global_footer.py","footer-drift")):
        p=subprocess.run(["python",script,"--check"],cwd=R,capture_output=True,text=True)
        if p.returncode: out["failures"].append(label); out[label]=p.stdout+p.stderr
    (O/"source-report.json").write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf-8")
    return out


def offenders(driver):
    return driver.execute_script("""
      const w=document.documentElement.clientWidth;
      return [...document.querySelectorAll('body *')].map(el=>{const r=el.getBoundingClientRect();return {tag:el.tagName.toLowerCase(),cls:(el.className&&typeof el.className==='string')?el.className.slice(0,120):'',left:Math.round(r.left),right:Math.round(r.right),width:Math.round(r.width),scroll:el.scrollWidth}}).filter(x=>x.right>w+1||x.left<-1).slice(0,12);
    """)


def rendered_qa():
    out={"failures":[],"cases":[],"interaction":{},"diagnostics":{}}
    opt=Options(); opt.add_argument("--headless=new"); opt.add_argument("--no-sandbox"); opt.add_argument("--disable-dev-shm-usage"); opt.add_argument("--window-size=1366,2200")
    server=subprocess.Popen(["python","-m","http.server","8773"],cwd=R,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
    try:
      for lang in ("ar","en"):
        d=webdriver.Chrome(options=opt)
        try:
          for width in (390,820,1366,1536):
            f=[]; detail={}
            try:
              d.set_window_size(width,2200); d.get(f"http://127.0.0.1:8773/{lang}/components.html"); time.sleep(.35)
              if d.find_element(By.TAG_NAME,"html").get_attribute("dir") != ("rtl" if lang=="ar" else "ltr"): f.append("direction")
              sw=d.execute_script("return document.documentElement.scrollWidth"); cw=d.execute_script("return document.documentElement.clientWidth")
              detail={"scrollWidth":sw,"clientWidth":cw}
              if sw>cw+1: f.append("document-overflow"); detail["offenders"]=offenders(d)
              if len(d.find_elements(By.TAG_NAME,"h1"))!=1: f.append("h1")
              if d.find_element(By.TAG_NAME,"html").get_attribute("data-pg32-diagnostics")!="ready": f.append("diagnostics-ready")
              rows=d.find_elements(By.CSS_SELECTOR,"[data-lab-diagnostic-row]")
              if len(rows)!=9: f.append("diagnostics-count")
              if any(r.get_attribute("data-state") not in ("aligned","backfit") for r in rows): f.append("diagnostics-wait")
            except Exception as e: f.append(type(e).__name__+":"+str(e)[:220])
            out["cases"].append({"lang":lang,"width":width,"failures":f,**detail}); out["failures"] += [f"{lang}-{width}:"+x for x in f]

          f=[]
          try:
            d.set_window_size(1366,2200); d.get(f"http://127.0.0.1:8773/{lang}/components.html"); time.sleep(.3)
            rows=d.find_elements(By.CSS_SELECTOR,"[data-lab-diagnostic-row]"); states={r.get_attribute("data-lab-diagnostic-row"):r.get_attribute("data-state") for r in rows}; out["diagnostics"][lang]=states
            if "backfit" not in states.values(): f.append("no-backfit")
            trigger=d.find_element(By.CSS_SELECTOR,"[data-orx-mega-trigger]"); trigger.click(); time.sleep(.05)
            if trigger.get_attribute("aria-expanded")!="true": f.append("mega-open")
            trigger.send_keys(Keys.ESCAPE); time.sleep(.05)
            if trigger.get_attribute("aria-expanded")!="false": f.append("mega-escape")
            tabs=d.find_elements(By.CSS_SELECTOR,"[data-orx-tabs] [role='tab']"); d.execute_script("arguments[0].scrollIntoView({block:'center'})",tabs[0]); tabs[0].click(); tabs[0].send_keys(Keys.ARROW_RIGHT); time.sleep(.08)
            if not any(t.get_attribute("aria-selected")=="true" and t.id!=tabs[0].id for t in tabs): f.append("tabs-keyboard")
            acc=d.find_elements(By.CSS_SELECTOR,"[data-orx-accordion-trigger]")[1]; d.execute_script("arguments[0].scrollIntoView({block:'center'})",acc); before=acc.get_attribute("aria-expanded"); acc.click(); time.sleep(.05)
            if acc.get_attribute("aria-expanded")==before: f.append("accordion")
            form=d.find_element(By.CSS_SELECTOR,"[data-lab-demo-form]"); submit=form.find_element(By.CSS_SELECTOR,"button[type='submit']"); d.execute_script("arguments[0].scrollIntoView({block:'center'}); arguments[0].click();",submit); time.sleep(.08)
            if not form.find_element(By.CSS_SELECTOR,"[data-lab-form-success]").is_displayed(): f.append("form-success")
            mt=d.find_element(By.CSS_SELECTOR,"[data-bs-toggle='modal']"); d.execute_script("arguments[0].scrollIntoView({block:'center'}); arguments[0].click();",mt); time.sleep(.2); modal=d.find_element(By.CSS_SELECTOR,".orx-lab-modal")
            if "show" not in (modal.get_attribute("class") or ""): f.append("modal-open")
            close=modal.find_element(By.CSS_SELECTOR,"[data-bs-dismiss='modal']"); d.execute_script("arguments[0].click();",close); time.sleep(.2)
            if "show" in (modal.get_attribute("class") or ""): f.append("modal-close")
            href=d.find_element(By.CSS_SELECTOR,".orx-lang-switch").get_attribute("href"); expected="/en/components.html" if lang=="ar" else "/ar/components.html"
            if not urlparse(href).path.endswith(expected): f.append("language")
          except Exception as e: f.append(type(e).__name__+":"+str(e)[:250])
          out["interaction"][lang+"-desktop"]=f; out["failures"] += [lang+"-desktop:"+x for x in f]

          f=[]
          try:
            d.set_window_size(390,1800); d.get(f"http://127.0.0.1:8773/{lang}/components.html"); time.sleep(.2); op=d.find_element(By.CSS_SELECTOR,"[data-orx-drawer-open]"); op.click(); time.sleep(.08); dr=d.find_element(By.CSS_SELECTOR,"[data-orx-mobile-drawer]")
            if dr.get_attribute("aria-hidden")!="false": f.append("drawer-open")
            d.find_element(By.CSS_SELECTOR,"[data-orx-drawer-close]").click(); time.sleep(.08)
            if dr.get_attribute("aria-hidden")!="true": f.append("drawer-close")
          except Exception as e: f.append(type(e).__name__+":"+str(e)[:220])
          out["interaction"][lang+"-mobile"]=f; out["failures"] += [lang+"-mobile:"+x for x in f]
        finally: d.quit()
    finally:
      server.terminate()
      try: server.wait(timeout=2)
      except Exception: server.kill()
    (O/"rendered-report.json").write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf-8")
    return out


def main():
    s=source_qa(); r=rendered_qa(); failures=s["failures"]+r["failures"]; status="PASS" if not failures else "FAIL"
    (O/"run-status.txt").write_text(status+"\n",encoding="utf-8"); print(json.dumps({"status":status,"failures":failures},ensure_ascii=False,indent=2)); raise SystemExit(1 if failures else 0)
if __name__=="__main__": main()
