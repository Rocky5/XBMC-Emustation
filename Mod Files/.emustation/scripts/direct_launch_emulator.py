'''
	Script by Rocky5
	Used to launch emulators directly
'''
import os, xbmc, xbmcgui
#####	Start markings for the log file.
try:
	direct_launch	= sys.argv[1:][0]
except:
	direct_launch	= "0"
print "| .emustation\Scripts\direct_launch_emulator.py loaded."
pDialog				= xbmcgui.DialogProgress()
dialog				= xbmcgui.Dialog()
MenuLabel 			= xbmc.getInfoLabel( 'Container(9000).ListItem.Label2' )
Virtual_ISO_Detacher = 'Q:\\system\\detacher\\default.xbe'
#####	Sets paths.
if str( xbmc.getCondVisibility( 'Skin.String(Custom_Emulator_Path)' ) ) == "1":
	Emulator_Folder_Path	= xbmc.getInfoLabel( 'Skin.String(Custom_Emulator_Path)' )
else:
	Emulator_Folder_Path	= 'Q:\\.emulators\\emulators\\'
###########
if direct_launch == "1":
	if os.path.isfile( os.path.join( Emulator_Folder_Path, MenuLabel, 'default.xbe' ) ):
		xbmc.executebuiltin('runxbe(' + Emulator_Folder_Path + '' + MenuLabel + '\\default.xbe)')
else:
	if MenuLabel == "xbox" or MenuLabel == "ports" or MenuLabel == "favs" or MenuLabel == xbmc.getLocalizedString(5) or MenuLabel == xbmc.getLocalizedString(427):
		if MenuLabel == xbmc.getLocalizedString(427):
			if dialog.yesno( "Detacher","Would you like to detach","the current virtual iso?" ) == 1:
				if os.path.isfile( Virtual_ISO_Detacher ):
					xbmc.executebuiltin('runxbe(' + Virtual_ISO_Detacher + ')')
				else:
					dialog.ok( "ERROR!","","Cant find default.xbe[CR]Reinstall XBMC-Emustation" )
		else:
			dialog.ok( "OOPS!","","This only works on Emulators." )
	else:
		if dialog.yesno( "Launch Emulator","Would you like to launch the emulator","menu system so you can edit the settings?" ) == 1:
			if os.path.isfile( os.path.join( Emulator_Folder_Path, MenuLabel, 'default.xbe' ) ):
				xbmc.executebuiltin('runxbe(' + Emulator_Folder_Path + '' + MenuLabel + '\\default.xbe)')
			else:
				dialog.ok( "ERROR!","","Cant find default.xbe[CR]Reinstall the emulator." )
		else:
			pass
xbmc.executebuiltin( 'SetFocus(9000)' )