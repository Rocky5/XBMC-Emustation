import hashlib, os, xbmc, xbmcgui
dialog	= xbmcgui.Dialog()
m = hashlib.md5()
for line in open( os.path.join( "x:\\downloads\\XBMC-Emustation-update-files.zip" ) ).readlines():
	m.update( line )

dialog.ok( "","Hash is: " + m.hexdigest() )