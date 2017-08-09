'''
	Script by Rocky5
	Used to create .cut files from your emulator and roms folder.
	
	Mame and FBA, must have there roms placed inside there root directory.
	( the script will generate the correct cut file for these emulators )
'''

import glob, os, shutil, sys, time, xbmc, xbmcgui

try:
	Manual_Scan	= sys.argv[1:][0]
	Full_Scan	= sys.argv[2:][0]
except:
	Manual_Scan	= "0"
	Full_Scan	= "0"

#####	Start markings for the log file.
print "================================================================================"
print "| _Scripts\XBMC-Emustation\scan.py loaded."
print "| ------------------------------------------------------------------------------"
pDialog							= xbmcgui.DialogProgress()
dialog							= xbmcgui.Dialog()

#####	Sets paths.
# Gets current XBMC4Gamers directory.
CharCount = 100 # How many characters you want after 'The executable running is: '
with open( xbmc.translatePath( "special://xbmc/system/" ) + "xbmc.log", "r" ) as XBMCLOG:
	for line in XBMCLOG:
		left,found,right = line.partition("The executable running is: ")
		if found:
			Working_Directory	= ( right[:CharCount] )
			Root_Directory		= Working_Directory[:-12] # Removed default.xbe
			Emulator_Path		= Root_Directory + '_emulators\\'
			CUTFile_Path		= Root_Directory + '_cuts\\'
			Scripts_Path		= Root_Directory + '_scripts\\XBMC-Emustation\\'
			Roms_Path			= Root_Directory + '_roms\\'
			TBN_Path			= Root_Directory + '_tbns\\'
			Content_List_Path	= xbmc.translatePath( "Special://skin/720p/content lists/" )
			Extensions			= [ "zip","bin","cue","img","iso","rom","n64","z64","smd","smc","gb","gbc","gba","nes","sms","swc","gg","a26","a78","col","lnx","sfc","sg","fig","vms","exe" ]

def log( input ):
	if logging: print "%s" % str( input )
			
def manual_scan():
	Found_Roms = 0
	Emu_Path = dialog.browse( 0,"Select a Emulator folder",'files','',False,False,Emulator_Path )
	
	log('|	Check if _emulators directory is selected instead of the emulator its self.')
	if Emu_Path == Emulator_Path: return
		
	log('|	Convert Q:\\ to XBMCs internal special protocol')
	if Emu_Path.startswith("Q:\\"): Emu_Path = Emu_Path.replace( "Q:\\", Root_Directory )

	log('|	Checking to make sure the emulator you selected exists.')
	if os.path.isdir( Emu_Path ):
		
		log('|	Set the Countlist variable and set the emu_name variable.')
		CountList = 1
		Parse_CUE_File = 0
		Parse_FBL_XML = 0
		Write_CUT_File = 1
		Emu_Name = os.path.split(os.path.dirname( Emu_Path ))[1]
		
		log('|	Check for a default .xbe in the emullator path you selected.')
		if os.path.isfile( os.path.join( Emu_Path, "default.xbe" ) ):
			Emu_XBE = os.path.join( Emu_Path, "default.xbe" )
		else:
			dialog.ok("Error","No default.xbe found in this directory")
			return manual_scan()
		
		log('|	Check for previous layout xml and if it exists remove it.')
		if os.path.isfile( Content_List_Path + Emu_Name + '.xml' ): os.remove( Content_List_Path + Emu_Name + '.xml' )

		log('|	Write new layout xml header.')
		with open( Content_List_Path + Emu_Name + '.xml', "w") as outputmenufile:
			WriteMenuFile = menu_entry_header
			outputmenufile.write( WriteMenuFile )
		
		log('|	Check to see if the folder you selected it fba, or mame as these emulators must have there roms in there own roms folder in the emulators root directory')
		if Emu_Name == "fba":
			Roms_Folder	= Emulator_Path + '\\fba\\roms\\'
			Parse_FBL_XML = 1
		elif Emu_Name == "mame":
			Roms_Folder	= dialog.browse( 0,"Select the Roms folder","files",'',False,False,Emulator_Path + '\\mame\\roms\\' )
		elif Emu_Name == "psx":
			Roms_Folder	= dialog.browse( 0,"Select the Roms folder","files",'',False,False,Roms_Path + Emu_Name )
			Parse_CUE_File = 1
		else:
			Roms_Folder	= dialog.browse( 0,"Select the Roms folder","files",'',False,False,Roms_Path + Emu_Name )
		
		log('|	Convert Q:\\ to XBMCs internal special protocol')
		if Roms_Folder.startswith("Q:\\"): Roms_Folder = Roms_Folder.replace( "Q:\\", Root_Directory )
		
		log('|	Couple more vars being set')
		Output_Path = os.path.join( CUTFile_Path, Emu_Name ) + '\\'
		TBN_File = os.path.join( TBN_Path, Emu_Name ) + '\\'
		
		log('|	Check to see if the emulators = rom folder is empty and exit if it is.')
		if len(os.listdir( Roms_Folder )) > 0:
			
			log('|	Listing the content of the roms folder for parsing.')
			for Items in sorted( os.listdir( Roms_Folder ) ):

					log('|	Checking the file I find, extension agains my table.')
					if Items.endswith(tuple(Extensions)):
						
						log('|	More vars being set.')
						Rom_Name = Items
						Rom_Name_noext = Rom_Name[:-4]
						PSX_Name_CUE = os.path.join( Roms_Folder, Rom_Name[:-4] ) + ".cue"
						Rom_Path = os.path.join( Roms_Folder, Rom_Name )

						log('|	Check if fba was found and parse its xml files to get the correct rom names for the list.')
						if Parse_FBL_XML == 1:
							if os.path.isfile( os.path.join( Emulator_Path, "fba\\info\\emulation\\" ) + Rom_Name_noext + ".ini" ):
								with open( os.path.join( Emulator_Path, "fba\\info\\emulation\\" ) + Rom_Name_noext + ".ini", 'r') as ini:
									FBA_Rom_Name = ini.readline()[:-1]
							else:
								FBA_Rom_Name = Rom_Name_noext
								
						log('|	Check if psx was found and parse its directory for cue files.')
						if Parse_CUE_File == 1:
							if os.path.isfile( PSX_Name_CUE ):
								if Rom_Path == PSX_Name_CUE:
									Write_CUT_File = 0
								else:
									Rom_Path = PSX_Name_CUE
									Write_CUT_File = 1
							else:
								Write_CUT_File = 1
						
						log('|	Check to see if vars are the value I need and create a new dialog.')
						if CountList == 1 and Found_Roms == 0: pDialog.create( "Scanning for Roms","","Please wait..." )
						
						log('|	Setting a var again :/')
						Found_Roms = 1
						
						log('|	Check to see if _tbns folder exists and if it doesnt create it.')
						if not os.path.isdir( TBN_File ): os.makedirs( TBN_File )
						
						log('|	Check to see if the output directory exists and remove it.')
						if CountList == 1 and os.path.isdir( Output_Path ):
							pDialog.update( 0,"","Doing house cleaning" )
							shutil.rmtree( Output_Path )# remove old cut files
						
						log('|	Create a new output directory.')
						if not os.path.isdir( Output_Path ): os.makedirs( Output_Path )
						
						log('|	Show the progress bar progress.')
						pDialog.update( ( CountList * 100 ) / len( os.listdir( Roms_Folder ) ),"Processing Roms",Rom_Name_noext,"Please wait..." )
						
						if Write_CUT_File:
							log('|	Create the rest of the layout xml file.')
							with open( Content_List_Path + Emu_Name + '.xml', "a") as outputmenufile:
								if Emu_Name == "fba":
									WriteMenuFile = menu_entry % (CountList,FBA_Rom_Name,'Runxbe( "' + Output_Path + Rom_Name_noext + '.cut" )',TBN_File + Rom_Name_noext + '.tbn',TBN_File + Rom_Name_noext + '.tbn')
								elif Emu_Name == "mame":
									WriteMenuFile = menu_entry % (CountList,Rom_Name_noext,'Runxbe( "' + Output_Path + Rom_Name_noext + '.cut" )',TBN_File + Rom_Name_noext + '.tbn',TBN_File + Rom_Name_noext + '.tbn')
								else:
									WriteMenuFile = menu_entry % (CountList,Rom_Name_noext,'Runxbe( "' + Output_Path + Rom_Name_noext + '.cut" )',TBN_File + Rom_Name_noext + '.tbn',TBN_File + Rom_Name_noext + '.tbn')
								outputmenufile.write( WriteMenuFile )

							log('|	Create the cut file for this rom.')
							with open(Output_Path + Rom_Name_noext + '.cut', "w") as outputfile:
								if Emu_Name == "fba":
									WriteFile = CUT_File_Layout % ( Emu_XBE,FBA_Rom_Name,Rom_Name_noext )
								elif Emu_Name == "mame":
									WriteFile = CUT_File_Layout % ( Emu_XBE,Rom_Name_noext,Rom_Name_noext )
								elif Emu_Name == "psx":
									WriteFile = CUT_File_Layout % ( Emu_XBE,Rom_Name_noext,Rom_Path )
								else:
									WriteFile = CUT_File_Layout % ( Emu_XBE,Rom_Name_noext,Rom_Path )
								outputfile.write( WriteFile )
						
						log('|	Add 1 to the Countlist.')
						CountList = CountList + 1
		else:
			log('|	No roms exist so do some cleanup.')
			shutil.rmtree( Output_Path )# remove old cut files
			if not os.path.isdir( Output_Path ): os.makedirs( Output_Path )
	
	log('|	Add the footer to the layout xml file.')
	with open( Content_List_Path + Emu_Name + '.xml', "a") as outputmenufile:
		WriteMenuFile = menu_entry_footer
		outputmenufile.write( WriteMenuFile )
		
	log('|	Set a property so I can run the next script without this one running on.')
	if ( Found_Roms == 1 ):
		xbmcgui.Window(xbmcgui.getCurrentWindowId()).setProperty("MyScript.ExternalRunning", "True")
		
		log('|	Running the scan script to update the counters.')
		xbmc.executebuiltin('RunScript(' + Scripts_Path + 'scan.py,scan_emus,scan_cuts,0)' )
		
		log('|	Loop.')
		while (xbmcgui.Window(xbmcgui.getCurrentWindowId()).getProperty("MyScript.ExternalRunning") == "True"):
			time.sleep(0.2)

		log('|	Run the create layouts script to refresh them.')
		xbmc.executebuiltin('RunScript(' + Scripts_Path + 'create layouts.py)' )
	pDialog.close()
	return


def full_scan(): ## not working yet

	Found_Roms = 0
	
	log('|	Check if _emulators directory is selected instead of the emulator its self.')
	if os.path.isdir( Emulator_Path ):
	
		log('|	Parse all folder in the Emulators_Path')
		for Emu_Path in sorted( os.listdir( Emulator_Path ) ):
		
			log('|	Set the Countlist variable.')
			CountList = 1
			Parse_CUE_File = 0
			Parse_FBL_XML = 0
			Write_CUT_File = 1
			
			log('|	Checking to make sure the emulator you selected exists.')
			if os.path.isdir( os.path.join( Emulator_Path, Emu_Path ) ):
			
				log('|	Set emu_name/path variable.')
				Emu_Path = os.path.join( Emulator_Path, Emu_Path ) + '\\'
				Emu_Name = os.path.split(os.path.dirname( Emu_Path ))[1]
				
				log('|	Check for previous layout xml and if it exists remove it.')
				if os.path.isfile( Content_List_Path + Emu_Name + '.xml' ): os.remove( Content_List_Path + Emu_Name + '.xml' )
				
				log('|	Write new layout xml header.')
				with open( Content_List_Path + Emu_Name + '.xml', "w") as outputmenufile:
				
					WriteMenuFile = menu_entry_header
					outputmenufile.write( WriteMenuFile )
				
				log('|	Check to see if a defualt.xbe exists')
				if os.path.isfile( os.path.join( Emu_Path, "default.xbe" ) ):
				
					log('|	default.xbe does exist so set the oath varable')
					Emu_XBE = os.path.join( Emu_Path, "default.xbe" )
				
					log('|	Check to see if the current directory is fba or mame and set the roms path.')
					if Emu_Name == "fba":
						Roms_Folder	= Emulator_Path + '\\fba\\roms\\'
						Parse_FBL_XML = 1
					elif Emu_Name == "mame":
						Roms_Folder	= Emulator_Path + '\\mame\\roms\\'
					elif Emu_Name == "psx":
						Roms_Folder	= Roms_Path + Emu_Name
						Parse_CUE_File = 1
					else:
						Roms_Folder	= Roms_Path + Emu_Name
						
					log('|	Convert Q:\\ to XBMCs internal special protocol')
					if Roms_Folder.startswith("Q:\\"): Roms_Folder = Roms_Folder.replace( "Q:\\", Root_Directory )
					
					log('|	Couple more vars being set')
					Output_Path = os.path.join( CUTFile_Path, Emu_Name ) + '\\'
					TBN_File = os.path.join( TBN_Path, Emu_Name ) + '\\'
					
					log('|	Check to see if the emulators = rom folder is empty and exit if it is.')
					if len(os.listdir( Roms_Folder )) > 0:
					
						log('|	Listing the content of the roms folder for parsing.')
						for Items in sorted( os.listdir( Roms_Folder ) ):
						
							log('|	Checking the file I find, extension agains my table.')
							if Items.endswith(tuple(Extensions)):
							
								log('|	More vars being set.')
								Rom_Name = Items
								Rom_Name_noext = Rom_Name[:-4]
								PSX_Name_CUE = os.path.join( Roms_Folder, Rom_Name[:-4] ) + ".cue"
								Rom_Path = os.path.join( Roms_Folder, Rom_Name )
								
								log('|	Check if fba was found and parse its xml files to get the correct rom names for the list.')
								if Parse_FBL_XML == 1:
									if os.path.isfile( os.path.join( Emulator_Path, "fba\\info\\emulation\\" ) + Rom_Name_noext + ".ini" ):
										with open( os.path.join( Emulator_Path, "fba\\info\\emulation\\" ) + Rom_Name_noext + ".ini", 'r') as ini:
											FBA_Rom_Name = ini.readline()[:-1]
									else:
										FBA_Rom_Name = Rom_Name_noext
										
								log('|	Check if psx was found and parse its directory for cue files.')
								if Parse_CUE_File == 1:
									if os.path.isfile( PSX_Name_CUE ):
										if Rom_Path == PSX_Name_CUE:
											Write_CUT_File = 0
										else:
											Rom_Path = PSX_Name_CUE
											Write_CUT_File = 1
									else:
										Write_CUT_File = 1
									
								log('|	Check to see if vars are the value I need and create a new dialog.')
								if CountList == 1 and Found_Roms == 0: pDialog.create( "Scanning for Roms","","Please wait..." )
								
								log('|	Setting a var again :/')
								Found_Roms = 1

								log('|	Check to see if _tbns folder exists and if it doesnt create it.')
								if not os.path.isdir( TBN_File ): os.makedirs( TBN_File )

								log('|	Check to see if the output directory exists and remove it.')
								if CountList == 1 and os.path.isdir( Output_Path ):
									pDialog.update( 0,"","Doing house cleaning" )
									shutil.rmtree( Output_Path )# remove old cut files
				
								log('|	Create a new output directory.')
								if not os.path.isdir( Output_Path ): os.makedirs( Output_Path )
								
								log('|	Show the progress bar progress.')
								pDialog.update( ( CountList * 100 ) / len( os.listdir( Roms_Folder ) ),"Processing [B][UPPERCASE]" + Emu_Name + "[/UPPERCASE][/B] Roms",Rom_Name_noext,"Please wait..." )
								
								if Write_CUT_File:
									log('|	Create the rest of the layout xml file.')
									with open( Content_List_Path + Emu_Name + '.xml', "a") as outputmenufile:
										if Emu_Name == "fba":
											WriteMenuFile = menu_entry % (CountList,FBA_Rom_Name,'Runxbe( "' + Output_Path + Rom_Name_noext + '.cut" )',TBN_File + Rom_Name_noext + '.tbn',TBN_File + Rom_Name_noext + '.tbn')
										elif Emu_Name == "mame":
											WriteMenuFile = menu_entry % (CountList,Rom_Name_noext,'Runxbe( "' + Output_Path + Rom_Name_noext + '.cut" )',TBN_File + Rom_Name_noext + '.tbn',TBN_File + Rom_Name_noext + '.tbn')
										else:
											WriteMenuFile = menu_entry % (CountList,Rom_Name_noext,'Runxbe( "' + Output_Path + Rom_Name_noext + '.cut" )',TBN_File + Rom_Name_noext + '.tbn',TBN_File + Rom_Name_noext + '.tbn')
										outputmenufile.write( WriteMenuFile )
									
									log('|	Create the cut file for this rom.')
									with open(Output_Path + Rom_Name_noext + '.cut', "w") as outputfile:
										if Emu_Name == "fba":
											WriteFile = CUT_File_Layout % ( Emu_XBE,FBA_Rom_Name,Rom_Name_noext )
										elif Emu_Name == "mame":
											WriteFile = CUT_File_Layout % ( Emu_XBE,Rom_Name_noext,Rom_Name_noext )
										else:
											WriteFile = CUT_File_Layout % ( Emu_XBE,Rom_Name_noext,Rom_Path )
										outputfile.write( WriteFile )
								
								log('|	Add 1 to the Countlist.')
								CountList = CountList + 1
					
					else:
						log('|	No roms exist so do some cleanup.')
						shutil.rmtree( Output_Path )# remove old cut files
						if not os.path.isdir( Output_Path ): os.makedirs( Output_Path )
						
			log('|	Add the footer to the layout xml file.')
			with open( Content_List_Path + Emu_Name + '.xml', "a") as outputmenufile:
				WriteMenuFile = menu_entry_footer
				outputmenufile.write( WriteMenuFile )
	
	log('|	Set a property so I can run the next script without this one running on.')			
	if ( Found_Roms == 1 ):
		xbmcgui.Window(xbmcgui.getCurrentWindowId()).setProperty("MyScript.ExternalRunning", "True")
		
		log('|	Running the scan script to update the counters.')
		xbmc.executebuiltin('RunScript(' + Scripts_Path + 'scan.py,scan_emus,scan_cuts,scan_xbes)' )
		
		log('|	Loop.')
		while (xbmcgui.Window(xbmcgui.getCurrentWindowId()).getProperty("MyScript.ExternalRunning") == "True"):
			time.sleep(0.2)

		log('|	Run the create layouts script to refresh them.')
		xbmc.executebuiltin('RunScript(' + Scripts_Path + 'create layouts.py)' )
	pDialog.close()
	return

				
CUT_File_Layout = '<shortcut>\n\
	<path>%s</path>\n\
	<label>%s</label>\n\
		<custom>\n\
			<game>%s</game>\n\
		</custom>\n\
</shortcut>'
		
menu_entry_header	= '<content>'		
menu_entry			= '\n\
	<item id="%s">\n\
		<label>%s</label>\n\
		<onclick>%s</onclick>\n\
		<icon>%s</icon>\n\
		<thumb>%s</thumb>\n\
	</item>\n\
'
menu_entry_footer	= '</content>'

logging = 0 # Setting this to 1 will spam the living hell out of your log file if you run the Auto mode, you have been warned
if not os.path.isdir( Content_List_Path + 'merged' ): os.makedirs( Content_List_Path + 'merged' )
if Manual_Scan == "manual" : manual_scan()
if Full_Scan == "auto" : full_scan()

pDialog.update(0)
pDialog.close()
#dialog.ok( "","","Process Complete" )