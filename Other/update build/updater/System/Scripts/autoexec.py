import fileinput, os, shutil, time, xbmc, xbmcgui, zipfile
Root_Directory	= xbmc.translatePath("Special://root/")[:-8]
zip_file = os.path.join(Root_Directory, 'updater/Update Files/update-files.zip')
zip_file_emus = os.path.join(Root_Directory, 'updater/Update Files/update-files-emus.zip')
xbmc.executebuiltin('Skin.SetString(DashboardUpdatedSmall,0)')
xbmc.executebuiltin('Skin.SetString(EmulatorsUpdatedSmall,0)')
xbmc.executebuiltin('Skin.Reset(DashboardUpdated)')
xbmc.executebuiltin('Skin.Reset(EmulatorsUpdated)')
pDialog	= xbmcgui.DialogProgress()
dialog	= xbmcgui.Dialog()
pDialog.update(0)

if os.path.isfile(zip_file):
	pDialog.create('Stage 2 of 3')

##############################################################
## Update folder names and remove old crap no longer needed

	if os.path.isdir(Root_Directory+'.emustation'):
		os.rename(Root_Directory+'.emustation', Root_Directory+'emustation')

	if os.path.isdir(Root_Directory+'system/scripts/.modules'):
		shutil.rmtree(Root_Directory+'system/scripts/.modules')

	if os.path.isfile(os.path.join(Root_Directory,'emustation/themes/simple/xml/Custom_Changes.xml')):
		os.remove(os.path.join(Root_Directory,'emustation/themes/simple/xml/Custom_Changes.xml'))
	
	if os.path.isfile(os.path.join(Root_Directory,'emustation/themes/simple/xml_sd_pal/Custom_Changes.xml')):
		os.remove(os.path.join(Root_Directory,'emustation/themes/simple/xml_sd_pal/Custom_Changes.xml'))
	
	if os.path.isfile(os.path.join(Root_Directory,'emustation/themes/simple/xml_sd_ntsc/Custom_Changes.xml')):
		os.remove(os.path.join(Root_Directory,'emustation/themes/simple/xml_sd_ntsc/Custom_Changes.xml'))

	if os.path.isdir(os.path.join(Root_Directory,'emustation/themes/simple/.xml_sd_pal')):
		shutil.rmtree(os.path.join(Root_Directory,'emustation/themes/simple/.xml_sd_pal'))
	if os.path.isdir(os.path.join(Root_Directory,'emustation/themes/simple/.xml_sd_ntsc')):
		shutil.rmtree(os.path.join(Root_Directory,'emustation/themes/simple/.xml_sd_ntsc'))

	if os.path.isdir(Root_Directory+'system/backups') and os.path.isdir(Root_Directory+'system/backup'):
		shutil.rmtree(Root_Directory+'system/backup')
	elif os.path.isdir(Root_Directory+'system/backup'):
		os.rename(Root_Directory+'system/backup', Root_Directory+'system/backups')

	if os.path.isfile(Root_Directory+'emustation/themes/simple/xml_sd_pal/Includes_Variables.xml'):
		os.remove(Root_Directory+'emustation/themes/simple/xml_sd_pal/Includes_Variables.xml')
	
	if os.path.isfile(Root_Directory+'emustation/themes/simple/xml_sd_ntsc/Includes_Variables.xml'):
		os.remove(Root_Directory+'emustation/themes/simple/xml_sd_ntsc/Includes_Variables.xml')
	
	if os.path.isfile(Root_Directory+'emustation/themes/simple/xml_sd_pal/Custom_ThemeSelect.xml'):
		os.remove(Root_Directory+'emustation/themes/simple/xml_sd_pal/Custom_ThemeSelect.xml')
	
	if os.path.isfile(Root_Directory+'emustation/themes/simple/xml_sd_ntsc/Custom_ThemeSelect.xml'):
		os.remove(Root_Directory+'emustation/themes/simple/xml_sd_ntsc/Custom_ThemeSelect.xml')
	
	if os.path.isfile(Root_Directory+'emustation/themes/simple/xml/Custom_ThemeSelect.xml'):
		os.remove(Root_Directory+'emustation/themes/simple/xml/Custom_ThemeSelect.xml')
	
	if os.path.isfile(Root_Directory+'splash.png'):
		os.remove(Root_Directory+'splash.png')
	
	if os.path.isfile(Root_Directory+'system/filezilla server.xml'):
		os.remove(Root_Directory+'system/filezilla server.xml')
	
	if os.path.isfile(Root_Directory+'emustation/scripts/updates_check.py'):
		os.remove(Root_Directory+'emustation/scripts/updates_check.py')
	
	if os.path.isfile(Root_Directory+'system/media/static.mp4'):
		os.remove(Root_Directory+'system/media/static.mp4')
	
	if os.path.isdir(Root_Directory +'emustation/themes/simple/720p'):
		shutil.rmtree(Root_Directory+'emustation/themes/simple/720p')
	
	if os.path.isdir(Root_Directory +'emustation/scripts/file types'):
		os.rename(Root_Directory+'emustation/scripts/file types', Root_Directory+'emustation/scripts/rom_extensions')
	
	if os.path.isdir(Root_Directory+'system/media/update'):
		shutil.rmtree(Root_Directory+'system/media/update')
	
	if os.path.isfile(Root_Directory+'emustation/scripts/dialog_res_check.py'):
		os.remove(Root_Directory+'emustation/scripts/dialog_res_check.py')
	
	if os.path.isfile(Root_Directory+'emustation/scripts/sort favourites.py'):
		os.remove(Root_Directory+'emustation/scripts/sort favourites.py')
	
	if os.path.isfile(Root_Directory+'emustation/scripts/last_rom_played.py'):
		os.remove(Root_Directory+'emustation/scripts/last_rom_played.py')
	
	if os.path.isfile(Root_Directory+'emustation/scripts/update_check.py'):
		os.remove(Root_Directory+'emustation/scripts/update_check.py')
	
	if os.path.isdir('E:/TDATA/Rocky5 needs these Logs/XBMC-Emustation'):
		shutil.rmtree('E:/TDATA/Rocky5 needs these Logs/XBMC-Emustation')
		os.mkdir('E:/TDATA/Rocky5 needs these Logs/XBMC-Emustation')	

	if os.path.isdir('E:/UDATA/09999991'): shutil.rmtree('E:/UDATA/09999991')

	if os.path.isdir(Root_Directory+'emustation/scripts/synopsis maker'):
		os.rename(Root_Directory+'emustation/scripts/synopsis maker', Root_Directory+'emustation/scripts/synopsis_maker')

	if os.path.isdir(Root_Directory+'emustation/scripts/rom_extensions'):
		for file in os.listdir(Root_Directory+'emustation/scripts/rom_extensions/'):
			if file.endswith('.ft'):
				file_noext, extension = os.path.splitext(file)
				if os.path.isfile(Root_Directory+'emustation/scripts/rom_extensions/'+file_noext+'.ext'): os.remove(Root_Directory+'emustation/scripts/rom_extensions/'+file_noext+'.ext')
				os.rename(Root_Directory+'emustation/scripts/rom_extensions/'+file, Root_Directory+'emustation/scripts/rom_extensions/'+file_noext+'.ext')

	if os.path.isdir(Root_Directory+'emustation/layouts/home/other'):
		shutil.rmtree(Root_Directory+'emustation/layouts/home/other')
	if os.path.isdir(Root_Directory+'emustation/synopsis/synopsis'):
		shutil.rmtree(Root_Directory+'emustation/synopsis/synopsis')
	if os.path.isdir(Root_Directory+'emustation/layouts'):
		shutil.rmtree(Root_Directory+'emustation/layouts')
	if os.path.isdir(Root_Directory+'default skin'):
		shutil.rmtree(Root_Directory+'default skin')
	if os.path.isdir(Root_Directory+'system/toggles'):
		shutil.rmtree(Root_Directory+'system/toggles')

##############################################################
## Extract the dashboard zip
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
				zip.extract(item, Root_Directory)
			except:
				print "Failed - "+item

##############################################################
## Change some values in the guisettings and favourites xml files
## Backup guisettings.xml and favourites.xml first
	shutil.copy2(os.path.join(Root_Directory, 'system/userdata/guisettings.xml'), os.path.join(Root_Directory, 'system/backups/guisettings.xml'))
	for line in fileinput.input(os.path.join(Root_Directory, 'system/userdata/guisettings.xml'), inplace=1):
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
	if emulator_path.startswith('Q:/'): emulator_path = emulator_path.replace('Q:/',Root_Directory)
	
## Favourites files
	if os.path.isfile(os.path.join(Root_Directory, 'system/userdata/favourites.xml')):
		shutil.copy2(os.path.join(Root_Directory, 'system/userdata/favourites.xml'), os.path.join(Root_Directory, 'system/backups/favourites.xml'))
		for line in fileinput.input(os.path.join(Root_Directory, 'system/userdata/favourites.xml'), inplace=1):
			print line.replace('.emustation', 'emustation'),
	if os.path.isfile(os.path.join(Root_Directory, 'system/userdata/favourites.backup')):
		for line in fileinput.input(os.path.join(Root_Directory, 'system/userdata/favourites.backup'), inplace=1):
			print line.replace('.emustation', 'emustation'),

## Update the progress bar and labels
	xbmc.executebuiltin('Skin.SetBool(DashboardUpdated)')
	pDialog.create('Stage 3 of 3')
	pDialog.update(50,"Download complete","Updating dashboard complete","Updating emulators")

## Extract the emulators zip
	if os.path.isfile(Root_Directory+'emustation/scripts/urldownloader/install_emus.bin'):
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
			os.remove(Root_Directory+'emustation/scripts/urldownloader/install_emus.bin')
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
	if os.path.isdir(os.path.join(Root_Directory,'emustation/themes/simple/xml_sd_pal')):
		os.rename( os.path.join(Root_Directory,'emustation/themes/simple/xml_sd_pal'), os.path.join(Root_Directory,'emustation/themes/simple/.xml_sd_pal') )
	if os.path.isdir(os.path.join(Root_Directory,'emustation/themes/simple/xml_sd_ntsc')):
		os.rename( os.path.join(Root_Directory,'emustation/themes/simple/xml_sd_ntsc'), os.path.join(Root_Directory,'emustation/themes/simple/.xml_sd_ntsc') )
## Write the cleanup script and reload the dashboard xbe
autoexec_data = '''import os, shutil, time, xbmc, xbmcgui
if os.path.isdir('Q:/Updater') and os.path.isfile('E:/CACHE/tmp.bin'):
	while True:
		time.sleep(0.5)
		if xbmc.getCondVisibility('Window.IsVisible(0)'):
			xbmcgui.Dialog().textviewer('Changes.txt', open('Special://root/system/SystemInfo/changes.txt).read())
			shutil.copy2('Q:/Updater/system/xbmc.log','Q:/system/xbmc-updater.log')
			shutil.rmtree('Q:/Updater')
			os.remove('E:/CACHE/tmp.bin')
			os.remove('Q:/system/nointroplay')
			break'''
with open(os.path.join(Root_Directory,'system/scripts/autoexec.py') , 'w') as autoexec: autoexec.write(autoexec_data)
with open(os.path.join(Root_Directory,'system/nointroplay'), 'w') as tmp: tmp.write('')
with open("E:/CACHE/tmp.bin", 'w') as tmp: tmp.write('')
time.sleep(2)
os.remove(xbmc.translatePath("Special://root/default.xbe"))
time.sleep(1)
xbmc.executebuiltin('RunXBE('+ Root_Directory +'default.xbe)')