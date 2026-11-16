from pathlib import Path
from urllib.request import urlopen
import re,json
folder=Path('assets/icons');folder.mkdir(exist_ok=True)
names=['users-round','armchair','tv-minimal-play','zap','calendar-clock','map-pin','menu','x','arrow-up','phone','arrow-up-right','arrow-down','clock']
for name in names:
 url=f'https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/{name}.svg'
 data=urlopen(url,timeout=30).read().decode()
 assert '<svg' in data and '<script' not in data
 (folder/(name+'.svg')).write_text(data,encoding='utf-8')
(folder/'LICENSE').write_bytes(urlopen('https://raw.githubusercontent.com/lucide-icons/lucide/main/LICENSE',timeout=30).read())
(folder/'SOURCES.json').write_text(json.dumps({name:f'https://github.com/lucide-icons/lucide/blob/main/icons/{name}.svg' for name in names},indent=2),encoding='utf-8')
p=Path('index.html');s=p.read_text(encoding='utf-8')
def icon(name,cls='icon'):
 svg=(folder/(name+'.svg')).read_text(encoding='utf-8')
 svg=svg.replace('<svg','<svg aria-hidden="true" focusable="false" class="'+cls+'"',1)
 return svg
s=re.sub(r'<span class="feature-icon"[^>]*>.*?</span>',lambda m:'<span class="feature-icon">'+icon(['users-round','armchair','tv-minimal-play','zap'][next(counter)])+'</span>',s,flags=re.S) if False else s
features=iter(['users-round','armchair','tv-minimal-play','zap'])
s=re.sub(r'<span class="feature-icon"[^>]*>.*?</span>',lambda m:'<span class="feature-icon">'+icon(next(features))+'</span>',s,flags=re.S)
s=re.sub(r'<div class="clock" aria-hidden="true">.*?</div>','<div class="clock" aria-hidden="true">'+icon('calendar-clock')+'</div>',s,flags=re.S)
s=re.sub(r'<div class="mobile-pin" aria-hidden="true">.*?</div>','<div class="mobile-pin" aria-hidden="true">'+icon('map-pin')+'</div>',s,flags=re.S)
s=re.sub(r'(<button class="menu-toggle"[^>]*>).*?(</button>)',lambda m:m[1]+icon('menu')+m[2],s,flags=re.S)
s=re.sub(r'(<button class="back-top"[^>]*>).*?(</button>)',lambda m:m[1]+icon('arrow-up')+m[2],s,flags=re.S)
s=re.sub(r'(<button class="lightbox-close"[^>]*>).*?(</button>)',lambda m:m[1]+icon('x')+m[2],s,flags=re.S)
s=s.replace('◷ يومياً',icon('clock','icon inline-icon')+' يومياً').replace('⌖ حي موريتانيا، وجدة',icon('map-pin','icon inline-icon')+' حي موريتانيا، وجدة')
s=s.replace('⌖ افتح الموقع في خرائط Google ↗',icon('map-pin','icon inline-icon')+' افتح الموقع في خرائط Google '+icon('arrow-up-right','icon inline-icon'))
p.write_text(s,encoding='utf-8')
print('Downloaded 13 official Lucide SVG icons with license and installed semantic feature / contact / navigation icons.')
