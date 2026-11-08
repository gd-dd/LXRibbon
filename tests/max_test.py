import sys, json, traceback
from pathlib import Path
root=Path('E:/Ruanjian/LXTool/LXRibbon'); sys.path.insert(0,str(root))
report={}
try:
 import plugin
 from pymxs import runtime as rt
 rt.resetMaxFile(rt.Name('noPrompt'))
 nodes=[]
 for i in range(4):
  n=rt.boneSys.createBone(rt.Point3(i*10,0,0),rt.Point3((i+1)*10,0,0),rt.Point3(0,0,1))
  if nodes: n.parent=nodes[-1]
  nodes.append(n)
 rt.select(nodes[0]); chain=plugin.chain_from_selection()
 (root/'tests/controllers.txt').write_text(str(rt.classOf(rt.getPropertyController(nodes[0],rt.Name('rotation')))),encoding='utf-8')
 plugin.bake(chain,0,20,dict(gravity=980,inertia=.95,mass=1,influence=1,damping=3))
 with plugin.pymxs.attime(20):
  positions=[plugin.vec(n.position) for n in nodes]
  assert positions[-1][2]<-1,positions
  for a,b in zip(positions,positions[1:]):
   assert abs(sum((x-y)**2 for x,y in zip(a,b))**.5-10)<.01,positions
 w=plugin.RibbonWindow(); assert w.end.value()==int(rt.animationRange.end.frame); w.close()
 report={'ok':True,'positions':positions,'widget':'constructed in Max without showing'}
except Exception: report={'ok':False,'error':traceback.format_exc()}
(root/'tests/result.json').write_text(json.dumps(report,indent=2),encoding='utf-8')


