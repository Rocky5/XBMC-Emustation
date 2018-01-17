'''
	Script by Rocky5
	Used to create static lists from your emulator and roms folder.
	
	Atarijaguar, must have there roms placed inside there root directory.
	( the script will generate static lists for emulators )
'''

import fileinput, glob, itertools, os, shutil, sys, time, xbmc, xbmcgui, zipfile

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
			Root_Directory        = os.path.dirname( Working_Directory ) + '\\'
			if str( xbmc.getCondVisibility( 'Skin.String(Custom_Emulator_Path)' ) ) == "1":
				Emulator_Path	= xbmc.getInfoLabel( 'Skin.String(Custom_Emulator_Path)' )
			else:
				Emulator_Path	= Root_Directory + '_emulators\\'
			if str( xbmc.getCondVisibility( 'Skin.String(Custom_Roms_Path)' ) ) == "1":
				Roms_Path		= xbmc.getInfoLabel( 'Skin.String(Custom_Roms_Path)' )
			else:
				Roms_Path		= Root_Directory + '_roms\\'
			if str( xbmc.getCondVisibility( 'Skin.String(Custom_Preview_Path)' ) ) == "1":
				Preview_Path	= xbmc.getInfoLabel( 'Skin.String(Custom_Preview_Path)' )
			else:
				Preview_Path	= Root_Directory + '_previews\\'
			if str( xbmc.getCondVisibility( 'Skin.String(Custom_TBNS_Path)' ) ) == "1":
				TBN_Path		= xbmc.getInfoLabel( 'Skin.String(Custom_TBNS_Path)' )
			else:
				TBN_Path		= Root_Directory + '_tbns\\'
				
			Synopsis_Path		= Root_Directory + '_synopsis\\'
			Scripts_Path		= Root_Directory + '_scripts\\XBMC-Emustation\\'
			Rom_List_Path		= Root_Directory + '_scripts\\XBMC-Emustation\\rom lists\\'
			Extensions			= [ "t64","d64","int","tap","z80","tzx","zip","bin","ccd","cue","j64","img","iso","rom","n64","z64","smd","smc","gb","gbc","gba","nes","sms","swc","gg","a26","a78","col","lnx","sfc","sg","fig","vms","exe" ]

def log( input ):
	if logging: print "%s" % str( input )
	
def Main_Code():
	log('|--------------------------------------------------------------------------------')
	log('|	Set the dialog create & found roms var.')	
	log('|--------------------------------------------------------------------------------')
	CreateDialog = 1 # Its outside the loop so it doesn't reset the dialog every time
	Found_Roms = 0
	log('|--------------------------------------------------------------------------------')
	log('|	Check if _emulators directory is selected instead of the emulator its self.')	
	log('|--------------------------------------------------------------------------------')
	if os.path.isdir( Emulator_Path ):	
		log('|--------------------------------------------------------------------------------')
		log('|	Parse all folder in the Emulators_Path')	
		log('|--------------------------------------------------------------------------------')
		for Emu_Path in sorted( os.listdir( Emulator_Path ) ):
			log('|--------------------------------------------------------------------------------')
			log('|	Set a load of variable.')
			log('|--------------------------------------------------------------------------------')
			CountList = 0
			JumpList = 0
			Jump_Counter = 8000
			Starts_with_0 = 0; Starts_with_A = 0; Starts_with_B = 0; Starts_with_C = 0; Starts_with_D = 0; Starts_with_E = 0; Starts_with_F = 0; Starts_with_G = 0; Starts_with_H = 0; Starts_with_I = 0; Starts_with_J = 0; Starts_with_K = 0; Starts_with_L = 0; Starts_with_M = 0; Starts_with_N = 0; Starts_with_O = 0; Starts_with_P = 0; Starts_with_Q = 0; Starts_with_R = 0; Starts_with_S = 0; Starts_with_T = 0; Starts_with_U = 0; Starts_with_V = 0; Starts_with_W = 0; Starts_with_X = 0; Starts_with_Y = 0; Starts_with_Z = 0;
			RomListCount = 0
			RenameCount = 0
			ZipCount = 0
			Parse_CUE_CCD_ISO_File = 0
			Parse_ISO_BIN_IMG_File = 0
			Parse_CUE_File = 0
			Parse_CCD_File = 0
			Parse_ISO_File = 0
			Parse_FBL_TXT = 0
			Parse_N64_TXT = 0
			N64ID = "0"
			Change_FBL_Rom_Path = 0
			Change_Mame_Rom_Path = 0
			Write_List_File = 1
			if ManualScan:
				Select_Emu_Folder = dialog.select( "Select a Emulator folder",sorted( os.listdir( Emulator_Path ) ) )
				if Select_Emu_Folder == -1:	return	
				log('|--------------------------------------------------------------------------------')
				log('|	Set Emulators and Roms folder paths.')
				log('|--------------------------------------------------------------------------------')
				Emu_Path = os.path.join( Emulator_Path, sorted( os.listdir( Emulator_Path ) )[Select_Emu_Folder] )
				Roms_Folder = os.path.join( Roms_Path, sorted( os.listdir( Emulator_Path ) )[Select_Emu_Folder] )
				Emu_Name = os.path.split(Emu_Path)[1]
				log('|--------------------------------------------------------------------------------')
				log('|	Convert Q:\\ to a direct path')
				log('|--------------------------------------------------------------------------------')
				if Emu_Path.startswith("Q:\\"): Emu_Path = Emu_Path.replace( "Q:\\", Root_Directory )
				log('|--------------------------------------------------------------------------------')
				log('|	Check for a default .xbe in the emulator path you selected.')
				log('|--------------------------------------------------------------------------------')
				if os.path.isfile( os.path.join( Emu_Path, "default.xbe" ) ):
					Emu_XBE = os.path.join( Emu_Path, "default.xbe" )
				else:
					dialog.ok("Error","No default.xbe found in this directory")
					return Main_Code()
			else:
				log('|--------------------------------------------------------------------------------')
				log('|	Set emu_path/name variable for autoscan mode.')
				log('|--------------------------------------------------------------------------------')
				Emu_Path = os.path.join( Emulator_Path, Emu_Path )
				Emu_Name = os.path.split(Emu_Path)[1]
				Roms_Folder	= os.path.join( Roms_Path,Emu_Name )
			log('|--------------------------------------------------------------------------------')
			log('|	If genesis emulator is selected or found use megadrive synopsis files.')
			log('|--------------------------------------------------------------------------------')
			if Emu_Name == "genesis":
				Synopsis_Zip = os.path.join( os.path.join( Synopsis_Path, 'megadrive' ) ) + '.zip'
			elif Emu_Name == "famicom":
				Synopsis_Zip = os.path.join( os.path.join( Synopsis_Path, 'nes' ) ) + '.zip'
			elif Emu_Name == "tg16":
				Synopsis_Zip = os.path.join( os.path.join( Synopsis_Path, 'pcengine' ) ) + '.zip'
			elif Emu_Name == "tg-cd":
				Synopsis_Zip = os.path.join( os.path.join( Synopsis_Path, 'pce-cd' ) ) + '.zip'
			else:
				Synopsis_Zip = os.path.join( os.path.join( Synopsis_Path, Emu_Name ) ) + '.zip'
			log('|--------------------------------------------------------------------------------')
			log('|	Check for previous layout xml and if it exists remove it.')
			log('|--------------------------------------------------------------------------------')
			if os.path.isfile( Rom_List_Path + Emu_Name + '.xml' ): os.remove( Rom_List_Path + Emu_Name + '.xml' )
			if os.path.isfile( Rom_List_Path + Emu_Name + '_favs.xml' ): os.remove( Rom_List_Path + Emu_Name + '_favs.xml' )
			if os.path.isfile( Rom_List_Path + Emu_Name + '_jump.xml' ): os.remove( Rom_List_Path + Emu_Name + '_jump.xml' )
			if not os.path.isdir( Rom_List_Path ): os.makedirs( Rom_List_Path )
			log('|--------------------------------------------------------------------------------')
			log('|	Write new layout xml header.')
			log('|--------------------------------------------------------------------------------')
			with open( Rom_List_Path + Emu_Name + '.xml', "wb") as outputmenufile:
				WriteMenuFile = menu_entry_header
				outputmenufile.write( WriteMenuFile )
			log('|--------------------------------------------------------------------------------')
			log('|	Check to make sure the xbe files exists.')
			log('|--------------------------------------------------------------------------------')
			if os.path.isfile( os.path.join( Emu_Path, "default.xbe" ) ):
				Emu_XBE = os.path.join( Emu_Path, "default.xbe" )
				log('|--------------------------------------------------------------------------------')
				log('|	Check to see if the if the emulator is one of the below so I can change it rom type or path.')
				log('|--------------------------------------------------------------------------------')
				if Emu_Name == "fba":
					Change_FBL_Rom_Path = 1
					Parse_FBL_TXT = 1
				elif Emu_Name == "atarijaguar":
					Roms_Folder	= os.path.join( Emulator_Path + 'atarijaguar\\roms' )
				elif Emu_Name == "atarijaguarcd":
					Roms_Folder	= os.path.join( Emulator_Path + 'atarijaguarcd\\roms' )
				elif Emu_Name == "mame":
					Change_Mame_Rom_Path = 1
				elif Emu_Name == "n64":
					Parse_N64_TXT = 1
				elif Emu_Name == "neogeocd":
					Parse_CUE_File = 1
				elif Emu_Name == "pce-cd":
					Parse_CUE_File = 1
				elif Emu_Name == "tg-cd":
					Parse_CUE_File = 1
				elif Emu_Name == "saturn":
					Parse_CUE_CCD_ISO_File = 1
				elif Emu_Name == "segacd":
					Parse_CUE_File = 1
				elif Emu_Name == "psx":
					Parse_CUE_CCD_ISO_File = 1
				else:
					pass
				if Emu_Name == "neogeocd" or Emu_Name == "pce-cd" or Emu_Name == "psx" or Emu_Name == "tg-cd" or Emu_Name == "segacd":
					Rom_Type_Total = (len(glob.glob1(Roms_Folder,'*.cue')) + len(glob.glob1(Roms_Folder,'*.ccd')) + len(glob.glob1(Roms_Folder,'*.img')) + len(glob.glob1(Roms_Folder,'*.iso')))
				log('|--------------------------------------------------------------------------------')
				log('|	Convert Q:\\ to a direct path')
				log('|--------------------------------------------------------------------------------')
				if Roms_Folder.startswith("Q:\\"): Roms_Folder = Roms_Folder.replace( "Q:\\", Root_Directory )
				log('|--------------------------------------------------------------------------------')
				log('|	Check to see if the emulators = rom folder is empty and exit if it is.')
				log('|--------------------------------------------------------------------------------')
				if len(os.listdir( Roms_Folder )) > 0:
					log('|--------------------------------------------------------------------------------')
					log('|	Check to see if vars are the value I need and create a new dialog.')
					log('|--------------------------------------------------------------------------------')
					if CreateDialog == 1:
						CreateDialog = 0
						if ManualScan:
							pDialog.create( "Manual Scan Mode","Initializing" )
						else:
							pDialog.create( "Auto Scan Mode","Initializing" )
					log('|--------------------------------------------------------------------------------')
					log('|	Checking filenames case and not leading with capital renaming it to do so.')
					log('|--------------------------------------------------------------------------------')
					for Roms in sorted( os.listdir( Roms_Folder ) ):
						Items_Full_Path = os.path.join( Roms_Folder, Roms )
						if Items_Full_Path != os.path.join( Roms_Folder, Roms.lower() ):
							tempname = Items_Full_Path[:-1]
							if not os.path.isfile( tempname ):
								os.rename( Items_Full_Path,  tempname )
								os.rename( tempname,  os.path.join( Roms_Folder, Roms.lower() ) )
								pDialog.update((RenameCount * 100) / len( os.listdir( Roms_Folder ) ),"Lower-casing rom names.","[B]" + Roms + "[/B]" ,"This can take some time, please be patient." )
								RenameCount = RenameCount + 1
					log('|--------------------------------------------------------------------------------')
					log('|	Setting a var again :/')
					log('|--------------------------------------------------------------------------------')
					Found_Roms = 1
					log('|--------------------------------------------------------------------------------')
					log('|	Check if fbl was found and change its rom path to where the roms are located.')
					log('|--------------------------------------------------------------------------------')
					if Change_FBL_Rom_Path == 1:
						if os.path.isfile(os.path.join( Emu_Path, 'Path.ini')):
							for line in fileinput.input(os.path.join( Emu_Path, 'Path.ini'), inplace=1):
								if 'ROMPath1=' in line:
									line = line = 'ROMPath1=' + Roms_Folder + '\n'
								print line,
							Change_FBL_Rom_Path = 0
						else:
							with open(os.path.join( Emu_Path, 'Path.ini'), "w") as outputfblfile:
								WriteFblFile = fbl_config % ( Roms_Folder )
								outputfblfile.write( WriteFBlFile )
							Change_FBL_Rom_Path = 0
					log('|--------------------------------------------------------------------------------')
					log('|	Check if mame was found and change it rom path to where the roms are located.')
					log('|--------------------------------------------------------------------------------')
					if Change_Mame_Rom_Path == 1:
						if not os.path.isdir(os.path.join( Emu_Path, "system")):
							os.makedirs( os.path.join( Emu_Path, "system") )
							if os.path.isfile(os.path.join( Emu_Path, "general\\DRIVERS.list" )): shutil.copy2(os.path.join( Emu_Path, "general\\DRIVERS.list" ), os.path.join( Emu_Path, "system") )
						if os.path.isfile(os.path.join( Emu_Path, "system\\MAMEoX.ini")):
							for line in fileinput.input(os.path.join( Emu_Path, "system\\MAMEoX.ini"), inplace=1):
								if 'RomsPath0 = ' in line:
									line = line = 'RomsPath0 = ' + Roms_Folder + '\n'
								print line,
							Change_Mame_Rom_Path = 0
						else:
							with open( os.path.join( Emu_Path, "system\\MAMEoX.ini"), "w") as outputmamefile:
								WriteMameFile = mame_config % ( Roms_Folder )
								outputmamefile.write( WriteMameFile )
							Change_Mame_Rom_Path = 0
					if Parse_FBL_TXT == 1:
						if os.path.isfile( os.path.join( Emulator_Path, "fba\\info\\" ) + "FBL Rom Names.zip" ):
							if os.path.isfile( os.path.join( Emulator_Path, "fba\\info\\rom names\\3countb.txt" ) ):
								pDialog.update( 0,"Found old FBA name files","Removing them before extracting the new ones.","This can take some time, please be patient." )
								shutil.rmtree( os.path.join( Emulator_Path, "fba\\info\\rom names" ) )
							log('|--------------------------------------------------------------------------------')
							log('|	Extracting the rom name files from the zip.')
							log('|--------------------------------------------------------------------------------')
							with zipfile.ZipFile( os.path.join( Emulator_Path, "fba\\info\\" ) + "FBL Rom Names.zip" ) as zip:
								if not os.path.isdir( os.path.join( Emulator_Path, "fba\\info\\rom names" ) ): os.makedirs( os.path.join( Emulator_Path, "fba\\info\\rom names" ) )
								if ZipCount == 0:
									#pDialog.create( "Extracting Zip","","Please wait..." )
									Total_TXT_Files = len( zip.namelist() ) or 1
									Devide = 100.0 / Total_TXT_Files
									Percent = 0
									for item in zip.namelist():
										Percent += Devide
										pDialog.update( int( Percent ),"Extracting final burn legends rom names","This only happens once per update","" )
										zip.extract( item, os.path.join( Emulator_Path, "fba\\info\\rom names\\" ) )
									ZipCount = 1
							os.remove( os.path.join( Emulator_Path, "fba\\info\\" ) + "FBL Rom Names.zip" )
						Roms_Folder = os.path.join( Emulator_Path, "fba\\info\\rom names" )
						# Used to name the rom name files so I can sort them by alphabetical order properly. ( this is only used by me ) 
						# for files in sorted( os.listdir( Roms_Folder ) ):
							# with open( os.path.join( Emulator_Path, "fba\\info\\rom names", files[:-3] + 'txt' ), 'r') as txt:
								# FBA_Rom_Name_Full = txt.readline()[:-2]
								# FBA_Rom_Name = FBA_Rom_Name_Full[:20]
								# FBA_Rom_Name = FBA_Rom_Name.replace( ',','' ); FBA_Rom_Name = FBA_Rom_Name.replace( ':','' ); FBA_Rom_Name = FBA_Rom_Name.replace( ';','' ); FBA_Rom_Name = FBA_Rom_Name.replace( '/','' ); FBA_Rom_Name = FBA_Rom_Name.replace( '?','' ); FBA_Rom_Name = FBA_Rom_Name.replace( '+','' ); FBA_Rom_Name = FBA_Rom_Name.replace( '*','' ); FBA_Rom_Name = FBA_Rom_Name.replace( 'amp','' ); FBA_Rom_Name = FBA_Rom_Name.replace( ' ','' );
								# FBA_Rom_Name = FBA_Rom_Name.lower()
							# if not os.path.isdir( "F:\\rom names" ): os.makedirs( "F:\\rom names" )
							# with open( os.path.join( "F:\\rom names", FBA_Rom_Name + '--' + files[:-3] + 'zip' ), 'w') as txt:
								# txt.write( FBA_Rom_Name_Full.lower() )
						# return
					log('|--------------------------------------------------------------------------------')
					log('|	Listing the content of the roms folder for parsing.')
					log('|--------------------------------------------------------------------------------')
					for Items in sorted( os.listdir( Roms_Folder ) ):
						log('|--------------------------------------------------------------------------------')
						log('|	Checking the file I find, extension agains my table.')
						log('|--------------------------------------------------------------------------------')
						if Items.endswith(tuple(Extensions)):
							log('|--------------------------------------------------------------------------------')
							log('|	More vars being set.')
							log('|--------------------------------------------------------------------------------')
							Rom_Name = Items
							Rom_Name_noext = Rom_Name[:-4]
							JumpList_Name = Rom_Name_noext.lower()
							TBN_File = os.path.join( TBN_Path, Emu_Name, Rom_Name_noext + '.png' )
							log('|--------------------------------------------------------------------------------')
							log('|	Check if fba was found and parse the name text files to get the correct rom names for the list.')
							log('|--------------------------------------------------------------------------------')
							if Parse_FBL_TXT == 1:
								Rom_Name_Full = Rom_Name
								Rom_Name_Beg = Rom_Name.split('--', 1)[0]
								Rom_Name = Rom_Name.split('--', 1)[1]
								Rom_Name_noext = Rom_Name[:-4]
								TBN_File = os.path.join( TBN_Path, Emu_Name, Rom_Name_noext + '.png' )
								if os.path.isfile( os.path.join( Roms_Path, "fba", Rom_Name ) ) and os.path.isfile( os.path.join( Emulator_Path, "fba\\info\\rom names", Rom_Name_Beg + '--' + Rom_Name ) ):
									with open( os.path.join( Emulator_Path, "fba\\info\\rom names", Rom_Name_Beg + '--' + Rom_Name ), 'r') as txt:
										FBA_Rom_Name = txt.readline()
										JumpList_Name = Rom_Name_Full.lower()
										Write_List_File = 1
								elif Rom_Name == "isgsm.zip":
										Write_List_File = 0
								elif Rom_Name == "neogeo.zip":
									Write_List_File = 0
								elif Rom_Name == "nmk004.zip":
									Write_List_File = 0
								elif Rom_Name == "pgm.zip":
									Write_List_File = 0
								else:
									Write_List_File = 0
							log('|--------------------------------------------------------------------------------')
							log('|	Check if n64 was found and parse the names from surreal.ini if the roms match.')
							log('|--------------------------------------------------------------------------------')
							if Parse_N64_TXT == 1:
								if os.path.isfile( os.path.join( Emulator_Path, "n64\\Surreal.ini" ) ):
									log('|--------------------------------------------------------------------------------')
									log('|	Extracting the rom names from the ini.')
									log('|--------------------------------------------------------------------------------')
									with open( os.path.join( Emulator_Path, "n64\\Surreal.ini" ), 'r') as ini:
										for line in itertools.islice(ini, 20, None):
											N64ID = str(line.lower())[1:-7]
											N64ID1 = N64ID.split('-', 1)[0]
											N64ID2 = N64ID.split('-', 1)[1]
											File_Name = ini.next().replace('Game Name=','')[:-1]
											File_Name = File_Name.lower()
											if Rom_Name_noext == File_Name:
												N64_Rom_Name = ini.next().replace('Alternate Title=','')[:-1]
												N64_Rom_Name = N64_Rom_Name.split('(', 1)[0]
												try:
													ini.next() # skip the comment line
													ini.next() # skip the blank line
												except: pass
												for N64_Thumb in os.listdir( os.path.join( Emulator_Path, 'n64\\media\\Cbagys3DArt' ) ):
													N64_Thumb = N64_Thumb.lower()
													if N64ID1 in N64_Thumb or N64ID2 in N64_Thumb:
														if not os.path.isdir( os.path.join( TBN_Path, Emu_Name ) ): os.makedirs( os.path.join( TBN_Path, Emu_Name ) )
														if not os.path.isdir( os.path.join( Synopsis_Path, Emu_Name ) ): os.makedirs( os.path.join( Synopsis_Path, Emu_Name ) )
														N64_Thumb_Location = os.path.join( Emulator_Path, 'n64\\media\\Cbagys3DArt', N64_Thumb )
														N64_Thumb_Destination = os.path.join( TBN_Path, Emu_Name, File_Name + '.png' )
														if os.path.isfile( N64_Thumb_Location ): shutil.copy2( N64_Thumb_Location, N64_Thumb_Destination )
												for N64_Synopsis in os.listdir( os.path.join( Emulator_Path, 'n64\\media\\synopsis' ) ):
													N64_Synopsis = N64_Synopsis.lower()
													if N64ID1 in N64_Synopsis or N64ID2 in N64_Synopsis:
															N64_Synopsis_Location = os.path.join( Emulator_Path, 'n64\\media\\synopsis', N64_Synopsis[:-3] + 'txt' )
															N64_Synopsis_Destination = os.path.join( Synopsis_Path, Emu_Name, File_Name + '.txt' )
															if os.path.isfile( N64_Synopsis_Location ): shutil.copy2( N64_Synopsis_Location, N64_Synopsis_Destination )
											else:
												try:
													ini.next() # skip the rom name
													ini.next() # skip the comment line
													ini.next() # skip the blank line
												except: pass
							else:
								pass
							log('|--------------------------------------------------------------------------------')
							log('|	Check for a synopsis zip for the current emulator.')
							log('|--------------------------------------------------------------------------------')
							if ZipCount == 0:
								if os.path.isfile( Synopsis_Zip ):
										log('|--------------------------------------------------------------------------------')
										log('|	Extracting the synopsis files from the zip.')
										log('|--------------------------------------------------------------------------------')
										with zipfile.ZipFile( Synopsis_Zip ) as zip:
											if ZipCount == 0:
												#pDialog.create( "Extracting Zip","","Please wait..." )
												Total_TXT_Files = len( zip.namelist() ) or 1
												Devide = 100.0 / Total_TXT_Files
												Percent = 0
												for item in zip.namelist():
													Percent += Devide
													pDialog.update( int( Percent ),"Extracting [B][UPPERCASE]" + Emu_Name + "[/UPPERCASE][/B] Synopsis files.",item,"" )
													zip.extract( item, Synopsis_Path )
												ZipCount = 1
										os.remove( os.path.join( Synopsis_Zip ) )
							else:
								pass
							log('|--------------------------------------------------------------------------------')
							log('|	Check for a synopsis file for the current emulator and parse it.')
							log('|--------------------------------------------------------------------------------')
							try:
								if Emu_Name == "genesis":
									Synopsis_File = os.path.join( Synopsis_Path, "megadrive", Rom_Name_noext + '.txt' )
								elif Emu_Name == "famicom":
									Synopsis_File = os.path.join( Synopsis_Path, "nes", Rom_Name_noext + '.txt' )
								elif Emu_Name == "tg16":
									Synopsis_File = os.path.join( Synopsis_Path, "pcengine", Rom_Name_noext + '.txt' )
								elif Emu_Name == "tg-cd":
									Synopsis_File = os.path.join( Synopsis_Path, "pce-cd", Rom_Name_noext + '.txt' )
								elif Emu_Name == "fba":
									Synopsis_File = os.path.join( Emulator_Path, "fba\\info\\emulation", Rom_Name_noext + '.ini' )
								else:
									Synopsis_File = os.path.join( Synopsis_Path, Emu_Name, Rom_Name_noext + '.txt' )
								with open( Synopsis_File ) as input:
									Synopsis = input.read()
									if Emu_Name == "fba":
										Synopsis1 = Synopsis.split('- TECHNICAL -', 1)[0]
										Synopsis1 = Synopsis1.strip('\n')
										Synopsis1 = Synopsis1.replace( '&', '&amp;' )
										Synopsis1 = Synopsis1.replace( '>', '&gt;' )
										Synopsis1 = Synopsis1.replace( '<', '&lt;' )
									else:
										Synopsis1 = Synopsis.split('_________________________', 1)[0]
										Synopsis1 = Synopsis1.split('\n')
										Synopsis_rating = ""; Synopsis_players = ""; Synopsis_genre = ""; Synopsis_developer = ""; Synopsis_publisher = ""; Synopsis_release_year = ""
										Synopsis_rating_Set = 0; Synopsis_players_Set = 0; Synopsis_genre_Set = 0; Synopsis_developer_Set = 0; Synopsis_publisher_Set = 0; Synopsis_release_year_Set = 0
										for _ in range(5):
											for line in Synopsis1:
												line = line.lower()
												# if 'rating:' in line:
													# Synopsis_rating = line.split(':',1)[1]
													# Synopsis_rating = '[B]Rating:[/B]\n ' + Synopsis_rating
													# Synopsis_rating_Set = 1
												# elif Synopsis_rating_Set == 0:
													# Synopsis_rating = '[B]Rating:[/B]\n None'
												if 'players:' in line:
													Synopsis_players = line.split(':',1)[1]
													Synopsis_players = '[B]Players:[/B]\n ' + Synopsis_players
													Synopsis_players_Set = 1
												elif Synopsis_players_Set == 0:
													Synopsis_players = '[B]Players:[/B]\n None'
												if 'genre:' in line:
													Synopsis_genre = line.split(':',1)[1]
													Synopsis_genre = '[B]Genre:[/B]\n ' + Synopsis_genre
													Synopsis_genre_Set = 1
												elif Synopsis_genre_Set == 0:
													Synopsis_genre = '[B]Genre:[/B]\n None'
												if 'developer:' in line:
													Synopsis_developer = line.split(':',1)[1]
													Synopsis_developer = '[B]Developer:[/B]\n ' + Synopsis_developer
													Synopsis_developer_Set = 1
												elif Synopsis_developer_Set == 0:
													Synopsis_developer = '[B]Developer:[/B]\n None'
												if 'publisher:' in line:
													Synopsis_publisher = line.split(':',1)[1]
													Synopsis_publisher = '[B]Publisher:[/B]\n ' + Synopsis_publisher
													Synopsis_publisher_Set = 1
												elif Synopsis_publisher_Set == 0:
													Synopsis_publisher = '[B]Publisher:[/B]\n None'
												if 'release year:' in line:
													Synopsis_release_year = line.split(':',1)[1]
													Synopsis_release_year = '[B]Released:[/B]\n ' + Synopsis_release_year
													Synopsis_release_year_Set = 1
												elif Synopsis_release_year_Set == 0:
													Synopsis_release_year = '[B]Released:[/B]\n None'
										# Synopsis1 = Synopsis_rating + '\n' + Synopsis_players + '\n' + Synopsis_genre + '\n' + Synopsis_developer + '\n' + Synopsis_publisher + '\n' + Synopsis_release_year
										Synopsis1 = Synopsis_players + '\n' + Synopsis_genre + '\n' + Synopsis_developer + '\n' + Synopsis_publisher + '\n' + Synopsis_release_year
										Synopsis2 = Synopsis.split('_________________________', 1)[1]
										Synopsis2 = Synopsis2.strip('\n')
										Synopsis2 = Synopsis2.replace( '&', '&amp;' )
										Synopsis2 = Synopsis2.replace( '>', '&gt;' )
										Synopsis2 = Synopsis2.replace( '<', '&lt;' )
							except:
								Synopsis1 = "No Synopsis"
								Synopsis2 = ""
							log('|--------------------------------------------------------------------------------')
							log('|	Fix labels that use only numbers, XBMC will use its internal labeling system if I dont.')
							log('|--------------------------------------------------------------------------------')
							if Rom_Name_noext == "1942": Rom_Name_noext = "1942 "
							if Rom_Name_noext == "1942": Rom_Name_noext = "1942 "
							if Rom_Name_noext == "1943": Rom_Name_noext = "1943 "
							if Rom_Name_noext == "720": Rom_Name_noext = "720 "
							log('|--------------------------------------------------------------------------------')
							log('|	Set Rom_Names for different types of CD images.')
							log('|--------------------------------------------------------------------------------')
							Rom_Name_ISO = os.path.join( Roms_Folder, Rom_Name[:-4] + ".iso" )
							Rom_Name_BIN = os.path.join( Roms_Folder, Rom_Name[:-4] + ".bin" )
							Rom_Name_IMG = os.path.join( Roms_Folder, Rom_Name[:-4] + ".img" )
							Rom_Name_CUE = os.path.join( Roms_Folder, Rom_Name[:-4] + ".cue" )
							Rom_Name_CCD = os.path.join( Roms_Folder, Rom_Name[:-4] + ".ccd" )
							Rom_Path = os.path.join( Roms_Folder, Rom_Name )
							log('|--------------------------------------------------------------------------------')
							log('|	Check and parse the directory for iso files.')
							log('|--------------------------------------------------------------------------------')
							if Parse_ISO_File == 1:
								if Items.endswith( '.iso' ):
									Rom_Path = Rom_Name_ISO
									Rom_Type_Total = Rom_Type_Total
									Write_List_File = 1
								else:
									Write_List_File = 0	
							log('|--------------------------------------------------------------------------------')
							log('|	Check and parse the directory for cue files.')
							log('|--------------------------------------------------------------------------------')
							if Parse_CUE_File == 1:
								if Items.endswith( '.cue' ):
									Rom_Path = Rom_Name_CUE
									Rom_Type_Total = Rom_Type_Total
									Write_List_File = 1
								else:
									Write_List_File = 0
							log('|--------------------------------------------------------------------------------')
							log('|	Check and parse the directory for bin/iso/img files.')
							log('|--------------------------------------------------------------------------------')
							if Parse_ISO_BIN_IMG_File == 1:
								if Items.endswith( '.bin' ):
									Rom_Path = Rom_Name_BIN
									Rom_Type_Total = Rom_Type_Total
									Write_List_File = 1
								elif Items.endswith( '.img' ):
									Rom_Path = Rom_Name_IMG
									Rom_Type_Total = Rom_Type_Total
									Write_List_File = 1
								elif Items.endswith( '.iso' ):
									Rom_Path = Rom_Name_ISO
									Rom_Type_Total = Rom_Type_Total
									Write_List_File = 1
								else:
									Write_List_File = 0
							log('|--------------------------------------------------------------------------------')
							log('|	Check and parse the directory for cue/ccd/iso files.')
							log('|--------------------------------------------------------------------------------')
							if Parse_CUE_CCD_ISO_File == 1:
								if Items.endswith( '.cue' ):
									Rom_Path = Rom_Name_CUE
									Rom_Type_Total = Rom_Type_Total
									Write_List_File = 1
								elif Items.endswith( '.ccd' ):
									Rom_Path = Rom_Name_CCD
									Rom_Type_Total = Rom_Type_Total
									Write_List_File = 1
								elif Items.endswith( '.iso' ):
									Rom_Path = Rom_Name_ISO
									Rom_Type_Total = Rom_Type_Total
									Write_List_File = 1
								else:
									Write_List_File = 0
							log('|--------------------------------------------------------------------------------')
							log('|	Check to see if _tbns folder exists and if it doesnt create it.')
							log('|--------------------------------------------------------------------------------')
							if not os.path.isdir( os.path.join( TBN_Path, Emu_Name ) ): os.makedirs( os.path.join( TBN_Path, Emu_Name ) )
							if not os.path.isdir( os.path.join( Preview_Path, Emu_Name ) ): os.makedirs( os.path.join( Preview_Path, Emu_Name ) )
							log('|--------------------------------------------------------------------------------')
							log('|	Create the rest of the layout xml file.')
							log('|--------------------------------------------------------------------------------')
							if Write_List_File:
								log('|--------------------------------------------------------------------------------')
								log('|	Show the progress bar progress and write rom list file.')
								log('|--------------------------------------------------------------------------------')
								RomListCount = RomListCount + 1
								with open( Rom_List_Path + Emu_Name + '.xml', "a") as outputmenufile:
									if Emu_Name == "fba":
										pDialog.update((CountList * 100) / len(os.listdir( os.path.join( Roms_Path, "fba" ) ) ),"Creating [B][UPPERCASE]" + Emu_Name + "[/UPPERCASE][/B] Rom list",FBA_Rom_Name,"This can take some time, please be patient." )
										WriteMenuFile = menu_entry % (CountList,FBA_Rom_Name,Synopsis1,'RunScript( Special://xbmc/_scripts/XBMC-Emustation/launcher.py,' + Emu_XBE + ',' + Rom_Name_noext + ',,' + str(CountList) + ' )',"ActivateWindow(1101)",Rom_Name_noext + " ",TBN_File)
									elif Emu_Name == "mame":
										pass
									elif Emu_Name == "n64":
										pDialog.update((CountList * 100) / len(os.listdir( Roms_Folder )),"Creating [B][UPPERCASE]" + Emu_Name + "[/UPPERCASE][/B] Rom list",N64_Rom_Name,"This can take some time, please be patient." )
										WriteMenuFile = menu_entry % (CountList,N64_Rom_Name,Synopsis1,'RunScript( Special://xbmc/_scripts/XBMC-Emustation/launcher.py,' + Emu_XBE + ',' + Rom_Path + ',,' + str(CountList) + ' )',"ActivateWindow(1101)",Synopsis2,TBN_File)
									elif Emu_Name == "neogeocd" or Emu_Name == "pce-cd" or Emu_Name == "psx" or Emu_Name == "tg-cd" or Emu_Name == "segacd":
										pDialog.update((CountList * 100) / Rom_Type_Total,"Creating [B][UPPERCASE]" + Emu_Name + "[/UPPERCASE][/B] Rom list",Rom_Name_noext,"This can take some time, please be patient." )
										WriteMenuFile = menu_entry % (CountList,Rom_Name_noext,Synopsis1,'RunScript( Special://xbmc/_scripts/XBMC-Emustation/launcher.py,' + Emu_XBE + ',' + Rom_Path + ',,' + str(CountList) + ' )',"ActivateWindow(1101)",Synopsis2,TBN_File)
									else:
										pDialog.update((CountList * 100) / len(os.listdir( Roms_Folder )),"Creating [B][UPPERCASE]" + Emu_Name + "[/UPPERCASE][/B] Rom list",Rom_Name_noext,"This can take some time, please be patient." )
										WriteMenuFile = menu_entry % (CountList,Rom_Name_noext,Synopsis1,'RunScript( Special://xbmc/_scripts/XBMC-Emustation/launcher.py,' + Emu_XBE + ',' + Rom_Path + ',,' + str(CountList) + ' )',"ActivateWindow(1101)",Synopsis2,TBN_File)
									outputmenufile.write( WriteMenuFile )
								log('|--------------------------------------------------------------------------------')
								log('|	Write favourites menu entries.')
								log('|--------------------------------------------------------------------------------')
								with open( Rom_List_Path + Emu_Name + '_favs.xml', "a") as favsmenufile:
									if Emu_Name == "fba":
										WriteMenuFile = favourites_entry % (FBA_Rom_Name,Rom_Name_noext)
									elif Emu_Name == "mame":
										pass
									elif Emu_Name == "n64":
										WriteMenuFile = favourites_entry % (N64_Rom_Name,Rom_Path)
									else:
										WriteMenuFile = favourites_entry % (Rom_Name_noext,Rom_Path)
									favsmenufile.write( WriteMenuFile )
								log('|--------------------------------------------------------------------------------')
								log('|	Write menu entry for quick jump')
								log('|--------------------------------------------------------------------------------')
								with open( Rom_List_Path + Emu_Name + '_jump.xml', "a") as outputmenuselectfile:
									if not Starts_with_0:
										if JumpList_Name.startswith("#") or JumpList_Name.startswith("'") or JumpList_Name.startswith("0") or JumpList_Name.startswith("1") or JumpList_Name.startswith("2") or JumpList_Name.startswith("3") or JumpList_Name.startswith("4") or JumpList_Name.startswith("5") or JumpList_Name.startswith("6") or JumpList_Name.startswith("7") or JumpList_Name.startswith("8") or JumpList_Name.startswith("9"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"#","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_0 = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_A:
										if JumpList_Name.startswith("a"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"A","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_A = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_B:
										if JumpList_Name.startswith("b"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"B","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_B = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_C:
										if JumpList_Name.startswith("c"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"C","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_C = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_D:
										if JumpList_Name.startswith("d"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"D","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_D = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_E:
										if JumpList_Name.startswith("e"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"E","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_E = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_F:
										if JumpList_Name.startswith("f"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"F","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_F = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_G:
										if JumpList_Name.startswith("g"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"G","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_G = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_H:
										if JumpList_Name.startswith("h"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"H","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_H = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_I:
										if JumpList_Name.startswith("i"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"I","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_I = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_J:
										if JumpList_Name.startswith("j"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"J","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_J = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_K:
										if JumpList_Name.startswith("k"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"K","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_K = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_L:
										if JumpList_Name.startswith("l"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"L","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_L = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_M:
										if JumpList_Name.startswith("m"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"M","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_M = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_N:
										if JumpList_Name.startswith("n"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"N","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_N = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_O:
										if JumpList_Name.startswith("o"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"O","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_O = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_P:
										if JumpList_Name.startswith("p"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"P","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_P = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_Q:
										if JumpList_Name.startswith("q"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"Q","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_Q = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_R:
										if JumpList_Name.startswith("r"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"R","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_R = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_S:
										if JumpList_Name.startswith("s"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"S","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_S = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_T:
										if JumpList_Name.startswith("t"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"T","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_T = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_U:
										if JumpList_Name.startswith("u"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"U","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_U = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_V:
										if JumpList_Name.startswith("v"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"V","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_V = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_W:
										if JumpList_Name.startswith("w"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"W","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_W = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_X:
										if JumpList_Name.startswith("x"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"X","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_X = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_Y:
										if JumpList_Name.startswith("y"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"Y","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_Y = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
									if not Starts_with_Z:
										if JumpList_Name.startswith("z"):
											WriteSearchFile = search_menu_entry % ( str(Jump_Counter),"Z","SetFocus(9000," + str(JumpList) + ")" )
											Starts_with_Z = 1
											Jump_Counter = Jump_Counter + 1
											outputmenuselectfile.write( WriteSearchFile )
								log('|--------------------------------------------------------------------------------')
								log('|	Add 1 to the Countlist and JumpList.')
								log('|--------------------------------------------------------------------------------')
								CountList = CountList + 1
								JumpList = JumpList + 1
					log('|--------------------------------------------------------------------------------')
					log('|	Set the rom count and remove any direct launch rom list.xml files.')
					log('|--------------------------------------------------------------------------------')
					xbmc.executebuiltin('Skin.SetString('+ Emu_Name +'_games,'+ str( RomListCount ) + ')')	
					if Emu_Name == "atarijaguar.xml" or Emu_Name == "atarijaguarcd.xml":
						if os.path.isfile( os.path.join( Rom_List_Path, Emu_Name + '.xml' ) ): os.remove( os.path.join( Rom_List_Path, Emu_Name + '.xml' ) )
						if os.path.isfile( os.path.join( Rom_List_Path, Emu_Name + '_favs.xml' ) ): os.remove( os.path.join( Rom_List_Path, Emu_Name + '_favs.xml' ) )
						if os.path.isfile( os.path.join( Rom_List_Path, Emu_Name + '_jump.xml' ) ): os.remove( os.path.join( Rom_List_Path, Emu_Name + '_jump.xml' ) )
					if Emu_Name == "mame":
						if os.path.isfile( os.path.join( Emu_Path, "system\\ROMS.list" )): os.remove( os.path.join( Emu_Path, "system\\ROMS.list" ))
						if os.path.isfile( os.path.join( Emu_Path, "system\\ROMS.metadata" )): os.remove( os.path.join( Emu_Path, "system\\ROMS.metadata" ))
						if os.path.isfile( os.path.join( Rom_List_Path, Emu_Name + '.xml' ) ): os.remove( os.path.join( Rom_List_Path, Emu_Name + '.xml' ) )
						if os.path.isfile( os.path.join( Rom_List_Path, Emu_Name + '_favs.xml' ) ): os.remove( os.path.join( Rom_List_Path, Emu_Name + '_favs.xml' ) )
						if os.path.isfile( os.path.join( Rom_List_Path, Emu_Name + '_jump.xml' ) ): os.remove( os.path.join( Rom_List_Path, Emu_Name + '_jump.xml' ) )	
				log('|--------------------------------------------------------------------------------')
				log('|	Add the footer to the layout xml file.')
				log('|--------------------------------------------------------------------------------')
				with open( Rom_List_Path + Emu_Name + '.xml', "a") as outputmenufile:
					WriteMenuFile = menu_entry_footer
					outputmenufile.write( WriteMenuFile )
			else:
				if os.path.isfile( os.path.join( Rom_List_Path, Emu_Name + '.xml' ) ): os.remove( os.path.join( Rom_List_Path, Emu_Name + '.xml' ) )
			log('|--------------------------------------------------------------------------------')		
			log('|	ManualMode - Set a property so I can run the next script without this one running on.')			
			log('|--------------------------------------------------------------------------------')		
			if Found_Roms == 1 and ManualScan == 1:
				xbmcgui.Window(xbmcgui.getCurrentWindowId()).setProperty("MyScript.ExternalRunning", "True")
				log('|	Running the scan script to update the counters.')
				xbmc.executebuiltin('RunScript(' + Scripts_Path + 'scanner.py,0,' + Emu_Name + ',0,0)' )
				log('|	Loop.')
				while (xbmcgui.Window(xbmcgui.getCurrentWindowId()).getProperty("MyScript.ExternalRunning") == "True"):
					time.sleep(0.2)
				pDialog.close()
				return

	log('|--------------------------------------------------------------------------------')	
	log('|	AutoMode - Set a property so I can run the next script without this one running on.')			
	log('|--------------------------------------------------------------------------------')		
	if Found_Roms == 1 and ManualScan == 0:
		xbmcgui.Window(xbmcgui.getCurrentWindowId()).setProperty("MyScript.ExternalRunning", "True")
		log('|	Running the scan script to update the counters.')
		xbmc.executebuiltin('RunScript(' + Scripts_Path + 'scanner.py,scan_emus,0,0,0)' )
		log('|	Loop.')
		while (xbmcgui.Window(xbmcgui.getCurrentWindowId()).getProperty("MyScript.ExternalRunning") == "True"):
			time.sleep(0.2)
	else:
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
search_menu_entry	= '<control type="button" id="%s">\n\
	<label>[UPPERCASE]jump to letter[/UPPERCASE]</label>\n\
	<label2>&lt; [UPPERCASE]%s[/UPPERCASE] &gt;</label2>\n\
	<include>MenuButtonCommonValues</include>\n\
	<onclick>Dialog.Close(1120)</onclick>\n\
	<onclick>%s</onclick>\n\
</control>\n\
'
favourites_entry	= '<favourites>%s,%s</favourites>\n'

mame_config			= '[Directories]\nALTDrive = t\nC_Mapping = \\device\\harddisk0\\partition1\nE_Mapping = \\device\\harddisk0\\partition1\nF_Mapping = \\device\\harddisk0\\partition6\nG_Mapping = \\device\\cdrom0\nH_Mapping = \\device\\harddisk0\\partition6\nRomsPath0 = %s\nRomsPath1 = d:\\roms\nRomsPath2 = d:\\roms\nRomsPath3 = d:\\roms\nArtPath = d:\\artwork\nAudioPath = d:\\samples\nConfigPath = d:\\cfg\nGeneralPath = d:\\general\nHDImagePath = d:\\hdimages\nHiScoresPath = d:\\hiscores\nNVRamPath = d:\\nvram\nBackupPath = d:\\roms\\backup\nScreenshotPath = d:\\screenshots\nAutoBootSavePath = d:\\autobootsaves\n\n\n[General]\nbios = 0\nCheatsEnabled = 1\nCheatFilename = cheat.dat\nSkipDisclaimer = 1\nSkipGameInfo = 1\nSkipWarnings = 1\nScreenSaverTimeout = 10\n\n\n[Input]\nLightgun1_Left = 4294934529\nLightgun1_CenterX = 0\nLightgun1_Right = 32767\nLightgun1_Top = 32767\nLightgun1_CenterY = 0\nLightgun1_Bottom = 4294934529\nLightgun2_Left = 4294934529\nLightgun2_CenterX = 0\nLightgun2_Right = 32767\nLightgun2_Top = 32767\nLightgun2_CenterY = 0\nLightgun2_Bottom = 4294934529\nLightgun3_Left = 4294934529\nLightgun3_CenterX = 0\nLightgun3_Right = 32767\nLightgun3_Top = 32767\nLightgun3_CenterY = 0\nLightgun3_Bottom = 4294934529\nLightgun4_Left = 4294934529\nLightgun4_CenterX = 0\nLightgun4_Right = 32767\nLightgun4_Top = 32767\nLightgun4_CenterY = 0\nLightgun4_Bottom = 4294934529\n\n\n[Network]\nDisableNetworking = 0\nIPAddress = \nGateway = \nSubnet = \nNameServer = \n\n\n[ROMListOptions]\nDisplayMode = 1\nSortMode = 0\nShowROMStatus = 0\nShowFAVEStatus = 1\nHideFilteredROMs = 0\nFilterMode = 0\nCursorPosition = 0.000000\nPageOffset = 0.000000\nSuperscrollIndex = 0\n\n\n[SkinOptions]\nSelectedSkin = Original\n\n\n[Sound]\nSoundEnable = 1\nSampleRate = 44100\nUseSamples = 1\nUseFilter = 1\n\n\n[VMMOptions]\nForceVMM = 0\nThreshold = 4194304\nCommitSize = 1048576\nDistribute = 65535\n\n\n[VectorOptions]\nVectorWidth = 640\nVectorHeight = 480\nBeamWidth = 2\nFlickerEffect = 0.000000\nBeamIntensity = 1.500000\nTranslucency = 1\n\n\n[Video]\nVSYNC = 1\nThrottleFramerate = 1\nAspectRatioCorrection = 1\nMinificationFilter = 2\nMagnificationFilter = 2\nFrameskip = 4294967295\nGraphicsFilter = 0\nSoftDisplayFilter = 0\nFlickerFilter = 5\nScreenRotation = 0\nBrightness = 1.000000\nPauseBrightness = 0.650000\nGamma = 1.000000\nScreenUsage_X = 0.850000\nScreenUsage_Y = 0.850000\nScreenPos_X = 0.000000\nScreenPos_Y = 0.000000\nArtwork = 1\n\n\n'
fbl_config			= 'UsePathINI=1\nROMPath1=D:\\roms\nROMPath2=\nROMPath3=\nROMPath4=\nROMPath5=\nROMPath6=\nROMPath7=\nROMPath8=\nD:\\artwork\\Shots 1\nD:\\artwork\\Shots 2\nD:\\artwork\\Shots 3\nD:\\artwork\\Shots 4\nD:\\artwork\\Shots 5\nD:\\artwork\\Shots 6\nD:\\artwork\\Shots 7\nD:\\artwork\\Shots 8\nD:\\nvram\nD:\\samples\nD:\\ini\nD:\\savestates\nD:\\config\nD:\\hiscores\nD:\\videos\n'

logging = 0 # Setting this to 1 will spam the living hell out of your log file if you run the Auto mode, you have been warned

# Remove old content files folder if it exists
if os.path.isdir( xbmc.translatePath( "Special://skin/720p/content lists/" ) ): shutil.rmtree( xbmc.translatePath( "Special://skin/720p/content lists/" ) )

if Manual_Scan == "manual" :
	ManualScan = 1
	Main_Code()

if Full_Scan == "auto" :
	ManualScan = 0
	Main_Code()