import os, xbmc
try:
	Rom_Mode = sys.argv[1:][0]
except:
	Rom_Mode = 0

if Rom_Mode:
	count = str(xbmc.getInfoLabel('Container(450).NumItems'))
	if count == "0":
		xbmc.executebuiltin('Skin.SetString(favs_games,0)')
	else:
		xbmc.executebuiltin('Skin.SetString(favs_games,' + count + ')')
else:
	if not os.path.isfile("special://Profile/favourites.xml"):
		with open("special://Profile/favourites.xml","w") as f:
			f.write("<favourites>\n</favourites>")
	with open("special://Profile/favourites.xml") as f:
		contents = f.read()
		count = str(contents.count('name="'))
		if count == "0":
			xbmc.executebuiltin('Skin.SetString(favs_games,0)')
		else:
			xbmc.executebuiltin('Skin.SetString(favs_games,' + count + ')')