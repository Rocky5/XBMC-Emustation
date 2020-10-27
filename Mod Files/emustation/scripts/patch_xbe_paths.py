import fileinput,glob,os,re,xbmc,xbmcgui
pDialog		= xbmcgui.DialogProgress()
dialog		= xbmcgui.Dialog()
if str(xbmc.getCondVisibility('Skin.String(Custom_Emulator_Path)')) == "1":
	Emulator_Folder_Path	= xbmc.getInfoLabel('Skin.String(Custom_Emulator_Path)')
else:
	Emulator_Folder_Path	= 'Q:\\emustation\\emulators\\'
def patch():
	if dialog.yesno("QUESTION TIME","This is used to try patching emulators","to look for there saves in there root directory.","If you have no need then pick no."):
		Select_Emu_Folder = dialog.select("SELECT A SYSTEM",sorted(os.listdir(Emulator_Folder_Path)))
		Emu_Path = os.path.join(Emulator_Folder_Path, sorted(os.listdir(Emulator_Folder_Path))[Select_Emu_Folder]) + "\\"
		Emu_Name = os.path.split(Emu_Path)[1]
		pDialog.update(0,"","")
		if Select_Emu_Folder == -1:
			return
		if os.path.isfile(os.path.join(Emu_Path, "default.xbe")):
			Emu_XBE = os.path.join(Emu_Path, "default.xbe")
		else:
			dialog.ok("Error","No default.xbe found in this directory")
			return patch()
		CountList = 1
		Emu_Name = os.path.split(os.path.dirname(Emu_Path))[1]
		XBE_Total = len(glob.glob(r'' + Emu_Path +'*.xbe'))
		for XBE_File in glob.glob(r'' + Emu_Path +'*.xbe'):
			if CountList == 1: pDialog.create("Scanning for Emulators","Initializing")
			 # Have to read the file 1MB at a time to stop out of memory errors.
			if Emu_Name == "mame":
				with open(os.path.join(Emu_Path, XBE_File), "rb") as inputfile:
					with open(os.path.join(Emu_Path, XBE_File + ' patched'), "wb") as outputfile:
						file_content = inputfile.read(1024*1024)
						while file_content:
							Find_ExitLabel = file_content.find(b'\x4C\x00\x6F\x00\x61\x00\x64\x00\x69\x00\x6E\x00\x67\x00\x2E\x00\x20\x00\x50\x00\x6C\x00\x65\x00\x61\x00\x73\x00\x65\x00\x20\x00\x77\x00\x61\x00\x69\x00\x74\x00\x2E\x00\x2E\x00\x2E\x00')
							if Find_ExitLabel:
								file_content = file_content.replace(b'\x4C\x00\x6F\x00\x61\x00\x64\x00\x69\x00\x6E\x00\x67\x00\x2E\x00\x20\x00\x50\x00\x6C\x00\x65\x00\x61\x00\x73\x00\x65\x00\x20\x00\x77\x00\x61\x00\x69\x00\x74\x00\x2E\x00\x2E\x00\x2E\x00',b'\x52\x00\x65\x00\x74\x00\x75\x00\x72\x00\x6E\x00\x69\x00\x6E\x00\x67\x00\x20\x00\x74\x00\x6F\x00\x20\x00\x6D\x00\x65\x00\x6E\x00\x75\x00\x2E\x00\x2E\x00\x2E\x00\x00\x00\x00\x00\x00\x00')
							Find_BarColour = file_content.find(b'\xC8\x78\x6E\xFF')
							if Find_BarColour:
								file_content = file_content.replace(b'\xC8\x78\x6E\xFF',b'\x00\x1E\xBE\xFF')
							outputfile.write(file_content.replace('T:\\SYSTEM','D:\\system'))
							file_content = inputfile.read(1024*1024)
				os.remove(os.path.join(Emu_Path, XBE_File))
				os.rename(os.path.join(Emu_Path, XBE_File + ' patched'), os.path.join(Emu_Path, XBE_File))
				if os.path.isfile(os.path.join(Emu_Path, 'skins/original/skin.ini')):
					for line in fileinput.input(os.path.join(Emu_Path, 'skins/original/skin.ini'), inplace=1):
						if 'ProgressBar.BarColor =' in line:
							line = line = 'ProgressBar.BarColor = 255 190 30 0\n'
						print line,
			else:
				with open(os.path.join(Emu_Path, XBE_File), "rb") as inputfile:
					with open(os.path.join(Emu_Path, XBE_File + ' patched'), "wb") as outputfile:
						file_content = inputfile.read(1024*1024)
						while file_content:
							file_content = file_content.replace('keepsave','save.sav')
							file_content = file_content.replace('e:\\s','D:\\S')
							file_content = file_content.replace('e:\\S','D:\\S')
							file_content = file_content.replace('E:\\S','D:\\S')
							file_content = file_content.replace('e:\\m','D:\\M')
							file_content = file_content.replace('e:\\M','D:\\M')
							file_content = file_content.replace('E:\\M','D:\\M')
							outputfile.write(file_content)
							file_content = inputfile.read(1024*1024)
				os.remove(os.path.join(Emu_Path, XBE_File))
				os.rename(os.path.join(Emu_Path, XBE_File + ' patched'), os.path.join(Emu_Path, XBE_File))
			pDialog.update((CountList * 100) / XBE_Total,"Patching XBE File",os.path.basename(XBE_File))
			CountList = CountList + 1
		pDialog.close()
		dialog.ok("Process Complete","xbe files patched")
	return
patch()