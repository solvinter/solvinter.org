"""Read-only source inventory. All derivatives stay in the separate destination."""
from pathlib import Path
from PIL import Image, ImageOps, ImageStat, ImageFilter
import argparse,hashlib,json,collections,datetime
ap=argparse.ArgumentParser();ap.add_argument('source',type=Path);ap.add_argument('destination',type=Path);a=ap.parse_args()
src=a.source.resolve();dst=a.destination.resolve()
if dst==src or src in dst.parents: raise SystemExit('Destination must be outside the original archive')
dst.mkdir(parents=True,exist_ok=True);(dst/'thumbs').mkdir(exist_ok=True)
rows=[];errors=[];hashes=collections.defaultdict(list)
for p in sorted(src.rglob('*')):
 if p.is_symlink() or not p.is_file() or p.suffix.lower() not in {'.jpg','.jpeg','.png','.heic','.tif','.tiff','.webp'}:continue
 try:
  digest=hashlib.sha256(p.read_bytes()).hexdigest();ident=hashlib.sha256(str(p.relative_to(src)).encode()).hexdigest()[:20]
  with Image.open(p) as im:
   date=str(im.getexif().get(36867,''));im=ImageOps.exif_transpose(im).convert('RGB');w,h=im.size
   im.thumbnail((480,480));im.save(dst/'thumbs'/f'{ident}.jpg',quality=78)
   gray=im.convert('L');brightness=ImageStat.Stat(gray).mean[0];sharp=ImageStat.Stat(gray.filter(ImageFilter.FIND_EDGES)).var[0]
   color=tuple(round(v) for v in ImageStat.Stat(im.resize((1,1))).mean)
   small=gray.resize((9,8));pix=list(small.getdata());dh=sum((pix[y*9+x]>pix[y*9+x+1])<<(y*8+x) for y in range(8) for x in range(8))
  row={'id':ident,'file':str(p.relative_to(src)),'bytes':p.stat().st_size,'modified':datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).isoformat(),'date':date,'width':w,'height':h,'format':p.suffix.lower(),'sha256':digest,'dhash':f'{dh:016x}','color':color,'brightness':round(brightness,1),'sharpness':round(sharp,1),'flags':(['low-resolution'] if min(w,h)<600 else [])+(['dark'] if brightness<35 else [])+(['bright'] if brightness>235 else [])+(['check-sharpness'] if sharp<80 else []),'thumb':'thumbs/'+ident+'.jpg'}
  rows.append(row);hashes[digest].append(ident)
 except Exception as e:errors.append({'file':str(p.relative_to(src)),'error':str(e)})
for row in rows:row['duplicates']=[i for i in hashes[row['sha256']] if i!=row['id']]
# Heuristic near matches, never deletion decisions.
buckets=collections.defaultdict(list)
for row in rows:buckets[row['dhash'][:2]].append(row)
for row in rows:
 row['similar']=[r['id'] for r in buckets[row['dhash'][:2]] if r['id']!=row['id'] and (int(row['dhash'],16)^int(r['dhash'],16)).bit_count()<=5][:12]
data={'generated':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':str(src),'count':len(rows),'bytes':sum(r['bytes'] for r in rows),'duplicateGroups':sum(len(v)>1 for v in hashes.values()),'errors':errors,'images':rows}
(dst/'inventory.json').write_text(json.dumps(data,ensure_ascii=False))
# Contact sheets for every image, separate from originals.
from PIL import ImageDraw
for start in range(0,len(rows),100):
 sheet=Image.new('RGB',(1200,1100),'#f7f5ef');draw=ImageDraw.Draw(sheet)
 for k,row in enumerate(rows[start:start+100]):
  with Image.open(dst/row['thumb']) as im:
   im.thumbnail((114,88));x=(k%10)*120;y=(k//10)*110;sheet.paste(im,(x,y));draw.text((x,y+89),str(start+k+1),fill='black')
 sheet.save(dst/f'contact-{start//100+1:03d}.jpg',quality=80)
print(json.dumps({k:v for k,v in data.items() if k not in ['images','errors']},ensure_ascii=False));print('Errors:',len(errors))
