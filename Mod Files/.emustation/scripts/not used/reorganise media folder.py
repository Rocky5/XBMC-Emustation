'''
	This was used by me when testing layout for the media folder, and settling on a final one
	I made this script to move stuff about and remove old folders.
	
	So this isn't to be used by the public.
'''
import os, shutil, xbmc, xbmcgui
doing this to force an error :)
media = xbmcgui.Dialog().browse( 3,"Select your media folder",'files','' )

for Path in sorted( os.listdir( media ) ):
	Media_Path = os.path.join( media, Path )
	if not os.path.isdir( os.path.join( Media_Path,'boxart' ) ): os.makedirs( os.path.join( Media_Path,'boxart' ) )
	if not os.path.isdir( os.path.join( Media_Path,'boxart3d' ) ): os.makedirs( os.path.join( Media_Path,'boxart3d' ) )
	if not os.path.isdir( os.path.join( Media_Path,'logo' ) ): os.makedirs( os.path.join( Media_Path,'logo' ) )
	if not os.path.isdir( os.path.join( Media_Path,'mix' ) ): os.makedirs( os.path.join( Media_Path,'mix' ) )
	if not os.path.isdir( os.path.join( Media_Path,'screenshots' ) ): os.makedirs( os.path.join( Media_Path,'screenshots' ) )
	if os.path.isdir( os.path.join( Media_Path, 'cartridge' ) ): shutil.rmtree( os.path.join( Media_Path, 'cartridge' )  )
	if os.path.isdir( os.path.join( Media_Path, 'mix-no-video' ) ): shutil.rmtree( os.path.join( Media_Path, 'mix-no-video' )  )
	if os.path.isdir( os.path.join( Media_Path, 'mix-video' ) ): shutil.rmtree( os.path.join( Media_Path, 'mix-video' )  )
	if os.path.isdir( os.path.join( Media_Path, 'previews' ) ): os.rename( os.path.join( Media_Path, 'previews' ), os.path.join( Media_Path, 'videos' )  )

xbmcgui.Dialog().ok("Complete","","Reorganised media folder.")