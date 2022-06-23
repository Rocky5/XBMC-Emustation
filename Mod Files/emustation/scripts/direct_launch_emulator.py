import os, xbmc, xbmcgui
def write_igr_file():
	try:
		if not os.path.isdir('E:\\CACHE'): makedirs('E:\\CACHE')
		with open("E:\\CACHE\\LocalCache20.bin","w") as tmp:
			for xbe in sorted(os.listdir(xbmc.translatePath("Special://root/"))):
				if xbe.endswith('.xbe'): tmp.write(xbmc.translatePath("Special://root/"+xbe))
	except: print "Couldn't create CACHE folder"
try:
	direct_launch	= sys.argv[1:][0]
	custom_launch	= sys.argv[2:][0]
except:
	direct_launch	= "0"
	custom_launch	= "0"
pDialog				= xbmcgui.DialogProgress()
dialog				= xbmcgui.Dialog()
MenuLabel 			= xbmc.getInfoLabel('Container(9000).ListItem.Label2')
Virtual_ISO_Detacher = 'Q:\\system\\detacher\\default.xbe'
#####	Sets paths.
if str(xbmc.getCondVisibility('Skin.String(Custom_Emulator_Path)')) == "1":
	Emulator_Folder_Path	= xbmc.getInfoLabel('Skin.String(Custom_Emulator_Path)')
else:
	Emulator_Folder_Path	= 'Q:\\.emulators\\emulators\\'
###########
if direct_launch == "1":
	if os.path.isfile(os.path.join(Emulator_Folder_Path, MenuLabel, 'default.xbe')):
		if xbmc.getCondVisibility('Skin.HasSetting(reloademustation)'): write_igr_file()
		xbmc.executebuiltin('runxbe(' + Emulator_Folder_Path + '' + MenuLabel + '\\default.xbe)')
if not custom_launch == "0":
	if os.path.isfile(custom_launch):
		if xbmc.getCondVisibility('Skin.HasSetting(reloademustation)'): write_igr_file()
		xbmc.executebuiltin('runxbe('+custom_launch+')')
else:
	if MenuLabel == "xbox" or MenuLabel == "ports" or MenuLabel == "favs" or MenuLabel == "customtile" or MenuLabel == xbmc.getLocalizedString(5) or MenuLabel == xbmc.getLocalizedString(427):
		if MenuLabel == xbmc.getLocalizedString(427):
			if dialog.yesno("Detacher","Would you like to detach","the current virtual iso?") == 1:
				if os.path.isfile(Virtual_ISO_Detacher):
					if xbmc.getCondVisibility('Skin.HasSetting(reloademustation)'): write_igr_file()
					xbmc.executebuiltin('runxbe(' + Virtual_ISO_Detacher + ')')
				else:
					dialog.ok("ERROR!","","Cant find default.xbe[CR]Reinstall XBMC-Emustation")
		else:
			dialog.ok("OOPS!","","This only works on Emulators.")
	else:
		if dialog.yesno("Launch Emulator","Would you like to launch the emulator","menu system so you can edit the settings?") == 1:
			if os.path.isfile(os.path.join(Emulator_Folder_Path, MenuLabel, 'default.xbe')):
				if xbmc.getCondVisibility('Skin.HasSetting(reloademustation)'): write_igr_file()
				xbmc.executebuiltin('runxbe(' + Emulator_Folder_Path + '' + MenuLabel + '\\default.xbe)')
			else:
				dialog.ok("ERROR!","","Cant find default.xbe[CR]Reinstall the emulator.")
		else:
			pass
xbmc.executebuiltin('SetFocus(9000)')