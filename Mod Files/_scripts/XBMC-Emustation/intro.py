'''
	Script by Rocky5
	Used to play a selected intro video.
'''

import os, time, xbmc, xbmcgui

## Updated by Rocky5 to add dynamic extensions and other stuff

time.sleep(0.5) #give the system time to initialize

filename	= xbmc.getInfoLabel( 'Skin.String(selectedintrofile)' )
Extensions	= [ "avi","mp4","wmv","xmv" ]
intro_found = 0

if os.path.isfile( filename ):
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
				while player.isPlaying():
					#continue
					time.sleep( 0.2 )
				xbmc.sleep( 1000 )
			intro_found = 1
			if str(  xbmc.getCondVisibility( 'Skin.HasSetting(Use_Startup_Playback)' ) ) == "1":
				print "worked"
				xbmc.executebuiltin( 'PlayMedia(' + xbmc.getInfoLabel( 'Skin.String(Startup_Playback_Path)' ) + ')' )
			xbmc.executebuiltin( "ReplaceWindow(Home)" )
else:
	xbmc.executebuiltin( "ReplaceWindow(Home)" )



'''
Original script from here: https://web.archive.org/web/20140712122422/http://passion-xbmc.org/addons/?Page=View&ID=script.xbmc.intro.movie
'''