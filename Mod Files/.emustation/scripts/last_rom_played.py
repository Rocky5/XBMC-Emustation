import os, time, xbmc, xbmcgui
#####	Start markings for the log file.
print "| last_rom_played.py loaded."
xbmc.executebuiltin('ActivateWindow(1)')
xbmc.executebuiltin('SetFocus(9000,'+xbmc.getInfoLabel('skin.string(lastrompos)')+')')
xbmc.executebuiltin('Skin.Reset(gameloaded)')
if os.path.isfile('Q:/system/nosplash'): os.remove('Q:/system/nosplash')