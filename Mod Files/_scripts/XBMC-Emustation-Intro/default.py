import os, time, xbmc, xbmcgui

try:
	filename = sys.argv[1]
except:
	filename = ""

if os.path.isfile( xbmc.translatePath( 'Special://xbmc/' + filename ) ):
	isplayed = xbmc.getInfoLabel( "Window(Home).Property(intro.isplayed)" ).lower() == "true"
	winPrograms = xbmc.getCondVisibility( 'Window.IsVisible(Programs)' )

	if not isplayed or winPrograms:
		ReplaceWindowHome = not winPrograms
		print "XBMC Intro Movie"

		intro = xbmc.translatePath( 'Special://xbmc/' + filename )
		player = xbmc.Player( xbmc.PLAYER_CORE_MPLAYER )
		#player = xbmc.Player( xbmc.PLAYER_CORE_DVDPLAYER )
		player.play( intro )
		xbmcgui.Window( 10000 ).setProperty( "intro.isplayed", "true" )

		if ReplaceWindowHome:
			xbmc.sleep( 500 )

			while player.isPlaying():
				#continue
				time.sleep( .2 )

			xbmc.executebuiltin( "ReplaceWindow(Home)" )

			xbmc.sleep( 1000 )
else:
	xbmc.executebuiltin( "ReplaceWindow(Home)" )