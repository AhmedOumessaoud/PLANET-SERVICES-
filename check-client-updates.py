from pathlib import Path
from html.parser import HTMLParser
from PIL import Image
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from urllib.request import urlopen
import threading,re
s=Path('index.html').read_text(encoding='utf-8')
class Check(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.paths=[];self.anchors=[];self.mobile=0;self.desktop=0;self.gallery=0
 def handle_starttag(self,t,a):
  d=dict(a);cls=d.get('class','').split()
  if 'id' in d:self.ids.append(d['id'])
  if t=='a':self.anchors.append(d.get('href',''))
  if 'ps-service' in cls:self.mobile+=1
  if 'service' in cls:self.desktop+=1
  if 'data-image' in d:self.gallery+=1;self.paths.append(d['data-image'])
  if t in ['img','script','link']:
   p=d.get('href') if t=='link' else d.get('src')
   if p and not p.startswith('http'):self.paths.append(p)
c=Check();c.feed(s)
assert c.mobile==c.desktop==6,(c.mobile,c.desktop)
assert c.gallery==8,c.gallery
assert len(c.ids)==len(set(c.ids))
for a in c.anchors:
 if a.startswith('#'):assert a[1:] in c.ids,a
for p in c.paths:assert Path(p).is_file(),p
assert s.count('وجدة: فضاؤكم الخاص')==3
assert s.count('للترفيه الرياضي والرهانات')>=3
assert s.count('aria-label="ممنوع على أقل من 18 سنة"')==2
for cls in ['ps-gallery','gallery']:
 content=re.search(r'<div class="'+cls+r'">(.*?)</div>',s,re.S)[1]
 assert content.count('data-image=')==4
 assert 'assets/football.webp' not in content
 assert 'assets/client/' in content
for f in ['style.css','poster.css','poster-fonts.css']:
 css=Path(f).read_text(encoding='utf-8-sig');assert css.count('{')==css.count('}')
 for u in re.findall(r'url\([\'\"]?([^\)\'\"]+)',css):
  if not u.startswith('http'):assert Path(u).is_file(),u
class Silent(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),Silent);threading.Thread(target=server.serve_forever,daemon=True).start()
try:
 for p in ['',*sorted(set(c.paths))]:
  with urlopen('http://127.0.0.1:'+str(server.server_port)+'/'+p) as r:
   assert r.status==200
   assert r.read(),p
finally:server.shutdown();server.server_close()
for p in Path('assets/client').glob('*.webp'):
 with Image.open(p) as im:im.verify()
print('PASS: six services in both layouts; four new screen originals per gallery; all assets load over HTTP; anchors and CSS references valid; approved slogan and 18+ notices present.')
