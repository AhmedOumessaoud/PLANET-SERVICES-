from urllib.request import urlopen, Request
from pathlib import Path
from PIL import Image
import json
root=Path('assets/brands');root.mkdir(exist_ok=True)
sources={'mdjs':'https://mdjs.ma/wp-content/uploads/2019/05/logo-mdjs-1.png','tifo':'https://mdjs.ma/wp-content/uploads/2019/06/tifo-2.png','chrono':'https://mdjs.ma/wp-content/uploads/2019/06/chrono-1.png','cote-sport':'https://mdjs.ma/wp-content/uploads/2023/06/COTESPORT.png'}
for name,url in sources.items():
 p=root/(name+'.png');p.write_bytes(urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0','Referer':'https://mdjs.ma/jeux/'}),timeout=30).read());im=Image.open(p);print(name,im.size,im.mode)
(root/'SOURCES.json').write_text(json.dumps({'source_page':'https://mdjs.ma/jeux/','assets':sources},indent=2),encoding='utf-8')

