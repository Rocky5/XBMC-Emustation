import random, xbmc, xbmcgui
try:
	ID	= "9000"
	Get_Item_Count	= int(xbmc.getInfoLabel('Container(' + ID + ').NumItems'))
	Random 			= str(random.randrange(0,Get_Item_Count,1))
	if xbmc.getCondVisibility('Window.IsVisible(10000)'):
		xbmc.executebuiltin('SetFocus('+ID+','+Random+')')
	else:
		if Get_Item_Count >= 10:
			xbmc.executebuiltin('SetFocus('+ID+','+Random+')')
except:
	try:
		ID	= "50"
		Get_Item_Count	= int(xbmc.getInfoLabel('Container(' + ID + ').NumItems'))
		Random 			= str(random.randrange(0,Get_Item_Count,1))
		if xbmc.getCondVisibility('Window.IsVisible(10000)'):
			xbmc.executebuiltin('SetFocus('+ID+','+Random+')')
		else:
			if Get_Item_Count >= 10:
				xbmc.executebuiltin('SetFocus('+ID+','+Random+')')
	except: print "No list with supported IDs, so random script didn't work :D"