'''
	Script by Rocky5
	Used to launch roms
'''
import xbmc, xbmcgui
try:
	Emu_Path		= sys.argv[1:][0]
	Rom_Name_Path	= sys.argv[2:][0]
	
	with open('z:\\tmp.cut', "w") as outputfile:
		outputfile.write( '<shortcut><path>%s</path><label>launcher</label><custom><game>%s</game></custom></shortcut>' % ( Emu_Path, Rom_Name_Path ) )
	with open('Q:\\system\\scripts\\autoexec.py', "w") as outputfile:
		WriteFile = 'if str( xbmc.getCondVisibility( "Skin.HasSetting(gameloaded)" ) ) and str( xbmc.getCondVisibility( "Skin.HasSetting(lastromlist)" ) ) == "1":\n\
		xbmc.executebuiltin("ActivateWindow(1)")\n\
		xbmc.executebuiltin("Skin.Reset(gameloaded)")\n\
else: xbmc.executebuiltin("Skin.Reset(gameloaded)")\n\
	'
		outputfile.write( WriteFile )
		xbmc.executebuiltin("Skin.SetBool(gameloaded)")
		xbmc.executebuiltin('runxbe( "z:\\tmp.cut" )')
except:
	xbmcgui.Dialog().ok("Error","Something went wrong.","Please rescan your roms.")
	

