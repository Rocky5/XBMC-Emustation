import os, time, xbmc, xbmcgui
#####	Start markings for the log file.
print "| intro.py loaded."
## Updated by Rocky5 to add dynamic extensions and other stuff
filename	= xbmc.getInfoLabel( 'Skin.String(selectedintrofile)' )
Extensions	= [ "avi","mp4","wmv","xmv" ]
if not xbmc.getCondVisibility( 'Skin.HasSetting(gameloaded)' ):
	if os.path.isfile(filename):
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
						time.sleep( 0.2 )
					xbmc.executebuiltin('ActivateWindow(2999)') # load the startup
	else:
		print "No intro video found: "+filename
		xbmc.executebuiltin('ActivateWindow(2999)') # load the startup
else: xbmc.executebuiltin('ActivateWindow(2999)') # load the startup