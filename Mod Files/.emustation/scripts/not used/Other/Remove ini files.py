import os, shutil, xbmc, xbmcgui, glob
pDialog	= xbmcgui.DialogProgress()
dialog	= xbmcgui.Dialog()
Game_Directories = [ "E:\\Games\\", "F:\\Games\\", "G:\\Games\\", "E:\\Games1\\", "F:\\Games1\\", "G:\\Games1\\", "E:\\Games2\\", "F:\\Games2\\", "G:\\Games2\\" ]
for Game_Directories in Game_Directories:
	if os.path.isdir( Game_Directories ):
		pDialog.create( "PARSING XBOX GAMES","Initializing" )
		pDialog.update(0,"Removing _Resources Folders","","This can take some time, please be patient.")
		for Items in sorted( os.listdir( Game_Directories ) ):
			if os.path.isdir(os.path.join( Game_Directories, Items)):
				Game_Directory = os.path.join( Game_Directories, Items )
				for file in glob.glob( Game_Directory + "\\*.ini"):
					DefaultTBN = os.path.join( Game_Directory, file )
					if os.path.isfile(DefaultTBN):
						os.remove(DefaultTBN)
pDialog.close()
dialog.ok("COMPLETE","Done, ini files removed.")