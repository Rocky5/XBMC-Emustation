import fileinput
import os
import shutil
import xbmc
import xbmcgui

Current_name = xbmc.getInfoLabel('Container(9000).ListItem.Label')
Emu_Name = xbmc.getInfoLabel('Skin.String(emuname)')
Root_Directory = xbmc.translatePath("Special://root/")
Emulator_Folder_Path = xbmc.getInfoLabel('Skin.String(Custom_Emulator_Path)') if str(xbmc.getCondVisibility('Skin.String(Custom_Emulator_Path)')) == '1' else os.path.join(Root_Directory, 'emustation', 'emulators')

Favourites_XML = xbmc.translatePath('special://Profile/favourites.xml')
Favourites_XML_Backup = xbmc.translatePath('special://Profile/favourites.backup')
Scripts_Path = os.path.join(Root_Directory, 'emustation', 'scripts')
Favs_List_XML = os.path.join(Root_Directory, 'emustation', 'gamelists', Emu_Name, 'favslist.xml')

if not os.path.isfile(Favourites_XML):
	with open(Favourites_XML, 'w') as f:
		f.write('<favourites>\n</favourites>')

if os.path.isfile(Favs_List_XML):
	try:
		with open(Favs_List_XML) as file:
			favlist_content = file.read()

		segments = favlist_content.split("<favourites>")

		for line in segments:
			if Current_name + '|' in line:
				TMP = line.split("</favourites>")[0].split("|")
				Display_Name, Emu_Path, Rom_Path = TMP
				Emu_Path = os.path.join('$INFO[skin.string(custom_emulator_path)]', Emu_Name, Emu_Path)
				if Emu_Name not in {"fba", "fbl", "fblc", "fbaxxx", "mame", "scummvm"}:
					Rom_Path = os.path.join('$INFO[skin.string(custom_roms_path)]', Emu_Name, Rom_Path)
				break

		if Emu_Path.startswith("Q:\\"):
			Emu_Path = Emu_Path.replace("Q:\\", Root_Directory)
		if Rom_Path.startswith("Q:\\"):
			Rom_Path = Rom_Path.replace("Q:\\", Root_Directory)

		Favourite_String = (
			'    <favourite name="{} [{}]" thumb="{}">'
			'RunScript("{}","{}","{}",1,0)</favourite>'
		).format(
			Display_Name,
			Emu_Name,
			os.path.join(xbmc.getInfoLabel('skin.string(Custom_Media_Path)'),
			Emu_Name, xbmc.getInfoLabel('Skin.String({}_artworkfolder)'.format(Emu_Name)),
			xbmc.getInfoLabel('Container(9000).ListItem.Thumb')),
			os.path.join(Scripts_Path, 'launcher.py'),
			Emu_Path,
			Rom_Path
		)

		if 'name="{} [{}]"'.format(Current_name, Emu_Name) in open(Favourites_XML).read():
			xbmc.executebuiltin('Notification(DOH!,This rom has already been added.)')
			xbmc.executebuiltin('SetFocus(9000)')
		else:
			for line in fileinput.input(Favourites_XML, inplace=1):
				if line.startswith('<favourites />'):
					line = line.replace('<favourites />', '<favourites>\n{}\n</favourites>'.format(Favourite_String))
				else:
					line = line.replace('</favourites>', '{}\n</favourites>'.format(Favourite_String))
				print(line),
			shutil.copy2(Favourites_XML, Favourites_XML_Backup)
			xbmc.executebuiltin("Notification({}, Has been added to your favourites.)".format(Display_Name.upper().replace(',', ' ')))
			xbmc.executebuiltin('RunScript({})'.format(os.path.join(Scripts_Path, 'update_favs_counter.py')))
			xbmc.executebuiltin('SetFocus(9000)')
	except IOError:
		pass
else:
	xbmc.executebuiltin('Notification(ERROR,Please rescan your roms.)')
	xbmc.executebuiltin('SetFocus(9000)')