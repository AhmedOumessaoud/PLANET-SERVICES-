from pathlib import Path
from PIL import Image
im=Image.open(r'C:\Users\hp\Downloads\UI UX.png')
print('Reference size:',im.size)
folder=Path('assets/poster');folder.mkdir(exist_ok=True)
# Separate illustration excerpts; every headline, description and control is real HTML.
regions={'pin-map':(31,1492,168,1648),'tifo-art':(17,850,109,918),'chrono-art':(127,850,224,918),'mdjs-art':(240,850,335,918),'loto-art':(352,850,447,918),'cote-art':(464,850,554,918),'footer-crowd':(0,1850,576,1965)}
for name,box in regions.items():
 im.crop(tuple(round(x*im.width/576) for x in box)).save(folder/(name+'.webp'),quality=95)
