'''
	Script by Rocky5
	Used to patch emulator xbe files to load files from there root directory instead of E:\.
'''

import glob, os, re, xbmc, xbmcgui

#####	Start markings for the log file.
print "| _Scripts\XBMC-Emustation\patch_xbe_paths.py loaded."
pDialog		= xbmcgui.DialogProgress()
dialog		= xbmcgui.Dialog()

if str( xbmc.getCondVisibility( 'Skin.String(Custom_Emulator_Path)' ) ) == "1":
	Emulator_Path	= xbmc.getInfoLabel( 'Skin.String(Custom_Emulator_Path)' )
else:
	Emulator_Path	= 'Q:\\_emulators\\'

def patch():
	Select_Emu_Folder = dialog.select( "Select a Emulator folder",sorted( os.listdir( Emulator_Path ) ) )
	Emu_Path = os.path.join( Emulator_Path, sorted( os.listdir( Emulator_Path ) )[Select_Emu_Folder] ) + "\\"
	if os.path.isfile( os.path.join( Emu_Path, "default.xbe" ) ):
		Emu_XBE = os.path.join( Emu_Path, "default.xbe" )
	elif Select_Emu_Folder == -1:
		return
	else:
		dialog.ok("Error","No default.xbe found in this directory")
		return patch()
	CountList = 1
	Emu_Name = os.path.split(os.path.dirname( Emu_Path ))[1]
		
	for XBE_File in glob.glob(r'' + Emu_Path +'*.xbe'):
		if CountList == 1: pDialog.create( "Scanning for Emulators","","Please wait..." )
		pDialog.update( ( CountList * 100 ) / len( os.listdir( Emu_Path ) ),"Processing Emulators",XBE_File,"Please wait..." )
		# Fastest way of doing it.
		with open( os.path.join( Emu_Path, XBE_File ), "rb") as inputfile:
			read_file = inputfile.read()
		with open( os.path.join( Emu_Path, XBE_File ), "wb") as outputfile:
			file_content = read_file.replace( 'e:\\s','D:\\S' )
			file_content = file_content.replace( 'e:\\S','D:\\S' )
			file_content = file_content.replace( 'E:\\S','D:\\S' )
			file_content = file_content.replace( 'e:\\m','D:\\M' )
			file_content = file_content.replace( 'e:\\M','D:\\M' )
			file_content = file_content.replace( 'E:\\M','D:\\M' )
			outputfile.write( file_content )
		# Slower way of doing it, but ignores case.
		# with open( os.path.join( Emu_Path, XBE_File ), "rb") as inputfile:
			# read_file = inputfile.read()
		# with open( os.path.join( Emu_Path, XBE_File ), "wb") as outputfile:
			# replace = re.compile(re.escape('E:\\S'), re.IGNORECASE)
			# replace = replace.sub( 'D:\\S',read_file )
			# outputfile.write( replace )
		# with open( os.path.join( Emu_Path, XBE_File ), "rb") as inputfile:
			# read_file = inputfile.read()
		# with open( os.path.join( Emu_Path, XBE_File ), "wb") as outputfile:
			# replace = re.compile(re.escape('E:\\M'), re.IGNORECASE)
			# replace = replace.sub( 'D:\\M',read_file )
			# outputfile.write( replace )
		CountList = CountList + 1
	pDialog.close()
	dialog.ok( "Process Complete","xbe files patched" )
	return

patch()
pDialog.update(0)
pDialog.close()