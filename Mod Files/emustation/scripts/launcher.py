import os
import sqlite3
import shutil
import time
import xbmc
import xbmcgui

def write_igr_file():
	if not os.path.isdir('E:\\CACHE'):
		makedirs('E:\\CACHE')
	with open("E:\\CACHE\\LocalCache20.bin","w") as tmp:
		for xbe in sorted(os.listdir(xbmc.translatePath("Special://root/"))):
			if xbe.endswith('.xbe'): tmp.write(xbmc.translatePath("Special://root/"+xbe))

def normalize_path(path):
	if path.startswith('Q:\\'):
		return path.replace('Q:\\', Root_Directory)
	return path

def handle_scummvm_emulator(cut, Emu_Name, Rom_Name_Path, Emu_Path_XBE, Custom_Emus_Path):
	if Emu_Name == 'favs':
		xbmc.executebuiltin('Skin.SetString(emuname,scummvm)')
		Emu_Name = 'scummvm'

	gameid = "donotaddgames"
	Game_Path = os.path.join(Custom_Emus_Path, Emu_Name, 'svms', Rom_Name_Path + ".svm")
	Game_Root = os.path.join(Custom_Emus_Path, Emu_Name, 'games')

	if not os.path.isdir(Game_Root):
		os.makedirs(Game_Root)

	shutil.copy2(os.path.join(Custom_Emus_Path, Emu_Name, "scummvm.ini"),
				 os.path.join(Custom_Emus_Path, Emu_Name, "scummvm.dat"))

	with open(Game_Path) as svm:
		svm_lines = svm.readlines()
		for line in svm_lines:
			if 'gameid=' in line:
				gameid = line.split("=")[1].strip()
				break
	
	with open(os.path.join(Custom_Emus_Path, Emu_Name, "scummvm.dat")) as ini:
		settings = ini.readlines()
	with open(os.path.join(Custom_Emus_Path, Emu_Name, "configs.ini"), "w") as ini:
		ini.write(''.join(settings + svm_lines))

	cut.write('<shortcut><path>{}</path><custom><game>{}</game></custom></shortcut>'.format(
		os.path.join(Custom_Emus_Path, Emu_Name, "loader.xbe"), gameid))

def handle_mame_emulator(Emu_Name, Rom_Name_Path, Custom_Emus_Path, Custom_Roms_Path):
	if Emu_Name == 'favs':
		xbmc.executebuiltin('Skin.SetString(emuname,mame)')
		Emu_Name = 'mame'

	Mame_Rom, Mame_Rom_Clone = Rom_Name_Path.split('--', 1)

	autobootrom_dir = os.path.join(Custom_Emus_Path, Emu_Name, 'autobootrom')
	if not os.path.exists(autobootrom_dir):
		os.makedirs(autobootrom_dir)

	for zip_file in os.listdir(autobootrom_dir):
		if zip_file.endswith('.zip'):
			shutil.move(os.path.join(autobootrom_dir, zip_file), os.path.join(Custom_Roms_Path, Emu_Name))

	shutil.move(os.path.join(Custom_Roms_Path, Emu_Name, Mame_Rom + '.zip'), autobootrom_dir)

	if Mame_Rom_Clone != 'parent':
		shutil.move(os.path.join(Custom_Roms_Path, Emu_Name, Mame_Rom_Clone + '.zip'), autobootrom_dir)
		with open(os.path.join(autobootrom_dir, 'clone.rom'), 'w'):
			pass

	if os.path.isfile(os.path.join(Custom_Emus_Path, Emu_Name, 'default.xbe')):
		os.rename(os.path.join(Custom_Emus_Path, Emu_Name, 'default.xbe'),
				  os.path.join(Custom_Emus_Path, Emu_Name, 'default disabled.xbe'))

	with open(os.path.join(autobootrom_dir, 'autobootrom.rom'), 'w'):
		pass
	with open(os.path.join(Custom_Emus_Path, Emu_Name, 'system', 'disable_ui'), 'w'):
		pass

try:
	xbmc.Player().stop()
	Emu_Path_XBE = sys.argv[1] if len(sys.argv) > 1 else 0
	Rom_Name_Path = sys.argv[2] if len(sys.argv) > 2 else 0
	Favourite_Launch = sys.argv[3] if len(sys.argv) > 3 else ""
	Current_position = sys.argv[4] if len(sys.argv) > 4 else ""

	Root_Directory = xbmc.translatePath('Special://root/')
	Rom_Name_Path = normalize_path(Rom_Name_Path)
	Custom_Emus_Path = normalize_path(xbmc.getInfoLabel('skin.string(custom_emulator_path)'))
	Custom_Roms_Path = normalize_path(xbmc.getInfoLabel('skin.string(custom_roms_path)'))
	xbmc.executebuiltin('Skin.SetString(lastrompos,'+str(Current_position)+')')
	Emu_Name = xbmc.getInfoLabel('Skin.String(emuname)')

	if Emu_Name == 'n64' or 'n64' in Emu_Path_XBE: # Have to do this or surreal will clear the config for the loaded rom.
		Rom_CRC = Rom_Name_Path.split('-CRC-',1)[1]
		Rom_Name_Path = Rom_Name_Path.split('-CRC-',1)[0]
		with open('E:\\TDATA\\64ce64ce\Tmp.ini', 'w') as f:
			f.write('[History]\nromname=Emustation Loader\nromCRC='+Rom_CRC+'\n')

	with open('z:\\tmp.cut', 'w') as cut:
		xbmc.executebuiltin('skin.setstring(xberegion,checking)')
		
		xberegion = ''
		game_auto_region = xbmc.executehttpapi('GetGUISetting(1;myprograms.gameautoregion)')
		myprograms6_db	= xbmc.translatePath("special://profile/database/MyPrograms6.db")
		valid_emulators = ['xbox', 'ports', 'homebrew']

		if Emu_Name in valid_emulators and 'True' in game_auto_region:
			# check db for region value
			con = sqlite3.connect(myprograms6_db)
			cur = con.cursor()
			con.text_factory = str
			query = 'SELECT * FROM files WHERE strFileName LIKE ?'
			cur.execute(query, (Emu_Path_XBE,))
			row = cur.fetchone()
			if row:
				regions = {
					1: '<video>ntsc</video>',
					2: '<video>ntsc-j</video>',
					4: '<video>pal</video>'
				}
				xberegion = regions.get(row[6], '')
			con.close()
			if xberegion == '':
				while True:
					xbmc.executebuiltin('xberegion({})'.format(Emu_Path_XBE))
					time.sleep(0.5)
					xberegion = xbmc.getInfoLabel('skin.string(xberegion)')
					if 'checking' not in xberegion:
						xberegion = '<video>{}</video>'.format(xberegion)
						break

		if Emu_Name == 'scummvm' or 'scummvm' in Emu_Path_XBE:
			handle_scummvm_emulator(cut, Emu_Name, Rom_Name_Path, Emu_Path_XBE, Custom_Emus_Path)
		elif Emu_Name in ('xbox', 'ports', 'homebrew'):
			cut.write('<shortcut>{}<path>{}</path></shortcut>'.format(xberegion, Emu_Path_XBE))
		else:
			cut.write('<shortcut><path>{}</path><custom><game>{}</game></custom></shortcut>'.format(
				os.path.join(Custom_Emus_Path, Emu_Name, Emu_Path_XBE), os.path.join(Custom_Roms_Path,Emu_Name,Rom_Name_Path)))

	if Emu_Name == 'mame' or 'mame' in Emu_Path_XBE:
		handle_mame_emulator(Emu_Name, Rom_Name_Path, Custom_Emus_Path, Custom_Roms_Path)

	if Emu_Name in ('mame', 'scummvm'):
		with open(os.path.join(Root_Directory,'emustation\\scripts\\return_rom.py') , 'w') as autoexec:
			autoexec.write('''import os, shutil, time, xbmc
	if xbmc.getInfoLabel('Skin.String(emuname)') == 'mame':
	Emu_Path_XBE = os.path.join(xbmc.getInfoLabel('skin.string(custom_emulator_path)'),xbmc.getInfoLabel('Skin.String(emuname)'))
	Autobootrom_Path = os.path.join(xbmc.getInfoLabel('skin.string(custom_emulator_path)'),xbmc.getInfoLabel('Skin.String(emuname)'),'autobootrom')
	EmuRom_Path = os.path.join(xbmc.getInfoLabel('skin.string(custom_roms_path)'),xbmc.getInfoLabel('Skin.String(emuname)'))
	time.sleep(2)
	try:
		if os.path.isfile(os.path.join(Autobootrom_Path,'autobootrom.rom')):
			for zip in os.listdir(Autobootrom_Path):
				if zip.endswith('.zip'):
					shutil.move(os.path.join(Autobootrom_Path,zip),EmuRom_Path)
			if os.path.isfile(os.path.join(Autobootrom_Path,'clone.rom')): os.remove(Autobootrom_Path+'/clone.rom')
			os.remove(Autobootrom_Path+'/autobootrom.rom')
			os.rename(os.path.join(Emu_Path_XBE,'default disabled.xbe'),os.path.join(Emu_Path_XBE,'default.xbe'))
	except: pass
	if xbmc.getInfoLabel('Skin.String(emuname)') == 'scummvm':
	ScummVM_SVM_Path = os.path.join(xbmc.getInfoLabel('skin.string(custom_emulator_path)'),xbmc.getInfoLabel('Skin.String(emuname)'), 'scummvm.dat')
	ScummVM_INI_Path = os.path.join(xbmc.getInfoLabel('skin.string(custom_emulator_path)'),xbmc.getInfoLabel('Skin.String(emuname)'), 'scummvm.ini')
	shutil.copy2(ScummVM_SVM_Path, ScummVM_INI_Path)
	time.sleep(2)''')

	if not Favourite_Launch and xbmc.getCondVisibility('Skin.HasSetting(lastromlist)'):
		xbmc.executebuiltin('Skin.SetBool(gameloaded)')
		if not os.path.isfile('Q:\\system\\nointroplay'):
			with open('Q:\\system\\nointroplay', 'w'):
				pass

	if not Emu_Name == 'favs':
		time.sleep(1)

	if xbmc.getCondVisibility('Skin.HasSetting(reloademustation)'):
		write_igr_file()

	time.sleep(1)
	xbmc.executebuiltin('Dialog.Close(134,false)')
	xbmc.executebuiltin('runxbe(z:\\tmp.cut)')
except IOError:
	xbmc.executebuiltin('Dialog.close(1101,true)')
	xbmcgui.Dialog().ok('Error', 'Something went wrong.', 'Z:\\tmp.cut is write protected.')
except Exception:
	xbmc.executebuiltin('Dialog.close(1101,true)')
	xbmcgui.Dialog().ok('Error', 'Something went wrong.', 'Please rescan your roms/games.')