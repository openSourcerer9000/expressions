from qgis.core import *
from qgis.gui import *
liist = [0.1,0.25,0.5,1,1.5,2,2.5,3,4,5,10,20,40]

@qgsfunction(args='auto', group='Custom')
def lyst(i, feature, parent):
    return liist[i]

