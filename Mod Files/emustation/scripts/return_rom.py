import os, shutil, time, xbmc
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