#!/usr/bin/env python3
"""PG32 QA V3 — V2 source contract + hardened interactions after N03 geometry correction."""
from urllib.parse import urlparse
import json, subprocess, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from qa_pg32_components_v2 import R, O, source_qa, offenders


def rendered_qa():
    out={"failures":[],"cases":[],"interaction":{},"diagnostics":{}}
    opt=Options(); opt.add_argument("--headless=new"); opt.add_argument("--no-sandbox"); opt.add_argument("--disable-dev-shm-usage"); opt.add_argument("--window-size=1366,2200")
    server=subprocess.Popen(["python","-m","http.server","8774"],cwd=R,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
    try:
      for lang in ("ar","en"):
        d=webdriver.Chrome(options=opt)
        try:
          for width in (390,820,1366,1536):
            f=[]; detail={}
            try:
              d.set_window_size(width,2200); d.get(f"http://127.0.0.1:8774/{lang}/components.html"); time.sleep(.35)
              if d.find_element(By.TAG_NAME,"html").get_attribute("dir") != ("rtl" if lang=="ar" else "ltr"): f.append("direction")
              sw=d.execute_script("return document.documentElement.scrollWidth"); cw=d.execute_script("return document.documentElement.clientWidth"); detail={"scrollWidth":sw,"clientWidth":cw}
              if sw>cw+1: f.append("document-overflow"); detail["offenders"]=offenders(d)
              if len(d.find_elements(By.TAG_NAME,"h1"))!=1: f.append("h1")
              if d.find_element(By.TAG_NAME,"html").get_attribute("data-pg32-diagnostics")!="ready": f.append("diagnostics-ready")
              rows=d.find_elements(By.CSS_SELECTOR,"[data-lab-diagnostic-row]")
              if len(rows)!=9: f.append("diagnostics-count")
              if any(r.get_attribute("data-state") not in ("aligned","backfit") for r in rows): f.append("diagnostics-wait")
              if not d.find_element(By.CSS_SELECTOR,".orx-lab-boundary").is_displayed(): f.append("boundary")
            except Exception as e: f.append(type(e).__name__+":"+str(e)[:220])
            out["cases"].append({"lang":lang,"width":width,"failures":f,**detail}); out["failures"] += [f"{lang}-{width}:"+x for x in f]

          f=[]; step="start"
          try:
            d.set_window_size(1366,2200); d.get(f"http://127.0.0.1:8774/{lang}/components.html"); time.sleep(.3)
            rows=d.find_elements(By.CSS_SELECTOR,"[data-lab-diagnostic-row]"); states={r.get_attribute("data-lab-diagnostic-row"):r.get_attribute("data-state") for r in rows}; out["diagnostics"][lang]=states
            if "backfit" not in states.values(): f.append("no-backfit")

            step="mega"
            trigger=d.find_element(By.CSS_SELECTOR,"[data-orx-mega-trigger]"); trigger.click(); time.sleep(.05)
            if trigger.get_attribute("aria-expanded")!="true": f.append("mega-open")
            trigger.send_keys(Keys.ESCAPE); time.sleep(.05)
            if trigger.get_attribute("aria-expanded")!="false": f.append("mega-escape")

            step="tabs-keyboard"
            tabs=d.find_elements(By.CSS_SELECTOR,"[data-orx-tabs] [role='tab']")
            d.execute_script("arguments[0].scrollIntoView({block:'center'}); arguments[0].focus();",tabs[0]); tabs[0].send_keys(Keys.ARROW_RIGHT); time.sleep(.1)
            if not any(t.get_attribute("aria-selected")=="true" and t.id!=tabs[0].id for t in tabs): f.append("tabs-keyboard")

            step="accordion"
            acc=d.find_elements(By.CSS_SELECTOR,"[data-orx-accordion-trigger]")[1]; before=acc.get_attribute("aria-expanded"); d.execute_script("arguments[0].scrollIntoView({block:'center'}); arguments[0].click();",acc); time.sleep(.08)
            if acc.get_attribute("aria-expanded")==before: f.append("accordion")

            step="form"
            form=d.find_element(By.CSS_SELECTOR,"[data-lab-demo-form]"); submit=form.find_element(By.CSS_SELECTOR,"button[type='submit']"); d.execute_script("arguments[0].scrollIntoView({block:'center'}); arguments[0].click();",submit); time.sleep(.1)
            if not form.find_element(By.CSS_SELECTOR,"[data-lab-form-success]").is_displayed(): f.append("form-success")

            step="modal"
            mt=d.find_element(By.CSS_SELECTOR,"[data-bs-toggle='modal']"); d.execute_script("arguments[0].scrollIntoView({block:'center'}); arguments[0].click();",mt); time.sleep(.4); modal=d.find_element(By.CSS_SELECTOR,".orx-lab-modal")
            if "show" not in (modal.get_attribute("class") or ""): f.append("modal-open")
            close=modal.find_element(By.CSS_SELECTOR,"[data-bs-dismiss='modal']"); close.click()
            for _ in range(20):
              if "show" not in (modal.get_attribute("class") or ""): break
              time.sleep(.1)
            if "show" in (modal.get_attribute("class") or ""): f.append("modal-close")

            step="language"
            href=d.find_element(By.CSS_SELECTOR,".orx-lang-switch").get_attribute("href"); expected="/en/components.html" if lang=="ar" else "/ar/components.html"
            if not urlparse(href).path.endswith(expected): f.append("language")
          except Exception as e: f.append(step+":"+type(e).__name__+":"+str(e)[:220])
          out["interaction"][lang+"-desktop"]=f; out["failures"] += [lang+"-desktop:"+x for x in f]

          f=[]; step="mobile"
          try:
            d.set_window_size(390,1800); d.get(f"http://127.0.0.1:8774/{lang}/components.html"); time.sleep(.22)
            op=d.find_element(By.CSS_SELECTOR,"[data-orx-drawer-open]"); op.click(); time.sleep(.1); dr=d.find_element(By.CSS_SELECTOR,"[data-orx-mobile-drawer]")
            if dr.get_attribute("aria-hidden")!="false": f.append("drawer-open")
            d.find_element(By.CSS_SELECTOR,"[data-orx-drawer-close]").click(); time.sleep(.1)
            if dr.get_attribute("aria-hidden")!="true": f.append("drawer-close")
          except Exception as e: f.append(step+":"+type(e).__name__+":"+str(e)[:220])
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
