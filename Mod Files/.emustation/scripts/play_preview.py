'''
	Script by Rocky5
	Used to find and play a preview video for the selected control ID.
'''

import glob, os, xbmc, xbmcgui, time
## Play preview video if it exists
dialog	= xbmcgui.Dialog()
Current_Memory = xbmc.getInfoLabel( "system.freememory" )[:-2]
if str( xbmc.getCondVisibility( 'Skin.String(Custom_Media_Path)' ) ) == "1":
	Media_Folder_Path		= xbmc.getInfoLabel( 'Skin.String(Custom_Media_Path)' )
else:
	Media_Folder_Path		= 'Q:\\.emustation\\media\\'

if xbmc.getInfoLabel('Skin.String(emuname)') == "xbox" or xbmc.getInfoLabel('Skin.String(emuname)') == "ports":
	Focus		= "50"
	Path		= xbmc.getInfoLabel('listitem.path')
	if xbmc.getCondVisibility( 'Skin.HasSetting(resourcesvideo)' ): Path = os.path.join( Path, '_resources\\media\\')
	FileName	= "Preview"
else:
	Focus		= "9000"
	Path		= os.path.join( Media_Folder_Path, xbmc.getInfoLabel('Skin.String(emuname)'), 'videos' )
	if xbmc.getInfoLabel('Skin.String(emuname)') == "fba":
		# this is a fix because I use the rom names for all emulators other than fba, as you wouldn't have a clue what's what game.
		# fba rom names are stored in the <icon> tag but due to numerical names I had to add a space to the end of each one. this just remove3s said space.
		FileName	= xbmc.getInfoLabel('Container(9000).ListItem.ActualIcon')[:-1]
	else:
		FileName	= xbmc.getInfoLabel('Container(9000).ListItem.Label')

if int(Current_Memory) >= 8:
	if xbmc.getCondVisibility( 'Skin.HasSetting(synopsislayout)' ):
		VideoFile = ""
		if xbmc.Player().isPlayingVideo():
			xbmc.Player().stop()
			xbmc.executebuiltin( 'SetFocus(' + Focus + ')' )
		else:
			for Files in glob.glob( os.path.join( Path, FileName + ".*") ):
				VideoFile = Files
			if os.path.isfile( VideoFile ):
				if VideoFile.endswith("xmv") or VideoFile.endswith("mp4"):
					print "dvdplayer"
					player = xbmc.Player( xbmc.PLAYER_CORE_DVDPLAYER )
				else:
					print "mplayer"
					player = xbmc.Player( xbmc.PLAYER_CORE_MPLAYER )
				xbmc.executebuiltin( 'playmedia( ' + VideoFile + ',1,noresume )' )
				time.sleep(1)
				xbmc.executebuiltin( 'SetFocus(9100)' )
			else:
				xbmc.executebuiltin( 'SetFocus(' + Focus + ')' )
	else:
		xbmc.executebuiltin( 'SetFocus(' + Focus + ')' )
else:
	dialog.ok("OOPS!","There isn't enough free ram to play this video.","Current free ram = " + xbmc.getInfoLabel( "system.freememory" ) )
	xbmc.executebuiltin( 'SetFocus(' + Focus + ')' )