'''
	Script by Rocky5
	Used to scan for emulators default.xbe files and enable the menu entry.
	Also scans for games default.xbe files and populates the counter for them.
'''
import glob, os, sys, time, xbmc, xbmcgui
#####	Start markings for the log file.
print "| .emustation\Scripts\refresh_carousel.py loaded."
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
	Emulator_Folder_Path		= xbmc.getInfoLabel( 'Skin.String(Custom_Emulator_Path)' )
else:
	Emulator_Folder_Path		= 'Q:\\.emustation\\emulators\\'
if str( xbmc.getCondVisibility( 'Skin.String(Custom_Media_Path)' ) ) == "1":
	Media_Folder_Path		= xbmc.getInfoLabel( 'Skin.String(Custom_Media_Path)' )
else:
	Media_Folder_Path		= 'Q:\\.emustation\\media\\'
if str( xbmc.getCondVisibility( 'Skin.String(Custom_Roms_Path)' ) ) == "1":
	Roms_Path			= xbmc.getInfoLabel( 'Skin.String(Custom_Roms_Path)' )
else:
	Roms_Path			= 'Q:\\.emustation\\roms\\'

Gamelist_Folder_Path	= 'Q:\\.emustation\\gamelists\\'
Game_Directories		= [ "E:\\Games\\","E:\\Games1\\","E:\\Games2\\","F:\\Games\\","F:\\Games1\\","F:\\Games2\\","G:\\Games\\","G:\\Games1\\","G:\\Games2\\" ]
Homebrew_Directories	= [ "E:\\Homebrew\\","F:\\Homebrew\\","G:\\Homebrew\\","E:\\Ports\\","F:\\Ports\\","G:\\Ports\\" ]
Apps_Directories		= [ "E:\\Apps\\","F:\\Apps\\","G:\\Apps\\","E:\\Applications\\","F:\\Applications\\","G:\\Applications\\" ]
EMU_Directories			= [ "3do","amiga","amstradcpc","apple2","atari2600","atari5200","atari7800","atari800","atarijaguar","atarilynx","atarist","atarixe","atarixl","c64","c64pet","chip8x","coco","colecovision","cv20","daphne","dreamcastvmu","famicom","fba","fbaxxx","fbl","fblc","gamegear","gb","gba","gbc","genesis","intellivision","mame","mastersystem","megadrive","mess","msx","n64","nds","neogeo","neogeocd","nes","ngp","ngpc","odyssey2","pc-98","pce-cd","pcengine","pokemonmini","psx","samcoupe","saturn","sc-3000","scummvm","sega32x","segacd","sf-7000","sg-1000","sgb","sgb2","snes","tg-cd","tg16","ti99","virtualboy","waterasupervision","wonderswan","x68000","zxspectrum" ] ## used to create folders of the supported emulators.

if Update_Emulators == "scan_emus":
	CountList = 1
	pDialog.update( 0 )
	if not os.path.isdir( Emulator_Folder_Path ): os.makedirs( Emulator_Folder_Path )
	if not os.path.isdir( Gamelist_Folder_Path ): os.makedirs( Gamelist_Folder_Path )
	for Emulators in EMU_Directories:
		if not os.path.isdir( os.path.join( Emulator_Folder_Path, Emulators ) ): os.makedirs( os.path.join( Emulator_Folder_Path, Emulators ) )
		if Emulators == "atarijaguar" or Emulators == "mame" or Emulators == "neogeocd":
			pass
		else:
			Media_Path	= os.path.join( Media_Folder_Path, Emulators )
			if not os.path.isdir( os.path.join( Media_Path,'boxart' ) ): os.makedirs( os.path.join( Media_Path,'boxart' ) )
			if not os.path.isdir( os.path.join( Media_Path,'boxart3d' ) ): os.makedirs( os.path.join( Media_Path,'boxart3d' ) )
			if not os.path.isdir( os.path.join( Media_Path,'logo' ) ): os.makedirs( os.path.join( Media_Path,'logo' ) )
			if not os.path.isdir( os.path.join( Media_Path,'mix' ) ): os.makedirs( os.path.join( Media_Path,'mix' ) )
			if not os.path.isdir( os.path.join( Media_Path,'videos' ) ): os.makedirs( os.path.join( Media_Path,'videos' ) )
			if not os.path.isdir( os.path.join( Media_Path,'screenshots' ) ): os.makedirs( os.path.join( Media_Path,'screenshots' ) )
		if Emulators == "atarijaguar":
			pass
		else:
			if not os.path.isdir( os.path.join( Roms_Path, Emulators ) ): os.makedirs( os.path.join( Roms_Path, Emulators ) )
	if not SilentMode == "silent_mode": pDialog.create( "Refreshing Emulator List","Initializing" )
	for EmuFolder in sorted( os.listdir( Emulator_Folder_Path ) ):
		if EmuFolder == "atarijaguar":
			Roms_Folder = os.path.join( Emulator_Folder_Path, EmuFolder, 'roms' )
		else:
			Roms_Folder = os.path.join( Roms_Path, EmuFolder )
		if os.path.isfile( os.path.join( Emulator_Folder_Path, EmuFolder, 'default.xbe' ) ) and len(os.listdir( Roms_Folder )) > 0:
			xbmc.executebuiltin('Skin.SetBool('+ EmuFolder  +'_exists)')
		else:
			xbmc.executebuiltin('Skin.Reset('+ EmuFolder +'_exists)' )
		if not SilentMode == "silent_mode": pDialog.update( ( CountList * 100 ) / len( os.listdir( Emulator_Folder_Path ) ),"Checking for " + EmuFolder + " emulator","and updating emulator list" )
		time.sleep(0.05) ## this is here so the progress bar can update
		CountList = CountList + 1

if not Update_Emulator == "0":	
	if not os.path.isdir( Emulator_Folder_Path ): os.makedirs( Emulator_Folder_Path )
	if not os.path.isdir( Gamelist_Folder_Path ): os.makedirs( Gamelist_Folder_Path )
	if not os.path.isdir( Media_Folder_Path ): os.makedirs( Media_Folder_Path )
	#pDialog.update( 0 )
	#pDialog.create( "Refreshing Emulator List","Checking for " + Update_Emulator + " emulator" )
	if os.path.isfile( os.path.join( Emulator_Folder_Path, Update_Emulator, "default.xbe" ) ):
		xbmc.executebuiltin('Skin.SetBool('+ Update_Emulator  +'_exists)')
		#pDialog.update( 0,"Checking for " + Update_Emulator + " emulator","and updating emulator list" )
	else:
		xbmc.executebuiltin('Skin.Reset('+ Update_Emulator +'_exists)')
		#pDialog.update( 0,"Checking for " + Update_Emulator + " emulator.","No emulator found." )
	
if Update_XBE_Games == "scan_xbes":
	xbecount = 0
	if not SilentMode == "silent_mode": pDialog.create( "Refreshing XBE Counter","Initializing" )
	# for Game_Directories in Game_Directories:
		# CountList = 1
		# pDialog.update( 0 )
		# if os.path.isdir( Game_Directories ):
			# for Items in sorted( os.listdir( Game_Directories ) ):
				# if os.path.isdir(os.path.join( Game_Directories, Items)):
					# Game_Path = os.path.join( Game_Directories, Items ) + "\\"
					# if os.path.isdir( Game_Path ):
						# XBEFiles = glob.glob( os.path.join( Game_Path, "default.xbe" ) )
						# if not ( pDialog.iscanceled() ):
							# for Default in XBEFiles:
								# if os.path.isfile( Default ):
									# xbecount = xbecount + 1
								# if not SilentMode == "silent_mode": 
									# pDialog.update( ( CountList * 100 ) / len( os.listdir( Game_Directories ) ),"Processing",Items )
									# CountList = CountList + 1
						# else:
							# Cancelled = "True"
							# pass
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
	xbmc.executebuiltin('RunScript(Q:\\.emustation\\scripts\\update_favs_counter.py)' )
	xbmc.executebuiltin("Notification(Complete,Menu counters populated)")