from pathlib import Path
from PIL import Image
import shutil,re,json,hashlib
folder=Path('assets/client');folder.mkdir(exist_ok=True)
files={'slog':'slog.png','mdjs-3d':'mdjs 3D.png','mdjs-3d-match':'mdjs 3D 2.png','lmatch-pro':'lmatch pro.png','keno':'keno.png'}
manifest={}
for slug,name in files.items():
 src=Path(r'C:\Users\hp\Downloads')/name
 shutil.copy2(src,folder/(slug+'.png'))
 im=Image.open(src);im.thumbnail((1600,1000));im.save(folder/(slug+'.webp'),quality=94,method=6)
 manifest[slug]={'source_filename':name,'original':f'assets/client/{slug}.png','optimized':f'assets/client/{slug}.webp','width':im.width,'height':im.height}
duplicate=Path(r'C:\Users\hp\Downloads\lmatch pro (1).png')
manifest['lmatch-pro']['duplicate_identical_pixels']=Image.open(duplicate).convert('RGBA').tobytes()==Image.open(folder/'lmatch-pro.png').convert('RGBA').tobytes()
(folder/'SOURCES.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
p=Path('index.html');s=p.read_text(encoding='utf-8')
# Apply the approved slogan to both layouts, without replacing the supporting shop description.
s=s.replace('<h1><a href="#p-services">وجهتكم المفضلة</a></h1><h2>للترفيه والمتابعة الرياضية</h2>','<h1><a href="#p-services">وجدة: فضاؤكم الخاص</a></h1><h2>للترفيه الرياضي والرهانات</h2>')
s=s.replace('<h1><span class="headline-primary">وجهتكم المفضلة</span><span class="headline-secondary">للترفيه والمتابعة الرياضية</span></h1>','<h1><span class="headline-primary">وجدة: فضاؤكم الخاص</span><span class="headline-secondary">للترفيه الرياضي والرهانات</span></h1>')
s=s.replace('<title>Planet Services | فضاؤكم الرياضي الخاص في وجدة</title>','<title>Planet Services | وجدة: فضاؤكم الخاص للترفيه الرياضي والرهانات</title>')
s=s.replace('وخدمات TIFO وCHRONO وMDJS وLOTO وCÔTÉ SPORT.','وخدمات TIFO وCHRONO وMDJS وLOTO وCÔTÉ SPORT وKENO.')
s=s.replace('وجدة · فضاؤكم الرياضي الخاص','وجدة · فضاؤكم الخاص للترفيه الرياضي والرهانات')
s=s.replace('خمس خدمات. وجهة واحدة.','ست خدمات. وجهة واحدة.')
mobile='<a class="ps-service ps-keno" href="#p-contact" aria-label="KENO — اكتشف الخدمة في المحل"><img class="ps-service-logo" src="assets/client/keno.webp" alt="KENO كينو" width="276" height="142" loading="lazy"><div class="ps-keno-word" aria-hidden="true" dir="ltr">KENO</div><h3>اكتشفوا<br>خدمات كينو<br>داخل المحل</h3></a>'
s=s.replace('</a></div></section>\n<section class="ps-screens"','</a>'+mobile+'</div></section>\n<section class="ps-screens"',1)
assert 'class="ps-service ps-keno"' in s
card='<article class="service reveal service-keno"><span class="number">06</span><img src="assets/client/keno.webp" class="official-brand" alt="KENO كينو — الشعار المقدم من العميل" loading="lazy" width="276" height="142"><h3 dir="ltr">KENO</h3><p>اكتشفوا خدمات كينو المتاحة داخل المحل.</p><a href="#contact">اكتشفها في المحل <span>↖</span></a></article>'
s=s.replace('</article></div><p class="service-note">','</article>'+card+'</div><p class="service-note">',1)
entries=[('mdjs-3d-match','CÔTÉ SPORT 3D — متابعة المباريات'),('mdjs-3d','CÔTÉ SPORT 3D — شاشة المباريات'),('lmatch-pro',"L’MATCH PRO — النتائج"),('slog','SLOG — نتائج السباقات')]
mg=''.join(f'<button class="ps-screen" data-image="assets/client/{key}.png" data-caption="{caption}" aria-label="تكبير {caption}"><img src="assets/client/{key}.webp" alt="{caption} — صورة مقدمة من العميل" width="{manifest[key]["width"]}" height="{manifest[key]["height"]}" loading="lazy"></button>' for key,caption in entries)
s,n=re.subn(r'(<div class="ps-gallery">).*?(</div></section>)',lambda m:m[1]+mg+m[2],s,count=1,flags=re.S);assert n==1
dg=''.join(f'<button class="gallery-item reveal" data-image="assets/client/{key}.png" data-caption="{caption}" aria-label="تكبير {caption}"><img src="assets/client/{key}.webp" alt="{caption} — صورة مقدمة من العميل" width="{manifest[key]["width"]}" height="{manifest[key]["height"]}" loading="lazy"><span>{caption}<b>↗</b></span></button>' for key,caption in entries)
s,n=re.subn(r'(<div class="gallery">).*?(</div><p class="asset-note">)',lambda m:m[1]+dg+m[2],s,count=1,flags=re.S);assert n==1
s=s.replace('صور الشاشات مقتطفة من الملصق المرجعي. تتوفر خدمات TIFO وLOTO وCÔTÉ SPORT داخل المحل.','صور الشاشات مقدمة من العميل للعرض التوضيحي، وليست نتائج أو أسعاراً مباشرة. اضغطوا لتكبير الصورة الأصلية.')
s=s.replace('كرة القدم، السباقات، وعالم MDJS.','CÔTÉ SPORT 3D، وL’MATCH PRO، وSLOG.')
s=s.replace('<b dir="ltr">18+</b><strong>العب بمسؤولية</strong>','<b dir="ltr" aria-label="ممنوع على أقل من 18 سنة">18+</b><strong>العب بمسؤولية</strong>')
s=s.replace('<b dir="ltr">18+</b><p>الخدمات','<b dir="ltr" aria-label="ممنوع على أقل من 18 سنة">18+</b><p>العب بمسؤولية. الخدمات')
p.write_text(s,encoding='utf-8')
print('Installed client originals + optimized images; KENO in both layouts; both galleries and slogan updated.')
print('Lmatch duplicate identical:',manifest['lmatch-pro']['duplicate_identical_pixels'])
