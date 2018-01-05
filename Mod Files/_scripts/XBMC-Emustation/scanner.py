'''
	Script by Rocky5
	Used to scan for emulators default.xbe files and enable the menu entry.
	Also scans for games default.xbe files and populates the counter for them.
'''
import glob, os, sys, time, xbmc, xbmcgui
#####	Start markings for the log file.
print "| _Scripts\XBMC-Emustation\scanner.py loaded."
pDialog							= xbmcgui.DialogProgress()
dialog							= xbmcgui.Dialog()
Cancelled						= ""
try:
	Update_Emulators = sys.argv[1:][0]
	Update_Emulator  = sys.argv[2:][0]
	Update_XBE_Games = sys.argv[3:][0]
	SilentMode		 = sys.argv[4:][0]
except:
	Update_Emulators = "0"
	Update_Emulator  = "0"
	Update_XBE_Games = "scan_xbes"
	SilentMode		 = "0"
#####	Sets paths.
if str( xbmc.getCondVisibility( 'Skin.String(Custom_Emulator_Path)' ) ) == "1":
	Emulator_Path		= xbmc.getInfoLabel( 'Skin.String(Custom_Emulator_Path)' )
else:
	Emulator_Path		= 'Q:\\_emulators\\'
if str( xbmc.getCondVisibility( 'Skin.String(Custom_Roms_Path)' ) ) == "1":
	Roms_Path			= xbmc.getInfoLabel( 'Skin.String(Custom_Roms_Path)' )
else:
	Roms_Path			= 'Q:\\_roms\\'
CUTFile_Path			= 'Q:\\_cuts\\'
Game_Directories		= [ "E:\\Games\\","E:\\Games1\\","E:\\Games2\\","F:\\Games\\","F:\\Games1\\","F:\\Games2\\","G:\\Games\\","G:\\Games1\\","G:\\Games2\\" ]
Homebrew_Directories	= [ "E:\\Homebrew\\","F:\\Homebrew\\","G:\\Homebrew\\" ]
Apps_Directories		= [ "E:\\Apps\\","F:\\Apps\\","G:\\Apps\\","E:\\Applications\\","F:\\Applications\\","G:\\Applications\\" ]
EMU_Directories			= [ "3do","amiga","amstradcpc","apple2","atari2600","atari5200","atari7800","atari800","atarijaguar","atarijaguarcd","atarilynx","atarist","atarixe","atarixl","c64","c64pet","chip8x","coco","colecovision","cv20","daphne","dreamcastvmu","famicom","fba","gamegear","gb","gba","gbc","genesis","intellivision","mame","mastersystem","megadrive","mess","msx","n64","nds","neogeo","neogeocd","nes","ngp","ngpc","odyssey2","pc-98","pce-cd","pcengine","psx","samcoupe","saturn","sc-3000","scummvm","sega32x","segacd","sf-7000","sg-1000","sgb","sgb2","snes","tg-cd","tg16","ti99","virtualboy","waterasupervision","wonderswan","x68000","zxspectrum" ] ## used to create folders of the supported emulators.

if Update_Emulators == "scan_emus":
	if not os.path.isdir( Emulator_Path ): os.makedirs( Emulator_Path )
	if not os.path.isdir( Roms_Path ): os.makedirs( Roms_Path )
	for EMU_Directories in EMU_Directories:
		if not os.path.isdir( os.path.join( Emulator_Path, EMU_Directories ) ): os.makedirs( os.path.join( Emulator_Path, EMU_Directories ) )
		if EMU_Directories == "atarijaguar" or EMU_Directories == "atarijaguarcd":
			pass
		else:
			if not os.path.isdir( os.path.join( Roms_Path, EMU_Directories ) ): os.makedirs( os.path.join( Roms_Path, EMU_Directories ) )
	CountList = 1
	pDialog.update( 0 )
	if not SilentMode == "silent_mode": pDialog.create( "Refreshing Emulator List","Initializing" )
	for Items in sorted( os.listdir( Emulator_Path ) ):
		EmuFolder = Items
		if EmuFolder == "atarijaguar" or EmuFolder == "atarijaguarcd":
			Roms_Folder = os.path.join( Emulator_Path + Items ) + "\\roms"
		else:
			Roms_Folder = os.path.join( Roms_Path + Items )
		if len(os.listdir( Roms_Folder )) > 0:
			if os.path.isdir(os.path.join( Emulator_Path, Items)):
				Emulator	= os.path.join( Emulator_Path, Items ) + '\\'
				if os.path.isfile( os.path.join( Emulator, "default.xbe" ) ):
					xbmc.executebuiltin('Skin.SetBool('+ EmuFolder  +'_exists)')
				else:
					xbmc.executebuiltin('Skin.Reset('+ EmuFolder +'_exists)')
		else:
			pass
			xbmc.executebuiltin('Skin.Reset('+ EmuFolder +'_exists)' )
		if not SilentMode == "silent_mode": pDialog.update( ( CountList * 100 ) / len( os.listdir( Emulator_Path ) ),"Checking for " + EmuFolder + " emulator","and updating emulator list" )
		time.sleep(0.1) ## this is here so the progress bar can update
		CountList = CountList + 1

if not Update_Emulator == "0":	
	if not os.path.isdir( Emulator_Path ): os.makedirs( Emulator_Path )
	if not os.path.isdir( Roms_Path ): os.makedirs( Roms_Path )
	#pDialog.update( 0 )
	#pDialog.create( "Refreshing Emulator List","Checking for " + Update_Emulator + " emulator" )
	EmuFolder = os.path.join( Emulator_Path, Update_Emulator )
	if os.path.isdir( EmuFolder ):
		if os.path.isfile( os.path.join( EmuFolder, "default.xbe" ) ):
			xbmc.executebuiltin('Skin.SetBool('+ EmuFolder  +'_exists)')
			#pDialog.update( 0,"Checking for " + Update_Emulator + " emulator","and updating emulator list" )
		else:
			xbmc.executebuiltin('Skin.Reset('+ EmuFolder +'_exists)')
			#pDialog.update( 0,"Checking for " + Update_Emulator + " emulator.","No emulator found." )
	else:
		pass
		xbmc.executebuiltin('Skin.Reset('+ EmuFolder +'_exists)' )
	#time.sleep(3) ## this is here so the progress bar can update
	
if Update_XBE_Games == "scan_xbes":
	xbecount = 0
	if not SilentMode == "silent_mode": pDialog.create( "Refreshing XBE Counter","Initializing" )
	for Game_Directories in Game_Directories:
		CountList = 1
		pDialog.update( 0 )
		if os.path.isdir( Game_Directories ):
			for Items in sorted( os.listdir( Game_Directories ) ):
				if os.path.isdir(os.path.join( Game_Directories, Items)):
					Game_Path = os.path.join( Game_Directories, Items ) + "\\"
					if os.path.isdir( Game_Path ):
						XBEFiles = glob.glob( os.path.join( Game_Path, "default.xbe" ) )
						if not ( pDialog.iscanceled() ):
							for Default in XBEFiles:
								if os.path.isfile( Default ):
									xbecount = xbecount + 1
								if not SilentMode == "silent_mode": 
									pDialog.update( ( CountList * 100 ) / len( os.listdir( Game_Directories ) ),"Processing",Items )
									CountList = CountList + 1
						else:
							Cancelled = "True"
							pass
	xbmc.executebuiltin('Skin.SetString(xbox_games,' + str(xbecount) + ')')
	xbecount = 0
	for Homebrew_Directories in Homebrew_Directories:
		CountList = 1
		pDialog.update( 0 )
		if os.path.isdir( Homebrew_Directories ):
			for Items in sorted( os.listdir( Homebrew_Directories ) ):
				if os.path.isdir(os.path.join( Homebrew_Directories, Items)):
					Game_Path = os.path.join( Homebrew_Directories, Items ) + "\\"
					if os.path.isdir( Game_Path ):
						XBEFiles = glob.glob( os.path.join( Game_Path, "default.xbe" ) )
						if not ( pDialog.iscanceled() ):
							for Default in XBEFiles:
								if os.path.isfile( Default ):
									xbecount = xbecount + 1
								if not SilentMode == "silent_mode": 
									pDialog.update( ( CountList * 100 ) / len( os.listdir( Homebrew_Directories ) ),"Processing",Items )
									CountList = CountList + 1
						else:
							Cancelled = "True"
							pass
	xbmc.executebuiltin('Skin.SetString(ports_games,' + str(xbecount) + ')')
	xbecount = 0
	for Apps_Directories in Apps_Directories:
		CountList = 1
		pDialog.update( 0 )
		if os.path.isdir( Apps_Directories ):
			for Items in sorted( os.listdir( Apps_Directories ) ):
				if os.path.isdir(os.path.join( Apps_Directories, Items)):
					Game_Path = os.path.join( Apps_Directories, Items ) + "\\"
					if os.path.isdir( Game_Path ):
						XBEFiles = glob.glob( os.path.join( Game_Path, "default.xbe" ) )
						if not ( pDialog.iscanceled() ):
							for Default in XBEFiles:
								if os.path.isfile( Default ):
									xbecount = xbecount + 1
								if not SilentMode == "silent_mode": 
									pDialog.update( ( CountList * 100 ) / len( os.listdir( Apps_Directories ) ),"Processing",Items )
									CountList = CountList + 1
						else:
							Cancelled = "True"
							pass
	xbmc.executebuiltin('Skin.SetString(apps_installed,' + str(xbecount) + ')')

if not SilentMode == "silent_mode": 
	pDialog.update(0)
	pDialog.close()
	xbmcgui.Window(xbmcgui.getCurrentWindowId()).setProperty("MyScript.ExternalRunning", "False")
	xbmc.executebuiltin("Notification(Complete,Emulator list updated)")
else:
	xbmc.executebuiltin('RunScript(Q:\\_scripts\\xbmc-emustation\\update_favs_counter.py)' )
	xbmc.executebuiltin("Notification(Complete,Menu counters and _roms folder populated)")