import os, shutil, xbmc, xbmcgui
pDialog	= xbmcgui.DialogProgress()
dialog	= xbmcgui.Dialog()
Game_Directories = [ "E:\\Games\\", "F:\\Games\\", "G:\\Games\\", "E:\\Applications\\", "F:\\Applications\\", "G:\\Applications\\", "E:\\Homebrew\\", "F:\\Homebrew\\", "G:\\Homebrew\\", "E:\\Apps\\", "F:\\Apps\\", "G:\\Apps\\", "E:\\Ports\\", "F:\\Ports\\", "G:\\Ports\\" ]
for Game_Directories in Game_Directories:
	if os.path.isdir( Game_Directories ):
		pDialog.create( "PARSING XBOX GAMES","Initializing" )
		pDialog.update(0,"Removing _Resources Folders","","This can take some time, please be patient.")
		for Items in sorted( os.listdir( Game_Directories ) ):
			if os.path.isdir(os.path.join( Game_Directories, Items)):
				Game_Directory = os.path.join( Game_Directories, Items )
				_Resources = os.path.join( Game_Directory, "_Resources" )
				DefaultTBN = os.path.join( Game_Directory, "default.tbn" )
				FanartJPG = os.path.join( Game_Directory, "fanart.jpg" )
				if os.path.isdir(_Resources):
					shutil.rmtree(_Resources)
				else:
					print "Cannot find: " + _Resources
				if os.path.isfile(DefaultTBN):
					os.remove(DefaultTBN)
				else:
					print "Cannot find: " + DefaultTBN
				if os.path.isfile(FanartJPG):
					os.remove(FanartJPG)
				else:
					print "Cannot find: " + FanartJPG
pDialog.close()
dialog.ok("COMPLETE","Done, _Resources Folders Removed.")