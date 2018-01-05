'''
	Script by Rocky5
	Used to rename all .tbn files to .png and convert the entries in the rom lists to png
'''

import fileinput, glob, os, xbmc, xbmcgui

#####	Start markings for the log file.
print "| _Scripts\XBMC-Emustation\rename_tbn_to_png.py loaded."
pDialog				= xbmcgui.DialogProgress()
dialog				= xbmcgui.Dialog()
Rom_List_Dir		= xbmc.translatePath( 'special://xbmc/_scripts/XBMC-Emustation/rom lists/' )
TBN_List_Dir		= xbmc.translatePath( 'special://xbmc/_tbns/' )

if os.path.isdir( TBN_List_Dir ):
	if os.path.isdir( Rom_List_Dir ):
		pDialog.update(0)
		CountList = 1
		if CountList == 1:	pDialog.create( "Converting Rom lists","Initializing" )
		Rom_List_Files = glob.glob( os.path.join( Rom_List_Dir, "*.xml" ) )
		for Rom_List_File in Rom_List_Files:
			Rom_List_Name = os.path.basename(Rom_List_File)
			pDialog.update( ( ( CountList-1 ) * 100 ) / len( Rom_List_Files ),"Converting Rom Lists to use .png",Rom_List_Name )
			for line in fileinput.input(Rom_List_File, inplace=1):
				line = line.replace('.tbn<','.png<')
				print line,
			CountList = CountList + 1
				
		CountList = 1
		if CountList == 1:	pDialog.create( "Renaming Thumbnails","Initializing" )
		for TBN_Folders in sorted( os.listdir( TBN_List_Dir ) ):
			CountList = 1
			TBN_Files = glob.glob( os.path.join( TBN_List_Dir, TBN_Folders, "*.tbn" ) )
			for TBN_File in TBN_Files:
				pDialog.update( ( ( CountList-1 ) * 100 ) / len( TBN_Files ),"Processing " + TBN_Folders + "","Renaming .tbn files to .png",TBN_File )
				name, ext = os.path.splitext(TBN_File)
				os.rename(TBN_File,name + ".png")
				CountList = CountList + 1
		
		pDialog.close()
		dialog.ok("Complete","","All .tbn files and entries in the[CR]rom list files have been converted to .png")