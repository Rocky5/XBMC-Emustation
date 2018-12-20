'''
	Script by Rocky5
	Used to create static lists from your emulator and roms folder.
	Atarijaguar have there roms placed inside there root directory.
	NeoGeoCD must have its ISO files in folders inside its roms\system folder and the .cue file must match the name of the folder.
	( the script will generate static lists for emulators )
'''
import fileinput, glob, itertools, re, operator, os, shutil, struct, sys, time, xbmc, xbmcgui, zipfile, filecmp
from xbe import *
## Start markings for the log file.
print "| create_rom_lists.py loaded."
try:
	Manual_Scan	= sys.argv[1:][0]
	Full_Scan	= sys.argv[2:][0]
except:
	Manual_Scan	= "0"
	Full_Scan	= "0"
pDialog	= xbmcgui.DialogProgress()
dialog	= xbmcgui.Dialog()
## Sets paths.
Root_Directory	= xbmc.translatePath("Special://root/")
if xbmc.getCondVisibility( 'Skin.String(Custom_Emulator_Path)' ):
	Emulator_Folder_Path = xbmc.getInfoLabel( 'Skin.String(Custom_Emulator_Path)' )
else:
	Emulator_Folder_Path = os.path.join( Root_Directory, '.emustation\\emulators\\' )
if xbmc.getCondVisibility( 'Skin.String(Custom_Roms_Path)' ):
	Roms_Folder_Path	 = xbmc.getInfoLabel( 'Skin.String(Custom_Roms_Path)' )
else:
	Roms_Folder_Path	 = os.path.join( Root_Directory, '.emustation\\roms\\' )
if xbmc.getCondVisibility( 'Skin.String(Custom_Media_Path)' ):
	Media_Folder_Path	 = xbmc.getInfoLabel( 'Skin.String(Custom_Media_Path)' )
else:
	Media_Folder_Path	 = os.path.join( Root_Directory, '.emustation\\media\\' )
Synopsis_Path		= os.path.join( Root_Directory, '.emustation\\synopsis\\' )
Scripts_Path		= os.path.join( Root_Directory, '.emustation\\scripts\\' )
Extensions			= [ "adf","md","xbg","lnx","a78","a52","dim","nds","t64","d64","int","tap","z80","tzx","zip","bin","ccd","cue","j64","img","iso","rom","n64","z64","smd","smc","gb","gbc","gba","nes","sms","swc","gg","a26","a78","col","lnx","sfc","sg","fig","vms","exe" ]
## Modified by me. Original by chunk_1970 - http://forum.kodi.tv/showthread.php?tid=24666&pid=125356#pid125356
def Extract_XbeInfo(FileName): ## Need to use this as the xbe.py Get_title misses letter and causes string issues, even when using .encode or .decode
	if os.path.isfile(FileName) and FileName.endswith('.xbe'):
		xbe			=	open(FileName,'rb')
		# Get XbeId Data #
		xbe.seek(0x104)
		tLoadAddr	=	xbe.read(4)
		xbe.seek(0x118)
		tCertLoc	=	xbe.read(4)
		LoadAddr	=	struct.unpack('L',tLoadAddr)
		CertLoc		=	struct.unpack('L',tCertLoc)
		CertBase	=	CertLoc[0] - LoadAddr[0]
		CertBase	+=	8
		IdStart		=	xbe.seek(CertBase)
		tIdData		=	xbe.read(4)
		IdData		=	struct.unpack('L',tIdData)
		# Get Xbe Title #
		XbeTitle	=	''
		for dta in struct.unpack(operator.repeat('H',40),xbe.read(0x0050)):
			try		:
				if dta != 00:	XbeTitle += str(unichr(dta))
			except	:	pass
		XbeDta		= str( str(XbeTitle) + '|' + str(hex(IdData[0])[2:10]).lower().zfill(8) )
		xbe.close()
	return XbeDta
def Get_Title_Letter(Title_Letter):
	Xbox_Thumb_Folder = {}
	Title_Letter = Title_Letter.lower().lstrip(' ')
	if Title_Letter.startswith("#") or Title_Letter.startswith("'") or Title_Letter.startswith("0") or Title_Letter.startswith("1") or Title_Letter.startswith("2") or Title_Letter.startswith("3") or Title_Letter.startswith("4") or Title_Letter.startswith("5") or Title_Letter.startswith("6") or Title_Letter.startswith("7") or Title_Letter.startswith("8") or Title_Letter.startswith("9"): Xbox_Thumb_Folder = "#"
	if Title_Letter.startswith("a"): Xbox_Thumb_Folder = "A"
	if Title_Letter.startswith("b"): Xbox_Thumb_Folder = "B"
	if Title_Letter.startswith("c"): Xbox_Thumb_Folder = "C"
	if Title_Letter.startswith("d"): Xbox_Thumb_Folder = "D"
	if Title_Letter.startswith("e"): Xbox_Thumb_Folder = "E"
	if Title_Letter.startswith("f"): Xbox_Thumb_Folder = "F"
	if Title_Letter.startswith("g"): Xbox_Thumb_Folder = "G"
	if Title_Letter.startswith("h"): Xbox_Thumb_Folder = "H"
	if Title_Letter.startswith("i"): Xbox_Thumb_Folder = "I"
	if Title_Letter.startswith("j"): Xbox_Thumb_Folder = "J"
	if Title_Letter.startswith("k"): Xbox_Thumb_Folder = "K"
	if Title_Letter.startswith("l"): Xbox_Thumb_Folder = "L"
	if Title_Letter.startswith("m"): Xbox_Thumb_Folder = "M"
	if Title_Letter.startswith("n"): Xbox_Thumb_Folder = "N"
	if Title_Letter.startswith("o"): Xbox_Thumb_Folder = "O"
	if Title_Letter.startswith("p"): Xbox_Thumb_Folder = "P"
	if Title_Letter.startswith("q"): Xbox_Thumb_Folder = "Q"
	if Title_Letter.startswith("r"): Xbox_Thumb_Folder = "R"
	if Title_Letter.startswith("s"): Xbox_Thumb_Folder = "S"
	if Title_Letter.startswith("t"): Xbox_Thumb_Folder = "T"
	if Title_Letter.startswith("u"): Xbox_Thumb_Folder = "U"
	if Title_Letter.startswith("v"): Xbox_Thumb_Folder = "V"
	if Title_Letter.startswith("w"): Xbox_Thumb_Folder = "W"
	if Title_Letter.startswith("x"): Xbox_Thumb_Folder = "X"
	if Title_Letter.startswith("y"): Xbox_Thumb_Folder = "Y"
	if Title_Letter.startswith("z"): Xbox_Thumb_Folder = "Z"
	return Xbox_Thumb_Folder
def Main_Code():
	## These are outside the loop so they don't reset every time.
	## Set the dialog create & found roms var.
	CreateDialog = 1 
	Found_Roms = 0
	intialrun = 0
	Use_NoIntroNames = 0
	_Resources = 0
	Allow_Xbox_Overwrite = 0
	## Check if _emulators directory is selected instead of the emulator its self.
	if os.path.isdir( Emulator_Folder_Path ):
		## Parse all folder in the Emulators_Path	
		if not os.path.isdir( os.path.join( Emulator_Folder_Path, "xbox" ) ): os.makedirs( os.path.join( Emulator_Folder_Path, "xbox" ) )
		for Emu_Folder in sorted( os.listdir( Emulator_Folder_Path ) ):
			## Set a load of variable.
			CountList = 0; JumpList = 0; Jump_Counter = 8000
			Starts_with_0 = 0; Starts_with_A = 0; Starts_with_B = 0; Starts_with_C = 0; Starts_with_D = 0; Starts_with_E = 0; Starts_with_F = 0; Starts_with_G = 0; Starts_with_H = 0; Starts_with_I = 0; Starts_with_J = 0; Starts_with_K = 0; Starts_with_L = 0; Starts_with_M = 0; Starts_with_N = 0; Starts_with_O = 0; Starts_with_P = 0; Starts_with_Q = 0; Starts_with_R = 0; Starts_with_S = 0; Starts_with_T = 0; Starts_with_U = 0; Starts_with_V = 0; Starts_with_W = 0; Starts_with_X = 0; Starts_with_Y = 0; Starts_with_Z = 0;
			Parse_CUE_CCD_ISO_File = 0; Parse_CUE_ZIP_ISO_ADF_File = 0; Parse_ISO_BIN_IMG_File = 0; Parse_CUE_File = 0; Parse_CCD_File = 0; Parse_ISO_File = 0; Parse_FBL_TXT = 0; Parse_Xbox_Games = 0; Parse_N64_TXT = 0; N64ID = "0"; FBA_Rom_Name = ""; Change_FBL_Rom_Path = 0; Change_Mame_Rom_Path = 0; Change_N64_Rom_Path = 0; Change_NeoGeoCD_Rom_Path = 0;
			RomListCount = 0; RenameCount = 0; ArtworkCount = 0; ZipCount = 0;
			Write_List_File = 1
			Emu_XBE = "default.xbe"
			Game_Directories = [ "E:\\Games\\", "F:\\Games\\", "G:\\Games\\", "E:\\Games1\\", "F:\\Games1\\", "G:\\Games1\\" ]
			if ManualScan:
				Select_Emu_Folder = dialog.select( "SELECT A SYSTEM",sorted( os.listdir( Emulator_Folder_Path ) ) )
				if Select_Emu_Folder == -1:	return
				## Set Emulators and Roms folder paths.
				Emu_Path = os.path.join( Emulator_Folder_Path, sorted( os.listdir( Emulator_Folder_Path ) )[Select_Emu_Folder] )
				Emu_Name = os.path.split(Emu_Path)[1]
				Roms_Folder = os.path.join( Roms_Folder_Path, sorted( os.listdir( Emulator_Folder_Path ) )[Select_Emu_Folder] )
				## Convert Q:\\ to a direct path.
				if Emu_Path.startswith("Q:\\"): Emu_Path = Emu_Path.replace( "Q:\\", Root_Directory )
				## Check for a default .xbe in the emulator path you selected.
				if os.path.isfile( os.path.join( Emu_Path, "default.xbe" ) ) or Emu_Name == "xbox":
					pass
				else:
					dialog.ok("ERROR","","No default.xbe found in this directory")
					return Main_Code()
			else:
				## Set emu_path/name variable for autoscan mode.
				Emu_Path = os.path.join( Emulator_Folder_Path, Emu_Folder )
				Emu_Name = os.path.split(Emu_Path)[1]
				Roms_Folder	= os.path.join( Roms_Folder_Path,Emu_Name )
			if intialrun == 0:
				intialrun = 1
				## Ask the user if they want to use the internal names from the synopsis files and if they want to use _Resources folders for Xbox game artwork.
				if not Emu_Name == "xbox" and dialog.yesno("ROM DISPLAY NAMES","Do you want to use the names stored in the","synopsis files instead of the roms filenames?","If you select no, rom filenames will be used.") == 1:
					Use_NoIntroNames = 1
				if Emu_Name == "xbox" or Full_Scan == "auto":
					if dialog.yesno("XBOX ARTWORK","Do you want to use _resources folders for art?","If you select no, covers will display your default.tbn","or an image will be extracted from the game xbe."): _Resources = 1
					if dialog.yesno("UPDATE XBOX ARTWORK?","Selecting yes, will update any artwork that","differs from the currently cached artwork.","Selecting no will add only new artwork."): Allow_Xbox_Overwrite = 1
			## Set tbn and gameslist path variable.
			Media_Path			= os.path.join( Media_Folder_Path, Emu_Name )
			Games_List_Path		= os.path.join( Root_Directory, '.emustation\\gamelists', Emu_Name )
			## If genesis emulator is selected or found use megadrive synopsis files.
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
			if not Emu_Name == "xbox":
				if not os.path.isdir( os.path.join( Media_Path,'boxart' ) ): os.makedirs( os.path.join( Media_Path,'boxart' ) )
				if not os.path.isdir( os.path.join( Media_Path,'boxart3d' ) ): os.makedirs( os.path.join( Media_Path,'boxart3d' ) )
				if not os.path.isdir( os.path.join( Media_Path,'logo' ) ): os.makedirs( os.path.join( Media_Path,'logo' ) )
				if not os.path.isdir( os.path.join( Media_Path,'mix' ) ): os.makedirs( os.path.join( Media_Path,'mix' ) )
				if not os.path.isdir( os.path.join( Media_Path,'videos' ) ): os.makedirs( os.path.join( Media_Path,'videos' ) )
				if not os.path.isdir( os.path.join( Media_Path,'screenshots' ) ): os.makedirs( os.path.join( Media_Path,'screenshots' ) )
			## Check to see if the emulator is one of the below so I can change it rom type or path.
			if Emu_Name == "fba" or Emu_Name == "fbl" or Emu_Name == "fblc" or Emu_Name == "fbaxxx":
				Change_FBL_Rom_Path = 1
				Parse_FBL_TXT = 1
			elif Emu_Name == "amiga":
				Parse_CUE_ZIP_ISO_ADF_File = 1
			elif Emu_Name == "atarijaguar":
				Roms_Folder	= os.path.join( Emu_Path, 'roms' )
			elif Emu_Name == "mame":
				Change_Mame_Rom_Path = 1
			elif Emu_Name == "n64":
				Parse_N64_TXT = 1
				Change_N64_Rom_Path = 1
			elif Emu_Name == "neogeocd":
				Change_NeoGeoCD_Rom_Path = 1
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
			elif Emu_Name == "xbox":
				Parse_Xbox_Games = 1
				Xbox_Games_Folder = "Z:\\temp\\xbox game list"
				Roms_Folder = Xbox_Games_Folder
			else:
				pass
			if Parse_CUE_File: Rom_Type_Total = (len(glob.glob1(Roms_Folder,'*.cue')))
			if Parse_CUE_CCD_ISO_File: Rom_Type_Total = (len(glob.glob1(Roms_Folder,'*.cue')) + len(glob.glob1(Roms_Folder,'*.ccd')) + len(glob.glob1(Roms_Folder,'*.iso')))
			if Parse_CUE_ZIP_ISO_ADF_File: Rom_Type_Total = (len(glob.glob1(Roms_Folder,'*.cue')) + len(glob.glob1(Roms_Folder,'*.zip')) +  + len(glob.glob1(Roms_Folder,'*.adf')) + len(glob.glob1(Roms_Folder,'*.iso')))
			## Convert Q:\\ to a direct path
			if Roms_Folder.startswith("Q:\\"): Roms_Folder = Roms_Folder.replace( "Q:\\", Root_Directory )
			## Check to see if the emulators = rom folder is empty and exit if it is.
			## below slower than just doing what I do below.
			# if len(os.walk(Roms_Folder).next()[2]) > 0:
			if len(os.listdir( Roms_Folder )) > 0 or Emu_Name == "xbox":
				## Check to see if vars are the value I need and create a new dialog.
				if CreateDialog == 1:
					#CreateDialog = 0
					if ManualScan:
						pDialog.create( "MANUAL SCAN MODE","Initializing" )
					else:
						pDialog.create( "AUTO SCAN MODE","Initializing" )
					pDialog.update(0,'Creating [B][UPPERCASE]' + Emu_Name + '[/UPPERCASE][/B] Rom list','','This can take some time, please be patient.')
				## Checking for .png artwork files and changing them to .jpg.
				if not Emu_Name == "xbox":
					for dirName, subdirList, fileList in os.walk( Media_Path ):
						pDialog.update(0,'Checking [B]' + Emu_Name + '[/B] artwork.','','This can take some time, please be patient.' )
						for PNGs in fileList:
							if PNGs.endswith('.png'):
								if os.path.isfile( os.path.join( dirName,PNGs[:-4] + '.jpg' ) ):
									os.remove( os.path.join( dirName,PNGs[:-4] + '.jpg' ) )
								os.rename( os.path.join( dirName,PNGs ),os.path.join( dirName,PNGs[:-4] + '.jpg' ))
								pDialog.update((ArtworkCount * 100) / len( os.listdir( Media_Path ) ),'Checking [B]' + Emu_Name + '[/B] artwork file extensions.','[B]' + PNGs + '[/B]' ,'This can take some time, please be patient.' )
								ArtworkCount = ArtworkCount + 1
				## Checking filenames case and not leading with capital renaming it to do so.
				if not Emu_Name == "xbox" and not Emu_Name == "fba" and not Emu_Name == "fbl" and not Emu_Name == "fblc" and not Emu_Name == "fbaxxx" and not Emu_Name == "mame":
					pDialog.update(0,'Checking [B]' + Emu_Name + '[/B] Rom filename casing.','','This can take some time, please be patient.' )
					for Roms in sorted( os.listdir( Roms_Folder ) ):
						Items_Full_Path = os.path.join( Roms_Folder, Roms )
						if Items_Full_Path != os.path.join( Roms_Folder, Roms.lower() ):
						#if Items_Full_Path != os.path.join( Roms_Folder, Roms.capitalize() ):
							tempname = Items_Full_Path[:-1]
							if not os.path.isfile( tempname ):
								os.rename( Items_Full_Path,	 tempname )
								os.rename( tempname,  os.path.join( Roms_Folder, Roms.lower() ) )
								#os.rename( tempname,  os.path.join( Roms_Folder, Roms.capitalize() ) )
								pDialog.update((RenameCount * 100) / len( os.listdir( Roms_Folder ) ),'Lower-casing rom names.','[B]' + Roms + '[/B]' ,'This can take some time, please be patient.' )
						RenameCount = RenameCount + 1
				## Setting a var again :/
				Found_Roms = 1
				## Check if fbl was found and change its rom path to where the roms are located.
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
				## Check if mame was found and change it rom path to where the roms are located.
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
				## Creating Xbox game list so its in alphabetical order.
				if Parse_Xbox_Games == 1:
					if os.path.isdir( Roms_Folder ): shutil.rmtree( Roms_Folder )
					if not os.path.isdir( Roms_Folder ): os.makedirs( Roms_Folder )
					previouse_title = ""
					dup_count = 1
					altnumb = 1
					for Game_Dirs in Game_Directories:
						if os.path.isdir( Game_Dirs ):
							for Item in sorted([f for f in os.listdir( Game_Dirs )]):
								pDialog.update(0,'Sorting List Order & Artwork For [B][UPPERCASE]' + Emu_Name + '[/UPPERCASE][/B] Games','[B][UPPERCASE]' + Item + '[/UPPERCASE][/B]','This can take some time, please be patient.')
								if os.path.isdir(os.path.join( Game_Dirs, Item)):
									Game_Directory = os.path.join( Game_Dirs, Item )
									if os.path.isfile( os.path.join( Game_Directory, "game.xbe" ) ):
										XBEFile = os.path.join( Game_Directory, "game.xbe" )
									elif os.path.isfile( os.path.join( Game_Directory, "tdgame.xbe" ) ):
										XBEFile = os.path.join( Game_Directory, "tdgame.xbe" )
									else:
										XBEFile = os.path.join( Game_Directory, "default.xbe" )
									if os.path.isfile( XBEFile ):
										_Resources_PosterFile = os.path.join( Game_Directory, "_resources\\artwork\\poster.jpg" )
										_Resources_Poster3dFile = os.path.join( Game_Directory, "_resources\\artwork\\dual3d.png" )
										_Resources_CDFile = os.path.join( Game_Directory, "_resources\\artwork\\cd.png" )
										_Resources_CDPosterFile = os.path.join( Game_Directory, "_resources\\artwork\\cdposter.png" )
										_Resources_IconFile = os.path.join( Game_Directory, "_resources\\artwork\\icon.png" )
										_Resources_ThumbFile = os.path.join( Game_Directory, "_resources\\artwork\\thumb.jpg" )
										_Resources_FanartFile = os.path.join( Game_Directory, "_resources\\artwork\\fanart.jpg" )
										_Resources_BannerFile = os.path.join( Game_Directory, "_resources\\artwork\\banner.png" )
										_Resources_OpenCaseFile = os.path.join( Game_Directory, "_resources\\artwork\\opencase.png" )
										_Resources_Screenshot = os.path.join( Game_Directory, "_resources\\screenshots\\screenshot-1.jpg" )
										_Resources_Synopsis = os.path.join( Game_Directory, "_resources\\default.xml" )
										TBNFile = os.path.join( Game_Directory, "default.tbn" )
										FanartFile = os.path.join( Game_Directory, "fanart.jpg" )
										Emu_XBE = XBEFile
										# this is set to the default.xbe because some of the main game xbe files don't have names. Some games use default.xbe as the loader to game.xbe or tdgame.xbe
										XBEInfo = Extract_XbeInfo( os.path.join( Game_Directory, "default.xbe" ) ).split('|')
										XBETitle =  XBEInfo[0].lstrip(' ')
										XBEInfo = Extract_XbeInfo( XBEFile ).split('|')
										XBEID = XBEInfo[1]
										# use the folder name if the xbe title is corrupt or not there.
										if XBETitle == "": XBETitle = Item.lstrip(' ')
										XBETitle_List = xbmc.makeLegalFilename( Xbox_Games_Folder + '\\' + XBETitle.lower().replace('/','').replace('\\','').replace(' ','') )
										# Get first letter of the games titleid and set a variable
										Xbox_Thumb_Folder = Get_Title_Letter( XBETitle )
										# Create folder structure for xbox games to speed up loading of images
										if not os.path.isdir( os.path.join( Media_Path,'boxart',Xbox_Thumb_Folder ) ): os.makedirs( os.path.join( Media_Path,'boxart',Xbox_Thumb_Folder ) )
										if not os.path.isdir( os.path.join( Media_Path,'boxart3d',Xbox_Thumb_Folder ) ): os.makedirs( os.path.join( Media_Path,'boxart3d',Xbox_Thumb_Folder ) )
										if not os.path.isdir( os.path.join( Media_Path,'disc',Xbox_Thumb_Folder ) ): os.makedirs( os.path.join( Media_Path,'disc',Xbox_Thumb_Folder ) )
										if not os.path.isdir( os.path.join( Media_Path,'cdposter',Xbox_Thumb_Folder ) ): os.makedirs( os.path.join( Media_Path,'cdposter',Xbox_Thumb_Folder ) )
										if not os.path.isdir( os.path.join( Media_Path,'dual',Xbox_Thumb_Folder ) ): os.makedirs( os.path.join( Media_Path,'dual',Xbox_Thumb_Folder ) )
										if not os.path.isdir( os.path.join( Media_Path,'fanart',Xbox_Thumb_Folder ) ): os.makedirs( os.path.join( Media_Path,'fanart',Xbox_Thumb_Folder ) )
										if not os.path.isdir( os.path.join( Media_Path,'opencase',Xbox_Thumb_Folder ) ): os.makedirs( os.path.join( Media_Path,'opencase',Xbox_Thumb_Folder ) )
										if not os.path.isdir( os.path.join( Media_Path,'screenshots',Xbox_Thumb_Folder ) ): os.makedirs( os.path.join( Media_Path,'screenshots',Xbox_Thumb_Folder ) )
										if not os.path.isdir( os.path.join( Media_Path,'videos',Xbox_Thumb_Folder ) ): os.makedirs( os.path.join( Media_Path,'videos',Xbox_Thumb_Folder ) )
										if os.path.isfile( os.path.join( Roms_Folder, 'idlist.xml' ) ):
											if str(XBEID) in open( os.path.join( Roms_Folder, 'idlist.xml' ) ).read():
												XBEID = str(XBEID)+"_"+str(dup_count)
												dup_count = dup_count+1
										if _Resources == 0:
											if os.path.isfile( TBNFile ):
												# Default.tbn
												if os.path.isfile( os.path.join( Media_Folder_Path + "xbox\\boxart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  ) ):
													if Allow_Xbox_Overwrite == 1 and not filecmp.cmp( os.path.join( Media_Folder_Path + "xbox\\boxart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	) , TBNFile, shallow=0 ):
														shutil.copy2( TBNFile, os.path.join( Media_Folder_Path + "xbox\\boxart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  ) )
												else:
													shutil.copy2( TBNFile, os.path.join( Media_Folder_Path + "xbox\\boxart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  ) )
											else:
												# TITLEIMAGE
												try:
													XBE( XBEFile ).Get_title_image().Write_PNG( os.path.join( Media_Folder_Path + "xbox\\boxart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	) )
												except:
													pass
											if os.path.isfile( os.path.join( Media_Folder_Path + "xbox\\fanart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  ) ):
												if os.path.isfile( FanartFile ):
													if Allow_Xbox_Overwrite == 1 and not filecmp.cmp( os.path.join( Media_Folder_Path + "xbox\\fanart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	) , FanartFile, shallow=0 ):
														shutil.copy2( FanartFile, Media_Folder_Path + "xbox\\fanart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	)
											else:
												if os.path.isfile( FanartFile ):
													shutil.copy2( FanartFile, Media_Folder_Path + "xbox\\fanart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	)
										else:
											# _Resources folder structure
											# Poster
											if os.path.isfile( os.path.join( Media_Folder_Path + "xbox\\boxart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  ) ):
												#print XBEID + " baxart already present"
												if os.path.isfile( _Resources_PosterFile ):
													if Allow_Xbox_Overwrite == 1 and not filecmp.cmp( os.path.join( Media_Folder_Path + "xbox\\boxart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	), _Resources_PosterFile, shallow=0 ):
														if os.path.isfile( _Resources_PosterFile ):
															shutil.copy2( _Resources_PosterFile, Media_Folder_Path + "xbox\\boxart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  )
											else:
												if os.path.isfile( _Resources_PosterFile ):
													shutil.copy2( _Resources_PosterFile, Media_Folder_Path + "xbox\\boxart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  )
												# Default.tbn
												elif os.path.isfile( TBNFile ):
													shutil.copy2( TBNFile, Media_Folder_Path + "xbox\\boxart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	 )
												else:												
													# TITLEIMAGE
													try:
														XBE( XBEFile ).Get_title_image().Write_PNG( os.path.join( Media_Folder_Path + "xbox\\boxart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	) )
													except:
														pass
											# 3D Boxart
											if os.path.isfile( os.path.join( Media_Folder_Path + "xbox\\boxart3d\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	 ) ):
												#print XBEID + " 3d boxart already present"
												if os.path.isfile( _Resources_IconFile ):
													if Allow_Xbox_Overwrite == 1 and not filecmp.cmp( os.path.join( Media_Folder_Path + "xbox\\boxart3d\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  ), _Resources_IconFile, shallow=0 ):
														if os.path.isfile( _Resources_IconFile ):
															shutil.copy2( _Resources_IconFile, Media_Folder_Path + "xbox\\boxart3d\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  )
											else:
												if os.path.isfile( _Resources_IconFile ):
													shutil.copy2( _Resources_IconFile, Media_Folder_Path + "xbox\\boxart3d\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  )
											# CD
											if os.path.isfile( os.path.join( Media_Folder_Path + "xbox\\disc\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	 ) ):
												#print XBEID + " cd already present"
												if os.path.isfile( _Resources_CDFile ):
													if Allow_Xbox_Overwrite == 1 and not filecmp.cmp( os.path.join( Media_Folder_Path + "xbox\\disc\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  ), _Resources_CDFile, shallow=0 ):
														if os.path.isfile( _Resources_CDFile ):
															shutil.copy2( _Resources_CDFile, Media_Folder_Path + "xbox\\disc\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	 )
											else:
												if os.path.isfile( _Resources_CDFile ):
													shutil.copy2( _Resources_CDFile, Media_Folder_Path + "xbox\\disc\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	 )
											# Disc case
											if os.path.isfile( os.path.join( Media_Folder_Path + "xbox\\cdposter\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	 ) ):
												#print XBEID + " disc case already present"
												if os.path.isfile( _Resources_CDPosterFile ):
													if Allow_Xbox_Overwrite == 1 and not filecmp.cmp( os.path.join( Media_Folder_Path + "xbox\\cdposter\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  ), _Resources_CDPosterFile, shallow=0 ):
														if os.path.isfile( _Resources_CDPosterFile ):
															shutil.copy2( _Resources_CDPosterFile, Media_Folder_Path + "xbox\\cdposter\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  )
											else:
												if os.path.isfile( _Resources_CDPosterFile ):
													shutil.copy2( _Resources_CDPosterFile, Media_Folder_Path + "xbox\\cdposter\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  )
											# Dual 3D
											if os.path.isfile( os.path.join( Media_Folder_Path + "xbox\\dual\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	 ) ):
												#print XBEID + " dual 3d already present"
												if os.path.isfile( _Resources_Poster3dFile ):
													if Allow_Xbox_Overwrite == 1 and not filecmp.cmp( os.path.join( Media_Folder_Path + "xbox\\dual\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  ), _Resources_Poster3dFile, shallow=0 ):
														if os.path.isfile( _Resources_Poster3dFile ):
															shutil.copy2( _Resources_Poster3dFile, Media_Folder_Path + "xbox\\dual\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  )
											else:
												if os.path.isfile( _Resources_Poster3dFile ):
													shutil.copy2( _Resources_Poster3dFile, Media_Folder_Path + "xbox\\dual\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  )
											# Open Case
											if os.path.isfile( os.path.join( Media_Folder_Path + "xbox\\opencase\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	 ) ):
												#print XBEID + " mix already present"
												if os.path.isfile( _Resources_OpenCaseFile ):
													if Allow_Xbox_Overwrite == 1 and not filecmp.cmp( os.path.join( Media_Folder_Path + "xbox\\opencase\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  ), _Resources_OpenCaseFile, shallow=0 ):
														if os.path.isfile( _Resources_OpenCaseFile ):
															shutil.copy2( _Resources_OpenCaseFile, Media_Folder_Path + "xbox\\opencase\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  )
											else:
												if os.path.isfile( _Resources_OpenCaseFile ):
													shutil.copy2( _Resources_OpenCaseFile, Media_Folder_Path + "xbox\\opencase\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  )
											# Fanart
											if os.path.isfile( os.path.join( Media_Folder_Path + "xbox\\fanart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  ) ):
												#print XBEID + " fanart already present"
												if os.path.isfile( _Resources_FanartFile ):
													if Allow_Xbox_Overwrite == 1 and not filecmp.cmp( os.path.join( Media_Folder_Path + "xbox\\fanart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	), _Resources_FanartFile, shallow=0 ):
														if os.path.isfile( _Resources_FanartFile ):
															shutil.copy2( _Resources_FanartFile, Media_Folder_Path + "xbox\\fanart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  )
														elif os.path.isfile( FanartFile ):
															shutil.copy2( FanartFile, Media_Folder_Path + "xbox\\fanart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	)
											else:
												if os.path.isfile( _Resources_FanartFile ):
													shutil.copy2( _Resources_FanartFile, Media_Folder_Path + "xbox\\fanart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"  )
												elif os.path.isfile( FanartFile ):
													shutil.copy2( FanartFile, Media_Folder_Path + "xbox\\fanart\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	)
											# Screenshots
											if os.path.isfile( os.path.join( Media_Folder_Path + "xbox\\screenshots\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	) ):
												#print XBEID + " screenshots already present"
												if os.path.isfile( _Resources_Screenshot ):
													if Allow_Xbox_Overwrite == 1 and not filecmp.cmp( os.path.join( Media_Folder_Path + "xbox\\screenshots\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	 ), _Resources_Screenshot, shallow=0 ):
														if os.path.isfile( _Resources_Screenshot ):
															shutil.copy2( _Resources_Screenshot, Media_Folder_Path + "xbox\\screenshots\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	)
											else:
												if os.path.isfile( _Resources_Screenshot ):
													shutil.copy2( _Resources_Screenshot, Media_Folder_Path + "xbox\\screenshots\\" + Xbox_Thumb_Folder + '\\' + XBEID + ".jpg"	)
											# Videos
											for Files in glob.glob( os.path.join( Game_Directory, "_resources\\media\\*.*") ):
												if os.path.isfile( os.path.join( Media_Folder_Path + "xbox\\videos\\" + Xbox_Thumb_Folder + '\\' + XBEID + os.path.splitext(Files)[1] ) ):
													#print XBEID + " videos already present"
													if os.path.isfile( Files ):
														if Allow_Xbox_Overwrite == 1 and not filecmp.cmp( os.path.join( Media_Folder_Path + "xbox\\videos\\" + Xbox_Thumb_Folder + '\\' + XBEID + os.path.splitext(Files)[1] ), Files, shallow=0 ):
															if os.path.isfile( Files ):
																shutil.copy2( Files, Media_Folder_Path + "xbox\\videos\\" + Xbox_Thumb_Folder + '\\' + XBEID + os.path.splitext(Files)[1]  )
												else:
													if os.path.isfile( Files ):
														shutil.copy2( Files, Media_Folder_Path + "xbox\\videos\\" + Xbox_Thumb_Folder + '\\' + XBEID + os.path.splitext(Files)[1] )
										with open( os.path.join( Roms_Folder, 'idlist.xml' ), "a") as idlistfile:
											idlistoutput = str(XBEID)+"\n"
											idlistfile.write( idlistoutput )
										if previouse_title == XBETitle_List:
											with open( XBETitle_List[:56] + "_alt"+str(altnumb)+".xbg","w") as ouput:
												ouput.write(XBETitle + " ( Duplicate Name " + str(altnumb) + " )\n")
												ouput.write(Emu_XBE + "\n")
												ouput.write(Xbox_Thumb_Folder + "\n")
												ouput.write(XBEID)
											altnumb = altnumb+1
										else:
											with open( XBETitle_List[:61] + ".xbg","w") as ouput:
												ouput.write(XBETitle + "\n")
												ouput.write(Emu_XBE + "\n")
												ouput.write(Xbox_Thumb_Folder + "\n")
												ouput.write(XBEID)
										previouse_title = XBETitle_List
				## Extracting the rom name files from the zip.
				if Parse_FBL_TXT == 1:
					if os.path.isfile( os.path.join( Emu_Path, "info\\FBL Rom Names.zip" ) ):
						with zipfile.ZipFile( os.path.join( Emu_Path, "info\\FBL Rom Names.zip" ) ) as zip:
							if not os.path.isdir( os.path.join( Emu_Path, "info\\rom names" ) ): os.makedirs( os.path.join( Emu_Path, "info\\rom names" ) )
							if ZipCount == 0:
								#pDialog.create( "EXTRACTING ZIP","","Please wait..." )
								Total_TXT_Files = len( zip.namelist() ) or 1
								Devide = 100.0 / Total_TXT_Files
								Percent = 0
								for item in zip.namelist():
									Percent += Devide
									pDialog.update( int( Percent ),'Extracting FBA, FBAXXX, FBL or FBLC rom names','This only happens once per update','' )
									zip.extract( item, os.path.join( Emu_Path, "info\\rom names\\" ) )
								ZipCount = 1
						os.remove( os.path.join( Emu_Path, "info\\FBL Rom Names.zip" ) )
					Roms_Folder = os.path.join( Emu_Path, "info\\rom names" )
					## Used to name the rom name files so I can sort them by alphabetical order properly. ( this is only used by me ) 
					# for files in sorted( os.listdir( os.path.join( Emu_Path, "info\\rom names" ) ) ):
						# try:
							# with open( os.path.join( Emu_Path, "info\\rom names", files[:-3] + 'txt' ), 'r') as txt:
								# FBA_Rom_Name_Full = txt.readline()[:-2]
								# FBA_Rom_Name = FBA_Rom_Name_Full[:20]
								# FBA_Rom_Name = FBA_Rom_Name.replace( ',','' ); FBA_Rom_Name = FBA_Rom_Name.replace( ':','' ); FBA_Rom_Name = FBA_Rom_Name.replace( ';','' ); FBA_Rom_Name = FBA_Rom_Name.replace( '/','' ); FBA_Rom_Name = FBA_Rom_Name.replace( '?','' ); FBA_Rom_Name = FBA_Rom_Name.replace( '+','' ); FBA_Rom_Name = FBA_Rom_Name.replace( '*','' ); FBA_Rom_Name = FBA_Rom_Name.replace( 'amp','' ); FBA_Rom_Name = FBA_Rom_Name.replace( ' ','' );
								# FBA_Rom_Name = FBA_Rom_Name.lower()
								# for line in txt: FBA_Rom_System_Full = '\n'+line
							# if not os.path.isdir( "F:\\rom names" ): os.makedirs( "F:\\rom names" )
							# with open( os.path.join( "F:\\rom names", FBA_Rom_Name + '--' + files[:-3] + 'zip' ), 'w') as txt:
								# txt.write( FBA_Rom_Name_Full.lower() )
								# txt.write( FBA_Rom_System_Full.lower() )
							# pDialog.update((CountList * 100) / len(os.listdir( os.path.join( Emu_Path, 'info\\rom names' ) ) ),'Processing Rom name files',files,'This can take some time, please be patient.' )
							# CountList = CountList + 1
						# except: pass
					# return
				## Check for previous layout xml and if it exists remove it.
				if os.path.isdir( Games_List_Path ): shutil.rmtree( Games_List_Path )
				if not os.path.isdir( Games_List_Path ): os.makedirs( Games_List_Path )
				if Parse_Xbox_Games == 1 and os.path.isfile( os.path.join( Media_Folder_Path, "xbox\\GameNames.txt" ) ): os.remove( os.path.join( Media_Folder_Path, "xbox\\GameNames.txt" ) )
				## Write new gamelist xml header.
				with open( os.path.join( Games_List_Path, 'gamelist.xml' ), "wb") as outputmenufile:
					WriteMenuFile = menu_entry_header
					outputmenufile.write( WriteMenuFile )
				## Listing the content of the roms folder for parsing.
				for Items in sorted([f for f in os.listdir( Roms_Folder )]):
					## Checking the file I find, extension against my table.
					if Items.lower().endswith(tuple(Extensions)) or Emu_Name == "neogeocd":
						## More vars being set.
						Rom_Name = Items.lower()
						Rom_Name_noext = Rom_Name[:-4]
						if Emu_Name == "xbox":
							with open(os.path.join( Xbox_Games_Folder, Rom_Name ), "r") as input:
								Rom_Name_noext = input.readline()
								Emu_XBE = input.readline()
								skip = input.readline()
								XBE_ID = input.readline()
						JumpList_Name = Rom_Name_noext.lower()
						if not xbmc.getCondVisibility( 'Skin.String(' + Emu_Name + '_artworkfolder)' ): xbmc.executebuiltin('Skin.SetString(' + Emu_Name + '_artworkfolder,boxart)')
						Thumbnail = Rom_Name_noext + '.jpg'
						## Check if fba was found and parse the name text files to get the correct rom names and system types for the list.
						if Parse_FBL_TXT == 1:
							Rom_Name_Full = Rom_Name
							Rom_Name_Beg = Rom_Name.split('--', 1)[0]
							Rom_Name = Rom_Name.split('--', 1)[1]
							Rom_Name_noext = Rom_Name[:-4]
							Thumbnail = Rom_Name_noext + '.jpg'
							if os.path.isfile( os.path.join( Roms_Folder_Path, Emu_Name, Rom_Name ) ) and os.path.isfile( os.path.join( Emu_Path, "info\\rom names", Rom_Name_Beg + '--' + Rom_Name ) ):
								with open( os.path.join( Emu_Path, "info\\rom names", Rom_Name_Beg + '--' + Rom_Name ), 'r') as txt:
									FBA_Rom_Name = txt.readline()[:-1]
									#FBA_Rom_Name = FBA_Rom_Name.split('(', 1)[0]
									#FBA_Rom_Name = FBA_Rom_Name.split('/', 1)[0]
									for line in txt:
										System_Name = line.lower()[:-2]
										Emu_XBE = "default.xbe"
										if System_Name == "psikyo 68ec020" or System_Name == "ps3-v1" or System_Name == "ps4" or System_Name == "ps5" or System_Name == "fg-3" or System_Name == "tecmo" or System_Name == "polygamemaster" or System_Name == "polygamemaster based" or System_Name == "ps5v2": Emu_XBE = "psykio.xbe"
										if System_Name == "neo geo aes" or System_Name == "neo geo mvs": Emu_XBE = "neogeocps2.xbe"
										if System_Name == "cps2": Emu_XBE = "neogeocps2.xbe"
										if System_Name == "cave": Emu_XBE = "cave.xbe"
										if System_Name == "toaplan gp9001 based" or System_Name == "toaplan bcu-2 / fcu-2 based" or System_Name == "dual toaplan gp9001 based": Emu_XBE = "toaplan.xbe" 
										if System_Name == "to": Emu_XBE = "taito.xbe"
										if System_Name == "sk" or System_Name == "cps-3" or System_Name == "nmk16" or System_Name == "ssv" or System_Name == "wr" or System_Name == "th2" or System_Name == "wr2" or System_Name == "fg-2" or System_Name == "mega system 1" or System_Name == "sf" or System_Name == "kaneko 16-bit": Emu_XBE = "new.xbe"
										if System_Name == "de": Emu_XBE = "dataeast.xbe"
										if System_Name == "kn": Emu_XBE = "konami.xbe"
										if System_Name == "system 16a" or System_Name == "system 16b" or System_Name == "system 18" or System_Name == "x-board" or System_Name == "y-board" or System_Name == "out run" or System_Name == "hang-on": Emu_XBE = "sega.xbe"
										if System_Name == "jc" or System_Name == "unico" or System_Name == "ss" or System_Name == "f1gp" or System_Name == "newer seta" or System_Name == "pwr": Emu_XBE = "xtra.xbe"
										if System_Name == "im": Emu_XBE = "irem.xbe"
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
						## Check if n64 was found and parse the names from surreal.ini if the roms match.
						if Parse_N64_TXT == 1:
							if os.path.isfile(os.path.join( Emu_Path, 'surreal.ini' )):
								if Change_N64_Rom_Path == 1:
									if os.path.isdir( 'E:\\TDATA\\64ce64ce' ): shutil.rmtree( 'E:\\TDATA\\64ce64ce' )
									for line in fileinput.input( os.path.join( Emu_Path, 'surreal.ini' ), inplace=1):
										if 'Rom Path=' in line:
											line = line = 'Rom Path=' + Roms_Folder + '\n'
										print line,
									os.makedirs( 'E:\\TDATA\\64ce64ce' )
									with open( os.path.join( 'E:\\TDATA\\64ce64ce\\surreal-ce.ini' ), "w") as outputn64file:
										WriteN64File = n64_config % ( Roms_Folder )
										outputn64file.write( WriteN64File )
									Change_N64_Rom_Path = 0
									Bypass_N64_Check = 0
								## Extracting the rom names from the ini.
								N64linenumb = 1
								foundN64line = 0
								with open( os.path.join( Emu_Path, 'surreal.ini' ), 'r') as ini:
									for line in itertools.islice(ini,0,None):
										if line.lower().startswith('[dcbc50d1'): foundN64line = 1
										if foundN64line == 1:
											N64ID = str(line.lower())
											N64ID = N64ID[1:]
											N64ID1 = N64ID.split('-')[0]
											N64ID2 = N64ID.split('-')[1]
											File_Name = ini.next().replace('Game Name=','')[:-1]
											File_Name = File_Name.lower()
											if os.path.isdir( os.path.join( Emu_Path, 'media\\Cbagys3DArt' ) ):
												if File_Name == "007 goldeneye (ultrahle)720pno" or Bypass_N64_Check == 1:
													Bypass_N64_Check = 1
													if Rom_Name_noext == File_Name:
														N64_Rom_Name = ini.next().replace('Alternate Title=','')[:-1]
														N64_Rom_Name = N64_Rom_Name.split(' (', 1)[0]
														try:
															ini.next() # skip the comment line
															ini.next() # skip the blank line
														except: pass
														for N64_Thumb in os.listdir( os.path.join( Emu_Path, 'media\\Cbagys3DArt' ) ):
															N64_Thumb = N64_Thumb.lower()
															if N64ID1 in N64_Thumb or N64ID2 in N64_Thumb:
																if not os.path.isdir( os.path.join( Synopsis_Path, Emu_Name ) ): os.makedirs( os.path.join( Synopsis_Path, Emu_Name ) )
																N64_Thumb_Location = os.path.join( Emu_Path, 'media\\Cbagys3DArt', N64_Thumb )
																#shutil.copy2( N64_Thumb_Location, "E:\\1\\" )
																N64_Thumb_Destination = os.path.join( Media_Path, 'boxart', File_Name + '.jpg' )
																if os.path.isfile( N64_Thumb_Location ) and not os.path.isfile( N64_Thumb_Destination ): shutil.copy2( N64_Thumb_Location, N64_Thumb_Destination )
														for N64_Thumb in os.listdir( os.path.join( Emu_Path, 'media\\Movies' ) ):
															N64_Thumb = N64_Thumb.lower()
															if N64ID1 in N64_Thumb or N64ID2 in N64_Thumb:
																if not os.path.isdir( os.path.join( Media_Path, 'videos' ) ): os.makedirs( os.path.join( Media_Path, 'videos' ) )
																N64_Thumb_Location = os.path.join( Emu_Path, 'media\\Movies', N64_Thumb )
																N64_Thumb_Destination = os.path.join( Media_Path, 'videos', File_Name + N64_Thumb[-4:] )
																if os.path.isfile( N64_Thumb_Location ) and not os.path.isfile( N64_Thumb_Destination ): shutil.copy2( N64_Thumb_Location, N64_Thumb_Destination )
														for N64_Synopsis in os.listdir( os.path.join( Emu_Path, 'media\\synopsis' ) ):
															N64_Synopsis = N64_Synopsis.lower()
															if N64ID1 in N64_Synopsis or N64ID2 in N64_Synopsis:
																	N64_Synopsis_Location = os.path.join( Emu_Path, 'media\\synopsis', N64_Synopsis[:-3] + 'txt' )
																	#shutil.copy2( N64_Synopsis_Location, "E:\\2\\" )
																	N64_Synopsis_Destination = os.path.join( Synopsis_Path, Emu_Name, File_Name + '.txt' )
																	#if os.path.isfile( N64_Synopsis_Location ) and not os.path.isfile( N64_Synopsis_Destination ): 
																	if os.path.isfile( N64_Synopsis_Location ): 
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
													dialog.ok("ERROR","","This isn't [B]EarthWormsJames[/B][CR]N64 emulator best of compilation")
													return
											else:
												dialog.ok("ERROR","","Reinstall the [B]EarthWormsJames[/B] N64 emulator.[CR]The Cbagys3DArt folder is missing.")
												return
										else:
											ini.next()
											N64linenumb += 1
											if N64linenumb >= 30 and foundN64line == 0:
												dialog.ok("ERROR","","Surreal.ini is corrupt or not formatted correctly[CR]Recopy/Download [B]EarthWormsJames[/B] N64 emulator")
												return
							else:
								dialog.ok("ERROR","","Surreal.ini is missing from the","N64 Emulators directory")
								return
						## Change neogeocd rom path.
						if Change_NeoGeoCD_Rom_Path == 1:
							if os.path.isfile(os.path.join( Emu_Path, "path.txt" )):
								with open( os.path.join( os.path.join( Emu_Path, "path.txt" ) ), "w") as outputneogeocdfile:
									WriteneogeocdFile = "rompath " + Roms_Folder + '\\\n'
									outputneogeocdfile.write( WriteneogeocdFile )
								Change_NeoGeoCD_Rom_Path = 0
							else:
								dialog.ok("ERROR","","path.txt is missing from the","Neogeocd Emulators directory")
								return
						## Check for a synopsis zip for the current emulator.
						if ZipCount == 0:
							if os.path.isfile( Synopsis_Zip ):
									## Extracting the synopsis files from the zip.
									with zipfile.ZipFile( Synopsis_Zip ) as zip:
										if ZipCount == 0:
											#pDialog.create( "EXTRACTING ZIP","","Please wait..." )
											Total_TXT_Files = len( zip.namelist() ) or 1
											Devide = 100.0 / Total_TXT_Files
											Percent = 0
											for item in zip.namelist():
												Percent += Devide
												pDialog.update( int( Percent ),'Extracting [B][UPPERCASE]' + Emu_Name + '[/UPPERCASE][/B] Synopsis files.',item,'' )
												zip.extract( item, Synopsis_Path )
											ZipCount = 1
									os.remove( os.path.join( Synopsis_Zip ) )
						else:
							pass
						## Check for a synopsis file for the current emulator and parse it.
						Synopsis_filename = '[B]Filename:[/B][CR] ' + Rom_Name; Synopsis_release_year = '[B]Released:[/B][CR] unknown '; Synopsis_players = '[B]Players:[/B][CR] at least 1'; Synopsis_genre = '[B]Genre:[/B][CR] unknown'; Synopsis_developer = '[B]Developer:[/B][CR] unknown'; Synopsis_publisher = '[B]Publisher:[/B][CR] unknown'; ynopsis_release_year = '[B]Released:[/B][CR] unknown'
						Synopsis_filename_Set = 0; Synopsis_nointroname_Set = 0; Synopsis_rating_Set = 0; Synopsis_players_Set = 0; Synopsis_genre_Set = 0; Synopsis_developer_Set = 0; Synopsis_publisher_Set = 0; Synopsis_release_year_Set = 0
						try:
							if Emu_Name == "genesis":
								Synopsis_File = os.path.join( Synopsis_Path, "megadrive", Rom_Name_noext + '.txt' )
							elif Emu_Name == "famicom":
								Synopsis_File = os.path.join( Synopsis_Path, "nes", Rom_Name_noext + '.txt' )
							elif Emu_Name == "tg16":
								Synopsis_File = os.path.join( Synopsis_Path, "pcengine", Rom_Name_noext + '.txt' )
							elif Emu_Name == "tg-cd":
								Synopsis_File = os.path.join( Synopsis_Path, "pce-cd", Rom_Name_noext + '.txt' )
							elif Emu_Name == "fbl" or Emu_Name == "fblc" or Emu_Name == "fbaxxx":
								Synopsis_File = os.path.join( Synopsis_Path, "fba", Rom_Name_noext + '.txt' )
							elif Emu_Name == "xbox":
								if '_' in XBE_ID:
									Synopsis_File = os.path.join( Synopsis_Path, "xbox", XBE_ID.split('_', 1)[0] + '.txt' )
								else:
									Synopsis_File = os.path.join( Synopsis_Path, "xbox", XBE_ID + '.txt' )
							else:
								Synopsis_File = os.path.join( Synopsis_Path, Emu_Name, Rom_Name_noext + '.txt' )
							with open( Synopsis_File ) as input:
								Synopsis = input.read()
								Synopsis1 = Synopsis.split('_________________________', 1)[0]
								Synopsis1 = Synopsis1.split('\n')
								for _ in range(11):
									for line in Synopsis1:
										line = line.lower()
										if line.startswith('name:') and Use_NoIntroNames == 1:
											if Emu_Name == "fba" or Emu_Name == "fbl" or Emu_Name == "fblc" or Emu_Name == "fbaxxx":
												FBA_Rom_Name = line.split(': ',1)[1]
												Synopsis_nointroname_Set = 1
											elif Emu_Name == "n64":
												Rom_Name_noext = line.split(': ',1)[1]
												if Rom_Name_noext.startswith('the'):
													N64_Rom_Name = Rom_Name_noext[4:] + ', the'
												else:
													N64_Rom_Name = Rom_Name_noext.split(' (',1)[0]
												Synopsis_nointroname_Set = 1
											else:
												Rom_Name_noext = line.split(': ',1)[1]
												if Rom_Name_noext.startswith('the'):
													Rom_Name_noext = Rom_Name_noext[4:] + ', the'
												else:
													Rom_Name_noext = Rom_Name_noext.split(' (',1)[0]  
												Synopsis_nointroname_Set = 1
										elif Synopsis_nointroname_Set == 0:
											pass
										if Emu_Name == "xbox":
											with open(os.path.join( Xbox_Games_Folder, Rom_Name ), "r") as input:
												skip = input.readline()
												skip = input.readline()
												skip = input.readline()
												Synopsis_filename = input.readline()
												if '_' in Synopsis_filename:
													Synopsis_filename = '[B]TITLEID:[/B][CR] ' + Synopsis_filename.split('_', 1)[0]
												else:
													Synopsis_filename = '[B]TITLEID:[/B][CR] ' + Synopsis_filename
										else:
											if line.startswith('filename:'):
												Synopsis_filename = line.split(': ',1)[1]
												Synopsis_filename = '[B]Filename:[/B][CR] ' + Synopsis_filename
												Synopsis_filename_Set = 1
											elif Synopsis_filename_Set == 0:
												Synopsis_filename = '[B]Filename:[/B][CR] ' + Rom_Name
										if line.startswith('rating:'):
											Synopsis_rating = line.split(': ',1)[1]
											Synopsis_rating = '[B]Rating:[/B][CR] ' + Synopsis_rating
											Synopsis_rating_Set = 1
										elif Synopsis_rating_Set == 0:
											Synopsis_rating = '[B]Rating:[/B][CR] unknown'
										if line.startswith('players:'):
											Synopsis_players = line.split(': ',1)[1]
											Synopsis_players = '[B]Players:[/B][CR] ' + Synopsis_players
											Synopsis_players_Set = 1
										elif Synopsis_players_Set == 0:
											Synopsis_players = '[B]Players:[/B][CR] at least 1'
										if line.startswith('genre:'):
											Synopsis_genre = line.split(': ',1)[1]
											Synopsis_genre = '[B]Genre:[/B][CR] ' + Synopsis_genre
											Synopsis_genre_Set = 1
										elif Synopsis_genre_Set == 0:
											Synopsis_genre = '[B]Genre:[/B][CR] unknown'
										if line.startswith('developer:'):
											Synopsis_developer = line.split(': ',1)[1]
											Synopsis_developer = '[B]Developer:[/B][CR] ' + Synopsis_developer
											Synopsis_developer_Set = 1
										elif Synopsis_developer_Set == 0:
											Synopsis_developer = '[B]Developer:[/B][CR] unknown'
										if line.startswith('publisher:'):
											Synopsis_publisher = line.split(': ',1)[1]
											Synopsis_publisher = '[B]Publisher:[/B][CR] ' + Synopsis_publisher
											Synopsis_publisher_Set = 1
										elif Synopsis_publisher_Set == 0:
											Synopsis_publisher = '[B]Publisher:[/B][CR] unknown'
										if line.startswith('release year:'):
											Synopsis_release_year = line.split(': ',1)[1]
											Synopsis_release_year = '[B]Released:[/B][CR] ' + Synopsis_release_year
											Synopsis_release_year_Set = 1
										elif Synopsis_release_year_Set == 0:
											Synopsis_release_year = '[B]Released:[/B][CR] unknown'
								Synopsis1 = Synopsis_release_year + '[CR]' + Synopsis_developer + '[CR]' + Synopsis_publisher + '[CR]' + Synopsis_genre + '[CR]' + Synopsis_players# + '[CR]' + Synopsis_filename
								Synopsis2 = Synopsis.split('_________________________', 1)[1]
								Synopsis2 = Synopsis2.strip('\n')
								Synopsis2 = Synopsis2.replace( '\n', '[CR]' )
								Synopsis2 = Synopsis2.replace( '&', '&amp;' )
								Synopsis2 = Synopsis2.replace( '>', '&gt;' )
								Synopsis2 = Synopsis2.replace( '<', '&lt;' )
						except:
							if Emu_Name == "xbox":
								with open(os.path.join( Xbox_Games_Folder, Rom_Name ), "r") as input:
									skip = input.readline()
									skip = input.readline()
									skip = input.readline()
									Synopsis_filename = input.readline()
									if '_' in Synopsis_filename:
										Synopsis_filename = '[B]TITLEID:[/B][CR] ' + Synopsis_filename.split('_', 1)[0]
									else:
										Synopsis_filename = '[B]TITLEID:[/B][CR] ' + Synopsis_filename
							Synopsis1 = Synopsis_release_year + '[CR]' + Synopsis_developer + '[CR]' + Synopsis_publisher + '[CR]' + Synopsis_genre + '[CR]' + Synopsis_players# + '[CR]' + Synopsis_filename
							Synopsis2 = ""
						## Fix labels that use only numbers, XBMC will use its internal labelling system if I don't.
						if FBA_Rom_Name == "1942": FBA_Rom_Name = "1942 "
						if Rom_Name_noext == "1942": Rom_Name_noext = "1942 "
						if Rom_Name_noext == "1943": Rom_Name_noext = "1943 "
						if Rom_Name_noext == "720": Rom_Name_noext = "720 "
						## Set Rom_Names for different types of CD images.
						Rom_Name_ISO = Rom_Name[:-4] + ".iso"
						Rom_Name_BIN = Rom_Name[:-4] + ".bin"
						Rom_Name_IMG = Rom_Name[:-4] + ".img"
						Rom_Name_CUE = Rom_Name[:-4] + ".cue"
						Rom_Name_CCD = Rom_Name[:-4] + ".ccd"
						Rom_Name_ZIP = Rom_Name[:-4] + ".zip"
						Rom_Name_ADF = Rom_Name[:-4] + ".adf"
						Rom_Path = Rom_Name
						## Check and parse the directory for iso files.
						if Parse_ISO_File == 1:
							if Items.endswith( '.iso' ):
								Rom_Path = Rom_Name_ISO
								Rom_Type_Total = Rom_Type_Total
								Write_List_File = 1
							else:
								Write_List_File = 0	
						## Check and parse the directory for cue files.
						if Parse_CUE_File == 1:
							if Items.endswith( '.cue' ):
								Rom_Path = Rom_Name_CUE
								Rom_Type_Total = Rom_Type_Total
								Write_List_File = 1
							else:
								Write_List_File = 0
						## Check and parse the directory for bin/iso/img files.
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
						## Check and parse the directory for cue/ccd/iso files.
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
								if os.path.isfile( os.path.join( Roms_Folder,Rom_Path[:-4]+'.cue' ) ):
									Write_List_File = 0
								else:
									Write_List_File = 1
							else:
								Write_List_File = 0
						## Check and parse the directory for cue/zip/adf/iso files.
						if Parse_CUE_ZIP_ISO_ADF_File == 1:
							if Items.endswith( '.cue' ):
								Rom_Path = Rom_Name_CUE
								Rom_Type_Total = Rom_Type_Total
								Write_List_File = 1
							elif Items.endswith( '.zip' ):
								Rom_Path = Rom_Name_ZIP
								Rom_Type_Total = Rom_Type_Total
								Write_List_File = 1
							elif Items.endswith( '.adf' ):
								Rom_Path = Rom_Name_ADF
								Rom_Type_Total = Rom_Type_Total
								Write_List_File = 1
							elif Items.endswith( '.iso' ):
								Rom_Path = Rom_Name_ISO
								Rom_Type_Total = Rom_Type_Total
								if os.path.isfile( os.path.join( Roms_Folder,Rom_Path[:-4]+'.cue' ) ):
									Write_List_File = 0
								else:
									Write_List_File = 1
							else:
								Write_List_File = 0
						## Create the rest of the layout xml file.
						if Write_List_File:
							## Show the progress bar progress and write rom list file.
							RomListCount = RomListCount + 1
							with open( os.path.join( Games_List_Path, 'gamelist.xml' ), "a") as outputmenufile:
								if Emu_Name == "fba" or Emu_Name == "fbl" or Emu_Name == "fblc" or Emu_Name == "fbaxxx":
									pDialog.update((CountList * 100) / len(os.listdir( os.path.join( Roms_Folder_Path, Emu_Name ) )),'Creating [B][UPPERCASE]' + Emu_Name + '[/UPPERCASE][/B] Rom list',FBA_Rom_Name,'This can take some time, please be patient.' )
									WriteMenuFile = menu_entry % (CountList,FBA_Rom_Name,Synopsis1,Synopsis2,Thumbnail,"[ArtworkFolder]",'RunScript( special://emustation_scripts/launcher.py,' + Emu_XBE + ',' + Rom_Name_noext + ',,' + str(CountList) + ' )',"ActivateWindow(1101)")
								elif Emu_Name == "mame" or Emu_Name == "neogeocd":
									pass
								elif Emu_Name == "n64":
									pDialog.update((CountList * 100) / len(os.listdir( Roms_Folder )),'Creating [B][UPPERCASE]' + Emu_Name + '[/UPPERCASE][/B] Rom list and coping media files',N64_Rom_Name,'This can take some time, please be patient.' )
									WriteMenuFile = menu_entry % (CountList,N64_Rom_Name,Synopsis1,Synopsis2,Thumbnail,"[ArtworkFolder]",'RunScript( special://emustation_scripts/launcher.py,' + Emu_XBE + ',' + Rom_Path + ',,' + str(CountList) + ' )',"ActivateWindow(1101)")
								elif Emu_Name == "amiga" or Emu_Name == "pce-cd" or Emu_Name == "psx" or Emu_Name == "tg-cd" or Emu_Name == "segacd":
									pDialog.update((CountList * 100) / Rom_Type_Total,'Creating [B][UPPERCASE]' + Emu_Name + '[/UPPERCASE][/B] Rom list',Rom_Name_noext,'This can take some time, please be patient.' )
									WriteMenuFile = menu_entry % (CountList,Rom_Name_noext,Synopsis1,Synopsis2,Thumbnail,"[ArtworkFolder]",'RunScript( special://emustation_scripts/launcher.py,' + Emu_XBE + ',' + Rom_Path + ',,' + str(CountList) + ' )',"ActivateWindow(1101)")
								elif Emu_Name == "xbox":
									with open(os.path.join( Xbox_Games_Folder, Rom_Name ), "r") as input:
										GameTitle = input.readline()
										GamePath = input.readline()
										GameLetter = input.readline()
										GameThumb = input.readline() + '.jpg'
									with open( os.path.join( Media_Folder_Path, "xbox\\GameNames.txt" ),"a") as ouput:
										ouput.write("Game Name: " + GameTitle + "SubFolder: " + GameLetter + "TitleID: " + GameThumb[:-4] + "\n\n")
									pDialog.update((CountList * 100) / len(os.listdir( Roms_Folder )),'Creating [B][UPPERCASE]' + Emu_Name + '[/UPPERCASE][/B] Game list',GameTitle[:-1],'This can take some time, please be patient.' )
									WriteMenuFile = menu_entry % (CountList,GameTitle[:-1],Synopsis1,Synopsis2,GameLetter[:-1]+'\\'+GameThumb,"[ArtworkFolder]",'RunScript( special://emustation_scripts/launcher.py,' + GamePath[:-1] + ',empty,,' + str(CountList) + ' )',"ActivateWindow(1101)")
								else:
									pDialog.update((CountList * 100) / len(os.listdir( Roms_Folder )),'Creating [B][UPPERCASE]' + Emu_Name + '[/UPPERCASE][/B] Rom list',Rom_Name_noext,'This can take some time, please be patient.' )
									WriteMenuFile = menu_entry % (CountList,Rom_Name_noext,Synopsis1,Synopsis2,Thumbnail,"[ArtworkFolder]",'RunScript( special://emustation_scripts/launcher.py,' + Emu_XBE + ',' + Rom_Path + ',,' + str(CountList) + ' )',"ActivateWindow(1101)")
								outputmenufile.write( WriteMenuFile )
							## Write favourites menu entries.
							with open( os.path.join( Games_List_Path, 'favslist.xml' ), "a") as favsmenufile:
								if Emu_Name == "fba" or Emu_Name == "fbl" or Emu_Name == "fblc" or Emu_Name == "fbaxxx":
									WriteMenuFile = favourites_entry % (FBA_Rom_Name,Emu_XBE,Rom_Name_noext)
								elif Emu_Name == "mame" or Emu_Name == "neogeocd":
									pass
								elif Emu_Name == "n64":
									WriteMenuFile = favourites_entry % (N64_Rom_Name,Emu_XBE,Rom_Path)
								elif Emu_Name == "xbox":
									with open(os.path.join( Xbox_Games_Folder, Rom_Name ), "r") as input:
										Rom_Name_noext = input.readline()
										Emu_XBE = input.readline()
										WriteMenuFile = favourites_entry % (Rom_Name_noext[:-1],Emu_XBE[:-1],"null")
								else:
									WriteMenuFile = favourites_entry % (Rom_Name_noext,Emu_XBE,Rom_Path)
								favsmenufile.write( WriteMenuFile )
							## Write menu entry for quick jump.
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
							## Add 1 to the Countlist and JumpList.
							CountList = CountList + 1
							JumpList = JumpList + 1
				## Add the footer to the layout xml file.
				with open( os.path.join( Games_List_Path, 'gamelist.xml' ), "a") as outputmenufile:
					WriteMenuFile = menu_entry_footer
					outputmenufile.write( WriteMenuFile )
			else:
				if os.path.isdir( Games_List_Path ): shutil.rmtree( Games_List_Path )
				if ManualScan == 1:
					dialog.ok("Error","","No roms/images found for this system")
					return Main_Code()
			## Set the rom count and remove any direct launch rom list.xml files.
			xbmc.executebuiltin('Skin.SetString('+ Emu_Name +'_games,'+ str( RomListCount ) + ')')
			if Emu_Name == "atarijaguar" or Emu_Name == "neogeocd":
				if os.path.isdir( Games_List_Path ): shutil.rmtree( Games_List_Path )
				if os.path.isdir( Media_Path ): shutil.rmtree( Media_Path )
			if Emu_Name == "mame":
				if os.path.isfile( os.path.join( Emu_Path, "system\\ROMS.list" )): os.remove( os.path.join( Emu_Path, "system\\ROMS.list" ))
				if os.path.isfile( os.path.join( Emu_Path, "system\\ROMS.metadata" )): os.remove( os.path.join( Emu_Path, "system\\ROMS.metadata" ))
				if os.path.isdir( Games_List_Path ): shutil.rmtree( Games_List_Path )
				if os.path.isdir( Media_Path ): shutil.rmtree( Media_Path )
			## ManualMode - Set a property so I can run the next script without this one running on.
			if Found_Roms == 1 and ManualScan == 1:
				xbmcgui.Window(xbmcgui.getCurrentWindowId()).setProperty("MyScript.ExternalRunning", "True")
				## Running the scan script to update the counters.
				xbmc.executebuiltin('RunScript(' + Scripts_Path + 'refresh_carousel.py,0,' + Emu_Name + ',0,0)' )
				## Loop.
				while (xbmcgui.Window(xbmcgui.getCurrentWindowId()).getProperty("MyScript.ExternalRunning") == "True"):
					time.sleep(0.2)
				if os.path.isdir( os.path.join( Emulator_Folder_Path, "xbox" ) ): shutil.rmtree( os.path.join( Emulator_Folder_Path, "xbox" ) )
				pDialog.close()
				return
	## AutoMode - Set a property so I can run the next script without this one running on.
	if Found_Roms == 1 and ManualScan == 0:
		xbmcgui.Window(xbmcgui.getCurrentWindowId()).setProperty("MyScript.ExternalRunning", "True")
		## Running the scan script to update the counters.
		xbmc.executebuiltin('RunScript(' + Scripts_Path + 'refresh_carousel.py,scan_emus,0,0,0)' )
		## Loop.
		while (xbmcgui.Window(xbmcgui.getCurrentWindowId()).getProperty("MyScript.ExternalRunning") == "True"):
			time.sleep(0.2)
		if os.path.isdir( os.path.join( Emulator_Folder_Path, "xbox" ) ): shutil.rmtree( os.path.join( Emulator_Folder_Path, "xbox" ) )
	else:
		if os.path.isdir( os.path.join( Emulator_Folder_Path, "xbox" ) ): shutil.rmtree( os.path.join( Emulator_Folder_Path, "xbox" ) )
		pDialog.close()
		return
menu_entry_header	= '<content>\n<!--\nTags used in the xml files:\nname = $INFO[listitem.Label]\ndetails = $INFO[listitem.Label2]\nsynopsis = $INFO[listitem.ActualIcon]\nthumbnail = $INFO[listitem.Thumb]\nmediapath = $INFO[listitem.SortLetter]\n-->'
menu_entry			= '\n	<item id="%s">\n		<name>%s</name>\n		<details>%s</details>\n		<synopsis>%s</synopsis>\n		<thumbnail>%s</thumbnail>\n		<mediapath>%s</mediapath>\n		<onclick>%s</onclick>\n		<onclick>%s</onclick>\n	</item>'
menu_entry_footer	= '\n</content>'
search_menu_entry	= '<control type="button" id="%s">\n	<label>[UPPERCASE]jump to letter[/UPPERCASE]</label>\n	<label2>&lt; [UPPERCASE]%s[/UPPERCASE] &gt;</label2>\n	<include>MenuButtonCommonValues</include>\n	<onclick>Dialog.Close(1120)</onclick>\n	<onclick>%s</onclick>\n</control>\n'
favourites_entry	= '<favourites>%s|%s|%s</favourites>\n'
n64_config			= '[Settings]\nskinname=Default\nonhd=true\nHideLaunchScreens=true\nEnableXMVPreview=false\nEnableVideoAudio=false\nEnableInfoPanel=false\nEnableBGMusic=false\nRandomBGMusic=false\nAudioBoost=false\nPathRoms=%s\\\nPathMedia=D:\Media\\\nPathSkins=D:\Skins\\\nPathSaves=D:\Saves\\\nPathScreenshots=D:\Screenshots\\'
mame_config			= '[Directories]\nALTDrive = t\nC_Mapping = \\device\\harddisk0\\partition1\nE_Mapping = \\device\\harddisk0\\partition1\nF_Mapping = \\device\\harddisk0\\partition6\nG_Mapping = \\device\\harddisk0\\partition7\nH_Mapping = \\device\\cdrom0\nRomsPath0 = %s\nRomsPath1 = d:\\roms\nRomsPath2 = d:\\roms\nRomsPath3 = d:\\roms\nArtPath = d:\\artwork\nAudioPath = d:\\samples\nConfigPath = d:\\cfg\nGeneralPath = d:\\general\nHDImagePath = d:\\hdimages\nHiScoresPath = d:\\hiscores\nNVRamPath = d:\\nvram\nBackupPath = d:\\roms\\backup\nScreenshotPath = d:\\screenshots\nAutoBootSavePath = d:\\autobootsaves\n\n\n[General]\nbios = 0\nCheatsEnabled = 1\nCheatFilename = cheat.dat\nSkipDisclaimer = 1\nSkipGameInfo = 1\nSkipWarnings = 1\nScreenSaverTimeout = 10\n\n\n[Input]\nLightgun1_Left = 4294934529\nLightgun1_CenterX = 0\nLightgun1_Right = 32767\nLightgun1_Top = 32767\nLightgun1_CenterY = 0\nLightgun1_Bottom = 4294934529\nLightgun2_Left = 4294934529\nLightgun2_CenterX = 0\nLightgun2_Right = 32767\nLightgun2_Top = 32767\nLightgun2_CenterY = 0\nLightgun2_Bottom = 4294934529\nLightgun3_Left = 4294934529\nLightgun3_CenterX = 0\nLightgun3_Right = 32767\nLightgun3_Top = 32767\nLightgun3_CenterY = 0\nLightgun3_Bottom = 4294934529\nLightgun4_Left = 4294934529\nLightgun4_CenterX = 0\nLightgun4_Right = 32767\nLightgun4_Top = 32767\nLightgun4_CenterY = 0\nLightgun4_Bottom = 4294934529\n\n\n[Network]\nDisableNetworking = 0\nIPAddress = \nGateway = \nSubnet = \nNameServer = \n\n\n[ROMListOptions]\nDisplayMode = 1\nSortMode = 0\nShowROMStatus = 0\nShowFAVEStatus = 1\nHideFilteredROMs = 0\nFilterMode = 0\nCursorPosition = 0.000000\nPageOffset = 0.000000\nSuperscrollIndex = 0\n\n\n[SkinOptions]\nSelectedSkin = Original\n\n\n[Sound]\nSoundEnable = 1\nSampleRate = 44100\nUseSamples = 1\nUseFilter = 1\n\n\n[VMMOptions]\nForceVMM = 0\nThreshold = 4194304\nCommitSize = 1048576\nDistribute = 65535\n\n\n[VectorOptions]\nVectorWidth = 640\nVectorHeight = 480\nBeamWidth = 2\nFlickerEffect = 0.000000\nBeamIntensity = 1.500000\nTranslucency = 1\n\n\n[Video]\nVSYNC = 1\nThrottleFramerate = 1\nAspectRatioCorrection = 1\nMinificationFilter = 2\nMagnificationFilter = 2\nFrameskip = 4294967295\nGraphicsFilter = 0\nSoftDisplayFilter = 0\nFlickerFilter = 5\nScreenRotation = 0\nBrightness = 1.000000\nPauseBrightness = 0.650000\nGamma = 1.000000\nScreenUsage_X = 0.850000\nScreenUsage_Y = 0.850000\nScreenPos_X = 0.000000\nScreenPos_Y = 0.000000\nArtwork = 1\n\n\n'
fbl_config			= 'UsePathINI=1\nROMPath1=D:\\roms\nROMPath2=\nROMPath3=\nROMPath4=\nROMPath5=\nROMPath6=\nROMPath7=\nROMPath8=\nD:\\artwork\\Shots 1\nD:\\artwork\\Shots 2\nD:\\artwork\\Shots 3\nD:\\artwork\\Shots 4\nD:\\artwork\\Shots 5\nD:\\artwork\\Shots 6\nD:\\artwork\\Shots 7\nD:\\artwork\\Shots 8\nD:\\nvram\nD:\\samples\nD:\\ini\nD:\\savestates\nD:\\config\nD:\\hiscores\nD:\\videos\n'
if Manual_Scan == "manual" :
	ManualScan = 1
	Main_Code()
if Full_Scan == "auto" :
	if dialog.yesno("QUESTION TIME","","Would you like to auto scan your roms?"):
		ManualScan = 0
		Main_Code()