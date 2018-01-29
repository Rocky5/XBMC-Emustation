'''
	Script by Rocky5
	Used to update the favourites counter.
'''
import os
#####	Start markings for the log file.
print "| .emustation\Scripts\update_favs_counter.py loaded."
try:
	Rom_Mode	= sys.argv[1:][0]
except:
	Rom_Mode	= 0
if Rom_Mode:
	count = str(xbmc.getInfoLabel( 'Container(450).NumItems' ))
	if count == "0":
		xbmc.executebuiltin('Skin.SetString(favs_games,0)')
	else:
		xbmc.executebuiltin('Skin.SetString(favs_games,' + count + ')')
else:
	if not os.path.isfile(xbmc.translatePath( "special://Profile/favourites.xml")):
		f = open(xbmc.translatePath( "special://Profile/favourites.xml"),"w")
		f.write("<favourites>\n")
		f.write("</favourites>")
		f.close()
	with open(xbmc.translatePath( "special://Profile/favourites.xml")) as f:
		contents = f.read()
		count = str(contents.count('name="'))
		if count == "0":
			xbmc.executebuiltin('Skin.SetString(favs_games,0)')
		else:
			xbmc.executebuiltin('Skin.SetString(favs_games,' + count + ')')