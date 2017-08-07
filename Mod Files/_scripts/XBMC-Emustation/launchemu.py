'''
	Script by Rocky5
	Used to launch emulators directly
'''

import glob, os, shutil, sqlite3, sys,time, xbmc, xbmcgui

#####	Start markings for the log file.
print "================================================================================"
print "| _Scripts\XBMC-Emustation\launchemu.py loaded."
print "| ------------------------------------------------------------------------------"
pDialog				= xbmcgui.DialogProgress()
dialog				= xbmcgui.Dialog()

#####	Sets paths.
# Gets current XBMC4Gamers directory.
CharCount = 100 # How many characters you want after 'The executable running is: '
with open( xbmc.translatePath( "special://xbmc/system/" ) + "xbmc.log", "r" ) as XBMCLOG:
	for line in XBMCLOG:
		left,found,right = line.partition("The executable running is: ")
		if found:
			Working_Directory		= ( right[:CharCount] )
			Root_Directory 			= Working_Directory[:-12] # Removed \default.xbe
			Emulator_Path			= Root_Directory + '_emulators\\'
			if xbmc.getCondVisibility( '!Skin.HasSetting(althomelayout)' ): MenuLabel = xbmc.getInfoLabel('Container(9001).ListItem.Label2')
			if xbmc.getCondVisibility( 'Skin.HasSetting(althomelayout)' ): MenuLabel = xbmc.getInfoLabel('Container(9002).ListItem.Label2')
###########
xbmc.executebuiltin('runxbe(' + Emulator_Path + '' + MenuLabel + '\\default.xbe)')