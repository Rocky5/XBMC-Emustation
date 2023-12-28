import os, shutil, time, xbmc, xbmcgui
def write_igr_file():
	try:
		if not os.path.isdir('E:\\CACHE'): makedirs('E:\\CACHE')
		with open("E:\\CACHE\\LocalCache20.bin","w") as tmp:
			for xbe in sorted(os.listdir(xbmc.translatePath("Special://root/"))):
				if xbe.endswith('.xbe'): tmp.write(xbmc.translatePath("Special://root/"+xbe))
	except: print "Couldn't create CACHE folder"
try:
	xbmc.Player().stop()
#####
	try:
		Emu_Path_XBE		= sys.argv[1:][0]
		Rom_Name_Path		= sys.argv[2:][0]
		Favourite_Launch	= sys.argv[3:][0]
		Current_position	= sys.argv[4:][0]
	except:
		Favourite_Launch	= 0
		Current_position	= 0
#####
	Root_Directory 			= xbmc.translatePath('Special://root/')
	Custom_Emus_Path 		= xbmc.getInfoLabel('skin.string(custom_emulator_path)')
	Custom_Roms_Path 		= xbmc.getInfoLabel('skin.string(custom_roms_path)')
	xbmc.executebuiltin('Skin.SetString(lastrompos,'+str(Current_position)+')')
	Emu_Name = xbmc.getInfoLabel('Skin.String(emuname)')
#####
	if Custom_Emus_Path.startswith('Q:\\'):
		Custom_Emus_Path = Custom_Emus_Path.replace('Q:\\', Root_Directory)
	
	if Custom_Roms_Path.startswith('Q:\\'):
		Custom_Roms_Path = Custom_Roms_Path.replace('Q:\\', Root_Directory)
	
	if Emu_Path_XBE.startswith('Q:\\'):
		Emu_Path_XBE = Emu_Path_XBE.replace('Q:\\', Root_Directory)
	
	if Rom_Name_Path.startswith('Q:\\'):
		Rom_Name_Path = Rom_Name_Path.replace('Q:\\', Root_Directory)
#####
	if Emu_Name == 'n64' or 'n64' in Emu_Path_XBE: # Have to do this or surreal will clear the config for the loaded rom.
		Rom_CRC = Rom_Name_Path.split('-CRC-',1)[1]
		Rom_Name_Path = Rom_Name_Path.split('-CRC-',1)[0]
		with open('E:\\TDATA\\64ce64ce\Tmp.ini', 'w') as f: f.write('[History]\nromname=Emustation Loader\nromCRC='+Rom_CRC+'\n')
#####
	with open('z:\\tmp.cut', 'w') as cut:
		xbmc.executebuiltin('skin.setstring(xberegion,checking)')
		
		if Emu_Name == 'xbox' or 'xbox' in Rom_Name_Path or Emu_Name == 'ports' or 'ports' in Rom_Name_Path or Emu_Name == 'homebrew' or 'homebrew' in Rom_Name_Path:
			while True:
				xbmc.executebuiltin('xberegion('+Emu_Path_XBE+')') # This is run to get the xbe region, will make it all internal at a later date.
				time.sleep(.5)
				xberegion = xbmc.getInfoLabel('skin.string(xberegion)')
				if xberegion != 'checking': break
		
		if Emu_Name == 'scummvm' or 'scummvm' in Emu_Path_XBE:
			if Emu_Name == 'favs':
				xbmc.executebuiltin('Skin.SetString(emuname,scummvm)')
				Emu_Name = 'scummvm'
			
			gameid = "donotaddgames"
			Game_Path = os.path.join(Custom_Emus_Path,Emu_Name,'svms',Rom_Name_Path+".svm")
			Game_Root = os.path.join(Custom_Emus_Path,Emu_Name,'games')
			
			if not os.path.isdir(Game_Root):
				os.makedirs(Game_Root)
			
			with open (Game_Path) as svm:
				svm = svm.read()
				for line in svm.split('\n'):
					if '[' in line:
						gameid = line.split("[")[1].split("]")[0]
			
			shutil.copy2(os.path.join(Custom_Emus_Path,Emu_Name,"scummvm.ini"), os.path.join(Custom_Emus_Path,Emu_Name,"scummvm.dat"))
			
			with open (Game_Path) as svm:
				svm = svm.readlines()
			with open (os.path.join(Custom_Emus_Path,Emu_Name,"scummvm.dat")) as ini:
				settings = ini.readlines()
			with open (os.path.join(Custom_Emus_Path,Emu_Name,"configs.ini"), "w") as ini:
				ini.write(''.join(settings + svm))
			
			cut.write('<shortcut><path>%s</path><custom><game>%s</game></custom></shortcut>' % (os.path.join(Custom_Emus_Path,Emu_Name,"loader.xbe"),gameid))
		
		elif Emu_Name == 'xbox' or Emu_Name == 'ports' or Emu_Name == 'homebrew':
			cut.write('<shortcut><video>%s</video><path>%s</path></shortcut>' % (xberegion,Emu_Path_XBE))
		elif Emu_Name == 'mame':
			cut.write('<shortcut><path>%s</path></shortcut>' % (os.path.join(Custom_Emus_Path,Emu_Name,Emu_Path_XBE)))
		elif Emu_Name == 'favs':
			if 'xbox' in Rom_Name_Path or 'ports' in Rom_Name_Path or 'homebrew' in Rom_Name_Path:
				cut.write('<shortcut><video>%s</video><path>%s</path></shortcut>' % (xberegion,Emu_Path_XBE))
			else:
				cut.write('<shortcut><path>%s</path><custom><game>%s</game></custom></shortcut>' % (Emu_Path_XBE,Rom_Name_Path))
		elif Emu_Name == 'fba' or Emu_Name == 'fbl' or Emu_Name == 'fblc' or Emu_Name == 'fbaxxx':
			cut.write('<shortcut><path>%s</path><custom><game>%s</game></custom></shortcut>' % (os.path.join(Custom_Emus_Path,Emu_Name,Emu_Path_XBE),Rom_Name_Path))
		else:
			cut.write('<shortcut><path>%s</path><custom><game>%s</game></custom></shortcut>' % (os.path.join(Custom_Emus_Path,Emu_Name,Emu_Path_XBE),os.path.join(Custom_Roms_Path,Emu_Name,Rom_Name_Path)))
#####
	if Emu_Name == 'mame' or 'mame' in Emu_Path_XBE:
		if Emu_Name == 'favs':
			xbmc.executebuiltin('Skin.SetString(emuname,mame)')
			Emu_Name = 'mame'
		if os.path.isfile(os.path.join(Custom_Emus_Path,Emu_Name,'system/ROMS.list')):
			os.remove(os.path.join(Custom_Emus_Path,Emu_Name,'system/ROMS.list'))
		
		if os.path.isfile(os.path.join(Custom_Emus_Path,Emu_Name,'system/ROMS.metadata')):
			os.remove(os.path.join(Custom_Emus_Path,Emu_Name,'system/ROMS.metadata'))
		
		if not os.path.isdir(os.path.join(Custom_Emus_Path,Emu_Name,'autobootrom')):
			os.makedirs(os.path.join(Custom_Emus_Path,Emu_Name,'autobootrom'))
		
		if os.path.isfile(os.path.join(Custom_Emus_Path,Emu_Name,'autobootrom','clone.rom')):
			os.remove(os.path.join(Custom_Emus_Path,Emu_Name,'autobootrom','clone.rom'))
		
		Mame_Rom = Rom_Name_Path.split('--',1)[0]
		Mame_Rom_Clone = Rom_Name_Path.split('--',1)[1]
		for zip in os.listdir(os.path.join(Custom_Emus_Path,Emu_Name,'autobootrom')):
			if zip.endswith('.zip'):
				shutil.move(os.path.join(Custom_Emus_Path,Emu_Name,'autobootrom\\'+zip), os.path.join(Custom_Roms_Path,Emu_Name))
		shutil.move(os.path.join(Custom_Roms_Path,Emu_Name,Mame_Rom+'.zip'), os.path.join(Custom_Emus_Path,Emu_Name,'autobootrom'))
		
		if not Mame_Rom_Clone == 'parent':
			shutil.move(os.path.join(Custom_Roms_Path,Emu_Name,Mame_Rom_Clone+'.zip'), os.path.join(Custom_Emus_Path,Emu_Name,'autobootrom'))
			with open(os.path.join(Custom_Emus_Path,Emu_Name,'autobootrom\\clone.rom'), 'w') as f: f.write('')
		
		if os.path.isfile(os.path.join(Custom_Emus_Path,Emu_Name,'default.xbe')):
			os.rename(os.path.join(Custom_Emus_Path,Emu_Name,'default.xbe'),os.path.join(Custom_Emus_Path,Emu_Name,'default disabled.xbe'))
		
		with open(os.path.join(Custom_Emus_Path,Emu_Name,'autobootrom\\autobootrom.rom'), 'w') as f:
			f.write('')
		with open(os.path.join(Custom_Emus_Path,Emu_Name,'system\\disable_ui'), 'w') as f:
			f.write('')
	
	if Emu_Name == 'mame' or Emu_Name == 'scummvm':
		with open(os.path.join(Root_Directory,'emustation\\scripts\\return_rom.py') , 'w') as autoexec: autoexec.write("import os, shutil, time, xbmc\nif xbmc.getInfoLabel('Skin.String(emuname)') == 'mame':\n	Emu_Path_XBE = os.path.join(xbmc.getInfoLabel('skin.string(custom_emulator_path)'),xbmc.getInfoLabel('Skin.String(emuname)'))\n	Autobootrom_Path = os.path.join(xbmc.getInfoLabel('skin.string(custom_emulator_path)'),xbmc.getInfoLabel('Skin.String(emuname)'),'autobootrom')\n	EmuRom_Path = os.path.join(xbmc.getInfoLabel('skin.string(custom_roms_path)'),xbmc.getInfoLabel('Skin.String(emuname)'))\n	time.sleep(2)\n	try:\n		if os.path.isfile(os.path.join(Autobootrom_Path,'autobootrom.rom')):\n			for zip in os.listdir(Autobootrom_Path):\n				if zip.endswith('.zip'):\n					shutil.move(os.path.join(Autobootrom_Path,zip),EmuRom_Path)\n			if os.path.isfile(os.path.join(Autobootrom_Path,'clone.rom')): os.remove(Autobootrom_Path+'/clone.rom')\n			os.remove(Autobootrom_Path+'/autobootrom.rom')\n			os.rename(os.path.join(Emu_Path_XBE,'default disabled.xbe'),os.path.join(Emu_Path_XBE,'default.xbe'))\n	except: pass\nif xbmc.getInfoLabel('Skin.String(emuname)') == 'scummvm':\n	ScummVM_SVM_Path = os.path.join(xbmc.getInfoLabel('skin.string(custom_emulator_path)'),xbmc.getInfoLabel('Skin.String(emuname)'), 'scummvm.dat')\n	ScummVM_INI_Path = os.path.join(xbmc.getInfoLabel('skin.string(custom_emulator_path)'),xbmc.getInfoLabel('Skin.String(emuname)'), 'scummvm.ini')\n	shutil.copy2(ScummVM_SVM_Path, ScummVM_INI_Path)\n	time.sleep(2)")

#####
	if not Favourite_Launch and xbmc.getCondVisibility('Skin.HasSetting(lastromlist)'):
		xbmc.executebuiltin('Skin.SetBool(gameloaded)')
		if not os.path.isfile('Q:\\system\\nointroplay'):
			with open('Q:\\system\\nointroplay', 'w') as nointroplay: nointroplay.write('')
	else: pass
	
#####
	if not Emu_Name == 'favs': time.sleep(1)
	
#####
	if xbmc.getCondVisibility('Skin.HasSetting(reloademustation)'):
		write_igr_file()
	
	time.sleep(1)
	xbmc.executebuiltin('Dialog.Close(134,false)')
	xbmc.executebuiltin('runxbe(z:\\tmp.cut)')
except:
	xbmc.executebuiltin('Dialog.close(1101,true)')
	xbmcgui.Dialog().ok('Error','Something went wrong.','Please rescan your roms/games.')