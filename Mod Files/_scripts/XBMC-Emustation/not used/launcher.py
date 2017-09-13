'''
	Script by Rocky5
	Used to launch roms
'''

#####	Start markings for the log file.
print "| _Scripts\XBMC-Emustation\launcher.py loaded."

with open('z:\\tmp.cut', "w") as outputfile:
	Emu_Path		= xbmc.getInfoLabel('Container(9000).ListItem.Label2')
	Rom_Name_Path	= xbmc.getInfoLabel('Container(9000).ListItem.ActualIcon')
	xbmc.executebuiltin('ActivateWindow(1101)')
	outputfile.write( '<shortcut><path>%s</path><label>launcher</label><custom><game>%s</game></custom></shortcut>' % ( Emu_Path, Rom_Name_Path ) )

xbmc.executebuiltin("Skin.SetBool(gameloaded)")

with open('Q:\\system\\scripts\\autoexec.py', "w") as outputfile:
	WriteFile = 'if str( xbmc.getCondVisibility( "Skin.HasSetting(gameloaded)" ) ) == "1":\n\
	xbmc.executebuiltin("ActivateWindow(1)")\n\
	xbmc.executebuiltin("Skin.Reset(gameloaded)")\n\
else:\n\
	pass\n\
'
	outputfile.write( WriteFile )

xbmc.executebuiltin('runxbe( "z:\\tmp.cut" )')