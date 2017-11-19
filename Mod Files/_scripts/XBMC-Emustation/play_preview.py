import glob, os, time, xbmc, xbmcgui

## Play preview video if it exists
# Gets current XBMC-Emustation directory.
CharCount = 100 # How many characters you want after 'The executable running is: '
with open( xbmc.translatePath( "special://xbmc/system/" ) + "xbmc.log", "r" ) as XBMCLOG:
	for line in XBMCLOG:
		left,found,right = line.partition("The executable running is: ")
		if found:
			Working_Directory		= ( right[:CharCount] )
			Root_Directory 			= Working_Directory[:-12] # Removed \default.xbe
			if str( xbmc.getCondVisibility( 'Skin.String(Custom_Preview_Path)' ) ) == "1":
				Previews_Path		= xbmc.getInfoLabel( 'Skin.String(Custom_Preview_Path)' )
			else:
				Previews_Path		= Root_Directory + '_previews\\'
			Path	= os.path.join( Previews_Path, xbmc.getInfoLabel('Skin.String(emuname)') )
			if xbmc.getInfoLabel('Skin.String(emuname)') == "xbox":
				FileName	= xbmc.getInfoLabel('ListItem.Label')
				Focus		= "50"
			else:
				FileName	= xbmc.getInfoLabel('Container(9000).ListItem.Label')
				Focus		= "9000"
			Extensions	= [ "avi","mp4","wmv","xmv" ]
			if xbmc.Player().isPlayingVideo():
				xbmc.Player().stop()
				xbmc.executebuiltin( 'SetFocus(' + Focus + ')' )
			else:
				for VideoFile in glob.glob( os.path.join( Path, FileName + ".*") ):
					if os.path.isfile( VideoFile ):
						if VideoFile.endswith(tuple(Extensions)):
							if VideoFile.endswith("xmv") or VideoFile.endswith("mp4"):
								print "dvdplayer"
								player = xbmc.Player( xbmc.PLAYER_CORE_DVDPLAYER )
							else:
								print "mplayer"
								player = xbmc.Player( xbmc.PLAYER_CORE_MPLAYER )
							xbmc.executebuiltin( 'playmedia( ' + VideoFile + ',1,noresume )' )
							xbmc.executebuiltin( 'setfocus(9100)' )
						
					else: pass