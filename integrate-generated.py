from pathlib import Path
from PIL import Image
import shutil
root=Path(r'C:\Users\hp\.codex\generated_images\01a1e5fc-d0c3-7cb1-b6c8-aa976033b446')
files={'lounge':'exec-a69ab501-c2e9-40d1-a8c0-5f50b7359c5c.png','stadium':'exec-a05ff311-12d9-4dc5-8a3a-c53e15571a5d.png','supporter':'exec-93853c64-e2b5-41fd-a583-3f447823047b.png'}
out=Path('assets/generated');out.mkdir(exist_ok=True)
for name,filename in files.items():
 shutil.copy2(root/filename,out/(name+'.png'))
 im=Image.open(root/filename);im.thumbnail((1600,1000) if name!='supporter' else (640,800));im.save(out/(name+'.webp'),quality=88,method=6)
 print(name,im.size,im.mode,'alpha extrema',im.getchannel('A').getextrema() if 'A' in im.getbands() else None)
p=Path('index.html');s=p.read_text(encoding='utf-8').replace('src="assets/lounge.webp"','src="assets/generated/lounge.webp"').replace('src="assets/supporter.webp"','src="assets/generated/supporter.webp"')
s=s.replace('تصور لأجواء الصالة الرياضية من الملصق المرجعي','تصور توضيحي مولد بالذكاء الاصطناعي لأجواء صالة رياضية').replace('أجواء الجلوس والشاشات كما تظهر في التصميم المرجعي','تصور مولد لأجواء الجلوس والشاشات، وليس صورة فعلية للمحل').replace('تصور الأجواء من الملصق المرجعي','تصور توضيحي مولد بالذكاء الاصطناعي')
p.write_text(s,encoding='utf-8')
p=Path('style.css');s=p.read_text(encoding='utf-8-sig').replace("url('assets/stadium.webp')","url('assets/generated/stadium.webp')")
s+='''\n/* Generated artwork exports preserve transparent cutout alpha. */\n@media(max-width:760px){.supporter{width:35%;height:245px;top:10px;right:-8%;object-fit:contain;object-position:right bottom;mask-image:linear-gradient(to bottom,#000 84%,transparent 100%);-webkit-mask-image:linear-gradient(to bottom,#000 84%,transparent 100%)}.space-image>img{aspect-ratio:2.35;object-position:center 54%}.header:before,.header:after{display:none}.header{background:linear-gradient(#00102022,#00102088),url('assets/generated/stadium.webp') center top/100% auto}.hero{background:linear-gradient(#01142780,#011427ee),url('assets/generated/stadium.webp') center top/cover}.hero-ball{mask-image:none;-webkit-mask-image:none}.final-cta{background-size:auto,100% auto}}\n'''
p.write_text(s,encoding='utf-8')
