# -*- coding: utf-8 -*-
import fileinput
import os
import shutil
import time
import xbmc
import xbmcgui
import zipfile

root_directory	= xbmc.translatePath("Special://root/")[:-8]

zip_file = os.path.join(root_directory, 'updater/Update Files/update-files.zip')
zip_file_emus = os.path.join(root_directory, 'updater/Update Files/update-files-emus.zip')

xbmc.executebuiltin('Skin.SetString(DashboardUpdatedSmall,0)')
xbmc.executebuiltin('Skin.SetString(EmulatorsUpdatedSmall,0)')
xbmc.executebuiltin('Skin.Reset(DashboardUpdated)')
xbmc.executebuiltin('Skin.Reset(EmulatorsUpdated)')

pDialog	= xbmcgui.DialogProgress()
dialog	= xbmcgui.Dialog()
pDialog.update(0)

if os.path.isfile(zip_file):
	pDialog.create('Stage 2 of 3')

	# Update folder names and remove old files no longer needed
	# Rename directories
	if os.path.isdir(root_directory + '.emustation'):
		os.rename(root_directory + '.emustation', root_directory + 'emustation')

	if os.path.isdir(root_directory + 'emustation/scripts/file types'):
		os.rename(root_directory + 'emustation/scripts/file types', root_directory + 'emustation/scripts/rom_extensions')

	if os.path.isdir(root_directory + 'emustation/scripts/synopsis maker'):
		os.rename(root_directory + 'emustation/scripts/synopsis maker', root_directory + 'emustation/scripts/synopsis_maker')

	# Remove directories
	directories_to_remove = [
		'system/scripts/.modules',
		'emustation/themes/simple/.xml_sd_pal',
		'emustation/themes/simple/.xml_sd_ntsc',
		'emustation/themes/simple/720p',
		'system/media/update',
		'emustation/layouts/home/other',
		'emustation/synopsis/synopsis',
		'emustation/layouts',
		'default skin',
		'system/toggles'
	]

	for directory in directories_to_remove:
		if os.path.isdir(root_directory + directory):
			shutil.rmtree(root_directory + directory)

	# Remove files
	files_to_remove = [
		'emustation/themes/simple/xml/Custom_Changes.xml',
		'emustation/themes/simple/xml_sd_pal/Custom_Changes.xml',
		'emustation/themes/simple/xml_sd_ntsc/Custom_Changes.xml',
		'emustation/themes/simple/xml_sd_pal/Includes_Variables.xml',
		'emustation/themes/simple/xml_sd_ntsc/Includes_Variables.xml',
		'emustation/themes/simple/xml_sd_pal/Custom_ThemeSelect.xml',
		'emustation/themes/simple/xml_sd_ntsc/Custom_ThemeSelect.xml',
		'emustation/themes/simple/xml/Custom_ThemeSelect.xml',
		'splash.png',
		'system/filezilla server.xml',
		'emustation/scripts/updates_check.py',
		'system/media/static.mp4',
		'emustation/themes/simple/system_list/_sort_name/mgt_sam_coup‚.xml',
		'emustation/themes/simple/system_list/_sort_name/mgt_sam_coupe.xml',
		'emustation/themes/simple/system_list/_sort_name/mgt_sam_coupé.xml',
		'emustation/themes/simple/system_list/_sort_name/nintendo_pok‚mon_mini.xml',
		'emustation/themes/simple/system_list/_sort_name/nintendo_pokemon_mini.xml',
		'emustation/themes/simple/system_list/_sort_name/nintendo_pokémon_mini.xml',
		'emustation/scripts/dialog_res_check.py',
		'emustation/scripts/sort favourites.py',
		'emustation/scripts/last_rom_played.py',
		'emustation/scripts/update_check.py'
	]

	for file in files_to_remove:
		if os.path.isfile(os.path.join(root_directory, file)):
			os.remove(os.path.join(root_directory, file))

	# Backup directories
	if os.path.isdir(root_directory + 'system/backups') and os.path.isdir(root_directory + 'system/backup'):
		shutil.rmtree(root_directory + 'system/backup')
	elif os.path.isdir(root_directory + 'system/backup'):
		os.rename(root_directory + 'system/backup', root_directory + 'system/backups')

	# Remove more
	if os.path.isdir('E:/TDATA/Rocky5 needs these Logs/XBMC-Emustation'):
		shutil.rmtree('E:/TDATA/Rocky5 needs these Logs/XBMC-Emustation')
		os.mkdir('E:/TDATA/Rocky5 needs these Logs/XBMC-Emustation')

	if os.path.isdir('E:/UDATA/09999991'):
		shutil.rmtree('E:/UDATA/09999991')

	if os.path.isdir(root_directory + 'emustation/scripts/rom_extensions'):
		for file in os.listdir(root_directory + 'emustation/scripts/rom_extensions/'):
			if file.endswith('.ft'):
				file_noext, extension = os.path.splitext(file)
				if os.path.isfile(root_directory + 'emustation/scripts/rom_extensions/' + file_noext + '.ext'):
					os.remove(root_directory + 'emustation/scripts/rom_extensions/' + file_noext + '.ext')
				os.rename(root_directory + 'emustation/scripts/rom_extensions/' + file, root_directory + 'emustation/scripts/rom_extensions/' + file_noext + '.ext')


	# Extract the dashboard zip
	with zipfile.ZipFile(zip_file) as zip:
		Total_TXT_Files = len(zip.namelist()) or 1
		Devide = 100.0 / Total_TXT_Files/2
		Percent = 0
		percentsmall = 0
		for item in zip.namelist():
			xbmc.executebuiltin('Skin.SetString(DashboardUpdatedSmall,'+str(int(percentsmall))+')')
			Percent += Devide
			percentsmall += Devide*2
			pDialog.update(int(Percent),"Download complete","Updating dashboard","Updating emulators")
			try:
				zip.extract(item, root_directory)
			except:
				print "Failed - "+item

	# Change some values in the guisettings and favourites xml files
	# Backup guisettings.xml and favourites.xml first
	shutil.copy2(os.path.join(root_directory, 'system/userdata/guisettings.xml'), os.path.join(root_directory, 'system/backups/guisettings.xml'))
	for line in fileinput.input(os.path.join(root_directory, 'system/userdata/guisettings.xml'), inplace=1):
		line = line.replace('<audio>384','<audio>0')
		line = line.replace('<audiotime>8','<audiotime>0')
		line = line.replace('<video>1024','<video>0')
		if line.strip().startswith('<font>'):
			line = '<font>Default</font>\n'
		if line.strip().startswith('<skincolors>'):
			line = '<skincolors>.xml</skincolors>\n'
		if line.strip().startswith('<skintheme>'):
			line = '<skintheme>simple</skintheme>\n'
		if line.strip().startswith('<soundskin>'):
			line = '<soundskin></soundskin>\n'
		if line.strip().startswith('<timeserver>'):
			line = '<timeserver>true</timeserver>\n'
		if line.strip().startswith('<timeserveraddress>'):
			line = '<timeserveraddress>pool.ntp.org</timeserveraddress>\n'
		if 'name="default skin.' in line:
			line = line.replace('name="default skin.', 'name="simple.')
		if 'xbmc/.emustation/' in line:
			line = line.replace('xbmc/.emustation/', 'xbmc/emustation/')
		if 'Q:\.emustation' in line:
			line = line.replace('Q:\.emustation', 'Q:\emustation')
		if 'simple.hide_sd_themes">true' in line:
			with open("Z:/temp/tmp.bin", 'w') as tmp: tmp.write('')
		if 'sort_system_name' in line:
			line = line.replace('true', 'false')
		if 'custom_emulator_path' in line:
			emulator_path = line.split('">')[1].split('</')[0]
		print line,
	
	if emulator_path.startswith('Q:/'):
		emulator_path = emulator_path.replace('Q:/',root_directory)
	
	# Favourites files
	if os.path.isfile(os.path.join(root_directory, 'system/userdata/favourites.xml')):
		shutil.copy2(os.path.join(root_directory, 'system/userdata/favourites.xml'), os.path.join(root_directory, 'system/backups/favourites.xml'))
		for line in fileinput.input(os.path.join(root_directory, 'system/userdata/favourites.xml'), inplace=1):
			print line.replace('.emustation', 'emustation'),
	
	if os.path.isfile(os.path.join(root_directory, 'system/userdata/favourites.backup')):
		for line in fileinput.input(os.path.join(root_directory, 'system/userdata/favourites.backup'), inplace=1):
			print line.replace('.emustation', 'emustation'),


	# Update the progress bar and labels
	xbmc.executebuiltin('Skin.SetBool(DashboardUpdated)')
	pDialog.create('Stage 3 of 3')
	if os.path.isfile(root_directory+'emustation/scripts/urldownloader/install_emus.bin'):
		pDialog.update(50,"Download complete","Updating dashboard complete","Updating emulators")
		# Extract the emulators zip
		with zipfile.ZipFile(zip_file_emus) as zip:
			Total_TXT_Files = len(zip.namelist()) or 1
			Devide = 100.0 / Total_TXT_Files/2
			Percent = 50
			percentsmall = 0
			for item in zip.namelist():
				xbmc.executebuiltin('Skin.SetString(EmulatorsUpdatedSmall,'+str(int(percentsmall))+')')
				Percent += Devide
				percentsmall += Devide*2
				pDialog.update(int(Percent),"Download complete","Updating dashboard complete","Updating emulators")
				try:
					zip.extract(item, emulator_path)
				except:
					print "Failed - "+item
			pDialog.update(100,"Download complete","Updating dashboard complete","Updating emulators complete")
			xbmc.executebuiltin('Skin.SetBool(EmulatorsUpdated)')
			os.remove(root_directory+'emustation/scripts/urldownloader/install_emus.bin')
			time.sleep(3)
	else:
		pDialog.update(100,"Download complete","Updating dashboard complete","")
		time.sleep(3)
else:
	pDialog.create('Error')
	pDialog.update(0,"Download complete","Files are missing")
	time.sleep(5)

if os.path.isfile("Z:/temp/tmp.bin"):
	# Disabled SD folders.
	if os.path.isdir(os.path.join(root_directory,'emustation/themes/simple/xml_sd_pal')):
		os.rename( os.path.join(root_directory,'emustation/themes/simple/xml_sd_pal'), os.path.join(root_directory,'emustation/themes/simple/.xml_sd_pal') )
	if os.path.isdir(os.path.join(root_directory,'emustation/themes/simple/xml_sd_ntsc')):
		os.rename( os.path.join(root_directory,'emustation/themes/simple/xml_sd_ntsc'), os.path.join(root_directory,'emustation/themes/simple/.xml_sd_ntsc') )

# Write the cleanup script and reload the dashboard xbe
autoexec_data = '''import os, shutil, time, xbmc, xbmcgui
if os.path.isdir('Q:/Updater') and os.path.isfile('E:/CACHE/tmp.bin'):
	while True:
		time.sleep(0.5)
		if xbmc.getCondVisibility('Window.IsVisible(0)'):
			xbmcgui.Dialog().textviewer('Changes.txt', open('Special://root/system/SystemInfo/changes.txt').read())
			shutil.copy2('Q:/Updater/system/xbmc.log','Q:/system/xbmc-updater.log')
			shutil.rmtree('Q:/Updater')
			os.remove('E:/CACHE/tmp.bin')
			os.remove('Q:/system/nointroplay')
			break'''

with open(os.path.join(root_directory,'system/scripts/autoexec.py') , 'w') as autoexec: autoexec.write(autoexec_data)
with open(os.path.join(root_directory,'system/nointroplay'), 'w') as tmp: tmp.write('')

with open("E:/CACHE/tmp.bin", 'w') as tmp: tmp.write('')

os.remove(xbmc.translatePath("Special://root/default.xbe"))

time.sleep(2)
xbmc.executebuiltin('RunXBE('+ root_directory +'default.xbe)')