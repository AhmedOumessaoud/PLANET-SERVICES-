from PIL import Image
from pathlib import Path
im=Image.open(r'C:\Users\hp\Downloads\Planet Services_ Sports Lounge Spectacular.png')
p=Path('assets'); p.mkdir(exist_ok=True)
# Coordinates refer to the supplied 576 x 2048 visual; extract individual assets only.
boxes={'logo':(120,5,450,108),'lounge':(9,343,568,523),'stadium':(0,1855,576,1960),'football':(23,1065,278,1180),'ematch':(300,1065,550,1180),'chrono-screen':(24,1202,278,1318),'astro':(301,1202,550,1318),'tifo':(19,813,107,909),'chrono':(128,814,225,912),'mdjs':(241,811,336,909),'loto':(351,813,447,912),'cote-sport':(466,811,555,912)}
for name,b in boxes.items():
 box=tuple(round(v*im.width/576) for v in b); im.crop(box).save(p/(name+'.webp'),'WEBP',quality=92)
