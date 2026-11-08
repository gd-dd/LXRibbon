from pathlib import Path
import json,hashlib,shutil
from PySide6.QtGui import QImage,QPainter,QPen,QColor,QPainterPath
r=Path(__file__).resolve().parent; d=r/'.lxtool'; d.mkdir(exist_ok=True)
img=QImage(256,256,QImage.Format_ARGB32); img.fill(QColor('#FFFFFF')); p=QPainter(img); p.setRenderHint(QPainter.Antialiasing)
path=QPainterPath();path.moveTo(55,45);path.cubicTo(240,40,10,160,205,205)
p.setPen(QPen(QColor('#86B83D'),32));p.drawPath(path);p.end();img.save(str(d/'icon.png'))
shutil.copyfile(r/'README.md',d/'README.md')
(d/'panel.json').write_text(json.dumps({'type':'declarative','title':'LX 飘带','accent':'#86B83D','sections':[{'title':'在 Max 中使用','text':'打开工具文件夹，在 Max 中运行 打开飘带.ms。窗口与解算均在 Max 内运行。'},{'actions':[{'action':'folder','label':'打开插件文件夹'}]}]},ensure_ascii=False),encoding='utf-8')
files=['solver.py','plugin.py','打开飘带.ms','.lxtool/icon.png','.lxtool/README.md','.lxtool/panel.json']
m={'schemaVersion':2,'kind':'lx-tool','name':'LX 飘带','description':'Max 内全中文飘带骨骼动力学与动画烘焙','version':'0.0.1','category':'动画工具','icon':'.lxtool/icon.png','readme':'.lxtool/README.md','panel':'.lxtool/panel.json','applications':{},'actions':{'folder':{'type':'openFolder'}},'files':{f:hashlib.sha256((r/f).read_bytes()).hexdigest() for f in files}}
(d/'manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')

