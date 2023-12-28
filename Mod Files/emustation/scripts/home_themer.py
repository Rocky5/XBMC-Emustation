import fileinput, glob, os, sys, time, xbmc, xbmcgui
pDialog				= xbmcgui.DialogProgress()
dialog				= xbmcgui.Dialog()
dialog				= xbmcgui.Dialog()

try:
	# This runs on startup to update the home screen.
	Init_Run		= sys.argv[1:][0]
except:
	Init_Run		= "0"

Resolution 			= xbmc.getInfoLabel('system.screenresolution')
HomeLayout 			= xbmc.getInfoLabel('Skin.CurrentTheme')
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
Home_XML_Path		= xbmc.translatePath('special://skin/' + XML_Mode + 'Home.xml')
Default_Layout_File	= xbmc.translatePath('special://skin/layouts/home/' + Layout_Mode + 'layout.xml')
Layout_File			= xbmc.translatePath('special://xbmc/emustation/themes/' + HomeLayout + '/layouts/home/' + Layout_Mode + 'layout.xml')
System_List			= xbmc.translatePath('special://skin/system_list/system_list.xml')
Jump_List			= xbmc.translatePath('special://skin/system_list/jumplist.xml')
# JumpData			= open(xbmc.translatePath('special://skin/' + XML_Mode + 'Includes_home_overlay.xml')).read()
# Jumpfile			= xbmc.translatePath('special://skin/' + XML_Mode + '_script_home_jumpList.xml')

if xbmc.getCondVisibility('Skin.HasSetting(sort_system_name)'):
	System_Sort		= xbmc.translatePath('special://skin/system_list/_Sort_Name')
else:
	System_Sort		= xbmc.translatePath('special://skin/system_list/_Sort_ID')

Header_Data			= '<window id="10000">\n\
	<defaultcontrol always="true">9000</defaultcontrol>\n\
	<onload>Skin.Reset(editmode)</onload>\n\
	<onload>Skin.Reset(videopreviewhorizontal)</onload>\n\
	<controls>\n\
		<include>SecretPassCode</include>\n\
		<control type="button" id="9100">\n\
			<left>-500</left>\n\
			<onclick>-</onclick>\n\
		</control>\n\
		<control type="button" id="9999">\n\
			<left>-500</left>\n\
			<onfocus>ActivateWindow(Screensaver)</onfocus>\n\
			<visible>!Player.HasAudio</visible>\n\
			<animation effect="fade" start="0" end="100" time="100" delay="1000">WindowOpen</animation>\n\
		</control>\n\
		<control type="button" id="9999">\n\
			<left>-500</left>\n\
			<onfocus>ActivateWindow(2006)</onfocus>\n\
			<visible>Player.HasAudio</visible>\n\
			<animation effect="fade" start="0" end="100" time="100" delay="1000">WindowOpen</animation>\n\
		</control>\n\
		<include>CommonBackground</include>\n\
		<control type="group">\n\
			<include>Home_Animation</include>\n\
			<include>Home_Fav_Animation</include>\n\
	'
Footer_Data				= '\n\
	</control>\n\
	<include>overlay_plane</include>\n\
	</controls>\n\
</window>'
if os.path.isfile(Layout_File):
	try:
		os.remove(Home_XML_Path)
		with open(Layout_File) as layoutfile:
			with open(Home_XML_Path, "w") as inputfile:
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
			with open(Default_Layout_File) as layoutfile:
				with open(Home_XML_Path, "w") as inputfile:
					inputfile.write(Header_Data)
					for code in layoutfile:
						inputfile.write(code)
					inputfile.write(Footer_Data)
		except:
			pass
	else:
		dialog.ok("ERROR!","layout.xml is missing from",'S:\\' + HomeLayout + '\\layouts\\home\\' + Layout_Mode + "","Reinstall this file to fix the issue.")
		Init_Run = ""

if os.path.isdir(System_Sort) and Init_Run == "2":
	xml_counter = 0
	files = sorted(glob.glob(System_Sort+'/*.xml'))
	with open(System_List, "w") as outfile:
		outfile.write('<content>\n')
		for xml in files:
			if not "direct launch" in xml.lower(): 
				with open(xml, "r") as infile:
					outfile.write(infile.read().replace('<item id="">','<item id="'+str(xml_counter)+'">'))
				xml_counter = xml_counter+1
		for xml in files:
			if "direct launch" in xml.lower(): 
				with open(xml, "r") as infile:
					outfile.write(infile.read().replace('<item id="">','<item id="'+str(xml_counter)+'">'))
				xml_counter = xml_counter+1
		outfile.write('\n</content>')

if os.path.isfile(System_List):
	# Starts_with_0 = 0; Starts_with_a = 0; Starts_with_b = 0; Starts_with_c = 0; Starts_with_d = 0; Starts_with_e = 0; Starts_with_f = 0; Starts_with_g = 0; Starts_with_h = 0; Starts_with_i = 0; Starts_with_j = 0; Starts_with_k = 0; Starts_with_l = 0; Starts_with_m = 0; Starts_with_n = 0; Starts_with_o = 0; Starts_with_p = 0; Starts_with_q = 0; Starts_with_r = 0; Starts_with_s = 0; Starts_with_t = 0; Starts_with_u = 0; Starts_with_v = 0; Starts_with_w = 0; Starts_with_x = 0; Starts_with_y = 0; Starts_with_z = 0;
	# xml_counter = 2
	# search_menu_entry	= '<control type="button" id="%s">\n	<label>[UPPERCASE]%s[/UPPERCASE][CR][UPPERCASE]%s[/UPPERCASE]</label>\n	<include>MenuButtonCommonValues</include>\n	<onclick>Dialog.Close(1130)</onclick>\n	<onclick>%s</onclick>\n</control>\n'
	# if os.path.isfile(Jump_List): os.remove(Jump_List)
	# files = sorted(glob.glob(System_Sort+'/*.xml'))
	# for	 xml in files:
		# with open(xml, "r") as infile:
			# for lines in infile.readlines():
				# if '<systemid>' in lines:
					# xml = os.path.basename(xml).lower()
					# system_id = lines.split('>',1)[1].split('<',1)[0].lower()
					# if xbmc.getCondVisibility('Skin.HasSetting('+system_id+'_exists)'):
						# print xml
						# Write_Jump_File = 0
						# if not Starts_with_0:
							# if xml.startswith("#") or xml.startswith("'") or xml[0].isdigit():
								# Starts_with_0 = 1; xml = "#"; Write_Jump_File = 1
						# if not Starts_with_a and xml.startswith("a"): Starts_with_a = 1; Write_Jump_File = 1
						# if not Starts_with_b and xml.startswith("b"): Starts_with_b = 1; Write_Jump_File = 1
						# if not Starts_with_c and xml.startswith("c"): Starts_with_c = 1; Write_Jump_File = 1
						# if not Starts_with_d and xml.startswith("d"): Starts_with_d = 1; Write_Jump_File = 1
						# if not Starts_with_e and xml.startswith("e"): Starts_with_e = 1; Write_Jump_File = 1
						# if not Starts_with_f and xml.startswith("f"): Starts_with_f = 1; Write_Jump_File = 1
						# if not Starts_with_g and xml.startswith("g"): Starts_with_g = 1; Write_Jump_File = 1
						# if not Starts_with_h and xml.startswith("h"): Starts_with_h = 1; Write_Jump_File = 1
						# if not Starts_with_i and xml.startswith("i"): Starts_with_i = 1; Write_Jump_File = 1
						# if not Starts_with_j and xml.startswith("j"): Starts_with_j = 1; Write_Jump_File = 1
						# if not Starts_with_k and xml.startswith("k"): Starts_with_k = 1; Write_Jump_File = 1
						# if not Starts_with_l and xml.startswith("l"): Starts_with_l = 1; Write_Jump_File = 1
						# if not Starts_with_m and xml.startswith("m"): Starts_with_m = 1; Write_Jump_File = 1
						# if not Starts_with_n and xml.startswith("n"): Starts_with_n = 1; Write_Jump_File = 1
						# if not Starts_with_o and xml.startswith("o"): Starts_with_o = 1; Write_Jump_File = 1
						# if not Starts_with_p and xml.startswith("p"): Starts_with_p = 1; Write_Jump_File = 1
						# if not Starts_with_q and xml.startswith("q"): Starts_with_q = 1; Write_Jump_File = 1
						# if not Starts_with_r and xml.startswith("r"): Starts_with_r = 1; Write_Jump_File = 1
						# if not Starts_with_s and xml.startswith("s"): Starts_with_s = 1; Write_Jump_File = 1
						# if not Starts_with_t and xml.startswith("t"): Starts_with_t = 1; Write_Jump_File = 1
						# if not Starts_with_u and xml.startswith("u"): Starts_with_u = 1; Write_Jump_File = 1
						# if not Starts_with_v and xml.startswith("v"): Starts_with_v = 1; Write_Jump_File = 1
						# if not Starts_with_w and xml.startswith("w"): Starts_with_w = 1; Write_Jump_File = 1
						# if not Starts_with_x and xml.startswith("x"): Starts_with_x = 1; Write_Jump_File = 1
						# if not Starts_with_y and xml.startswith("y"): Starts_with_y = 1; Write_Jump_File = 1
						# if not Starts_with_z and xml.startswith("z"): Starts_with_z = 1; Write_Jump_File = 1
						# system_id_pluss = system_id +','+system_id
						# if Write_Jump_File:
							# with open(Jump_List,"a") as outputmenuselectfile:
								# WriteSearchFile = search_menu_entry % (str(xml_counter),xml[:1].upper(),system_id_pluss.upper(),"SetFocus(9000,"+str(xml_counter)+")")
								# outputmenuselectfile.write(WriteSearchFile)
								# system_id_pluss = ""
						# xml_counter = xml_counter+1
	try:
		# with open(Jumpfile, "w") as inputfile:
			# inputfile.write(JumpData)
		# with open(Jump_List) as jumpfile:
			# jumpfile = jumpfile.read()
			# for line in fileinput.FileInput(Jumpfile,inplace=1):
				# if '<!-- jumpcode -->' in line:
					# line = line.replace(line,line+jumpfile)
				# print line,
		with open(System_List) as fin:
				fin = fin.read()
				for line in fileinput.FileInput(Home_XML_Path,inplace=1):
					if '</focusedlayout>' in line:
						if "</focusedlayout> <!-- don't populate -->" in line:
							pass
						else:
							line = line.replace(line,line+fin)
					elif '<!-- Home_Layout -->' in line:
						line = line.replace(line,line+fin)
					print line,
	except:
		pass
else:
	dialog.ok("ERROR!","system_list.xml is missing from","S:\\simple\\system_list\\","Reinstall this file to fix the issue.")
	Init_Run = ""

if Init_Run == "0":
	# required for the custom theme selector to reload the skin and apply the new theme.
	time.sleep(0.1)
	xbmc.executebuiltin('Skin.Reset(ReloadSkin)')
	xbmc.executebuiltin('ReloadSkin')
	xbmc.executebuiltin('Dialog.Close(all,true)')

if Init_Run == "1":
	time.sleep(1)
	# This will determine what screen is loaded.
	if xbmc.getCondVisibility('!Skin.HasSetting(firstrun)'):
		xbmc.executebuiltin('ReplaceWindow(Home)') # loaded so back works
		xbmc.executebuiltin('ActivateWindow(1310)') # welcome screen
	elif xbmc.getCondVisibility('Skin.HasSetting(gameloaded)') and xbmc.getCondVisibility('Skin.HasSetting(lastromlist)'):
		if os.path.isfile('Q:/system/nointroplay'):
			os.remove('Q:/system/nointroplay')
		if xbmc.getCondVisibility('Skin.HasSetting(videolayout)'):
			xbmc.executebuiltin('RunScript(special://emustation_scripts/auto_play_preview.py)')
			xbmc.executebuiltin('ReplaceWindow(Home)') # home screen
		else:
			xbmc.executebuiltin('Skin.Reset(gameloaded)')
			xbmc.executebuiltin('ReplaceWindow(Home)') # loaded so back works
			xbmc.executebuiltin('ActivateWindow(Programs,Static_Menu,return)') # myprograms window
			xbmc.executebuiltin('SetFocus(9000,'+xbmc.getInfoLabel('skin.string(lastrompos)')+')') # last system and rom
	else:
		xbmc.executebuiltin('ReplaceWindow(Home)') # home screen