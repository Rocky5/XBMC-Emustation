import os, time, xbmc, xbmcgui

## Updated by Rocky5 to add dynamic extensions

filename = xbmc.getInfoLabel( 'Skin.String(selectedintrofile)' )
	
Extensions		= [ "avi","mp4","wmv","xmv" ]
intro_found = 0

if filename.endswith(tuple(Extensions)):
	isplayed = xbmc.getInfoLabel( "Window(Home).Property(intro.isplayed)" ).lower() == "true"
	winPrograms = xbmc.getCondVisibility( 'Window.IsVisible(Programs)' )

	if not isplayed or winPrograms:
		ReplaceWindowHome = not winPrograms
		print "XBMC Intro Movie"

		if filename.endswith("xmv") or filename.endswith("mp4"):
			print "dvdplayer"
			player = xbmc.Player( xbmc.PLAYER_CORE_DVDPLAYER )
		else:
			print "mplayer"
			player = xbmc.Player( xbmc.PLAYER_CORE_MPLAYER )
		player.play( filename )
		xbmcgui.Window( 10000 ).setProperty( "intro.isplayed", "true" )

		if ReplaceWindowHome:
			xbmc.sleep( 500 )

			while player.isPlaying():
				#continue
				time.sleep( .2 )

			xbmc.executebuiltin( "ReplaceWindow(Home)" )

			xbmc.sleep( 1000 )
			intro_found = 1
		
if not intro_found: xbmc.executebuiltin( "ReplaceWindow(Home)" )