'''
	Script by Rocky5
	Used to launch roms
'''
import xbmc, xbmcgui

autoexec_data = "import os\n\
if xbmc.getCondVisibility( 'Skin.HasSetting(lastromlist)' ) == 1:\n\
	if xbmc.getCondVisibility( 'Skin.HasSetting(gameloaded)' ) == 1:\n\
		xbmc.executebuiltin('Skin.Reset(gameloaded)')\n\
		if os.path.isfile('Q:\\\\system\\\\nosplash.bin'): os.remove('Q:\\\\system\\\\nosplash.bin')\n\
		xbmc.executebuiltin('ActivateWindow(1)')\n\
else:\n\
	xbmc.executebuiltin('Skin.Reset(gameloaded)')"

try:
	Emu_Path		= sys.argv[1:][0]
	Rom_Name_Path	= sys.argv[2:][0]
	with open('z:\\tmp.cut', 'w') as cut:
		cut.write( '<shortcut><path>%s</path><label>launcher</label><custom><game>%s</game></custom></shortcut>' % ( Emu_Path, Rom_Name_Path ) )
	if str( xbmc.getCondVisibility( 'Skin.HasSetting(lastromlist)' ) ) == "1":
		with open('Q:\\system\\nosplash.bin', 'w') as nosplash: nosplash.write( '' )
		with open('Q:\\system\\scripts\\autoexec.py', 'w') as autoexec: autoexec.write( autoexec_data )
	else: pass
	xbmc.executebuiltin('Skin.SetBool(gameloaded)')
	xbmc.executebuiltin('runxbe( z:\\tmp.cut )')
	xbmc.executebuiltin('Dialog.close(1101,true)')
except:
	xbmc.executebuiltin('Dialog.close(1101,true)')
	xbmcgui.Dialog().ok('Error','Something went wrong.','Please rescan your roms.')