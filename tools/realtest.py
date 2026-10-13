# Uruchom z katalogu repo: python3 tools/realtest.py  (wymaga: pip install playwright; Chromium)
# Symulacja realnych iPhone'ów w trybie apki: górna wstawka (wyspa/status bar) + obcięty dół w iOS 26.
from playwright.sync_api import sync_playwright
import os,sys
DEV={'16pro':(393,791,59,852),'se':(375,667,20,667),'promax':(440,895,62,956)}
def k(pg,pad,key): pg.click(f'.kp[data-pad="{pad}"] button[data-k="{key}"]')
def page(b,dev,sch):
    w,h,top,sh=DEV[dev]
    pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=2,color_scheme=sch,has_touch=True,is_mobile=True)
    pg.add_init_script(f"""Object.defineProperty(navigator,'standalone',{{get:()=>true}});Object.defineProperty(screen,'height',{{get:()=>{sh}}});
    """)
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    src=open('index.html').read().replace('</title>','</title><style>body{padding-top:%dpx!important}</style>'%top,1)
    tmp='/tmp/sim_%s.html'%dev; open(tmp,'w').write(src)
    pg.goto('file://'+tmp); pg.wait_for_timeout(300)
    return pg,errs
def overlap(pg):
    # czy jakikolwiek klawisz/element panelu wchodzi pod pasek kart lub poza ekran
    return pg.evaluate("""(()=>{const t=document.getElementById('tabs').getBoundingClientRect();const out=[];
      document.querySelectorAll('.pane:not([hidden]) .kp button, .pane:not([hidden]) .tv, .pane:not([hidden]) .inp').forEach(e=>{const r=e.getBoundingClientRect();
      if(r.height&&(r.bottom>t.top-1||r.bottom>innerHeight))out.push(e.className+' '+e.textContent.trim().slice(0,6))});
      return {over:out,kh:getComputedStyle(document.documentElement).getPropertyValue('--kh'),cls:document.documentElement.className,tabsBottom:t.bottom,ih:innerHeight}})()""")
with sync_playwright() as p:
    b=p.chromium.launch()
    for dev in DEV:
        for sch in ['light','dark']:
            pg,errs=page(b,dev,sch)
            for x in ['5','000']: k(pg,0,x)
            if sch=='dark': pg.click('#mode button[data-m="1"]')
            pg.wait_for_timeout(400); r0=overlap(pg); pg.screenshot(path=f'/tmp/r_{dev}_{sch}_0.png')
            pg.click('#tabs button[data-t="1"]'); pg.wait_for_timeout(300)
            for seq,cur in [(['1','2','000','+'],'ALL'),(['8','5','0','+'],'ALL'),(['4','5',',','9','9','+'],'PLN'),(['1','2',',','5','+'],'EUR'),(['3','0','0','-'],'ALL'),(['6','8','0','+'],'ALL')]:
                pg.click(f'#icur button[data-c="{cur}"]')
                for x in seq: k(pg,1,x)
            for x in ['1','9','0']: k(pg,1,x)
            pg.wait_for_timeout(500); r1=overlap(pg); pg.screenshot(path=f'/tmp/r_{dev}_{sch}_1.png')
            print(dev,sch,errs,'P:',r0,'S:',r1)
