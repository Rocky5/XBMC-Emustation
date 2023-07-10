import os, shutil, xbmc, xbmcgui
PAL = os.path.join(xbmc.translatePath('special://skin/xml_sd_pal'))
PAL_Dis = os.path.join(xbmc.translatePath('special://skin/.xml_sd_pal'))
NTSC = os.path.join(xbmc.translatePath('special://skin/xml_sd_ntsc'))
NTSC_Dis = os.path.join(xbmc.translatePath('special://skin/.xml_sd_ntsc'))

if xbmc.getCondVisibility('Skin.HasSetting(hide_sd_themes)'):
	xbmc.executebuiltin('Skin.Reset(hide_sd_themes)')
	try:
		os.rename( PAL_Dis, PAL )
	except: pass
	try:
		os.rename( NTSC_Dis, NTSC )
	except: pass
elif not xbmc.getCondVisibility('Skin.HasSetting(hide_sd_themes)'):
	xbmc.executebuiltin('Skin.SetBool(hide_sd_themes)')
	try:
		os.rename( PAL, PAL_Dis )
	except: pass
	try:
		os.rename( NTSC, NTSC_Dis )
	except: pass