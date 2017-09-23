'''
	Script by Rocky5
	Used to create static lists from your emulator and roms folder.
	
	Mame and FBA, must have there roms placed inside there root directory.
	( the script will generate static lists for emulators )
'''

import glob, os, shutil, sys, time, xbmc, xbmcgui

try:
	Manual_Scan	= sys.argv[1:][0]
	Full_Scan	= sys.argv[2:][0]
except:
	Manual_Scan	= "0"
	Full_Scan	= "0"

#####	Start markings for the log file.
print "| _Scripts\XBMC-Emustation\create_rom_lists.py loaded."

pDialog							= xbmcgui.DialogProgress()
dialog							= xbmcgui.Dialog()

#####	Sets paths.
# Gets current XBMC-Emustation directory.
CharCount = 100 # How many characters you want after 'The executable running is: '
with open( xbmc.translatePath( "special://xbmc/system/" ) + "xbmc.log", "r" ) as XBMCLOG:
	for line in XBMCLOG:
		left,found,right = line.partition("The executable running is: ")
		if found:
			Working_Directory	= ( right[:CharCount] )
			Root_Directory		= Working_Directory[:-12] # Removed default.xbe
			if str( xbmc.getCondVisibility( 'Skin.String(Custom_Emulator_Path)' ) ) == "1":
				Emulator_Path	= xbmc.getInfoLabel( 'Skin.String(Custom_Emulator_Path)' )
			else:
				Emulator_Path	= Root_Directory + '_emulators\\'
			if str( xbmc.getCondVisibility( 'Skin.String(Custom_Roms_Path)' ) ) == "1":
				Roms_Path		= xbmc.getInfoLabel( 'Skin.String(Custom_Roms_Path)' )
			else:
				Roms_Path		= Root_Directory + '_roms\\'
				
			Synopsis_Path		= Root_Directory + '_synopsis\\'
			CUTFile_Path		= Root_Directory + '_cuts\\'
			Scripts_Path		= Root_Directory + '_scripts\\XBMC-Emustation\\'
			TBN_Path			= Root_Directory + '_tbns\\'
			Rom_List_Path		= Root_Directory + '_scripts\\XBMC-Emustation\\rom lists\\'
			Extensions			= [ "zip","bin","ccd","cue","j64","img","iso","rom","n64","z64","smd","smc","gb","gbc","gba","nes","sms","swc","gg","a26","a78","col","lnx","sfc","sg","fig","vms","exe" ]

def log( input ):
	if logging: print "%s" % str( input )
			
def manual_scan():
	Found_Roms = 0
	Select_Emu_Folder = dialog.select( "Select a Emulator folder",sorted( os.listdir( Emulator_Path ) ) )
	Emu_Path = os.path.join( Emulator_Path, sorted( os.listdir( Emulator_Path ) )[Select_Emu_Folder] ) + "\\"
	Roms_Folder = os.path.join( Roms_Path, sorted( os.listdir( Emulator_Path ) )[Select_Emu_Folder] ) + "\\"
	
	log('|	Convert Q:\\ to a direct path')
	if Emu_Path.startswith("Q:\\"): Emu_Path = Emu_Path.replace( "Q:\\", Root_Directory )

	log('|	Set the Countlist variable and set the emu_name variable.')
	CountList = 1
	CUTCount = 0
	Parse_CUE_CCD_ISO_File = 0
	Parse_ISO_BIN_IMG_File = 0
	Parse_ISO_File = 0
	Parse_FBL_TXT = 0
	Write_CUT_File = 1
	Emu_Name = os.path.split(os.path.dirname( Emu_Path ))[1]
	
	log('|	Check for a default .xbe in the emullator path you selected.')
	if os.path.isfile( os.path.join( Emu_Path, "default.xbe" ) ):
		Emu_XBE = os.path.join( Emu_Path, "default.xbe" )
	elif Select_Emu_Folder == -1:
		return
	else:
		dialog.ok("Error","No default.xbe found in this directory")
		return manual_scan()
	
	log('|	Check for previous layout xml and if it exists remove it.')
	if os.path.isfile( Rom_List_Path + Emu_Name + '.xml' ): os.remove( Rom_List_Path + Emu_Name + '.xml' )
	if not os.path.isdir( Rom_List_Path ): os.makedirs( Rom_List_Path )

	log('|	Write new layout xml header.')
	with open( Rom_List_Path + Emu_Name + '.xml', "wb") as outputmenufile:
		WriteMenuFile = menu_entry_header
		outputmenufile.write( WriteMenuFile )
	
	log('|	Check to see if the folder you selected it fba, or mame as these emulators must have there roms in there own roms folder in the emulators root directory')
	if Emu_Name == "fba":
		Roms_Folder	= Emulator_Path + 'fba\\roms\\'
		Parse_FBL_TXT = 1
	elif Emu_Name == "atarijaguar":
		Roms_Folder	= Emulator_Path + 'atarijaguar\\roms\\'
	elif Emu_Name == "atarijaguarcd":
		Roms_Folder	= Emulator_Path + 'atarijaguarcd\\roms\\'
	elif Emu_Name == "mame":
		Roms_Folder	= Emulator_Path + 'mame\\roms\\'
	elif Emu_Name == "neogeocd":
		Parse_CUE_CCD_ISO_File = 1
	elif Emu_Name == "pce-cd":
		Parse_CUE_CCD_ISO_File = 1
	elif Emu_Name == "saturn":
		Parse_CUE_CCD_ISO_File = 1
	elif Emu_Name == "segacd":
		Parse_ISO_BIN_IMG_File = 1
	elif Emu_Name == "psx":
		Parse_CUE_CCD_ISO_File = 1
	else:
		pass
	
	log('|	Convert Q:\\ to a direct path')
	if Roms_Folder.startswith("Q:\\"): Roms_Folder = Roms_Folder.replace( "Q:\\", Root_Directory )
	
	log('|	Check to see if the emulators = rom folder is empty and exit if it is.')
	if len(os.listdir( Roms_Folder )) > 0:
		
		log('|	Listing the content of the roms folder for parsing.')
		for Items in sorted( os.listdir( Roms_Folder ) ):

				log('|	Checking the file I find, extension agains my table.')
				if Items.endswith(tuple(Extensions)):
					
					log('|	More vars being set.')
					Rom_Name = Items
					CUT_File_Name = Rom_Name[:-4]
					Rom_Name_noext = Rom_Name[:-4]
	
					log('|	Couple more vars being set')
					Output_Path = os.path.join( CUTFile_Path, Emu_Name ) + '\\'
					TBN_File = os.path.join( TBN_Path, Emu_Name, CUT_File_Name ) + '.tbn'
					
					try:
						if Emu_Name == "genesis":
							Synopsis_File = os.path.join( Synopsis_Path, "megadrive", Rom_Name_noext + '.txt' )
						else:
							Synopsis_File = os.path.join( Synopsis_Path, Emu_Name, Rom_Name_noext + '.txt' )
						with open( Synopsis_File ) as input:
							Synopsis = input.read()
							Synopsis1 = Synopsis.split('_________________________', 1)[0]
							Synopsis2 = Synopsis.split('_________________________', 1)[1]
							Synopsis1 = Synopsis1.replace( '&', '&amp;' )
							Synopsis1 = Synopsis1.replace( '>', '&gt;' )
							Synopsis1 = Synopsis1.replace( '<', '&lt;' )
							Synopsis2 = Synopsis2.replace( '&', '&amp;' )
							Synopsis2 = Synopsis2.replace( '>', '&gt;' )
							Synopsis2 = Synopsis2.replace( '<', '&lt;' )
					except:
						Synopsis1 = "No Synopsis"
						Synopsis2 = ""
					# Damn internal labelling system kicks in if these are left alone.
					if Emu_Name == "gbc" and Rom_Name_noext == "1942": Rom_Name_noext = "1942 "
					if Emu_Name == "nes" and Rom_Name_noext == "1942": Rom_Name_noext = "1942 "
					if Emu_Name == "nes" and Rom_Name_noext == "1943": Rom_Name_noext = "1943 "
					if Emu_Name == "nes" and Rom_Name_noext == "720": Rom_Name_noext = "720 "
					Rom_Name_ISO = os.path.join( Roms_Folder, Rom_Name[:-4] ) + ".iso"
					Rom_Name_BIN = os.path.join( Roms_Folder, Rom_Name[:-4] ) + ".bin"
					Rom_Name_IMG = os.path.join( Roms_Folder, Rom_Name[:-4] ) + ".img"
					Rom_Name_CUE = os.path.join( Roms_Folder, Rom_Name[:-4] ) + ".cue"
					Rom_Name_CCD = os.path.join( Roms_Folder, Rom_Name[:-4] ) + ".ccd"
					Rom_Path = os.path.join( Roms_Folder, Rom_Name )

					log('|	Check if fba was found and parse the name text files to get the correct rom names for the list.')
					if Parse_FBL_TXT == 1:
						if os.path.isfile( os.path.join( Emulator_Path, "fba\\info\\rom names\\" ) + Rom_Name_noext + ".txt" ):
							with open( os.path.join( Emulator_Path, "fba\\info\\rom names\\" ) + Rom_Name_noext + ".txt", 'r') as txt:
								FBA_Rom_Name = txt.readline()[:-2]
								Write_CUT_File = 1
						else:
							if Rom_Name == "isgsm.zip":
								Write_CUT_File = 0
							elif Rom_Name == "neogeo.zip":
								Write_CUT_File = 0
							elif Rom_Name == "nmk004.zip":
								Write_CUT_File = 0
							elif Rom_Name == "pgm.zip":
								Write_CUT_File = 0
							else:
								FBA_Rom_Name = Rom_Name_noext
								Write_CUT_File = 1
							
					log('|	Check and parse the directory for iso files.')
					if Parse_ISO_File == 1:
						if Items.endswith( '.iso' ):
							Rom_Path = Rom_Name_ISO
							Write_CUT_File = 1
						else:
							Write_CUT_File = 0	
							
					log('|	Check and parse the directory for bin/iso/img files.')
					if Parse_ISO_BIN_IMG_File == 1:
						if Items.endswith( '.bin' ):
							Rom_Path = Rom_Name_BIN
							Write_CUT_File = 1
						elif Items.endswith( '.img' ):
							Rom_Path = Rom_Name_IMG
							Write_CUT_File = 1
						elif Items.endswith( '.iso' ):
							Rom_Path = Rom_Name_ISO
							Write_CUT_File = 1
						else:
							Write_CUT_File = 0

					log('|	Check and parse the directory for cue/ccd/iso files.')
					if Parse_CUE_CCD_ISO_File == 1:
						if Items.endswith( '.cue' ):
							Rom_Path = Rom_Name_CUE
							Write_CUT_File = 1
						elif Items.endswith( '.ccd' ):
							Rom_Path = Rom_Name_CCD
							Write_CUT_File = 1
						elif Items.endswith( '.iso' ):
							Rom_Path = Rom_Name_ISO
							Write_CUT_File = 1
						else:
							Write_CUT_File = 0
					
					log('|	Check to see if vars are the value I need and create a new dialog.')
					if CountList == 1 and Found_Roms == 0: pDialog.create( "Scanning for Roms","","Please wait..." )
					
					log('|	Setting a var again :/')
					Found_Roms = 1
					
					log('|	Check to see if _tbns folder exists and if it doesnt create it.')
					if not os.path.isdir( os.path.join( TBN_Path, Emu_Name ) ): os.makedirs( os.path.join( TBN_Path, Emu_Name ) )
					
					log('|	Check to see if the output directory exists and remove it.')
					if CountList == 1 and os.path.isdir( Output_Path ):
						pDialog.update( 0,"","Doing house cleaning" )
						shutil.rmtree( Output_Path )# remove old cut files
					
					#log('|	Create a new output directory.')
					#if not os.path.isdir( Output_Path ): os.makedirs( Output_Path )
					
					log('|	Show the progress bar progress.')
					pDialog.update( ( CountList * 100 ) / len( os.listdir( Roms_Folder ) ),"Processing Roms",Rom_Name_noext,"Please wait..." )
					
					if Write_CUT_File:
						log('|	Create the rest of the layout xml file.')
						CUTCount = CUTCount + 1
						with open( Rom_List_Path + Emu_Name + '.xml', "a") as outputmenufile:
							if Emu_Name == "fba":
								WriteMenuFile = menu_entry % (CountList,FBA_Rom_Name,Synopsis1,'RunScript( Special://xbmc/_scripts/XBMC-Emustation/launcher.py,' + Emu_XBE + ',' + CUT_File_Name + ' )',"ActivateWindow(1101)",Synopsis2,TBN_File)
							elif Emu_Name == "mame":
								WriteMenuFile = menu_entry % (CountList,Rom_Name_noext,Synopsis1,'RunScript( Special://xbmc/_scripts/XBMC-Emustation/launcher.py,' + Emu_XBE + ',' + CUT_File_Name + ' )',"ActivateWindow(1101)",Synopsis2,TBN_File)
							else:
								WriteMenuFile = menu_entry % (CountList,Rom_Name_noext,Synopsis1,'RunScript( Special://xbmc/_scripts/XBMC-Emustation/launcher.py,' + Emu_XBE + ',' + Rom_Path + ' )',"ActivateWindow(1101)",Synopsis2,TBN_File)
							outputmenufile.write( WriteMenuFile )

						# log('|	Create the cut file for this rom.')
						# with open(Output_Path + CUT_File_Name + '.cut', "wb") as outputfile:
							# if Emu_Name == "fba":
								# WriteFile = CUT_File_Layout % ( Emu_XBE,CUT_File_Name )
							# elif Emu_Name == "atarijaguar":
								# WriteFile = CUT_File_Layout % ( Emu_XBE,CUT_File_Name )
							# elif Emu_Name == "atarijaguarcd":
								# WriteFile = CUT_File_Layout % ( Emu_XBE,CUT_File_Name )
							# elif Emu_Name == "mame":
								# WriteFile = CUT_File_Layout % ( Emu_XBE,CUT_File_Name )
							# else:
								# WriteFile = CUT_File_Layout % ( Emu_XBE,Rom_Path )
							# outputfile.write( WriteFile )
					
					log('|	Add 1 to the Countlist.')
					CountList = CountList + 1
				
		xbmc.executebuiltin('Skin.SetString('+ Emu_Name +'_games,'+ str( CUTCount ) + ')')	
	else:
		log('|	No roms exist so do some cleanup.')
		# shutil.rmtree( Output_Path )# remove old cut files
		# if not os.path.isdir( Output_Path ): os.makedirs( Output_Path )
	
	log('|	Add the footer to the layout xml file.')
	with open( Rom_List_Path + Emu_Name + '.xml', "a") as outputmenufile:
		WriteMenuFile = menu_entry_footer
		outputmenufile.write( WriteMenuFile )
		
	log('|	Set a property so I can run the next script without this one running on.')
	if ( Found_Roms == 1 ):
		xbmcgui.Window(xbmcgui.getCurrentWindowId()).setProperty("MyScript.ExternalRunning", "True")
		
		log('|	Running the scan script to update the counters.')
		xbmc.executebuiltin('RunScript(' + Scripts_Path + 'scanner.py,scan_emus,0,0,0)' )
		
		log('|	Loop.')
		while (xbmcgui.Window(xbmcgui.getCurrentWindowId()).getProperty("MyScript.ExternalRunning") == "True"):
			time.sleep(0.2)

	pDialog.close()
	return


def full_scan():

	Found_Roms = 0
	
	log('|	Check if _emulators directory is selected instead of the emulator its self.')
	if os.path.isdir( Emulator_Path ):
	
		log('|	Parse all folder in the Emulators_Path')
		for Emu_Path in sorted( os.listdir( Emulator_Path ) ):
		
			log('|	Set the Countlist variable.')
			CountList = 1
			CUTCount = 0
			Parse_CUE_CCD_ISO_File = 0
			Parse_ISO_BIN_IMG_File = 0
			Parse_ISO_File = 0
			Parse_FBL_TXT = 0
			Write_CUT_File = 1
			
			log('|	Checking to make sure the emulator you selected exists.')
			if os.path.isdir( os.path.join( Emulator_Path, Emu_Path ) ):
			
				log('|	Set emu_name/path variable.')
				Emu_Path = os.path.join( Emulator_Path, Emu_Path ) + '\\'
				Emu_Name = os.path.split(os.path.dirname( Emu_Path ))[1]
				
				log('|	Check for previous layout xml and if it exists remove it.')
				if os.path.isfile( Rom_List_Path + Emu_Name + '.xml' ): os.remove( Rom_List_Path + Emu_Name + '.xml' )
				if not os.path.isdir( Rom_List_Path ): os.makedirs( Rom_List_Path )
				
				log('|	Write new layout xml header.')
				with open( Rom_List_Path + Emu_Name + '.xml', "wb") as outputmenufile:
				
					WriteMenuFile = menu_entry_header
					outputmenufile.write( WriteMenuFile )
				
				log('|	Check to see if a defualt.xbe exists')
				if os.path.isfile( os.path.join( Emu_Path, "default.xbe" ) ):
				
					log('|	default.xbe does exist so set the oath varable')
					Emu_XBE = os.path.join( Emu_Path, "default.xbe" )
				
					log('|	Check to see if the current directory is fba or mame and set the roms path.')
					Roms_Folder	= Roms_Path + Emu_Name
					if Emu_Name == "fba":
						Roms_Folder	= Emulator_Path + 'fba\\roms\\'
						Parse_FBL_TXT = 1
					elif Emu_Name == "atarijaguar":
						Roms_Folder	= Emulator_Path + 'atarijaguar\\roms\\'
					elif Emu_Name == "atarijaguarcd":
						Roms_Folder	= Emulator_Path + 'atarijaguarcd\\roms\\'
					elif Emu_Name == "mame":
						Roms_Folder	= Emulator_Path + 'mame\\roms\\'
					elif Emu_Name == "neogeocd":
						Parse_CUE_CCD_ISO_File = 1
					elif Emu_Name == "pce-cd":
						Parse_CUE_CCD_ISO_File = 1
					elif Emu_Name == "saturn":
						Parse_CUE_CCD_ISO_File = 1
					elif Emu_Name == "segacd":
						Parse_ISO_BIN_IMG_File = 1
					elif Emu_Name == "psx":
						Parse_CUE_CCD_ISO_File = 1
					else:
						pass
						
					log('|	Convert Q:\\ to a direct path')
					if Roms_Folder.startswith("Q:\\"): Roms_Folder = Roms_Folder.replace( "Q:\\", Root_Directory )
					
					log('|	Check to see if the emulators = rom folder is empty and exit if it is.')
					if len(os.listdir( Roms_Folder )) > 0:
					
						log('|	Listing the content of the roms folder for parsing.')
						for Items in sorted( os.listdir( Roms_Folder ) ):
						
							log('|	Checking the file I find, extension agains my table.')
							if Items.endswith(tuple(Extensions)):

								log('|	More vars being set.')
								Rom_Name = Items
								CUT_File_Name = Rom_Name[:-4]
								Rom_Name_noext = Rom_Name[:-4]

								log('|	Couple more vars being set')
								Output_Path = os.path.join( CUTFile_Path, Emu_Name ) + '\\'
								TBN_File = os.path.join( TBN_Path, Emu_Name, CUT_File_Name ) + '.tbn'
								
								try:
									if Emu_Name == "genesis":
										Synopsis_File = os.path.join( Synopsis_Path, "megadrive", Rom_Name_noext + '.txt' )
									else:
										Synopsis_File = os.path.join( Synopsis_Path, Emu_Name, Rom_Name_noext + '.txt' )
									with open( Synopsis_File ) as input:
										Synopsis = input.read()
										Synopsis1 = Synopsis.split('_________________________')[0]
										Synopsis2 = Synopsis.split('_________________________')[1]
										Synopsis1 = Synopsis1.replace( '&', '&amp;' )
										Synopsis1 = Synopsis1.replace( '>', '&gt;' )
										Synopsis1 = Synopsis1.replace( '<', '&lt;' )
										Synopsis2 = Synopsis2.replace( '&', '&amp;' )
										Synopsis2 = Synopsis2.replace( '>', '&gt;' )
										Synopsis2 = Synopsis2.replace( '<', '&lt;' )
								except:
									Synopsis1 = "No Synopsis"
									Synopsis2 = ""
								# Damn internal labelling system kicks in if these are left alone.
								if Emu_Name == "gbc" and Rom_Name_noext == "1942": Rom_Name_noext = "1942 "
								if Emu_Name == "nes" and Rom_Name_noext == "1942": Rom_Name_noext = "1942 "
								if Emu_Name == "nes" and Rom_Name_noext == "1943": Rom_Name_noext = "1943 "
								if Emu_Name == "nes" and Rom_Name_noext == "720": Rom_Name_noext = "720 "
								Rom_Name_ISO = os.path.join( Roms_Folder, Rom_Name[:-4] ) + ".iso"
								Rom_Name_BIN = os.path.join( Roms_Folder, Rom_Name[:-4] ) + ".bin"
								Rom_Name_IMG = os.path.join( Roms_Folder, Rom_Name[:-4] ) + ".img"
								Rom_Name_CUE = os.path.join( Roms_Folder, Rom_Name[:-4] ) + ".cue"
								Rom_Name_CCD = os.path.join( Roms_Folder, Rom_Name[:-4] ) + ".ccd"
								Rom_Path = os.path.join( Roms_Folder, Rom_Name )

								log('|	Check if fba was found and parse the name text files to get the correct rom names for the list.')
								if Parse_FBL_TXT == 1:
									if os.path.isfile( os.path.join( Emulator_Path, "fba\\info\\rom names\\" ) + Rom_Name_noext + ".txt" ):
										with open( os.path.join( Emulator_Path, "fba\\info\\rom names\\" ) + Rom_Name_noext + ".txt", 'r') as txt:
											FBA_Rom_Name = txt.readline()[:-2]
											Write_CUT_File = 1
									else:
										if Rom_Name == "isgsm.zip":
											Write_CUT_File = 0
										elif Rom_Name == "neogeo.zip":
											Write_CUT_File = 0
										elif Rom_Name == "nmk004.zip":
											Write_CUT_File = 0
										elif Rom_Name == "pgm.zip":
											Write_CUT_File = 0
										else:
											FBA_Rom_Name = Rom_Name_noext
											Write_CUT_File = 1
										
								log('|	Check and parse the directory for iso files.')
								if Parse_ISO_File == 1:
									if Items.endswith( '.iso' ):
										Rom_Path = Rom_Name_ISO
										Write_CUT_File = 1
									else:
										Write_CUT_File = 0	
										
								log('|	Check and parse the directory for bin/iso/img files.')
								if Parse_ISO_BIN_IMG_File == 1:
									if Items.endswith( '.bin' ):
										Rom_Path = Rom_Name_BIN
										Write_CUT_File = 1
									elif Items.endswith( '.img' ):
										Rom_Path = Rom_Name_IMG
										Write_CUT_File = 1
									elif Items.endswith( '.iso' ):
										Rom_Path = Rom_Name_ISO
										Write_CUT_File = 1
									else:
										Write_CUT_File = 0

								log('|	Check and parse the directory for cue/ccd/iso files.')
								if Parse_CUE_CCD_ISO_File == 1:
									if Items.endswith( '.cue' ):
										Rom_Path = Rom_Name_CUE
										Write_CUT_File = 1
									elif Items.endswith( '.ccd' ):
										Rom_Path = Rom_Name_CCD
										Write_CUT_File = 1
									elif Items.endswith( '.iso' ):
										Rom_Path = Rom_Name_ISO
										Write_CUT_File = 1
									else:
										Write_CUT_File = 0
									
								log('|	Check to see if vars are the value I need and create a new dialog.')
								if CountList == 1 and Found_Roms == 0: pDialog.create( "Scanning for Roms","","Please wait..." )
								
								log('|	Setting a var again :/')
								Found_Roms = 1

								log('|	Check to see if _tbns folder exists and if it doesnt create it.')
								if not os.path.isdir( os.path.join( TBN_Path, Emu_Name ) ): os.makedirs( os.path.join( TBN_Path, Emu_Name ) )

								log('|	Check to see if the output directory exists and remove it.')
								if CountList == 1 and os.path.isdir( Output_Path ):
									pDialog.update( 0,"","Doing house cleaning" )
									shutil.rmtree( Output_Path )# remove old cut files
				
								#log('|	Create a new output directory.')
								#if not os.path.isdir( Output_Path ): os.makedirs( Output_Path )
								
								log('|	Show the progress bar progress.')
								pDialog.update( ( CountList * 100 ) / len( os.listdir( Roms_Folder ) ),"Processing [B][UPPERCASE]" + Emu_Name + "[/UPPERCASE][/B] Roms",Rom_Name_noext,"Please wait..." )
								
								if Write_CUT_File:
									log('|	Create the rest of the layout xml file.')
									CUTCount = CUTCount + 1
									with open( Rom_List_Path + Emu_Name + '.xml', "a") as outputmenufile:
										if Emu_Name == "fba":
											WriteMenuFile = menu_entry % (CountList,FBA_Rom_Name,Synopsis1,'RunScript( Special://xbmc/_scripts/XBMC-Emustation/launcher.py,' + Emu_XBE + ',' + CUT_File_Name + ' )',"ActivateWindow(1101)",Synopsis2,TBN_File)
										elif Emu_Name == "mame":
											WriteMenuFile = menu_entry % (CountList,Rom_Name_noext,Synopsis1,'RunScript( Special://xbmc/_scripts/XBMC-Emustation/launcher.py,' + Emu_XBE + ',' + CUT_File_Name + ' )',"ActivateWindow(1101)",Synopsis2,TBN_File)
										else:
											WriteMenuFile = menu_entry % (CountList,Rom_Name_noext,Synopsis1,'RunScript( Special://xbmc/_scripts/XBMC-Emustation/launcher.py,' + Emu_XBE + ',' + Rom_Path + ' )',"ActivateWindow(1101)",Synopsis2,TBN_File)
										outputmenufile.write( WriteMenuFile )

									# log('|	Create the cut file for this rom.')
									# with open(Output_Path + CUT_File_Name + '.cut', "wb") as outputfile:
										# if Emu_Name == "fba":
											# WriteFile = CUT_File_Layout % ( Emu_XBE,CUT_File_Name )
										# elif Emu_Name == "atarijaguar":
											# WriteFile = CUT_File_Layout % ( Emu_XBE,CUT_File_Name )
										# elif Emu_Name == "atarijaguarcd":
											# WriteFile = CUT_File_Layout % ( Emu_XBE,CUT_File_Name )
										# elif Emu_Name == "mame":
											# WriteFile = CUT_File_Layout % ( Emu_XBE,CUT_File_Name )
										# else:
											# WriteFile = CUT_File_Layout % ( Emu_XBE,Rom_Path )
										# outputfile.write( WriteFile )
								
								log('|	Add 1 to the Countlist.')
								CountList = CountList + 1

						xbmc.executebuiltin('Skin.SetString('+ Emu_Name +'_games,'+ str( CUTCount ) + ')')	
					else:
						log('|	No roms exist so do some cleanup.')
						#shutil.rmtree( Output_Path )# remove old cut files
						#if not os.path.isdir( Output_Path ): os.makedirs( Output_Path )
						
			log('|	Add the footer to the layout xml file.')
			with open( Rom_List_Path + Emu_Name + '.xml', "a") as outputmenufile:
				WriteMenuFile = menu_entry_footer
				outputmenufile.write( WriteMenuFile )
	
	log('|	Set a property so I can run the next script without this one running on.')			
	if ( Found_Roms == 1 ):
		xbmcgui.Window(xbmcgui.getCurrentWindowId()).setProperty("MyScript.ExternalRunning", "True")
		
		log('|	Running the scan script to update the counters.')
		xbmc.executebuiltin('RunScript(' + Scripts_Path + 'scanner.py,scan_emus,0,0,0)' )
		
		log('|	Loop.')
		while (xbmcgui.Window(xbmcgui.getCurrentWindowId()).getProperty("MyScript.ExternalRunning") == "True"):
			time.sleep(0.2)

	pDialog.close()
	return

				
CUT_File_Layout = '<shortcut><path>%s</path><custom><game>%s</game></custom></shortcut>'
		
menu_entry_header	= '<content>'
## had to add a space to the end of the label or XBMC will use the damn internal labels for games with numbers for names
menu_entry			= '\n\
	<item id="%s">\n\
		<label>%s</label>\n\
		<label2>%s</label2>\n\
		<onclick>%s</onclick>\n\
		<onclick>%s</onclick>\n\
		<icon>%s</icon>\n\
		<thumb>%s</thumb>\n\
	</item>'
menu_entry_footer	= '\n</content>'

logging = 0 # Setting this to 1 will spam the living hell out of your log file if you run the Auto mode, you have been warned

# Remove old content files folder if it exists
if os.path.isdir( xbmc.translatePath( "Special://skin/720p/content lists/" ) ): shutil.rmtree( xbmc.translatePath( "Special://skin/720p/content lists/" ) )

if Manual_Scan == "manual" : manual_scan()
if Full_Scan == "auto" : full_scan()

pDialog.update(0)
pDialog.close()
#dialog.ok( "","","Process Complete" )