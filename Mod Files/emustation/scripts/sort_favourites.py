import fileinput,os,re,shutil,sys,time,xbmc,xbmcgui
import xml.etree.ElementTree as ET
from random import *
tmp_dir = 'Z:\\temp\\'+str(randint(1, 10000))+"\\"
Favourites_XML				= xbmc.translatePath('special://xbmc/system/userdata/favourites.xml')
Favourites_XML_Backup		= xbmc.translatePath('special://xbmc/system/userdata/favourites.before sorting')
Favourites_XML_TMP			= xbmc.translatePath('Z:/temp/favourites.xml')
pDialog	= xbmcgui.DialogProgress()
dialog	= xbmcgui.Dialog()
counter = 0
pDialog.update(0)
def Fix_Fav_Encoding():
	# Used to fix any unicode txt as eltree doesn't like it.
	shutil.copy2(Favourites_XML,Favourites_XML_TMP)
	for line in fileinput.input(Favourites_XML_TMP, inplace=1):
		line = line.replace("'",'&#39;').replace('&','&amp;')
		print line,
try:
	sort_s	= sys.argv[1:][0]
except:
	sort_s	= 0
if os.path.isfile(Favourites_XML):
	try:
		if os.path.isfile(Favourites_XML_Backup): os.remove(Favourites_XML_Backup)
		Fix_Fav_Encoding()
		tree = ET.parse(Favourites_XML_TMP)
		root = tree.getroot()
		if sort_s:
			xbmc.executebuiltin('Notification(SORTING METHOD,System)')
			shutil.copy2(Favourites_XML,Favourites_XML_Backup)
			time.sleep(1)
			for child in root:
				attrib_name = child.attrib.get('name');
				attrib_thumb = child.attrib.get('thumb');
				child_data = child.text
				sort_name = attrib_name.rsplit('[',1)[1][:-1]+attrib_name[:25]
				fav_data = '    <favourite name="'+attrib_name+'" thumb="'+attrib_thumb+'">'+child_data+'</favourite>'
				if not os.path.isdir(tmp_dir): os.makedirs(tmp_dir)
				save_file = open(tmp_dir+re.sub('[^A-Za-z0-9]+', '', sort_name.lower()), 'w')
				save_file.write(fav_data)
				save_file.close()
		else:
			xbmc.executebuiltin('Notification(SORTING METHOD,Name)')
			shutil.copy2(Favourites_XML,Favourites_XML_Backup)
			time.sleep(1)
			for child in root:
				attrib_name = child.attrib.get('name');
				attrib_thumb = child.attrib.get('thumb');
				child_data = child.text
				sort_name = attrib_name[:25]+attrib_name.rsplit('[',1)[1][:-1]
				fav_data = '    <favourite name="'+attrib_name+'" thumb="'+attrib_thumb+'">'+child_data+'</favourite>'
				if not os.path.isdir(tmp_dir): os.makedirs(tmp_dir)
				save_file = open(tmp_dir+re.sub('[^A-Za-z0-9]+', '', sort_name.lower()), 'w')
				save_file.write(fav_data)
				save_file.close()
				
		if os.path.isdir(tmp_dir):
			save_file = open(Favourites_XML, 'w')
			save_file.write('<favourites>\n')
			for files in sorted([f for f in os.listdir(tmp_dir)]):
				if os.path.isfile(tmp_dir+files):
					read_file = open(tmp_dir+files, 'r')
					read_file = read_file.readline().replace('$info','$INFO')
					save_file.write(str(read_file)+'\n')
			save_file.write('</favourites>\n')
			save_file.close()
		shutil.rmtree(tmp_dir)
	except:
		dialog.ok("ERROR","Your favourites file is malformed, ElemenTree","doesn't like it so you're here. I tried to fix it","but well it must be really buggered.")
	# Check if we are in a favs menu reload the menu.
	if xbmc.getCondVisibility('Window.IsVisible(10134)'):
		xbmc.executebuiltin('Dialog.Close(134,true)');
		time.sleep(0.1)
		xbmc.executebuiltin('RunScript(special://emustation_scripts/menu_loader.py,favs)')