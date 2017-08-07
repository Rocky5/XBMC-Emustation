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
			Extensions			= [ "zip","bin","img","iso","rom","n64","z64","smd","smc","gb","gbc","gba","nes","sms","swc","gg","a26","a78","col","lnx","sfc","sg","fig","vms","exe" ]

def manual_scan():
	Found_Roms = 0
	Emu_Path = dialog.browse( 0,"Select a Emulator folder",'files','',False,False,Emulator_Path )
	
	if Emu_Path == Emulator_Path: return
	
	if Emu_Path.startswith("Q:\\"): Emu_Path = Emu_Path.replace( "Q:\\", Root_Directory )
	
	if os.path.isdir( Emu_Path ):
	
		CountList = 1
		Emu_Name = os.path.split(os.path.dirname( Emu_Path ))[1]
		
		if os.path.isfile( Content_List_Path + Emu_Name + '.xml' ): os.remove( Content_List_Path + Emu_Name + '.xml' )
		
		with open( Content_List_Path + Emu_Name + '.xml', "w") as outputmenufile:
			WriteMenuFile = menu_entry_header
			outputmenufile.write( WriteMenuFile )
			
		if os.path.isfile( os.path.join( Emu_Path, "default.xbe" ) ):
			Emu_XBE = os.path.join( Emu_Path, "default.xbe" )
		else:
			dialog.ok("Error","No default.xbe found in this directory")
			return manual_scan()
			
		if Emu_Name == "fba":
			Roms_Folder	= Emulator_Path + '\\fba\\roms\\'
			Parse_FBL_XML = 1
		elif Emu_Name == "mame":
			Roms_Folder	= dialog.browse( 0,"Select the Roms folder","files",'',False,False,Emulator_Path + '\\mame\\roms\\' )
		else:
			Roms_Folder	= dialog.browse( 0,"Select the Roms folder","files",'',False,False,Roms_Path + Emu_Name )
			Parse_FBL_XML = 0
			
		if Roms_Folder.startswith("Q:\\"): Roms_Folder = Roms_Folder.replace( "Q:\\", Root_Directory )
		
		Output_Path = os.path.join( CUTFile_Path, Emu_Name ) + '\\'
		TBN_File = os.path.join( TBN_Path, Emu_Name ) + '\\'
		
		if len(os.listdir( Roms_Folder )) > 0:
			
			for Items in sorted( os.listdir( Roms_Folder ) ):

					if Items.endswith(tuple(Extensions)):
					
						Rom_Name = Items
						Rom_Name_noext = Rom_Name[:-4]
						Rom_Path = os.path.join( Roms_Folder, Rom_Name )

						if Parse_FBL_XML == 1:
							if os.path.isfile( os.path.join( Emulator_Path, "fba\\info\\emulation\\" ) + Rom_Name_noext + ".ini" ):
								with open( os.path.join( Emulator_Path, "fba\\info\\emulation\\" ) + Rom_Name_noext + ".ini", 'r') as ini:
									FBA_Rom_Name = ini.readline()[:-1]
							else:
								FBA_Rom_Name = Rom_Name_noext
								
						if ( pDialog.iscanceled() ): return
						
						if CountList == 1 and Found_Roms == 0: pDialog.create( "Scanning for Roms","","Please wait..." )
						
						Found_Roms = 1
						
						if not os.path.isdir( TBN_File ): os.makedirs( TBN_File )
						
						if CountList == 1 and os.path.isdir( Output_Path ):
						
							pDialog.update( 0,"","Doing house cleaning" )
							shutil.rmtree( Output_Path )# remove old cut files
							
						if not os.path.isdir( Output_Path ): os.makedirs( Output_Path )
						
						pDialog.update( ( CountList * 100 ) / len( os.listdir( Roms_Folder ) ),"Processing Roms",Rom_Name_noext,"Please wait..." )
						
						with open( Content_List_Path + Emu_Name + '.xml', "a") as outputmenufile:
							if Emu_Name == "fba":
								WriteMenuFile = menu_entry % (CountList,FBA_Rom_Name,'Runxbe( "' + Output_Path + Rom_Name_noext + '.cut" )',TBN_File + Rom_Name_noext + '.tbn',TBN_File + Rom_Name_noext + '.tbn')
							elif Emu_Name == "mame":
								WriteMenuFile = menu_entry % (CountList,Rom_Name_noext,'Runxbe( "' + Output_Path + Rom_Name_noext + '.cut" )',TBN_File + Rom_Name_noext + '.tbn',TBN_File + Rom_Name_noext + '.tbn')
							else:
								WriteMenuFile = menu_entry % (CountList,Rom_Name_noext,'Runxbe( "' + Output_Path + Rom_Name_noext + '.cut" )',TBN_File + Rom_Name_noext + '.tbn',TBN_File + Rom_Name_noext + '.tbn')
							outputmenufile.write( WriteMenuFile )
							
						with open(Output_Path + Rom_Name_noext + '.cut', "w") as outputfile:
							if Emu_Name == "fba":
								WriteFile = CUT_File_Layout % ( Emu_XBE,FBA_Rom_Name,Rom_Name_noext )
							elif Emu_Name == "mame":
								WriteFile = CUT_File_Layout % ( Emu_XBE,Rom_Name_noext,Rom_Name_noext )
							else:
								WriteFile = CUT_File_Layout % ( Emu_XBE,Rom_Name_noext,Rom_Path )
							outputfile.write( WriteFile )
							
						CountList = CountList + 1
		else:
			shutil.rmtree( Output_Path )# remove old cut files
			if not os.path.isdir( Output_Path ): os.makedirs( Output_Path )
					
	with open( Content_List_Path + Emu_Name + '.xml', "a") as outputmenufile:
		WriteMenuFile = menu_entry_footer
		outputmenufile.write( WriteMenuFile )
		
	if ( Found_Roms == 1 ):
		xbmcgui.Window(xbmcgui.getCurrentWindowId()).setProperty("MyScript.ExternalRunning", "True")
		xbmc.executebuiltin('RunScript(' + Scripts_Path + 'scan.py,scan_emus,scan_cuts,0)' )
		
		while (xbmcgui.Window(xbmcgui.getCurrentWindowId()).getProperty("MyScript.ExternalRunning") == "True"):
			time.sleep(0.2)

		xbmc.executebuiltin('RunScript(' + Scripts_Path + 'create layouts.py)' )
	pDialog.close()
	return

def full_scan(): ## not working yet

	Found_Roms = 0
	Parse_FBL_XML = 0
	
	if os.path.isdir( Emulator_Path ):
	
		for Emu_Path in sorted( os.listdir( Emulator_Path ) ):
		
			CountList = 1
			
			if os.path.isdir( os.path.join( Emulator_Path, Emu_Path ) ):
			
				Emu_Path = os.path.join( Emulator_Path, Emu_Path ) + '\\'
				Emu_Name = os.path.split(os.path.dirname( Emu_Path ))[1]
				
				if os.path.isfile( Content_List_Path + Emu_Name + '.xml' ): os.remove( Content_List_Path + Emu_Name + '.xml' )
				
				with open( Content_List_Path + Emu_Name + '.xml', "w") as outputmenufile:
				
					WriteMenuFile = menu_entry_header
					outputmenufile.write( WriteMenuFile )
					
				if os.path.isfile( os.path.join( Emu_Path, "default.xbe" ) ):
				
					Emu_XBE = os.path.join( Emu_Path, "default.xbe" )
				
					if Emu_Name == "fba":
						Roms_Folder	= Emulator_Path + '\\fba\\roms\\'
						Parse_FBL_XML = 1
					elif Emu_Name == "mame":
						Roms_Folder	= Emulator_Path + '\\mame\\roms\\'
					else:
						Roms_Folder	= Roms_Path + Emu_Name
						
					if Roms_Folder.startswith("Q:\\"): Roms_Folder = Roms_Folder.replace( "Q:\\", Root_Directory )
					
					Output_Path = os.path.join( CUTFile_Path, Emu_Name ) + '\\'
					TBN_File = os.path.join( TBN_Path, Emu_Name ) + '\\'
					
					if len(os.listdir( Roms_Folder )) > 0:
					
						for Items in sorted( os.listdir( Roms_Folder ) ):
						
							if Items.endswith(tuple(Extensions)):
							
								Rom_Name = Items
								Rom_Name_noext = Rom_Name[:-4]
								Rom_Path = os.path.join( Roms_Folder, Rom_Name )
								
								if Parse_FBL_XML == 1:
								
									if os.path.isfile( os.path.join( Emulator_Path, "fba\\info\\emulation\\" ) + Rom_Name_noext + ".ini" ):
										with open( os.path.join( Emulator_Path, "fba\\info\\emulation\\" ) + Rom_Name_noext + ".ini", 'r') as ini:
											FBA_Rom_Name = ini.readline()[:-1]
									else:
										FBA_Rom_Name = Rom_Name_noext
										
									if CountList == 1 and Found_Roms == 0: pDialog.create( "Scanning for Roms","","Please wait..." )
									
									Found_Roms = 1

									if not os.path.isdir( TBN_File ): os.makedirs( TBN_File )

									if CountList == 1 and os.path.isdir( Output_Path ):
									
										pDialog.update( 0,"","Doing house cleaning" )
										shutil.rmtree( Output_Path )# remove old cut files
					
									if not os.path.isdir( Output_Path ): os.makedirs( Output_Path )
									
									pDialog.update( ( CountList * 100 ) / len( os.listdir( Roms_Folder ) ),"Processing [B][UPPERCASE]" + Emu_Name + "[/UPPERCASE][/B] Roms",Rom_Name_noext,"Please wait..." )
									
									with open( Content_List_Path + Emu_Name + '.xml', "a") as outputmenufile:
										if Emu_Name == "fba":
											WriteMenuFile = menu_entry % (CountList,FBA_Rom_Name,'Runxbe( "' + Output_Path + Rom_Name_noext + '.cut" )',TBN_File + Rom_Name_noext + '.tbn',TBN_File + Rom_Name_noext + '.tbn')
										elif Emu_Name == "mame":
											WriteMenuFile = menu_entry % (CountList,Rom_Name_noext,'Runxbe( "' + Output_Path + Rom_Name_noext + '.cut" )',TBN_File + Rom_Name_noext + '.tbn',TBN_File + Rom_Name_noext + '.tbn')
										else:
											WriteMenuFile = menu_entry % (CountList,Rom_Name_noext,'Runxbe( "' + Output_Path + Rom_Name_noext + '.cut" )',TBN_File + Rom_Name_noext + '.tbn',TBN_File + Rom_Name_noext + '.tbn')
										outputmenufile.write( WriteMenuFile )
									
									with open(Output_Path + Rom_Name_noext + '.cut', "w") as outputfile:
										if Emu_Name == "fba":
											WriteFile = CUT_File_Layout % ( Emu_XBE,FBA_Rom_Name,Rom_Name_noext )
										elif Emu_Name == "mame":
											WriteFile = CUT_File_Layout % ( Emu_XBE,Rom_Name_noext,Rom_Name_noext )
										else:
											WriteFile = CUT_File_Layout % ( Emu_XBE,Rom_Name_noext,Rom_Path )
										outputfile.write( WriteFile )
									CountList = CountList + 1
					
					else:
						shutil.rmtree( Output_Path )# remove old cut files
						if not os.path.isdir( Output_Path ): os.makedirs( Output_Path )
						
			with open( Content_List_Path + Emu_Name + '.xml', "a") as outputmenufile:
				WriteMenuFile = menu_entry_footer
				outputmenufile.write( WriteMenuFile )
				
	if ( Found_Roms == 1 ):
		xbmcgui.Window(xbmcgui.getCurrentWindowId()).setProperty("MyScript.ExternalRunning", "True")
		xbmc.executebuiltin('RunScript(' + Scripts_Path + 'scan.py,scan_emus,scan_cuts,scan_xbes)' )
		
		while (xbmcgui.Window(xbmcgui.getCurrentWindowId()).getProperty("MyScript.ExternalRunning") == "True"):
			time.sleep(0.2)

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
if not os.path.isdir( Content_List_Path + 'merged' ): os.makedirs( Content_List_Path + 'merged' )

if Manual_Scan == "manual" : manual_scan()
if Full_Scan == "auto" : full_scan()

pDialog.update(0)
pDialog.close()
#dialog.ok( "","","Process Complete" )