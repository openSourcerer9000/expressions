from qgis.core import *
from qgis.gui import *
import math
#---USER INPUT:--------------
ARIs = [ 5,10,25,50,100,500 ]
lyrSuffix = '-YR_UC'
#----------------------------
dictARI = dict(enumerate(ARIs,1))

@qgsfunction(args='auto', group='Custom')
def lyr(i, feature, parent):
    return f'{dictARI[i]}{lyrSuffix}'

from datetime import datetime

@qgsfunction(args='auto', group='Custom')
def daMonth(feature, parent):
    return datetime.now().strftime('%b %Y').upper()

@qgsfunction(args='auto', group='Custom')
def daDate(feature, parent):
    return f"{datetime.now().month}{datetime.now().strftime('/%d/%Y')}"

@qgsfunction(args='auto', group='Custom')
def oryent(ang,feature,parent):
    while ang>=90 and ang<=270:
        ang-=90
    return ang
    
import re
@qgsfunction(args='auto', group='Custom')
def atlasPgNm(strng, feature, parent):
    '''replaces 'text<field>_text' with 'text' + to_str("field") + '_text' \n
    to keep fields dynamic'''
    res = re.sub(r'<(.*?)>',lambda x: str(feature[x.group()[1:-1]]),strng)
    ari = feature["ARI"]
    ari = 'Harvey' if ari>5000 else f'{ari}-YR'
    res = res.replace('[ari]',ari)
    return res
    
    #reggie = re.compile("|".join(map(re.escape,r'<(.*)>')))
    #re.sub(r'<(.*)>',feature['\\1'],strng)
    #return reggie.sub(lambda match: feature[match.group(0)], strng)
