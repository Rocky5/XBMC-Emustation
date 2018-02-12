'''
	Script by Rocky5
	Used to create static lists from your emulator and roms folder.
	
	Atarijaguar and neogeocd must have there roms placed inside there root directory.
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
print "| .emustation\Scripts\create_rom_lists.py loaded."

pDialog	= xbmcgui.DialogProgress()
dialog	= xbmcgui.Dialog()

#####	Sets paths.
# Gets current XBMC-Emustation directory.
CharCount = 100 # How many characters you want after 'The executable running is: '
with open( xbmc.translatePath( "special://xbmc/system/" ) + "xbmc.log", "r" ) as XBMCLOG:
	for line in XBMCLOG:
		left,found,right = line.partition("The executable running is: ")
		if found:
			Working_Directory	= ( right[:CharCount] )
			Root_Directory        = os.path.dirname( Working_Directory ) + '\\'
			if xbmc.getCondVisibility( 'Skin.String(Custom_Emulator_Path)' ):
				Emulator_Folder_Path = xbmc.getInfoLabel( 'Skin.String(Custom_Emulator_Path)' )
			else:
				Emulator_Folder_Path = Root_Directory + '.emustation\\emulators\\'
			if xbmc.getCondVisibility( 'Skin.String(Custom_Roms_Path)' ):
				Roms_Folder_Path	 = xbmc.getInfoLabel( 'Skin.String(Custom_Roms_Path)' )
			else:
				Roms_Folder_Path	 = Root_Directory + '.emustation\\roms\\'
			if xbmc.getCondVisibility( 'Skin.String(Custom_Media_Path)' ):
				Media_Folder_Path 	 = xbmc.getInfoLabel( 'Skin.String(Custom_Media_Path)' )
			else:
				Media_Folder_Path 	 = Root_Directory + '.emustation\\media\\'
			Synopsis_Path		= Root_Directory + '.emustation\\synopsis\\'
			Scripts_Path		= Root_Directory + '.emustation\\scripts\\'
			Extensions			= [ "nds","t64","d64","int","tap","z80","tzx","zip","bin","ccd","cue","j64","img","iso","rom","n64","z64","smd","smc","gb","gbc","gba","nes","sms","swc","gg","a26","a78","col","lnx","sfc","sg","fig","vms","exe" ]

def log( input ):
	if logging: print "%s" % str( input )
	
def Main_Code():
	#--------
	log('|	Set the dialog create & found roms var.')	
	#--------
	CreateDialog = 1 # Its outside the loop so it doesn't reset the dialog every time
	Found_Roms = 0
	#--------
	log('|	Check if _emulators directory is selected instead of the emulator its self.')	
	#--------
	if os.path.isdir( Emulator_Folder_Path ):
		#--------
		log('| '+ Emulator_Folder_Path +  '	Parse all folder in the Emulators_Path')	
		#--------
		for Emu_Path in sorted( os.listdir( Emulator_Folder_Path ) ):
			#--------
			log('|--------------------------------------------------------------------------------')	
			log('| '+ Emu_Path +  '	- Set a load of variable.')
			#--------
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
			FBA_Rom_Name = ""
			Change_FBL_Rom_Path = 0
			Change_Mame_Rom_Path = 0
			Change_N64_Rom_Path = 0
			Write_List_File = 1
			if ManualScan:
				Select_Emu_Folder = dialog.select( "SELECT A SYSTEM",sorted( os.listdir( Emulator_Folder_Path ) ) )
				if Select_Emu_Folder == -1:	return
				#--------
				log('| '+ Emu_Path +  '	- Set Emulators and Roms folder paths.')
				#--------
				Emu_Path = os.path.join( Emulator_Folder_Path, sorted( os.listdir( Emulator_Folder_Path ) )[Select_Emu_Folder] )
				Roms_Folder = os.path.join( Roms_Folder_Path, sorted( os.listdir( Emulator_Folder_Path ) )[Select_Emu_Folder] )
				Emu_Name = os.path.split(Emu_Path)[1]
				#--------
				log('| '+ Emu_Name +  '	- Convert Q:\\ to a direct path')
				#--------
				if Emu_Path.startswith("Q:\\"): Emu_Path = Emu_Path.replace( "Q:\\", Root_Directory )
				#--------
				log('| '+ Emu_Name +  '	- Check for a default .xbe in the emulator path you selected.')
				#--------
				if os.path.isfile( os.path.join( Emu_Path, "default.xbe" ) ):
					Emu_XBE = os.path.join( Emu_Path, "default.xbe" )
				else:
					dialog.ok("ERROR","","No default.xbe found in this directory")
					return Main_Code()
			else:
				#--------
				log('| '+ Emu_Path +  '	- Set emu_path/name variable for autoscan mode.')
				#--------
				Emu_Path = os.path.join( Emulator_Folder_Path, Emu_Path )
				Emu_Name = os.path.split(Emu_Path)[1]
				Roms_Folder	= os.path.join( Roms_Folder_Path,Emu_Name )
			#--------
			log('| '+ Emu_Name +  '	- Set tbn and gameslist path variable.')
			#--------
			Media_Path			= os.path.join( Media_Folder_Path, Emu_Name )
			Games_List_Path		= os.path.join( Root_Directory, '.emustation\\gamelists', Emu_Name )
			#--------
			log('| '+ Emu_Name +  '	- If genesis emulator is selected or found use megadrive synopsis files.')
			#--------
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
			#--------
			log('| '+ Emu_Name +  '	- Check for previous layout xml and if it exists remove it.')
			#--------
			if os.path.isdir( Games_List_Path ): shutil.rmtree( Games_List_Path )
			if not os.path.isdir( Games_List_Path ): os.makedirs( Games_List_Path )
			if not os.path.isdir( os.path.join( Media_Path,'boxart' ) ): os.makedirs( os.path.join( Media_Path,'boxart' ) )
			if not os.path.isdir( os.path.join( Media_Path,'boxart3d' ) ): os.makedirs( os.path.join( Media_Path,'boxart3d' ) )
			if not os.path.isdir( os.path.join( Media_Path,'logo' ) ): os.makedirs( os.path.join( Media_Path,'logo' ) )
			if not os.path.isdir( os.path.join( Media_Path,'mix' ) ): os.makedirs( os.path.join( Media_Path,'mix' ) )
			if not os.path.isdir( os.path.join( Media_Path,'videos' ) ): os.makedirs( os.path.join( Media_Path,'videos' ) )
			if not os.path.isdir( os.path.join( Media_Path,'screenshots' ) ): os.makedirs( os.path.join( Media_Path,'screenshots' ) )
			#--------
			log('| '+ Emu_Name +  '	- Check to make sure the xbe files exists.')
			#--------
			Emu_XBE = os.path.join( Emu_Path, "default.xbe" )
			if os.path.isfile( Emu_XBE ):
				#--------
				log('| '+ Emu_Name +  '	- Check to see if the emulator is one of the below so I can change it rom type or path.')
				#--------
				if Emu_Name == "fba":
					Change_FBL_Rom_Path = 1
					Parse_FBL_TXT = 1
				elif Emu_Name == "atarijaguar":
					Roms_Folder	= os.path.join( Emulator_Folder_Path, 'atarijaguar\\roms' )
				elif Emu_Name == "mame":
					Change_Mame_Rom_Path = 1
				elif Emu_Name == "n64":
					Parse_N64_TXT = 1
					Change_N64_Rom_Path = 1
				elif Emu_Name == "neogeocd":
					Roms_Folder	= os.path.join( Emulator_Folder_Path, 'neogeocd\\roms' )
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
				if Parse_CUE_File: Rom_Type_Total = (len(glob.glob1(Roms_Folder,'*.cue')))
				if Parse_CUE_CCD_ISO_File: Rom_Type_Total = (len(glob.glob1(Roms_Folder,'*.cue')) + len(glob.glob1(Roms_Folder,'*.ccd')) + len(glob.glob1(Roms_Folder,'*.iso')))
				#--------
				log('| '+ Emu_Name +  '	- Convert Q:\\ to a direct path')
				#--------
				if Roms_Folder.startswith("Q:\\"): Roms_Folder = Roms_Folder.replace( "Q:\\", Root_Directory )
				#--------
				log('| '+ Emu_Name +  '	- Check to see if the emulators = rom folder is empty and exit if it is.')
				#--------
				# if len(os.walk(Roms_Folder).next()[2]) > 0: # slower than just doing what I do below.
				if len(os.listdir( Roms_Folder )) > 0:
					#--------
					log('| '+ Emu_Name +  '	- Write new gamelist xml header.')
					#--------
					with open( os.path.join( Games_List_Path, 'gamelist.xml' ), "wb") as outputmenufile:
						WriteMenuFile = menu_entry_header
						outputmenufile.write( WriteMenuFile )
					#--------
					log('| '+ Emu_Name +  '	- Check to see if vars are the value I need and create a new dialog.')
					#--------
					if CreateDialog == 1:
						#CreateDialog = 0
						if ManualScan:
							pDialog.create( "MANUAL SCAN MODE","Initializing" )
						else:
							pDialog.create( "AUTO SCAN MODE","Initializing" )
						pDialog.update(0,"Creating [B][UPPERCASE]" + Emu_Name + "[/UPPERCASE][/B] Rom list","","This can take some time, please be patient.")
					#--------
					log('| '+ Emu_Name +  '	- Checking filenames case and not leading with capital renaming it to do so.')
					#--------
					if not Emu_Name == "fba" or Emu_Name == "mame":
						for Roms in sorted( os.listdir( Roms_Folder ) ):
							pDialog.update(0,"Checking [B]" + Emu_Name + "s[/B] Rom filename casing.","[B]" + Roms + "[/B]","This can take some time, please be patient." )
							Items_Full_Path = os.path.join( Roms_Folder, Roms )
							if Items_Full_Path != os.path.join( Roms_Folder, Roms.lower() ):
							##if Items_Full_Path != os.path.join( Roms_Folder, Roms.capitalize() ):
								tempname = Items_Full_Path[:-1]
								if not os.path.isfile( tempname ):
									os.rename( Items_Full_Path,  tempname )
									os.rename( tempname,  os.path.join( Roms_Folder, Roms.lower() ) )
									##os.rename( tempname,  os.path.join( Roms_Folder, Roms.capitalize() ) )
									pDialog.update((RenameCount * 100) / len( os.listdir( Roms_Folder ) ),"Lower-casing rom names.","[B]" + Roms + "[/B]" ,"This can take some time, please be patient." )
									RenameCount = RenameCount + 1
					#--------
					log('| '+ Emu_Name +  '	- Setting a var again :/')
					#--------
					Found_Roms = 1
					#--------
					log('| '+ Emu_Name +  '	- Check if fbl was found and change its rom path to where the roms are located.')
					#--------
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
					#--------
					log('| '+ Emu_Name +  '	- Check if mame was found and change it rom path to where the roms are located.')
					#--------
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
						if os.path.isfile( os.path.join( Emulator_Folder_Path, "fba\\info\\" ) + "FBL Rom Names.zip" ):
							if os.path.isfile( os.path.join( Emulator_Folder_Path, "fba\\info\\rom names\\3countb.txt" ) ):
								pDialog.update( 0,"Found old FBA name files","Removing them before extracting the new ones.","This can take some time, please be patient." )
								shutil.rmtree( os.path.join( Emulator_Folder_Path, "fba\\info\\rom names" ) )
							#--------
							log('| '+ Emu_Name +  '	- Extracting the rom name files from the zip.')
							#--------
							with zipfile.ZipFile( os.path.join( Emulator_Folder_Path, "fba\\info\\" ) + "FBL Rom Names.zip" ) as zip:
								if not os.path.isdir( os.path.join( Emulator_Folder_Path, "fba\\info\\rom names" ) ): os.makedirs( os.path.join( Emulator_Folder_Path, "fba\\info\\rom names" ) )
								if ZipCount == 0:
									#pDialog.create( "EXTRACTING ZIP","","Please wait..." )
									Total_TXT_Files = len( zip.namelist() ) or 1
									Devide = 100.0 / Total_TXT_Files
									Percent = 0
									for item in zip.namelist():
										Percent += Devide
										pDialog.update( int( Percent ),"Extracting final burn legends rom names","This only happens once per update","" )
										zip.extract( item, os.path.join( Emulator_Folder_Path, "fba\\info\\rom names\\" ) )
									ZipCount = 1
							os.remove( os.path.join( Emulator_Folder_Path, "fba\\info\\" ) + "FBL Rom Names.zip" )
						Roms_Folder = os.path.join( Emulator_Folder_Path, "fba\\info\\rom names" )
						## Used to name the rom name files so I can sort them by alphabetical order properly. ( this is only used by me ) 
						# for files in sorted( os.listdir( os.path.join( Emulator_Folder_Path, "fba\\roms1" ) ) ):
							# try:
								# with open( os.path.join( Emulator_Folder_Path, "fba\\info\\rom names", files[:-3] + 'txt' ), 'r') as txt:
									# FBA_Rom_Name_Full = txt.readline()[:-2]
									# FBA_Rom_Name = FBA_Rom_Name_Full[:20]
									# FBA_Rom_Name = FBA_Rom_Name.replace( ',','' ); FBA_Rom_Name = FBA_Rom_Name.replace( ':','' ); FBA_Rom_Name = FBA_Rom_Name.replace( ';','' ); FBA_Rom_Name = FBA_Rom_Name.replace( '/','' ); FBA_Rom_Name = FBA_Rom_Name.replace( '?','' ); FBA_Rom_Name = FBA_Rom_Name.replace( '+','' ); FBA_Rom_Name = FBA_Rom_Name.replace( '*','' ); FBA_Rom_Name = FBA_Rom_Name.replace( 'amp','' ); FBA_Rom_Name = FBA_Rom_Name.replace( ' ','' );
									# FBA_Rom_Name = FBA_Rom_Name.lower()
									# for line in txt: FBA_Rom_System_Full = '\n'+line
								# if not os.path.isdir( "F:\\rom names" ): os.makedirs( "F:\\rom names" )
								# with open( os.path.join( "F:\\rom names", FBA_Rom_Name + '--' + files[:-3] + 'zip' ), 'w') as txt:
									# txt.write( FBA_Rom_Name_Full.lower() )
									# txt.write( FBA_Rom_System_Full.lower() )
								# pDialog.update((CountList * 100) / len(os.listdir( os.path.join( Emulator_Folder_Path, "fba\\roms1" ) ) ),"Processing Rom name files",files,"This can take some time, please be patient." )
								# CountList = CountList + 1
							# except: pass
						# return
					#--------
					log('| '+ Emu_Name +  '	- Listing the content of the roms folder for parsing.')
					#--------
					for Items in sorted( os.listdir( Roms_Folder ) ):
						#--------
						log('| '+ Emu_Name +  '	- Checking the file I find, extension agains my table.')
						#--------
						if Items.lower().endswith(tuple(Extensions)):
							#--------
							log('| '+ Emu_Name +  '	- More vars being set.')
							#--------
							Rom_Name = Items.lower()
							Rom_Name_noext = Rom_Name[:-4]
							JumpList_Name = Rom_Name_noext.lower()
							if not xbmc.getCondVisibility( 'Skin.String(' + Emu_Name + '_artworkfolder)' ): xbmc.executebuiltin('Skin.SetString(' + Emu_Name + '_artworkfolder,boxart)')
							Thumbnails_Path = os.path.join( Media_Path, '$INFO[Skin.String(' + Emu_Name + '_artworkfolder)]', Rom_Name_noext + '.png' )
							#--------
							log('| '+ Emu_Name +  '	- Check if fba was found and parse the name text files to get the correct rom names and system types for the list.')
							#--------
							if Parse_FBL_TXT == 1:
								Rom_Name_Full = Rom_Name
								Rom_Name_Beg = Rom_Name.split('--', 1)[0]
								Rom_Name = Rom_Name.split('--', 1)[1]
								Rom_Name_noext = Rom_Name[:-4]
								Thumbnails_Path = os.path.join( Media_Path, '$INFO[Skin.String(' + Emu_Name + '_artworkfolder)]', Rom_Name_noext + '.png' )
								if os.path.isfile( os.path.join( Roms_Folder_Path, "fba", Rom_Name ) ) and os.path.isfile( os.path.join( Emulator_Folder_Path, "fba\\info\\rom names", Rom_Name_Beg + '--' + Rom_Name ) ):
									with open( os.path.join( Emulator_Folder_Path, "fba\\info\\rom names", Rom_Name_Beg + '--' + Rom_Name ), 'r') as txt:
										FBA_Rom_Name = txt.readline()[:-1]
										#FBA_Rom_Name = FBA_Rom_Name.split('(', 1)[0]
										#FBA_Rom_Name = FBA_Rom_Name.split('/', 1)[0]
										for line in txt:
											System_Name = line.lower()[:-2]
											Emu_XBE = os.path.join( Emu_Path, "default.xbe" )
											if System_Name == "psikyo 68ec020" or System_Name == "ps3-v1" or System_Name == "ps4" or System_Name == "ps5" or System_Name == "fg-3" or System_Name == "tecmo" or System_Name == "polygamemaster" or System_Name == "polygamemaster based" or System_Name == "ps5v2": Emu_XBE = os.path.join( Emu_Path, "psykio.xbe" )
											if System_Name == "neo geo aes" or System_Name == "neo geo mvs": Emu_XBE = os.path.join( Emu_Path, "neogeocps2.xbe" )
											if System_Name == "cps2": Emu_XBE = os.path.join( Emu_Path, "neogeocps2.xbe" )
											if System_Name == "cave": Emu_XBE = os.path.join( Emu_Path, "cave.xbe" )
											if System_Name == "toaplan gp9001 based" or System_Name == "toaplan bcu-2 / fcu-2 based" or System_Name == "dual toaplan gp9001 based": Emu_XBE = os.path.join( Emu_Path, "toaplan.xbe" )
											if System_Name == "to": Emu_XBE = os.path.join( Emu_Path, "taito.xbe" )
											if System_Name == "sk" or System_Name == "cps-3" or System_Name == "nmk16" or System_Name == "ssv" or System_Name == "wr" or System_Name == "th2" or System_Name == "wr2" or System_Name == "fg-2" or System_Name == "mega system 1" or System_Name == "sf" or System_Name == "kaneko 16-bit": Emu_XBE = os.path.join( Emu_Path, "new.xbe" )
											if System_Name == "de": Emu_XBE = os.path.join( Emu_Path, "dataeast.xbe" )
											if System_Name == "kn": Emu_XBE = os.path.join( Emu_Path, "konami.xbe" )
											if System_Name == "system 16a" or System_Name == "system 16b" or System_Name == "system 18" or System_Name == "x-board" or System_Name == "y-board" or System_Name == "out run" or System_Name == "hang-on": Emu_XBE = os.path.join( Emu_Path, "sega.xbe" )
											if System_Name == "jc" or System_Name == "unico" or System_Name == "ss" or System_Name == "f1gp" or System_Name == "newer seta" or System_Name == "pwr": Emu_XBE = os.path.join( Emu_Path, "xtra.xbe" )
											if System_Name == "im": Emu_XBE = os.path.join( Emu_Path, "irem.xbe" )
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
							#--------
							log('| '+ Emu_Name +  '	- Check if n64 was found and parse the names from surreal.ini if the roms match.')
							#--------
							if Parse_N64_TXT == 1:
								if os.path.isfile( os.path.join( Emulator_Folder_Path, "n64\\Surreal.ini" ) ):
									#--------
									log('| '+ Emu_Name +  '	- Extracting the rom names from the ini.')
									#--------
									with open( os.path.join( Emulator_Folder_Path, "n64\\Surreal.ini" ), 'r') as ini:
										for line in itertools.islice(ini, 20, None):
											N64ID = str(line.lower())[1:-7]
											N64ID1 = N64ID.split('-', 1)[0]
											N64ID2 = N64ID.split('-', 1)[1]
											File_Name = ini.next().replace('Game Name=','')[:-1]
											File_Name = File_Name.lower()
											if Rom_Name_noext == File_Name:
												N64_Rom_Name = ini.next().replace('Alternate Title=','')[:-1]
												N64_Rom_Name = N64_Rom_Name.split(' (', 1)[0]
												try:
													ini.next() # skip the comment line
													ini.next() # skip the blank line
												except: pass
												for N64_Thumb in os.listdir( os.path.join( Emulator_Folder_Path, 'n64\\media\\Cbagys3DArt' ) ):
													N64_Thumb = N64_Thumb.lower()
													if N64ID1 in N64_Thumb or N64ID2 in N64_Thumb:
														if not os.path.isdir( os.path.join( Synopsis_Path, Emu_Name ) ): os.makedirs( os.path.join( Synopsis_Path, Emu_Name ) )
														N64_Thumb_Location = os.path.join( Emulator_Folder_Path, 'n64\\media\\Cbagys3DArt', N64_Thumb )
														N64_Thumb_Destination = os.path.join( Media_Path, 'boxart3d', File_Name + '.png' )
														if os.path.isfile( N64_Thumb_Location ) and not os.path.isfile( N64_Thumb_Destination ): shutil.copy2( N64_Thumb_Location, N64_Thumb_Destination )
												for N64_Synopsis in os.listdir( os.path.join( Emulator_Folder_Path, 'n64\\media\\synopsis' ) ):
													N64_Synopsis = N64_Synopsis.lower()
													if N64ID1 in N64_Synopsis or N64ID2 in N64_Synopsis:
															N64_Synopsis_Location = os.path.join( Emulator_Folder_Path, 'n64\\media\\synopsis', N64_Synopsis[:-3] + 'txt' )
															N64_Synopsis_Destination = os.path.join( Synopsis_Path, Emu_Name, File_Name + '.txt' )
															if os.path.isfile( N64_Synopsis_Location ) and not os.path.isfile( N64_Synopsis_Destination ): 
																with open( N64_Synopsis_Location ) as readn64tmp:
																	readn64 = readn64tmp.read()
																	readn64 = readn64.strip()
																	with open( N64_Synopsis_Destination, 'w' ) as n64tmp:
																		amended_n64tmp = 'Name: ' + readn64
																		n64tmp.write(amended_n64tmp)
															#if os.path.isfile( N64_Synopsis_Location ): shutil.copy2( N64_Synopsis_Location, N64_Synopsis_Destination )
											else:
												try:
													ini.next() # skip the rom name
													ini.next() # skip the comment line
													ini.next() # skip the blank line
												except: pass
							else:
								pass
							if Change_N64_Rom_Path == 1:
								if os.path.isdir( 'E:\\TDATA\\64ce64ce' ): shutil.rmtree( 'E:\\TDATA\\64ce64ce' )
								if os.path.isfile(os.path.join( Emu_Path, "surreal.ini" )):
									for line in fileinput.input( os.path.join( Emu_Path, "surreal.ini" ), inplace=1):
										if 'Rom Path=' in line:
											line = line = 'Rom Path=' + Roms_Folder + '\n'
										print line,
									os.makedirs( 'E:\\TDATA\\64ce64ce' )
									with open( os.path.join( 'E:\\TDATA\\64ce64ce\\surreal-ce.ini' ), "w") as outputn64file:
										WriteN64File = n64_config % ( Roms_Folder )
										outputn64file.write( WriteN64File )
									Change_N64_Rom_Path = 0
								else:
									dialog.ok("ERROR","Surreal.ini is missing from the","N64 Emulators directory.")
									return
							#--------
							log('| '+ Emu_Name +  '	- Check for a synopsis zip for the current emulator.')
							#--------
							if ZipCount == 0:
								if os.path.isfile( Synopsis_Zip ):
										#--------
										log('| '+ Emu_Name +  '	- Extracting the synopsis files from the zip.')
										#--------
										with zipfile.ZipFile( Synopsis_Zip ) as zip:
											if ZipCount == 0:
												#pDialog.create( "EXTRACTING ZIP","","Please wait..." )
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
							#--------
							log('| '+ Emu_Name +  '	- Check for a synopsis file for the current emulator and parse it.')
							#--------
							try:
								if Emu_Name == "genesis":
									Synopsis_File = os.path.join( Synopsis_Path, "megadrive", Rom_Name_noext + '.txt' )
								elif Emu_Name == "famicom":
									Synopsis_File = os.path.join( Synopsis_Path, "nes", Rom_Name_noext + '.txt' )
								elif Emu_Name == "tg16":
									Synopsis_File = os.path.join( Synopsis_Path, "pcengine", Rom_Name_noext + '.txt' )
								elif Emu_Name == "tg-cd":
									Synopsis_File = os.path.join( Synopsis_Path, "pce-cd", Rom_Name_noext + '.txt' )
								else:
									Synopsis_File = os.path.join( Synopsis_Path, Emu_Name, Rom_Name_noext + '.txt' )
								with open( Synopsis_File ) as input:
									Synopsis = input.read()
									Synopsis1 = Synopsis.split('_________________________', 1)[0]
									Synopsis1 = Synopsis1.split('\n')
									Synopsis_filename = ""; Synopsis_rating = ""; Synopsis_players = ""; Synopsis_genre = ""; Synopsis_developer = ""; Synopsis_publisher = ""; Synopsis_release_year = ""
									Synopsis_filename_Set = 0; Synopsis_nointroname_Set = 0; Synopsis_rating_Set = 0; Synopsis_players_Set = 0; Synopsis_genre_Set = 0; Synopsis_developer_Set = 0; Synopsis_publisher_Set = 0; Synopsis_release_year_Set = 0
									for _ in range(11):
										for line in Synopsis1:
											line = line.lower()
											if line.startswith('name:') and xbmc.getCondVisibility( 'Skin.HasSetting(Use_NoIntroNames)' ):
												if Emu_Name == "fba":
													FBA_Rom_Name = line.split(': ',1)[1]
													Synopsis_nointroname_Set = 1
												else:
													Rom_Name_noext = line.split(': ',1)[1]
													if Rom_Name_noext.startswith('the'):
														Rom_Name_noext = Rom_Name_noext[4:] + ', The'
														N64_Rom_Name = Rom_Name_noext[4:] + ', The'
													else:
														Rom_Name_noext = Rom_Name_noext.split(' (',1)[0]
														N64_Rom_Name = Rom_Name_noext.split(' (',1)[0]
													Synopsis_nointroname_Set = 1
											elif Synopsis_nointroname_Set == 0:
												pass
											if line.startswith('filename:'):
												Synopsis_filename = line.split(': ',1)[1]
												Synopsis_filename = '[B]Filename:[/B]\n ' + Synopsis_filename
												Synopsis_filename_Set = 1
											elif Synopsis_filename_Set == 0:
												Synopsis_filename = '[B]Filename:[/B]\n ' + Rom_Name
											# if line.startswith('rating:'):
												# Synopsis_rating = line.split(': ',1)[1]
												# Synopsis_rating = '[B]Rating:[/B]\n ' + Synopsis_rating
												# Synopsis_rating_Set = 1
											# elif Synopsis_rating_Set == 0:
												# Synopsis_rating = '[B]Rating:[/B]\n unknown'
											if line.startswith('players:'):
												Synopsis_players = line.split(': ',1)[1]
												Synopsis_players = '[B]Players:[/B]\n ' + Synopsis_players
												Synopsis_players_Set = 1
											elif Synopsis_players_Set == 0:
												Synopsis_players = '[B]Players:[/B]\n at least 1'
											if line.startswith('genre:'):
												Synopsis_genre = line.split(': ',1)[1]
												Synopsis_genre = '[B]Genre:[/B]\n ' + Synopsis_genre
												Synopsis_genre_Set = 1
											elif Synopsis_genre_Set == 0:
												Synopsis_genre = '[B]Genre:[/B]\n unknown'
											if line.startswith('developer:'):
												Synopsis_developer = line.split(': ',1)[1]
												Synopsis_developer = '[B]Developer:[/B]\n ' + Synopsis_developer
												Synopsis_developer_Set = 1
											elif Synopsis_developer_Set == 0:
												Synopsis_developer = '[B]Developer:[/B]\n unknown'
											if line.startswith('publisher:'):
												Synopsis_publisher = line.split(': ',1)[1]
												Synopsis_publisher = '[B]Publisher:[/B]\n ' + Synopsis_publisher
												Synopsis_publisher_Set = 1
											elif Synopsis_publisher_Set == 0:
												Synopsis_publisher = '[B]Publisher:[/B]\n unknown'
											if line.startswith('release year:'):
												Synopsis_release_year = line.split(': ',1)[1]
												Synopsis_release_year = '[B]Released:[/B]\n ' + Synopsis_release_year
												Synopsis_release_year_Set = 1
											elif Synopsis_release_year_Set == 0:
												Synopsis_release_year = '[B]Released:[/B]\n unknown'
									Synopsis1 = Synopsis_players + '\n' + Synopsis_genre + '\n' + Synopsis_developer + '\n' + Synopsis_publisher + '\n' + Synopsis_release_year + '\n' + Synopsis_filename
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
							if FBA_Rom_Name == "1942": FBA_Rom_Name = "1942 "
							if Rom_Name_noext == "1942": Rom_Name_noext = "1942 "
							if Rom_Name_noext == "1943": Rom_Name_noext = "1943 "
							if Rom_Name_noext == "720": Rom_Name_noext = "720 "
							#--------
							log('| '+ Emu_Name +  '	- Set Rom_Names for different types of CD images.')
							#--------
							Rom_Name_ISO = os.path.join( Roms_Folder, Rom_Name[:-4] + ".iso" )
							Rom_Name_BIN = os.path.join( Roms_Folder, Rom_Name[:-4] + ".bin" )
							Rom_Name_IMG = os.path.join( Roms_Folder, Rom_Name[:-4] + ".img" )
							Rom_Name_CUE = os.path.join( Roms_Folder, Rom_Name[:-4] + ".cue" )
							Rom_Name_CCD = os.path.join( Roms_Folder, Rom_Name[:-4] + ".ccd" )
							Rom_Path = os.path.join( Roms_Folder, Rom_Name )
							#--------
							log('| '+ Emu_Name +  '	- Check and parse the directory for iso files.')
							#--------
							if Parse_ISO_File == 1:
								if Items.endswith( '.iso' ):
									Rom_Path = Rom_Name_ISO
									Rom_Type_Total = Rom_Type_Total
									Write_List_File = 1
								else:
									Write_List_File = 0	
							#--------
							log('| '+ Emu_Name +  '	- Check and parse the directory for cue files.')
							#--------
							if Parse_CUE_File == 1:
								if Items.endswith( '.cue' ):
									Rom_Path = Rom_Name_CUE
									Rom_Type_Total = Rom_Type_Total
									Write_List_File = 1
								else:
									Write_List_File = 0
							#--------
							log('| '+ Emu_Name +  '	- Check and parse the directory for bin/iso/img files.')
							#--------
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
							#--------
							log('| '+ Emu_Name +  '	- Check and parse the directory for cue/ccd/iso files.')
							#--------
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
							#--------
							log('| '+ Emu_Name +  '	- Create the rest of the layout xml file.')
							#--------
							if Write_List_File:
								#--------
								log('| '+ Emu_Name +  '	- Show the progress bar progress and write rom list file.')
								#--------
								RomListCount = RomListCount + 1
								with open( os.path.join( Games_List_Path, 'gamelist.xml' ), "a") as outputmenufile:
									if Emu_Name == "fba":
										pDialog.update((CountList * 100) / len(os.listdir( os.path.join( Roms_Folder_Path, "fba" ) ) ),"Creating [B][UPPERCASE]" + Emu_Name + "[/UPPERCASE][/B] Rom list",FBA_Rom_Name,"This can take some time, please be patient." )
										WriteMenuFile = menu_entry % (CountList,FBA_Rom_Name,Synopsis1,'RunScript( Special://xbmc/.emustation/scripts/launcher.py,' + Emu_XBE + ',' + Rom_Name_noext + ',,' + str(CountList) + ' )',"ActivateWindow(1101)",Synopsis2,Thumbnails_Path)
									elif Emu_Name == "mame" or Emu_Name == "neogeocd":
										pass
									elif Emu_Name == "n64":
										pDialog.update((CountList * 100) / len(os.listdir( Roms_Folder )),"Creating [B][UPPERCASE]" + Emu_Name + "[/UPPERCASE][/B] Rom list",N64_Rom_Name,"This can take some time, please be patient." )
										WriteMenuFile = menu_entry % (CountList,N64_Rom_Name,Synopsis1,'RunScript( Special://xbmc/.emustation/scripts/launcher.py,' + Emu_XBE + ',' + Rom_Path + ',,' + str(CountList) + ' )',"ActivateWindow(1101)",Synopsis2,Thumbnails_Path)
									elif Emu_Name == "pce-cd" or Emu_Name == "psx" or Emu_Name == "tg-cd" or Emu_Name == "segacd":
										pDialog.update((CountList * 100) / Rom_Type_Total,"Creating [B][UPPERCASE]" + Emu_Name + "[/UPPERCASE][/B] Rom list",Rom_Name_noext,"This can take some time, please be patient." )
										WriteMenuFile = menu_entry % (CountList,Rom_Name_noext,Synopsis1,'RunScript( Special://xbmc/.emustation/scripts/launcher.py,' + Emu_XBE + ',' + Rom_Path + ',,' + str(CountList) + ' )',"ActivateWindow(1101)",Synopsis2,Thumbnails_Path)
									else:
										pDialog.update((CountList * 100) / len(os.listdir( Roms_Folder )),"Creating [B][UPPERCASE]" + Emu_Name + "[/UPPERCASE][/B] Rom list",Rom_Name_noext,"This can take some time, please be patient." )
										WriteMenuFile = menu_entry % (CountList,Rom_Name_noext,Synopsis1,'RunScript( Special://xbmc/.emustation/scripts/launcher.py,' + Emu_XBE + ',' + Rom_Path + ',,' + str(CountList) + ' )',"ActivateWindow(1101)",Synopsis2,Thumbnails_Path)
									outputmenufile.write( WriteMenuFile )
								#--------
								log('| '+ Emu_Name +  '	- Write favourites menu entries.')
								#--------
								with open( os.path.join( Games_List_Path, 'favslist.xml' ), "a") as favsmenufile:
									if Emu_Name == "fba":
										WriteMenuFile = favourites_entry % (FBA_Rom_Name,Rom_Name_noext)
									elif Emu_Name == "mame" or Emu_Name == "neogeocd":
										pass
									elif Emu_Name == "n64":
										WriteMenuFile = favourites_entry % (N64_Rom_Name,Rom_Path)
									else:
										WriteMenuFile = favourites_entry % (Rom_Name_noext,Rom_Path)
									favsmenufile.write( WriteMenuFile )
								#--------
								log('| '+ Emu_Name +  '	- Write menu entry for quick jump')
								#--------
								with open( os.path.join( Games_List_Path, 'jumplist.xml' ), "a") as outputmenuselectfile:
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
								#--------
								log('| '+ Emu_Name +  '	- Add 1 to the Countlist and JumpList.')
								#--------
								CountList = CountList + 1
								JumpList = JumpList + 1
					#--------
					log('| '+ Emu_Name +  '	- Add the footer to the layout xml file.')
					#--------
					with open( os.path.join( Games_List_Path, 'gamelist.xml' ), "a") as outputmenufile:
						WriteMenuFile = menu_entry_footer
						outputmenufile.write( WriteMenuFile )
				else:
					if os.path.isdir( Games_List_Path ): shutil.rmtree( Games_List_Path )
					if ManualScan == 1:
						dialog.ok("Error","","No roms/images found for this system")
						return Main_Code()
			else:
				if os.path.isdir( Games_List_Path ): shutil.rmtree( Games_List_Path )
			#--------
			log('| '+ Emu_Name +  '	- Set the rom count and remove any direct launch rom list.xml files.')
			#--------
			xbmc.executebuiltin('Skin.SetString('+ Emu_Name +'_games,'+ str( RomListCount ) + ')')
			if Emu_Name == "atarijaguar" or Emu_Name == "neogeocd":
				if os.path.isdir( Games_List_Path ): shutil.rmtree( Games_List_Path )
				if os.path.isdir( Media_Path ): shutil.rmtree( Media_Path )
			if Emu_Name == "mame":
				if os.path.isfile( os.path.join( Emu_Path, "system\\ROMS.list" )): os.remove( os.path.join( Emu_Path, "system\\ROMS.list" ))
				if os.path.isfile( os.path.join( Emu_Path, "system\\ROMS.metadata" )): os.remove( os.path.join( Emu_Path, "system\\ROMS.metadata" ))
				if os.path.isdir( Games_List_Path ): shutil.rmtree( Games_List_Path )
				if os.path.isdir( Media_Path ): shutil.rmtree( Media_Path )
			#--------		
			log('| '+ Emu_Name +  '	- ManualMode - Set a property so I can run the next script without this one running on.')			
			#--------
			if Found_Roms == 1 and ManualScan == 1:
				xbmcgui.Window(xbmcgui.getCurrentWindowId()).setProperty("MyScript.ExternalRunning", "True")
				log('| '+ Emu_Name +  '	- Running the scan script to update the counters.')
				xbmc.executebuiltin('RunScript(' + Scripts_Path + 'scanner.py,0,' + Emu_Name + ',0,0)' )
				log('| '+ Emu_Name +  '	- Loop.')
				while (xbmcgui.Window(xbmcgui.getCurrentWindowId()).getProperty("MyScript.ExternalRunning") == "True"):
					time.sleep(0.2)
				pDialog.close()
				return
	#--------	
	log('| '+ Emu_Name +  '	- AutoMode - Set a property so I can run the next script without this one running on.')			
	#--------		
	if Found_Roms == 1 and ManualScan == 0:
		xbmcgui.Window(xbmcgui.getCurrentWindowId()).setProperty("MyScript.ExternalRunning", "True")
		log('| '+ Emu_Name +  '	- Running the scan script to update the counters.')
		xbmc.executebuiltin('RunScript(' + Scripts_Path + 'scanner.py,scan_emus,0,0,0)' )
		log('| '+ Emu_Name +  '	- Loop.')
		while (xbmcgui.Window(xbmcgui.getCurrentWindowId()).getProperty("MyScript.ExternalRunning") == "True"):
			time.sleep(0.2)
	else:
		pDialog.close()
		return

CUT_File_Layout = '<shortcut><path>%s</path><custom><game>%s</game></custom></shortcut>'
menu_entry_header	= '<content>'
menu_entry			= '\n<item id="%s">\n		<label>%s</label>\n		<label2>%s</label2>\n		<onclick>%s</onclick>\n		<onclick>%s</onclick>\n		<icon>%s</icon>\n		<thumb>%s</thumb>\n	</item>'
menu_entry_footer	= '\n</content>'
search_menu_entry	= '<control type="button" id="%s">\n	<label>[UPPERCASE]jump to letter[/UPPERCASE]</label>\n	<label2>&lt; [UPPERCASE]%s[/UPPERCASE] &gt;</label2>\n	<include>MenuButtonCommonValues</include>\n	<onclick>Dialog.Close(1120)</onclick>\n	<onclick>%s</onclick>\n</control>\n'
favourites_entry	= '<favourites>%s,%s</favourites>\n'
n64_config			= '[Settings]\nskinname=Default\nonhd=true\nHideLaunchScreens=true\nEnableXMVPreview=false\nEnableVideoAudio=false\nEnableInfoPanel=false\nEnableBGMusic=false\nRandomBGMusic=false\nAudioBoost=false\nPathRoms=%s\\\nPathMedia=D:\Media\\\nPathSkins=D:\Skins\\\nPathSaves=D:\Saves\\\nPathScreenshots=D:\Screenshots\\'
mame_config			= '[Directories]\nALTDrive = t\nC_Mapping = \\device\\harddisk0\\partition1\nE_Mapping = \\device\\harddisk0\\partition1\nF_Mapping = \\device\\harddisk0\\partition6\nG_Mapping = \\device\\cdrom0\nH_Mapping = \\device\\harddisk0\\partition6\nRomsPath0 = %s\nRomsPath1 = d:\\roms\nRomsPath2 = d:\\roms\nRomsPath3 = d:\\roms\nArtPath = d:\\artwork\nAudioPath = d:\\samples\nConfigPath = d:\\cfg\nGeneralPath = d:\\general\nHDImagePath = d:\\hdimages\nHiScoresPath = d:\\hiscores\nNVRamPath = d:\\nvram\nBackupPath = d:\\roms\\backup\nScreenshotPath = d:\\screenshots\nAutoBootSavePath = d:\\autobootsaves\n\n\n[General]\nbios = 0\nCheatsEnabled = 1\nCheatFilename = cheat.dat\nSkipDisclaimer = 1\nSkipGameInfo = 1\nSkipWarnings = 1\nScreenSaverTimeout = 10\n\n\n[Input]\nLightgun1_Left = 4294934529\nLightgun1_CenterX = 0\nLightgun1_Right = 32767\nLightgun1_Top = 32767\nLightgun1_CenterY = 0\nLightgun1_Bottom = 4294934529\nLightgun2_Left = 4294934529\nLightgun2_CenterX = 0\nLightgun2_Right = 32767\nLightgun2_Top = 32767\nLightgun2_CenterY = 0\nLightgun2_Bottom = 4294934529\nLightgun3_Left = 4294934529\nLightgun3_CenterX = 0\nLightgun3_Right = 32767\nLightgun3_Top = 32767\nLightgun3_CenterY = 0\nLightgun3_Bottom = 4294934529\nLightgun4_Left = 4294934529\nLightgun4_CenterX = 0\nLightgun4_Right = 32767\nLightgun4_Top = 32767\nLightgun4_CenterY = 0\nLightgun4_Bottom = 4294934529\n\n\n[Network]\nDisableNetworking = 0\nIPAddress = \nGateway = \nSubnet = \nNameServer = \n\n\n[ROMListOptions]\nDisplayMode = 1\nSortMode = 0\nShowROMStatus = 0\nShowFAVEStatus = 1\nHideFilteredROMs = 0\nFilterMode = 0\nCursorPosition = 0.000000\nPageOffset = 0.000000\nSuperscrollIndex = 0\n\n\n[SkinOptions]\nSelectedSkin = Original\n\n\n[Sound]\nSoundEnable = 1\nSampleRate = 44100\nUseSamples = 1\nUseFilter = 1\n\n\n[VMMOptions]\nForceVMM = 0\nThreshold = 4194304\nCommitSize = 1048576\nDistribute = 65535\n\n\n[VectorOptions]\nVectorWidth = 640\nVectorHeight = 480\nBeamWidth = 2\nFlickerEffect = 0.000000\nBeamIntensity = 1.500000\nTranslucency = 1\n\n\n[Video]\nVSYNC = 1\nThrottleFramerate = 1\nAspectRatioCorrection = 1\nMinificationFilter = 2\nMagnificationFilter = 2\nFrameskip = 4294967295\nGraphicsFilter = 0\nSoftDisplayFilter = 0\nFlickerFilter = 5\nScreenRotation = 0\nBrightness = 1.000000\nPauseBrightness = 0.650000\nGamma = 1.000000\nScreenUsage_X = 0.850000\nScreenUsage_Y = 0.850000\nScreenPos_X = 0.000000\nScreenPos_Y = 0.000000\nArtwork = 1\n\n\n'
fbl_config			= 'UsePathINI=1\nROMPath1=D:\\roms\nROMPath2=\nROMPath3=\nROMPath4=\nROMPath5=\nROMPath6=\nROMPath7=\nROMPath8=\nD:\\artwork\\Shots 1\nD:\\artwork\\Shots 2\nD:\\artwork\\Shots 3\nD:\\artwork\\Shots 4\nD:\\artwork\\Shots 5\nD:\\artwork\\Shots 6\nD:\\artwork\\Shots 7\nD:\\artwork\\Shots 8\nD:\\nvram\nD:\\samples\nD:\\ini\nD:\\savestates\nD:\\config\nD:\\hiscores\nD:\\videos\n'

logging = 0 # Setting this to 1 will spam the living hell out of your log file if you run the Auto mode, you have been warned

# Ask the user if they want to use the internal names from the synopsis files, I recommend this as they will be the proper names.
if dialog.yesno('ROM NAMES','Would you like to use the names stored in','synopsis files instead of the roms filenames?','If no name is found, rom filenames will be used.') == 1:
	xbmc.executebuiltin('Skin.SetBool(Use_NoIntroNames)')
else:
	xbmc.executebuiltin('Skin.Reset(Use_NoIntroNames)')

if Manual_Scan == "manual" :
	ManualScan = 1
	Main_Code()

if Full_Scan == "auto" :
	ManualScan = 0
	Main_Code()