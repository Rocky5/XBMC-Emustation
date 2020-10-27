import fileinput, os, sys, time, xbmc, xbmcgui
pDialog					= xbmcgui.DialogProgress()
dialog					= xbmcgui.Dialog()
dialog				= xbmcgui.Dialog()
time.sleep(1)
HomeLayout 			= xbmc.getInfoLabel('Skin.CurrentTheme')
Home_XML_Path		= xbmc.translatePath('special://skin/xml/Home.xml')
Default_Layout_File	= xbmc.translatePath('special://xbmc/emustation/themes/SIMPLE/layouts/home/layout.xml')
Layout_File			= xbmc.translatePath('special://xbmc/emustation/themes/' + HomeLayout + '/layouts/home/layout.xml')
System_List			= xbmc.translatePath('special://xbmc/emustation/themes/SIMPLE/system_list/system_list.xml')
xbmc.executebuiltin('Skin.Reset(ReloadSkin)')
xbmcgui.lock()
Header_Data			= '<window id="10000">\n\
	<defaultcontrol always="true">9000</defaultcontrol>\n\
	<onload>Skin.Reset(editmode)</onload>\n\
	<onload>Skin.Reset(videopreviewhorizontal)</onload>\n\
	<controls>\n\
		<include>SecretPassCode</include>\n\
		<control type="button" id="9100">\n\
			<posx>-500</posx>\n\
			<onclick>-</onclick>\n\
		</control>\n\
		<control type="button" id="9999">\n\
			<posx>-500</posx>\n\
			<onfocus>ActivateWindow(Screensaver)</onfocus>\n\
			<visible>!Player.HasAudio</visible>\n\
			<animation effect="fade" start="0" end="100" time="100" delay="1000">WindowOpen</animation>\n\
		</control>\n\
		<control type="button" id="9999">\n\
			<posx>-500</posx>\n\
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
		xbmcgui.unlock()
		dialog.ok("ERROR!","layout.xml is missing from","Q:\\emustation\\themes\\SIMPLE\\layouts\\home\\","Reinstall this file to fix the issue.")
if os.path.isfile(System_List):
	try:
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
	xbmcgui.unlock()
	dialog.ok("ERROR!","system_list.xml is missing from","Q:\\emustation\\themes\\SIMPLE\\homescreen\\system_list\\","Reinstall this file to fix the issue.")
xbmcgui.unlock()
xbmc.executebuiltin('ActivateWindow(10000)') # required for the custom them selector to reload the skin and apply the new theme.
xbmc.executebuiltin('ReloadSkin') # required for the custom them selector to reload the skin and apply the new theme.