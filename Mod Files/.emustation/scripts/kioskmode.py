import xbmc,xbmcgui
#####	Start markings for the log file.
print "| kioskmode.py loaded."
if xbmc.getCondVisibility( 'Skin.HasSetting(KioskMode)' ):
	xbmc.executebuiltin('Skin.Reset(KioskMode)')
else:
	if xbmcgui.Dialog().yesno("KIOSK MODE","You are changing the UI to a restricted mode:","This will hide most menu-options to prevent","changes to the system."):
		xbmcgui.Dialog().ok("KIOSK MODE","To unlock and return to the full UI, enter this code:","BLACK,UP,UP,DOWN,DOWN","LEFT,LEFT,RIGHT,RIGHT,A")
		xbmc.executebuiltin('Skin.SetBool(KioskMode)')
		xbmc.executebuiltin('Dialog.Close(1113,true)')
		xbmc.executebuiltin('SetFocus(2)')
	else:
		xbmc.executebuiltin('Skin.Reset(KioskMode)')