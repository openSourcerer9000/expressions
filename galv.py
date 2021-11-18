from qgis.core import *
from qgis.gui import *
from pathlib import Path
import re
class smart_dict(dict):
    def __missing__(self, key):
        return key
idmap = smart_dict({'DB7x':'DB10','DB2': 'DB1', 'DB3': 'DB2', 'DB7': 'DB3', 'DB8': 'DB4', 'DB9': 'DB5', 'DB10': 'DB6', 'DB11': 'DB7', 'DB12': 'DB8', 'DB13': 'DB9', 'MB2': 'MB1', 'MB3': 'MB2', 'HB2': 'HB1', 'HB3': 'HB2', 'HB5': 'HB3', 'HB6': 'HB4', 'HB8': 'HB5', 'HB10': 'HB6', 'HA3': 'HA1'})

def replaceMulti(adict, text):
    '''Note: happens in one pass!\n
    returns the new str'''
    # Create a regular expression from all of the dictionary keys
    regex = re.compile("|".join(map(re.escape, adict.keys(  ))))

    # For each match, look up the corresponding value in the dictionary
    return regex.sub(lambda match: adict[match.group(0)], text)

@qgsfunction(args='auto', group='Custom')
def dictIDmapRep(strng, feature, parent):
    return replaceMulti(idmap,strng)

@qgsfunction(args='auto', group='Custom')
def dictIDmap(oldnm, feature, parent):
    return idmap[oldnm]

@qgsfunction(args='auto', group='Custom')
def temp(nm,feature,parent):
    pass

@qgsfunction(args='auto', group='Custom')
def wshedID(nm,feature,parent):
    return re.split('[0-9]',nm)[0]
    

@qgsfunction(args='auto', group='galv')
def BLDGsRemd(paf,feature,parent):
    pth = Path(r'J:\007896 Galveston County MDP Update\03.01 GIS\Shapefiles\02Dickinson_Bayou\InundationRasters\BLDGs_removed')
    return pth/f'{paf}.shp'
    
@qgsfunction(args='auto', group='galv')
def dirr(thing,feature,parent):
    return str(dir(thing))
