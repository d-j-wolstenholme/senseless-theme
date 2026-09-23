import json, re, sys, time, random, urllib.request, os, glob
UAS=["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36",
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36",
     "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1"]
def get(url):
    req=urllib.request.Request(url,headers={"User-Agent":random.choice(UAS),"Accept":"text/html","Cache-Control":"no-cache"})
    with urllib.request.urlopen(req,timeout=30) as r:
        return r.status, r.geturl(), r.read().decode('utf-8','replace')
def parse(html):
    blocks=re.findall(r'<script([^>]*type="application/ld\+json"[^>]*)>(.*?)</script>',html,re.S)
    canon=re.findall(r'<link[^>]+rel="canonical"[^>]*>',html)
    og=re.findall(r'<meta[^>]+property="(og:[^"]+)"[^>]+content="([^"]*)"',html)
    return blocks,canon,og
os.makedirs('jsonld',exist_ok=True); os.makedirs('html',exist_ok=True)
targets=json.load(open('targets.json'))
out={}
for label,url in targets:
    cb=f"cb={int(time.time()*1000)}{random.randint(100,999)}"
    full=url+("&" if "?" in url else "?")+cb
    if os.path.exists(f'jsonld/{label}.json'):
        continue
    for attempt in range(4):
        try:
            st,final,html=get(full); break
        except Exception as e:
            print('retry',label,e); time.sleep(3)
    else:
        print('FAILED',label); continue
    open(f'html/{label}.html','w').write(html)
    blocks,canon,og=parse(html)
    raw=[]
    for attrs,body in blocks:
        raw.append({"attrs":attrs.strip(),"body":body.strip()})
    json.dump({"url_requested":full,"status":st,"final_url":final,"fetched_utc":time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),"canonical_tags":canon,"og":og,"ld_json_blocks":raw},open(f'jsonld/{label}.json','w'),indent=1)
    print(label,st,len(blocks),'blocks',canon)
    time.sleep(0.6)
