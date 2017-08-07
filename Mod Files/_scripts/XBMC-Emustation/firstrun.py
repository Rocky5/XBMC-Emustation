'''
	Script by Rocky5
	Used to create the _roms directory structure.
'''

import glob, os, sys, time, xbmc, xbmcgui

#####	Start markings for the log file.
print "================================================================================"
print "| _Scripts\XBMC-Emustation\firstrun.py loaded."
print "| ------------------------------------------------------------------------------"


#####	Sets paths.
# Gets current XBMC4Gamers directory.
CharCount = 100 # How many characters you want after 'The executable running is: '
with open( xbmc.translatePath( "special://xbmc/system/" ) + "xbmc.log", "r" ) as XBMCLOG:
	for line in XBMCLOG:
		left,found,right = line.partition("The executable running is: ")
		if found:
			Working_Directory		= ( right[:CharCount] )
			Root_Directory 			= Working_Directory[:-12] # Removed \default.xbe
			Emulator_Path			= Root_Directory + '_emulators\\'
			CUTFile_Path			= Root_Directory + '_cuts\\'
			Rom_Path				= Root_Directory + '_roms\\'
			EMU_Directories			= [ "3do","amiga","amstradcpc","coco","colecovision","apple2","atari800","atari2600","atari5200","atari7800","atarijaguar","atarilynx","atarist","atarixe","atarixl","c64","c64pet","chip8x","cv20","daphnex","dreamcastvmu","fba","gamegear","gb","gba","gbc","genesis","intellivision","mame","mastersystem","megadrive","mess","msx","n64","neogeocd","ngpc","nds","nes","odyssey2","pc-98","pcengine","psx","samcoupe","saturn","sc-3000","scummvm","sega32x","segacd","sf-7000","sg-1000","sgb","sgb2","snes","ti99","virtualboy","wonderswan","waterasupervision","x68000","zxspectrum", ] ## used to create folders of the supported emulators.
###########

if os.path.isdir( Emulator_Path ):
	for EMU_Directories in EMU_Directories:
		if not os.path.isdir( os.path.join( Emulator_Path, EMU_Directories ) ): os.makedirs( os.path.join( Emulator_Path, EMU_Directories ) )
		if EMU_Directories == "fba":
			pass
		elif EMU_Directories == "mame":
			pass
		else:
			if not os.path.isdir( os.path.join( Rom_Path, EMU_Directories ) ): os.makedirs( os.path.join( Rom_Path, EMU_Directories ) )