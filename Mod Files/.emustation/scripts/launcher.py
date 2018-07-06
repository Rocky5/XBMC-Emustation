'''
	Script by Rocky5
	Used to launch roms
'''
import os, xbmc, xbmcgui
xbmcgui.lock()
autoexec_data = "import os, xbmcgui\n\
if xbmc.getCondVisibility( 'Skin.HasSetting(lastromlist)' ) == 1:\n\
	if xbmc.getCondVisibility( 'Skin.HasSetting(gameloaded)' ) == 1:\n\
		xbmc.executebuiltin('Skin.Reset(gameloaded)')\n\
		if os.path.isfile('Q:\\\\system\\\\nosplash.bin'): os.remove('Q:\\\\system\\\\nosplash.bin')\n\
		xbmc.executebuiltin('ActivateWindow(1)')\n\
		xbmc.executebuiltin('SetFocus(9000,%s)')\n\
else:\n\
	xbmc.executebuiltin('Skin.Reset(gameloaded)')"
try:
	try:
		Emu_Path			= sys.argv[1:][0]
		Rom_Name_Path		= sys.argv[2:][0]
		Favourite_Launch	= sys.argv[3:][0]
		Current_position	= sys.argv[4:][0]
	except:
		Favourite_Launch	= 0
		Current_position	= 0
	Root_Directory 			= xbmc.translatePath("Special://root/")
	Custom_Emus_Path 		= xbmc.getInfoLabel('skin.string(custom_emulator_path)')
	Custom_Roms_Path 		= xbmc.getInfoLabel('skin.string(custom_roms_path)')
	if Custom_Emus_Path.startswith("Q:\\"): Custom_Emus_Path = Custom_Emus_Path.replace( "Q:\\", Root_Directory )
	if Custom_Roms_Path.startswith("Q:\\"): Custom_Roms_Path = Custom_Roms_Path.replace( "Q:\\", Root_Directory )
	if Emu_Path.startswith("Q:\\"): Emu_Path = Emu_Path.replace( "Q:\\", Root_Directory )
	if Rom_Name_Path.startswith("Q:\\"): Rom_Name_Path = Rom_Name_Path.replace( "Q:\\", Root_Directory )
	Emu_Name = xbmc.getInfoLabel('Skin.String(emuname)')
	with open('z:\\tmp.cut', 'w') as cut:
		if Emu_Name == "xbox":
			cut.write( '<shortcut><path>%s</path><label>launcher</label></shortcut>' % ( Emu_Path ) )
		elif Emu_Name == "favs":
			cut.write( '<shortcut><path>%s</path><label>launcher</label><custom><game>%s</game></custom></shortcut>' % ( Emu_Path,Rom_Name_Path ) )
		elif Emu_Name == "fba" or Emu_Name == "fbl" or Emu_Name == "fblc" or Emu_Name == "fbaxxx":
			cut.write( '<shortcut><path>%s</path><label>launcher</label><custom><game>%s</game></custom></shortcut>' % ( os.path.join( Custom_Emus_Path,Emu_Name,Emu_Path ),Rom_Name_Path ) )
		else:
			cut.write( '<shortcut><path>%s</path><label>launcher</label><custom><game>%s</game></custom></shortcut>' % ( os.path.join( Custom_Emus_Path,Emu_Name,Emu_Path ),os.path.join( Custom_Roms_Path,Emu_Name,Rom_Name_Path ) ) )
	if not Favourite_Launch and str( xbmc.getCondVisibility( 'Skin.HasSetting(lastromlist)' ) ) == "1":
		with open('Q:\\system\\nosplash.bin', 'w') as nosplash: nosplash.write( '' )
		with open('Q:\\system\\scripts\\autoexec.py', 'w') as autoexec: autoexec.write( autoexec_data % ( Current_position ) )
	else: pass
	if not Favourite_Launch: xbmc.executebuiltin('Skin.SetBool(gameloaded)')
	xbmcgui.unlock()
	xbmc.executebuiltin('runxbe( z:\\tmp.cut )')
except:
	xbmcgui.unlock()
	xbmc.executebuiltin('Dialog.close(1101,true)')
	xbmcgui.Dialog().ok('Error','Something went wrong.','Please rescan your roms.')