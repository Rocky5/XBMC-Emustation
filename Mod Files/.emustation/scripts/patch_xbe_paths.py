'''
	Script by Rocky5
	Used to patch emulator xbe files to load files from there root directory instead of E:\.
'''

import glob, os, re, xbmc, xbmcgui

#####	Start markings for the log file.
print "| .emustation\Scripts\patch_xbe_paths.py loaded."
pDialog		= xbmcgui.DialogProgress()
dialog		= xbmcgui.Dialog()

if str( xbmc.getCondVisibility( 'Skin.String(Custom_Emulator_Path)' ) ) == "1":
	Emulator_Folder_Path	= xbmc.getInfoLabel( 'Skin.String(Custom_Emulator_Path)' )
else:
	Emulator_Folder_Path	= 'Q:\\.emustation\\emulators\\'

def patch():
	Select_Emu_Folder = dialog.select( "SELECT A SYSTEM",sorted( os.listdir( Emulator_Folder_Path ) ) )
	Emu_Path = os.path.join( Emulator_Folder_Path, sorted( os.listdir( Emulator_Folder_Path ) )[Select_Emu_Folder] ) + "\\"
	Emu_Name = os.path.split(Emu_Path)[1]
	if Select_Emu_Folder == -1:
		return
	if os.path.isfile( os.path.join( Emu_Path, "default.xbe" ) ):
		Emu_XBE = os.path.join( Emu_Path, "default.xbe" )
	else:
		dialog.ok("Error","No default.xbe found in this directory")
		return patch()
	CountList = 1
	Emu_Name = os.path.split(os.path.dirname( Emu_Path ))[1]
	XBE_Total = len(glob.glob(r'' + Emu_Path +'*.xbe'))
	for XBE_File in glob.glob(r'' + Emu_Path +'*.xbe'):
		if CountList == 1: pDialog.create( "Scanning for Emulators","Initializing" )
		pDialog.update( ( CountList * 100 ) / XBE_Total,"Processing Emulators",XBE_File )
		 # Have to read the file 1MB at a time to stop out of memory errors.
		if Emu_Name == "mame":
			with open( os.path.join( Emu_Path, XBE_File ), "rb") as inputfile:
				with open( os.path.join( Emu_Path, XBE_File + ' patched' ), "wb") as outputfile:
					file_content = inputfile.read(1024*1024)
					while file_content:
						outputfile.write( file_content.replace( 'T:\\SYSTEM','D:\\system' ) )
						file_content = inputfile.read(1024*1024)
			os.remove(os.path.join( Emu_Path, XBE_File ))
			os.rename(os.path.join( Emu_Path, XBE_File + ' patched' ), os.path.join( Emu_Path, XBE_File ))
		else:
			with open( os.path.join( Emu_Path, XBE_File ), "rb") as inputfile:
				with open( os.path.join( Emu_Path, XBE_File + ' patched' ), "wb") as outputfile:
					file_content = inputfile.read(1024*1024)
					while file_content:
						file_content = file_content.replace( 'keepsave','save.sav' )
						file_content = file_content.replace( 'e:\\s','D:\\S' )
						file_content = file_content.replace( 'e:\\S','D:\\S' )
						file_content = file_content.replace( 'E:\\S','D:\\S' )
						file_content = file_content.replace( 'e:\\m','D:\\M' )
						file_content = file_content.replace( 'e:\\M','D:\\M' )
						file_content = file_content.replace( 'E:\\M','D:\\M' )
						outputfile.write( file_content )
						file_content = inputfile.read(1024*1024)
			os.remove(os.path.join( Emu_Path, XBE_File ))
			os.rename(os.path.join( Emu_Path, XBE_File + ' patched' ), os.path.join( Emu_Path, XBE_File ) )
		CountList = CountList + 1
	pDialog.close()
	dialog.ok( "Process Complete","xbe files patched" )
	return

patch()