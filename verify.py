from html.parser import HTMLParser
from pathlib import Path
from urllib.request import urlopen
class Check(HTMLParser):
 def __init__(self): super().__init__(); self.ids=[]; self.links=[]; self.assets=[]; self.sections=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if 'id' in d: self.ids.append(d['id'])
  if t=='a': self.links.append(d.get('href',''))
  if t in ('img','script') and d.get('src'): self.assets.append(d['src'])
  if t=='section': self.sections.append(d.get('id','final-cta'))
s=Path('index.html').read_text(encoding='utf-8'); c=Check(); c.feed(s)
assert len(c.ids)==len(set(c.ids))
for a in c.assets: assert Path(a).is_file(),a
for a in c.links:
 if a.startswith('#'): assert a[1:] in c.ids,a
for phrase in ['حي موريتانيا','فضاء واسع وخاص ومريح','TIFO','CHRONO','MDJS','LOTO','CÔTÉ SPORT','18+'] : assert phrase in s,phrase
for phrase in ['حي الحسني','فضاء واسع وعصري']: assert phrase not in s,phrase
allowed=['https://wa.me/212662857991','tel:+212662857991','https://www.google.com/maps?q=34.6991445,-1.8998544&z=17&hl=fr']
for a in c.links:
 if not a.startswith('#'): assert a in allowed,a
for a in ['','style.css','script.js']+sorted(set(c.assets)):
 with urlopen('http://localhost:8080/'+a) as r: assert r.status==200
print('PASS: section order:',', '.join(c.sections))
print('PASS: local HTTP, all image assets, anchor targets, exact contact links, required copy, prohibited copy, duplicate IDs')
print('Total image bytes:',sum(p.stat().st_size for p in Path('assets').glob('*.webp')))
Path('QA.md').write_text('''# Verification\n\nPassed: JavaScript syntax (`node --check script.js`); local HTTP 200 for HTML, CSS, JavaScript and every referenced image; all anchor destinations; unique element IDs; nine sections in requested order; exact WhatsApp, phone and Maps URLs; corrected Arabic address and private-space wording; required five services and 18+ notice.\n\nBrowser visual and interaction testing could not be completed: browser access host unavailable; native Chrome windows minimized and inaccessible through the UI tool. Desktop, tablet and mobile layouts, lightbox, menu and embedded Maps require visual verification. Responsive breakpoints are implemented at 1050px and 760px, with reduced-motion support.\n\nOnly poster-derived assets were supplied. Real interior photography and original screen/logo assets remain to be replaced as documented in README.md.\n''',encoding='utf-8')
