'''
	Script by Rocky5
	Used to disabled or enable the sounds.xml
'''

import os, xbmc

#####	Start markings for the log file.
print "| _Scripts\XBMC-Emustation\dis-enable_sound.py loaded."


Sound_XML_Path					= xbmc.translatePath( 'special://skin/sounds/sounds.xml' )

if os.path.isfile( Sound_XML_Path ):
	os.rename( Sound_XML_Path, Sound_XML_Path + ' disbled' )
	xbmc.executebuiltin("Skin.SetBool(DisabledSound)")
	xbmc.executebuiltin("ReloadSkin")
	xbmc.executebuiltin("ActivateWindow(1111)")
	xbmc.executebuiltin("ActivateWindow(1112)")
	xbmc.executebuiltin("SetFocus(2)")

elif os.path.isfile( Sound_XML_Path + ' disbled' ):
	os.rename( Sound_XML_Path + ' disbled', Sound_XML_Path )
	xbmc.executebuiltin("Skin.Reset(DisabledSound)")
	xbmc.executebuiltin("ReloadSkin")
	xbmc.executebuiltin("ActivateWindow(1111)")
	xbmc.executebuiltin("ActivateWindow(1112)")
	xbmc.executebuiltin("SetFocus(2)")

else:
	pass