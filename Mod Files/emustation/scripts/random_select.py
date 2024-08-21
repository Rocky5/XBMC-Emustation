import random
import xbmc

def set_focus(ID):
	Get_Item_Count = int(xbmc.getInfoLabel('Container(' + ID + ').NumItems'))
	Random = str(random.randrange(0,Get_Item_Count,1))
	if xbmc.getCondVisibility('Window.IsVisible(home)'):
		xbmc.executebuiltin('SetFocus('+ID+','+Random+')')
	elif Get_Item_Count >= 10:
		xbmc.executebuiltin('SetFocus('+ID+','+Random+')')

try:
	# first attempt with id "9000"
	set_focus("9000")
except:
	# if that fails, try with id "50"
	set_focus("50")