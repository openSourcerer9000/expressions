from qgis.core import *
from qgis.gui import *
from pathlib import Path
import math

@qgsfunction(args='auto', group='Custom')
def angul(geo,feature,parent):
    verts = list(geo.vertices())
    dists={}
    for i in range(len(verts)):
        #xy = [ [verts[i].x(),verts[i].y()],[verts[i-1].x(),verts[i-1].y()] ]
        dxy = [ verts[i].x()-verts[i-1].x(),verts[i].y()-verts[i-1].y() ]
        dists.update({math.hypot(*dxy):dxy})
    dxx,dyy = dists[max(dists.keys())]
    
    #x1,y1,x2,y2 = verts[0].x(),verts[0].y(),verts[1].x(),verts[1].y()
    ang = math.degrees(math.atan2(dyy,dxx))
    # thresh=7
    # ang=geo.vertices()
    # ang = math.degrees(ang)
    if ang>=90 and ang<=270:
        ang+=180
    if ang>360:
        ang-=360
    #if ang<thresh or ang>360-thresh:
        #ang=0
    return ang
    
@qgsfunction(args='auto', group='Custom')
def myFolderSlashMe(nm,ext,feature,parent):
    """
    if pond name is DB8.1, save as pth/DB8/DB8.1.tif
    """
    pth = r'C:/Users/sean.micek/Desktop/Galv/DickinsonBayouModelingCombined10.23.2020/Terrain/PropPonds'
    pos = nm.find('.')
    flder = nm[:pos] if pos>0 else nm
    return f'{pth}/{flder}/{nm}{ext}'
    
@qgsfunction(args='auto', group='Files and Paths')
def pthparent(filenm,feature,parent):
    pth = Path(filenm)
    return pth.parent.name

@qgsfunction(args='auto', group='Files and Paths')
def pthname(filenm,feature,parent):
    pth = Path(filenm)
    return pth.name
