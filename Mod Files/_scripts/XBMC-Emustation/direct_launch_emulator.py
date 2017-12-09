'''
	Script by Rocky5
	Used to launch emulators directly
'''

import os, xbmc, xbmcgui

#####	Start markings for the log file.
print "| _Scripts\XBMC-Emustation\direct_launch_emulator.py loaded."

pDialog				= xbmcgui.DialogProgress()
dialog				= xbmcgui.Dialog()

#####	Sets paths.
# Gets current XBMC-Emustation directory.
CharCount = 100 # How many characters you want after 'The executable running is: '
with open( xbmc.translatePath( "special://xbmc/system/" ) + "xbmc.log", "r" ) as XBMCLOG:
	for line in XBMCLOG:
		left,found,right = line.partition("The executable running is: ")
		if found:
			Working_Directory		= ( right[:CharCount] )
			Root_Directory 			= Working_Directory[:-12] # Removed \default.xbe
			if str( xbmc.getCondVisibility( 'Skin.String(Custom_Emulator_Path)' ) ) == "1":
				Emulator_Path		= xbmc.getInfoLabel( 'Skin.String(Custom_Emulator_Path)' )
			else:
				Emulator_Path		= Root_Directory + '_emulators\\'
			if xbmc.getCondVisibility( '!Skin.HasSetting(althomelayout)' ): MenuLabel = xbmc.getInfoLabel('Container(9001).ListItem.Label2')
			if xbmc.getCondVisibility( 'Skin.HasSetting(althomelayout)' ): MenuLabel = xbmc.getInfoLabel('Container(9002).ListItem.Label2')
###########
if os.path.isfile( os.path.join( Emulator_Path, MenuLabel, 'default.xbe' ) ):
	xbmc.executebuiltin('runxbe(' + Emulator_Path + '' + MenuLabel + '\\default.xbe)')
else:
	pass