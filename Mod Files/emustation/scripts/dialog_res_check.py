import time, xbmc, xbmcgui
if xbmc.getCondVisibility('StringCompare(system.screenwidthxheight,1920x1080)'):
	xbmcgui.Dialog().ok('1080I RESOLUTION DETECTED','Due to the complexity of this dashboard 1080i must','be disabled. I will disable it and restart.')
	xbmc.executebuiltin('resolution(720p)')
	time.sleep(1)
	xbmc.executebuiltin('RunXBE(Q:\\default.xbe)')