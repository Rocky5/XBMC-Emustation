'''
	Script by Rocky5
	Used to scan for emulators default.xbe files and enable the menu entry.
	Also scans for games default.xbe files and emulator CUT files.
'''

import glob, os, sys, time, xbmc, xbmcgui

#####	Start markings for the log file.
print "| _Scripts\XBMC-Emustation\scanner.py loaded."

pDialog							= xbmcgui.DialogProgress()
dialog							= xbmcgui.Dialog()
Cancelled						= ""

try:
	Updaye_Emulators = sys.argv[1:][0]
	Update_CUT_Games = sys.argv[2:][0]
	Update_XBE_Games = sys.argv[3:][0]
	SilentMode		 = sys.argv[4:][0]
except:
	Updaye_Emulators = "0"
	Update_CUT_Games = "0"
	Update_XBE_Games = "scan_xbes"
	SilentMode		 = "0"

#####	Sets paths.
# Gets current XBMC4Gamers directory.
CharCount = 100 # How many characters you want after 'The executable running is: '
with open( xbmc.translatePath( "special://xbmc/system/" ) + "xbmc.log", "r" ) as XBMCLOG:
	for line in XBMCLOG:
		left,found,right = line.partition("The executable running is: ")
		if found:
			Working_Directory		= ( right[:CharCount] )
			Root_Directory 			= Working_Directory[:-12] # Removed \default.xbe
			if str( xbmc.getCondVisibility( 'Skin.String(Custom_Emulator_Path)' ) ) == "1":
				Emulator_Path		= xbmc.getInfoLabel( 'Skin.String(Custom_Emulator_Path)' )
			else:
				Emulator_Path		= Root_Directory + '_emulators\\'
			if str( xbmc.getCondVisibility( 'Skin.String(Custom_Roms_Path)' ) ) == "1":
				Roms_Path			= xbmc.getInfoLabel( 'Skin.String(Custom_Roms_Path)' )
			else:
				Roms_Path			= Root_Directory + '_roms\\'
			CUTFile_Path			= Root_Directory + '_cuts\\'
			Game_Directories		= [ "E:\\Games\\","E:\\Games1\\","E:\\Games2\\","F:\\Games\\","F:\\Games1\\","F:\\Games2\\","G:\\Games\\","G:\\Games1\\","G:\\Games2\\" ]
			Homebrew_Directories	= [ "E:\\Homebrew\\","F:\\Homebrew\\","G:\\Homebrew\\" ]
			Apps_Directories		= [ "E:\\Apps\\","F:\\Apps\\","G:\\Apps\\","E:\\Applications\\","F:\\Applications\\","G:\\Applications\\" ]
			EMU_Directories			= [ "3do","amiga","amstradcpc","apple2","atari2600","atari5200","atari7800","atari800","atarijaguar","atarijaguarcd","atarilynx","atarist","atarixe","atarixl","c64","c64pet","chip8x","coco","colecovision","cv20","daphne","dreamcastvmu","fba","gamegear","gb","gba","gbc","genesis","intellivision","mame","mastersystem","megadrive","mess","msx","n64","nds","neogeo","neogeocd","nes","ngp","ngpc","odyssey2","pc-98","pce-cd","pcengine","psx","samcoupe","saturn","sc-3000","scummvm","sega32x","segacd","sf-7000","sg-1000","sgb","sgb2","snes","ti99","virtualboy","waterasupervision","wonderswan","x68000","zxspectrum" ] ## used to create folders of the supported emulators.
###########

if Updaye_Emulators == "scan_emus":

	if os.path.isdir( Emulator_Path ):
	
		for EMU_Directories in EMU_Directories:
		
			if not os.path.isdir( os.path.join( Emulator_Path, EMU_Directories ) ): os.makedirs( os.path.join( Emulator_Path, EMU_Directories ) )
			
			if EMU_Directories == "fba":
				pass
			elif EMU_Directories == "atarijaguar":
				pass
			elif EMU_Directories == "mame":
				pass
			else:
				if not os.path.isdir( os.path.join( Roms_Path, EMU_Directories ) ): os.makedirs( os.path.join( Roms_Path, EMU_Directories ) )
		
		CountList = 1
		pDialog.update( 0 )
		
		if not SilentMode == "silent_mode": pDialog.create( "Refreshing Emulator List","","Please wait..." )
		
		for Items in sorted( os.listdir( Emulator_Path ) ):
		
			EmuFolder = Items
			
			if EmuFolder == "fba":
				Roms_Folder = os.path.join( Emulator_Path + Items  ) +  "\\roms"
			elif EmuFolder == "atarijaguar":
				Roms_Folder = os.path.join( Emulator_Path + Items ) + "\\roms"
			elif EmuFolder == "mame":
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
				xbmc.executebuiltin('Skin.Reset('+ EmuFolder +'_exists)' )
				
			if not SilentMode == "silent_mode": pDialog.update( ( CountList * 100 ) / len( os.listdir( Emulator_Path ) ),"Scanning folders",EmuFolder )
			time.sleep(0.1) ## this is here so the progress bar can update
			CountList = CountList + 1
			
	else:
		dialog.ok( "Error",'No [B]"_emulator files"[/B] folder found.' )

if Update_CUT_Games == "scan_cuts":	

	if not SilentMode == "silent_mode": pDialog.create( "Refreshing .CUT File Counters","","Please wait..." )

	if os.path.isdir( Emulator_Path ): ## this is here to get the directory names for the _cut files folder and if it doesn't exist create it.
	
		for Items in sorted( os.listdir( Emulator_Path ) ):
		
			Emu_Folder_Names = os.path.join( CUTFile_Path, Items )
			
			if not os.path.isdir( Emu_Folder_Names ): os.makedirs( Emu_Folder_Names )		
		
		if os.path.isdir( CUTFile_Path ):
		
			CountList = 1
			pDialog.update( 0 )
			
			for Items in sorted( os.listdir( CUTFile_Path ) ):
			
				EmuFolder = Items
				
				if os.path.isdir(os.path.join( CUTFile_Path, Items)):
				
					if not ( pDialog.iscanceled() ):
					
						Emulator	= os.path.join( CUTFile_Path, Items ) + "\\"
						CUTTotal = str(len(glob.glob1(Emulator,"*.cut")))
						
						if not SilentMode == "silent_mode": pDialog.update( ( CountList * 100 ) / len( os.listdir( CUTFile_Path ) ),"Processing",EmuFolder,"Please wait..." )
						
						CountList = CountList + 1
						time.sleep(0.1) ## this is here so the progress bar can update
						
						if CUTTotal == "0":
							xbmc.executebuiltin('Skin.Reset('+ EmuFolder +'_exists)' )
							xbmc.executebuiltin('Skin.Reset('+ EmuFolder +'_games)' )
						else:
							xbmc.executebuiltin('Skin.SetString('+ EmuFolder +'_games,'+ CUTTotal + ')')
					else:
						Cancelled = "True"
						pass
	else:
		dialog.ok( "Error",'No [B]"_emulator files"[/B] folder found.',"Default to XBE file scan." )
		

if Update_XBE_Games == "scan_xbes":

	xbecount = 0
	
	if not SilentMode == "silent_mode": pDialog.create( "Refreshing XBE Counter","","Please wait..." )
	
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
									
									pDialog.update( ( CountList * 100 ) / len( os.listdir( Game_Directories ) ),"Processing",Items,"Please wait..." )
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
									
									pDialog.update( ( CountList * 100 ) / len( os.listdir( Homebrew_Directories ) ),"Processing",Items,"Please wait..." )
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
									
									pDialog.update( ( CountList * 100 ) / len( os.listdir( Apps_Directories ) ),"Processing",Items,"Please wait..." )
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
	xbmc.executebuiltin("Notification(Complete,Menu counters and _roms folder populated)")