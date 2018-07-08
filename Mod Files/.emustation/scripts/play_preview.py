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
Current_System = xbmc.getInfoLabel('Skin.String(emuname)')
if Current_System == "ports":
	Focus		= "50"
	Path		= xbmc.getInfoLabel('listitem.path')
	#if xbmc.getCondVisibility( 'Skin.HasSetting(resourcesvideo)' ): Path = os.path.join( Path, '_resources\\media\\')
	FileName	= "Preview"
else:
	Focus		= "9000"
	FileName = xbmc.getInfoLabel('Container(9000).ListItem.Thumb')[:-4]
	Path	= os.path.join( Media_Folder_Path, Current_System, 'videos', FileName )
try:
	if int(Current_Memory) >= 8:
		if xbmc.getCondVisibility( 'Skin.HasSetting(synopsislayout)' ):
			VideoFile = ""
			if xbmc.Player().isPlayingVideo():
				xbmc.Player().stop()
				xbmc.executebuiltin( 'SetFocus(' + Focus + ')' )
			else:
				for Files in glob.glob( Path+ ".*" ):
					VideoFile = Files.lower()
				if os.path.isfile( VideoFile ):
					if VideoFile.endswith("xmv") or VideoFile.endswith("mp4"):
						player = xbmc.Player( xbmc.PLAYER_CORE_DVDPLAYER )
					else:
						player = xbmc.Player( xbmc.PLAYER_CORE_MPLAYER )
					xbmc.executebuiltin( 'playmedia( ' + VideoFile + ',1,noresume )' )
					time.sleep(1)
					xbmc.executebuiltin( 'SetFocus(9100)' )
				else:
					player = xbmc.Player( xbmc.PLAYER_CORE_MPLAYER )
					xbmc.executebuiltin( 'playmedia( Q:\\default skin\\media\\static.mp4,1,noresume )' )
					xbmc.executebuiltin( 'SetFocus(9100)' )
		else:
			xbmc.executebuiltin( 'SetFocus(' + Focus + ')' )
	else:
		dialog.ok("OOPS!","There isn't enough free ram to play this video.","Current free ram = " + xbmc.getInfoLabel( "system.freememory" ) )
		xbmc.executebuiltin( 'SetFocus(' + Focus + ')' )
except:
	dialog.ok("ERROR","","Please rescan your roms to fix this issue." )
	xbmc.executebuiltin( 'SetFocus(' + Focus + ')' )
	
