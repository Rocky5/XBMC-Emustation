'''
	Script by Rocky5
	Used to launch emulators directly
'''
import os, xbmc, xbmcgui
#####	Start markings for the log file.
print "| _Scripts\XBMC-Emustation\direct_launch_emulator.py loaded."
pDialog				= xbmcgui.DialogProgress()
dialog				= xbmcgui.Dialog()
MenuLabel 			= xbmc.getInfoLabel( 'Container(9000).ListItem.Label2' )
#####	Sets paths.
if str( xbmc.getCondVisibility( 'Skin.String(Custom_Emulator_Path)' ) ) == "1":
	Emulator_Path	= xbmc.getInfoLabel( 'Skin.String(Custom_Emulator_Path)' )
else:
	Emulator_Path	= 'Q:\\_emulators\\'
###########

if MenuLabel == "xbox" or MenuLabel == "ports":
	dialog.ok( "OOPS!","","This only works on Emulators." )
else:
	if dialog.yesno( "Launch Emulator","Would you like to launch the emulator","menu system so you can edit the settings?" ) == 1:
		if os.path.isfile( os.path.join( Emulator_Path, MenuLabel, 'default.xbe' ) ):
			xbmc.executebuiltin('runxbe(' + Emulator_Path + '' + MenuLabel + '\\default.xbe)')
		else:
			dialog.ok( "ERROR!","","Cant find default.xbe[CR]Reinstall the emulator." )
	else:
		pass