import fileinput, glob, os, sys, time, xbmc, xbmcgui
pDialog				= xbmcgui.DialogProgress()
dialog				= xbmcgui.Dialog()
dialog				= xbmcgui.Dialog()

# This runs on startup to update the home screen.
Init_Run = sys.argv[1] if len(sys.argv) > 1 else "0"
Resolution = xbmc.getInfoLabel('system.screenresolution')
HomeLayout = xbmc.getInfoLabel('Skin.CurrentTheme')

# Determine Layout_Mode and XML_Mode
if "PAL" in Resolution and os.path.isdir(os.path.join(xbmc.translatePath('special://skin/xml_sd_pal'))):
	print "SD PAL Mode"
	Layout_Mode = 'sd_pal/'
	XML_Mode = 'xml_sd_pal/'
elif "NTSC" in Resolution and os.path.isdir(os.path.join(xbmc.translatePath('special://skin/xml_sd_ntsc'))) or "480p" in Resolution and os.path.isdir(os.path.join(xbmc.translatePath('special://skin/xml_sd_ntsc'))):
	print "SD NTSC Mode"
	Layout_Mode = 'sd_ntsc/'
	XML_Mode = 'xml_sd_ntsc/'
else:
	print "Progressive Mode"
	Layout_Mode = ''
	XML_Mode = 'xml/'

# File paths
Home_XML_Path = xbmc.translatePath('special://skin/{}Home.xml'.format(XML_Mode))
Default_Layout_File = xbmc.translatePath('special://skin/layouts/home/{}layout.xml'.format(Layout_Mode))
Layout_File = xbmc.translatePath('special://xbmc/emustation/themes/{}/layouts/home/{}layout.xml'.format(HomeLayout,Layout_Mode))
System_List = xbmc.translatePath('special://skin/system_list/system_list.xml')
Jump_List = xbmc.translatePath('special://skin/system_list/jumplist.xml')

if xbmc.getCondVisibility('Skin.HasSetting(sort_system_name)'):
	System_Sort = xbmc.translatePath('special://skin/system_list/_Sort_Name')
else:
	System_Sort = xbmc.translatePath('special://skin/system_list/_Sort_ID')

# Header and Footer data
Header_Data = '''<window id="10000">
	<defaultcontrol always="true">9000</defaultcontrol>
	<onload>Skin.Reset(editmode)</onload>
	<onload>Skin.Reset(videopreviewhorizontal)</onload>
	<controls>
		<include>SecretPassCode</include>
		<control type="button" id="9100">
			<left>-500</left>
			<onclick>-</onclick>
		</control>
		<control type="button" id="9999">
			<left>-500</left>
			<onfocus>ActivateWindow(Screensaver)</onfocus>
			<visible>!Player.HasAudio</visible>
			<animation effect="fade" start="0" end="100" time="100" delay="1000">WindowOpen</animation>
		</control>
		<control type="button" id="9999">
			<left>-500</left>
			<onfocus>ActivateWindow(2006)</onfocus>
			<visible>Player.HasAudio</visible>
			<animation effect="fade" start="0" end="100" time="100" delay="1000">WindowOpen</animation>
		</control>
		<include>CommonBackground</include>
		<control type="group">
			<include>Home_Animation</include>
			<include>Home_Fav_Animation</include>
'''
Footer_Data = '''
	</control>
	<include>overlay_plane</include>
	<include>clock</include>
	</controls>
</window>'''

# Handle layout file
if os.path.isfile(Layout_File):
	try:
		os.remove(Home_XML_Path)
		with open(Layout_File) as layoutfile, open(Home_XML_Path, "w") as inputfile:
			inputfile.write(Header_Data)
			for code in layoutfile:
				inputfile.write(code)
			inputfile.write(Footer_Data)
	except:
		pass
else:
	if os.path.isfile(Default_Layout_File):
		try:
			os.remove(Home_XML_Path)
			with open(Default_Layout_File) as layoutfile, open(Home_XML_Path, "w") as inputfile:
				inputfile.write(Header_Data)
				for code in layoutfile:
					inputfile.write(code)
				inputfile.write(Footer_Data)
		except:
			pass
	else:
		dialog.ok("ERROR!", "layout.xml is missing from", 'S:\\' + HomeLayout + '\\layouts\\home\\' + Layout_Mode, "Reinstall this file to fix the issue.")
		Init_Run = ""

# Generate system list
if os.path.isdir(System_Sort) and Init_Run == "2":
	xml_counter = 0
	files = sorted(glob.glob(System_Sort + '/*.xml'))
	with open(System_List, "w") as outfile:
		outfile.write('<content>\n')
		# Systems with menus go first in the list
		for xml in files:
			if not "direct launch" in xml.lower():
				with open(xml, "r") as infile:
					outfile.write(infile.read().replace('<item id="">','<item id="'+str(xml_counter)+'">'))
				xml_counter = xml_counter+1
		# Direct launch files go at the end of the list
		for xml in files:
			if "direct launch" in xml.lower():
				with open(xml, "r") as infile:
					outfile.write(infile.read().replace('<item id="">','<item id="'+str(xml_counter)+'">'))
				xml_counter = xml_counter+1
		outfile.write('\n</content>')

# Update Home XML
if os.path.isfile(System_List):
	try:
		with open(System_List) as fin:
			system_list_content = fin.read()
			for line in fileinput.FileInput(Home_XML_Path, inplace=1):
				if '</focusedlayout>' in line and "</focusedlayout> <!-- don't populate -->" not in line:
					line += system_list_content
				elif '<!-- Home_Layout -->' in line:
					line += system_list_content
				print line,
	except:
		pass
else:
	dialog.ok("ERROR!", "system_list.xml is missing from", "S:\\simple\\system_list\\", "Reinstall this file to fix the issue.")
	Init_Run = ""

if Init_Run == "0":
	time.sleep(0.1)
	xbmc.executebuiltin('Skin.Reset(ReloadSkin)')
	xbmc.executebuiltin('ReloadSkin')
	xbmc.executebuiltin('Dialog.Close(all,true)')

if Init_Run == "1":
	if xbmc.getCondVisibility('!Skin.HasSetting(firstrun)'):
		xbmc.executebuiltin('ReplaceWindow(Home)')
		xbmc.executebuiltin('ActivateWindow(1310)')
	elif xbmc.getCondVisibility('Skin.HasSetting(gameloaded)') and xbmc.getCondVisibility('Skin.HasSetting(lastromlist)'):
		if os.path.isfile('Q:/system/nointroplay'):
			os.remove('Q:/system/nointroplay')
		if xbmc.getCondVisibility('Skin.HasSetting(videolayout)'):
			xbmc.executebuiltin('RunScript(special://emustation_scripts/auto_play_preview.py)')
			xbmc.executebuiltin('ReplaceWindow(Home)')
		else:
			xbmc.executebuiltin('Skin.Reset(gameloaded)')
			xbmc.executebuiltin('ReplaceWindow(Home)')
			xbmc.executebuiltin('ActivateWindow(Programs,Static_Menu,return)')
			xbmc.executebuiltin('SetFocus(9000,{})'.format(xbmc.getInfoLabel('skin.string(lastrompos)')))
	else:
		time.sleep(1)
		xbmc.executebuiltin('ReplaceWindow(Home)')