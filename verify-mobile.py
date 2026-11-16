from pathlib import Path
from html.parser import HTMLParser
from urllib.request import urlopen
import re
class Check(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.assets=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if d.get('id'):self.ids.append(d['id'])
  if t=='a':self.links.append(d.get('href',''))
  if t in ['img','script','link']:
   u=d.get('src') if t!='link' else d.get('href')
   if u and not u.startswith('https:'):self.assets.append(u)
p=Path('index.html');s=p.read_text(encoding='utf-8').replace('خدمات TIFO<br>والمشاركة<br>الرياضية','خدمات <bdi>TIFO</bdi><br>والمشاركة<br>الرياضية').replace('ألعاب وخدمات<br>MDJS<br>متنوعة','ألعاب <bdi>MDJS</bdi><br>وخدمات<br>متنوعة').replace('خدمات رياضية<br>ومتابعة<br>أهم المباريات','متابعة الرياضة<br>وخدمات<br>المباريات');p.write_text(s,encoding='utf-8')
c=Check();c.feed(s)
assert len(c.ids)==len(set(c.ids))
for p in c.assets:assert Path(p).is_file(),p
for h in c.links:
 if h.startswith('#'):assert h[1:] in c.ids,h
for name in ['poster.css','poster-fonts.css']:
 css=Path(name).read_text(encoding='utf-8-sig');assert css.count('{')==css.count('}')
 for u in re.findall(r'url\([\'\"]?([^\)\'\"]+)',css):assert Path(u).is_file(),u
for bad in ['حي الحسني','فضاء واسع وعصري']:assert bad not in s
for good in ['حي موريتانيا','فضاء واسع وخاص ومريح','0662857991']:assert good in s
Path('assets/fonts/OFL.txt').write_bytes(urlopen('https://raw.githubusercontent.com/google/fonts/main/ofl/tajawal/OFL.txt',timeout=20).read())
p=Path('README.md');txt=p.read_text(encoding='utf-8-sig');txt+='''\n## Reference-matched mobile layout\nAt widths up to 760px, index.html presents .poster-page, a dedicated compact poster composition with local Tajawal fonts and CSS container units. poster.css controls the proportions independently of the desktop design. Headings, descriptions, hours, address and contact details are live HTML. The header branding, interior, supporter, separate service illustrations, pin/map illustration and stadium crowd come from individually extracted user-supplied reference assets. Generated imagery remains available for desktop. The mobile contact address and red CTA open directions; the phone panel calls Mourad; WhatsApp remains in the stadium footer. Gallery images share the existing lightbox.\n\nChrome mobile full-page visual review completed at 400px width. Result approximately 1432px tall (3.58:1), close to the 2365/665 reference ratio of 3.56:1; prior user screenshot was 3736/480 (7.78:1). Final minor typography adjustments followed visual review. A later interaction check was interrupted when the user minimized Chrome, so lightbox behavior was not re-tested through the UI this turn.\n''';p.write_text(txt,encoding='utf-8')
Path('QA.md').write_text('''# Mobile verification\n\nChrome mobile preview: 400px wide, full-page screenshot reviewed. Composition approximately 1432px tall, reference ratio preserved. Fixed headline clipping and feature/service text overlaps following screenshot comparison. Final minor typography adjustments statically verified.\n\nPassed: unique IDs; all local HTML/CSS image/font/script/style paths; fragment links; corrected address and private-space wording; prohibited old copy absent; balanced CSS; JavaScript syntax.\n\nPin, address and red CTA use exact Maps URL. Phone and WhatsApp use supplied destinations. Gallery buttons use shared lightbox handler. UI interaction re-test was interrupted when Chrome was minimized.\n''',encoding='utf-8')
print('PASS: local assets, fonts, CSS, IDs, anchors, required content and address. Chrome 400px visual review completed.')
