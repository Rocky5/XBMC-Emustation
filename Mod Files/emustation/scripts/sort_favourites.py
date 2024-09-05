import fileinput,os,re,shutil,sys,time,xbmc,xbmcgui
import xml.etree.ElementTree as ET
from random import *

pDialog	= xbmcgui.DialogProgress()
dialog	= xbmcgui.Dialog()
tmp_dir = 'Z:\\temp\\'+str(randint(1, 10000))+"\\"
Favourites_XML = xbmc.translatePath('special://xbmc/system/userdata/favourites.xml')
Favourites_XML_Backup = xbmc.translatePath('special://xbmc/system/userdata/favourites.before sorting')
Favourites_XML_TMP = xbmc.translatePath('Z:/temp/favourites.xml')
counter = 0
pDialog.update(0)
fav_data_with_sort = []
sort_type = sys.argv[1] if len(sys.argv) > 1 else 0

if os.path.isfile(Favourites_XML):
	try:
		if os.path.isfile(Favourites_XML_Backup):
			os.remove(Favourites_XML_Backup)
		shutil.copy2(Favourites_XML,Favourites_XML_Backup)
		
		with open(Favourites_XML, 'r') as xml:
			content = xml.read().replace('&', '&amp;')

		root = ET.fromstring(content)

		for child in root:
			attrib_name = child.attrib.get('name')
			attrib_thumb = child.attrib.get('thumb')
			child_data = child.text

			if sort_type:
				sort_name = attrib_name.rsplit('[', 1)[1][:-1] + attrib_name[:25]
			else:
				sort_name = attrib_name[:25] + attrib_name.rsplit('[', 1)[1][:-1]
			
			if 'media\\' in attrib_thumb.lower():
				if xbmc.getCondVisibility('Skin.String(Custom_Media_Path)'):
					Media_Folder_Path	 = xbmc.getInfoLabel('Skin.String(Custom_Media_Path)')
				else:
					Media_Folder_Path	 = 'Q:\\emustation\\media\\'
				split_thumb = attrib_thumb.split("media\\")[1]
				attrib_thumb = os.path.join(Media_Folder_Path, split_thumb)

			fav_data = '    <favourite name="{}" thumb="{}">{}</favourite>'.format(attrib_name, attrib_thumb, child_data)

			fav_data_with_sort.append((fav_data, sort_name)) # Append the pair

		with open(Favourites_XML, 'w') as save_file:
			save_file.write('<favourites>\n')
			for fav_data, sort_name in sorted(fav_data_with_sort, key=lambda x: x[1]):
				modified_fav_data = fav_data.replace('$info', '$INFO')
				save_file.write(modified_fav_data + '\n')
			save_file.write('</favourites>\n')
	
		# Check if we are in a favs menu reload the menu.
		if xbmc.getCondVisibility('Window.IsVisible(10134)'):
			xbmc.executebuiltin('RunScript(special://emustation_scripts/menu_loader.py,favs)')
			xbmc.executebuiltin('Dialog.Close(134,true)');
			time.sleep(1)
			if sort_type:
				xbmc.executebuiltin('Notification(SORTING METHOD,System)')
			else:
				xbmc.executebuiltin('Notification(SORTING METHOD,Name)')
	except Exception:
		dialog.ok("ERROR", "Your favourites file is malformed, ElementTree", "doesn't like it so you're here. I tried to fix it", "but well, it must be really buggered.")