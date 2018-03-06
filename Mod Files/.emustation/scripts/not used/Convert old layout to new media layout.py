'''
	This is to be used for converting the old _ folder system to the new media system.
	
	Select your _tbns folder first followed by the _previews folder and I do the rest.
	When complete you can move the media folder into the .emustation folder or set a
	custom path via the Other Settings menu.	
'''
import os, shutil, xbmc, xbmcgui
pDialog	= xbmcgui.DialogProgress()
dialog	= xbmcgui.Dialog()
folder1 = dialog.browse( 3,"Select old _tbns folder",'files','' )
folder2 = dialog.browse( 3,"Select old _previews folder",'files','' )
pDialog.create( "Restructuring old _tbns folder." )
for Path in sorted( os.listdir( folder1 ) ):
	CountList = 0
	New_Media_Path = os.path.join( folder1, Path, 'boxart' )
	Old_Media_Path = os.path.join( folder1, Path )
	Media_Path = os.path.join( folder1, Path )
	if not os.path.isdir( os.path.join( Media_Path,'boxart' ) ): os.makedirs( os.path.join( Media_Path,'boxart' ) )
	if not os.path.isdir( os.path.join( Media_Path,'boxart3d' ) ): os.makedirs( os.path.join( Media_Path,'boxart3d' ) )
	if not os.path.isdir( os.path.join( Media_Path,'logo' ) ): os.makedirs( os.path.join( Media_Path,'logo' ) )
	if not os.path.isdir( os.path.join( Media_Path,'mix' ) ): os.makedirs( os.path.join( Media_Path,'mix' ) )
	if not os.path.isdir( os.path.join( Media_Path,'screenshots' ) ): os.makedirs( os.path.join( Media_Path,'screenshots' ) )
	if not os.path.isdir( os.path.join( Media_Path,'videos' ) ): os.makedirs( os.path.join( Media_Path,'videos' ) )
	for file in sorted( os.listdir( Old_Media_Path ) ):
		if file.endswith('.png'):
			shutil.copyfile( os.path.join( Old_Media_Path,file ), os.path.join( New_Media_Path,file ) )
			if os.path.isfile( os.path.join( folder1, Path, file ) ): os.remove( os.path.join( folder1, Path, file )  )
			pDialog.update((CountList * 100) / len(os.listdir( Old_Media_Path )),"Restructuring old _tbns folder.",file,"This can take some time, please be patient." )
			CountList = CountList + 1
pDialog.create( "Transplanting _previews folder." )
for Path in sorted( os.listdir( folder2 ) ):
	CountList = 0
	New_Media_Path = os.path.join( folder1, Path, 'videos' )
	Old_Media_Path = os.path.join( folder2, Path )
	Media_Path = os.path.join( folder2, Path )
	for file in sorted( os.listdir( Old_Media_Path ) ):
		if os.path.isfile( os.path.join( Old_Media_Path,file ) ):
			try:
				shutil.copyfile( os.path.join( Old_Media_Path,file ), os.path.join( New_Media_Path,file ) )
				if os.path.isfile( os.path.join( folder2, Path, file ) ): os.remove( os.path.join( folder2, Path, file )  )
				pDialog.update((CountList * 100) / len(os.listdir( Old_Media_Path )),"Transplanting _previews folder.",file,"This can take some time, please be patient." )
				CountList = CountList + 1
			except:
				pass
os.rename( folder1, folder1[:-6] + 'media' )
shutil.rmtree( folder2 )
dialog.ok("Complete","Now you can rename your _emulators folder to","emulators and your _roms folder to roms","and move them into .emustation folder.")