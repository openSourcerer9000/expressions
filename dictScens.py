from qgis.core import *
from qgis.gui import *
import itertools
aeps=[2,5,100]
condishs = ['EXIST','PROP']
#condishs = ['PROP','EXIST']

@qgsfunction(args='auto', group='Custom')
def dictScens(i, feature, parent):
    scenz = itertools.product(aeps,condishs)
    scens = [f'Q{aep}{condish}' for aep,condish in scenz]
    scens = { i:scen for i,scen in enumerate(scens) }
    return scens[i-1]
    
   
@qgsfunction(args='auto', group='Custom')
def dictPages(i, feature, parent):
    condishs = ['Existing','Proposed']
    scenz = itertools.product(aeps,condishs)
    scens = [f'{condish} {aep}-YR Inundation Map' for aep,condish in scenz]
    scens = { i:scen for i,scen in enumerate(scens) }
    return scens[i-1]
