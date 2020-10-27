import os, time, xbmc, xbmcgui
if xbmc.getCondVisibility('Skin.HasSetting(videolayout)'):
	if os.path.isfile('Q:/system/introplay'): os.remove('Q:/system/introplay')
	xbmc.executebuiltin('RunScript(special://emustation_scripts/auto_play_preview.py)')
else:
	xbmc.executebuiltin('ActivateWindow(1)')
	xbmc.executebuiltin('SetFocus(9000,'+xbmc.getInfoLabel('skin.string(lastrompos)')+')')
	xbmc.executebuiltin('Skin.Reset(gameloaded)')
	if os.path.isfile('Q:/system/introplay'): os.remove('Q:/system/introplay')