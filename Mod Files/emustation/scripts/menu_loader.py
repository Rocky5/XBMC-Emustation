import fileinput, os, time, xbmc, xbmcgui
try:
	MenuLabel	= sys.argv[1:][0]
except:
	MenuLabel	=  xbmc.getInfoLabel('Container(9000).ListItem.Label2')
try:
	XBE_Edit_Mode	= sys.argv[2:][0]
except:
	XBE_Edit_Mode	= 0

pDialog			= xbmcgui.DialogProgress()
dialog			= xbmcgui.Dialog()
XBE_Files		= 0
XBE_Content		= 0
EMU_Files		= 0
FAV_Files		= 0
Default_Layout_XML_Path	= "0"
Layout_XML_Path	= "0"
Resolution		= xbmc.getInfoLabel('system.screenresolution')
ThemeType		= xbmc.getInfoLabel('Skin.CurrentTheme')

if "PAL" in Resolution and os.path.isdir(os.path.join(xbmc.translatePath('special://skin/xml_sd_pal'))):
	print "SD PAL Mode"
	Layout_Mode = '/sd_pal'
	XML_Mode = 'xml_sd_pal/'
elif "NTSC" in Resolution and os.path.isdir(os.path.join(xbmc.translatePath('special://skin/xml_sd_ntsc'))) or "480p" in Resolution and os.path.isdir(os.path.join(xbmc.translatePath('special://skin/xml_sd_ntsc'))):
	print "SD NTSC Mode"
	Layout_Mode = '/sd_ntsc'
	XML_Mode = 'xml_sd_ntsc/'
else:
	print "Progressive Mode"
	Layout_Mode = ''
	XML_Mode = 'xml/'

MyPrograms_Path					= xbmc.translatePath('special://skin/' + XML_Mode + 'MyPrograms.xml')
_Script_Jump_Path				= xbmc.translatePath('special://skin/' + XML_Mode + '_script_jumpList.xml')
FAV_XML_Path					= xbmc.translatePath('special://skin/' + XML_Mode + 'DialogFavourites.xml')
Overlay_JumpXML_File			= open(xbmc.translatePath('special://skin/' + XML_Mode + 'Includes_layout_overlay.xml')).read()
Overlay_JumpXML_XBE_File		= open(xbmc.translatePath('special://skin/' + XML_Mode + 'Includes_layout_overlay_xbe.xml')).read()
XML_Files_Path					= xbmc.translatePath('special://xbmc/emustation/gamelists/' + MenuLabel)
Default_Layout_Path				= xbmc.translatePath('special://xbmc/emustation/themes/simple/layouts/default' + Layout_Mode)
Default_Theme_Layout_Path		= xbmc.translatePath('special://xbmc/emustation/themes/' + ThemeType + '/layouts/default' + Layout_Mode)
Custom_Theme_Layout_Path		= xbmc.translatePath('special://xbmc/emustation/themes/' + ThemeType + '/layouts/' + MenuLabel + Layout_Mode)
Default_Favs_Layout_Path		= xbmc.translatePath('special://xbmc/emustation/themes/simple/layouts/favs' + Layout_Mode)
Custom_Theme_Favs_Layout_Path	= xbmc.translatePath('special://xbmc/emustation/themes/' + ThemeType + '/layouts/favs' + Layout_Mode)

Default_Layout					= os.path.join(Default_Theme_Layout_Path, 'layout.xml')
Default_Synopsis_Layout			= os.path.join(Default_Theme_Layout_Path, 'synopsis_layout.xml')
Default_Thumb_Layout			= os.path.join(Default_Theme_Layout_Path, 'thumb_layout.xml')
Default_Video_Layout			= os.path.join(Default_Theme_Layout_Path, 'video_layout.xml')
Default_No_Layout				= os.path.join(Default_Layout_Path, 'layout.xml')
Default_No_Synopsis_Layout		= os.path.join(Default_Layout_Path, 'synopsis_layout.xml')
Default_No_Thumb_Layout			= os.path.join(Default_Layout_Path, 'thumb_layout.xml')
Default_No_Video_Layout			= os.path.join(Default_Layout_Path, 'video_layout.xml')
Custom_Layout					= os.path.join(Custom_Theme_Layout_Path, 'layout.xml')
Custom_Synopsis_Layout			= os.path.join(Custom_Theme_Layout_Path, 'synopsis_layout.xml')
Custom_Thumb_Layout				= os.path.join(Custom_Theme_Layout_Path, 'thumb_layout.xml')
Custom_Video_Layout				= os.path.join(Custom_Theme_Layout_Path, 'video_layout.xml')

Default_Favs_Layout				= os.path.join(Default_Favs_Layout_Path, 'layout.xml')
Default_Favs_Synopsis_Layout	= os.path.join(Default_Favs_Layout_Path, 'synopsis_layout.xml')
Default_Favs_Thumb_Layout		= os.path.join(Default_Favs_Layout_Path, 'thumb_layout.xml')
Default_Favs_Video_Layout		= os.path.join(Default_Favs_Layout_Path, 'video_layout.xml')
Default_No_Favs_Layout			= os.path.join(Default_Favs_Layout_Path, 'layout.xml')
Default_No_Favs_Synopsis_Layout	= os.path.join(Default_Favs_Layout_Path, 'synopsis_layout.xml')
Default_No_Favs_Thumb_Layout	= os.path.join(Default_Favs_Layout_Path, 'thumb_layout.xml')
Default_No_Favs_Video_Layout	= os.path.join(Default_Favs_Layout_Path, 'video_layout.xml')
Custom_Favs_Layout				= os.path.join(Custom_Theme_Favs_Layout_Path, 'layout.xml')
Custom_Favs_Synopsis_Layout		= os.path.join(Custom_Theme_Favs_Layout_Path, 'synopsis_layout.xml')
Custom_Favs_Thumb_Layout		= os.path.join(Custom_Theme_Favs_Layout_Path, 'thumb_layout.xml')
Custom_Favs_Video_Layout		= os.path.join(Custom_Theme_Favs_Layout_Path, 'video_layout.xml')

XBE_Default_Layout				= os.path.join(Default_Theme_Layout_Path, 'XBE files/layout.xml')
XBE_Default_Synopsis_Layout		= os.path.join(Default_Theme_Layout_Path, 'XBE files/synopsis_layout.xml')
XBE_Default_Thumb_Layout		= os.path.join(Default_Theme_Layout_Path, 'XBE files/thumb_layout.xml')
XBE_Default_Video_Layout		= os.path.join(Default_Theme_Layout_Path, 'XBE files/video_layout.xml')
XBE_Default_No_Layout			= os.path.join(Default_Layout_Path, 'XBE files/layout.xml')
XBE_Default_No_Synopsis_Layout	= os.path.join(Default_Layout_Path, 'XBE files/synopsis_layout.xml')
XBE_Default_No_Thumb_Layout		= os.path.join(Default_Layout_Path, 'XBE files/thumb_layout.xml')
XBE_Default_No_Video_Layout		= os.path.join(Default_Layout_Path, 'XBE files/video_layout.xml')


if XBE_Edit_Mode == "editmode" or MenuLabel == "apps" or MenuLabel == "demos":
	XBE_Files = 1
elif MenuLabel == "favs":
	FAV_Files = 1
else:
	EMU_Files = 1

xbmc.executebuiltin('Skin.SetString(emuname,' + MenuLabel + ')')
Header_Data_EMU	= '''<window type="window" id="1">
		<onunload condition="Player.HasVideo">Stop</onunload>
		<defaultcontrol always="true">9000</defaultcontrol>
		<allowoverlay>no</allowoverlay>
		<view>50</view>
		<layout>%s</layout>
		<controls>
		<control type="button" id="9200">
			<left>-500</left>
		</control>
		<control type="group">
				<visible>!Window.IsVisible(1101)</visible>
				<animation type="Hidden">
						<effect type="fade" start="100" end="0" delay="1100" time="1000"/>
				</animation>
				<include>CommonBackground</include>
		</control>
		<control type="group">
		<include>Layout_Animation</include>
		<animation type="Hidden">
				<effect type="zoom" start="100" end="200" center="auto" easing="in" tween="cubic" delay="100" time="1100"/>
				<effect type="fade" start="100" end="0" delay="300" time="600"/>
		</animation>
		<visible>!Window.IsVisible(1101)</visible>
		<!-- Used to run the script and stop folk moving the list forward or backwards -->
		<control type="button" id="9999">
			<left>-500</left>
			<onfocus>RunScript(special://emustation_scripts/play_preview.py)</onfocus>
			<visible>!Skin.HasSetting(videolayout)</visible>
		</control>
		<control type="button" id="9990">
			<left>-500</left>
			<onfocus>SetFocus(9000)</onfocus>
			<onfocus>ActivateWindow(1120)</onfocus>
		</control>
		<!-- Used to stop playback if one of the direction buttons are pressed or the (A) button -->
		<control type="button" id="9100">
			<left>-500</left>
			<onup>setfocus(9000)</onup>
			<ondown>setfocus(9000)</ondown>
			<onleft>setfocus(9000)</onleft>
			<onright>setfocus(9000)</onright>
			<onclick>setfocus(9000)</onclick>
			<onup>stop</onup>
			<ondown>stop</ondown>
			<onleft>stop</onleft>
			<onright>stop</onright>
			<onclick>stop</onclick>
			<onup>Control.Move(9000,-1)</onup>
			<ondown>Control.Move(9000,1)</ondown>
			<onleft>PageUp</onleft>
			<onright>PageDown</onright>
			<visible>!Skin.HasSetting(videolayout) + !Skin.HasSetting(videopreviewhorizontal)</visible>
		</control>
		<control type="button" id="9100">
			<left>-500</left>
			<onup>setfocus(9000)</onup>
			<ondown>setfocus(9000)</ondown>
			<onleft>setfocus(9000)</onleft>
			<onright>setfocus(9000)</onright>
			<onclick>setfocus(9000)</onclick>
			<onup>stop</onup>
			<ondown>stop</ondown>
			<onleft>stop</onleft>
			<onright>stop</onright>
			<onclick>stop</onclick>
			<onup>PageDown</onup>
			<ondown>PageUp</ondown>
			<onleft>Control.Move(9000,-1)</onleft>
			<onright>Control.Move(9000,1)</onright>
			<visible>!Skin.HasSetting(videolayout) + Skin.HasSetting(videopreviewhorizontal)</visible>
		</control>
'''
Footer_Data_EMU	= '''
	</control>
	<include>clock</include>
	</controls>
	</window>
'''
Header_Data_FAVS	= '''<window type="dialog" id="134">
	<defaultcontrol always="true">450</defaultcontrol>
	<onunload>Skin.Reset(favsloading)</onunload>
	<include>Fav_Layout_Animation</include>
	<controls>
		<control type="button" id="9990">
			<left>-500</left>
			<onfocus>SetFocus(1000)</onfocus>
		</control>\n'''
Footer_Data_FAVS	= '''
	<include>clock</include>
	</controls>
	</window>
'''

if not MenuLabel == "xbox" and not MenuLabel == "homebrew" and not MenuLabel == "ports":
	Jump_File_Data	= Overlay_JumpXML_File
else:
	XBE_Content = 1
	Jump_File_Data	= Overlay_JumpXML_XBE_File

Header_Data_XBE	= '''<window id="1">
		<onunload condition="Player.HasVideo">Stop</onunload>
		<defaultcontrol always="true">50</defaultcontrol>
		<allowoverlay>no</allowoverlay>
		<view>50</view>
		<layout>%s</layout>
		<controls>
		<include>CommonBackground</include>
		<control type="group">
		<include>Layout_Animation</include>
		<control type="button" id="9990">
			<left>-500</left>
			<onfocus>SetFocus(50)</onfocus>
			<onfocus>ContextMenu</onfocus>
		</control>
		<control type="button" id="9000">
			<left>-500</left>
			<onfocus>SetFocus(50)</onfocus>
		</control>
		<!-- Used to stop playback if one of the direction buttons are pressed or the (A) button -->
		<control type="button" id="9100">
			<left>-500</left>
			<onup>setfocus(50)</onup>
			<ondown>setfocus(50)</ondown>
			<onleft>setfocus(50)</onleft>
			<onright>setfocus(50)</onright>
			<onclick>setfocus(50)</onclick>
			<onup>stop</onup>
			<ondown>stop</ondown>
			<onleft>stop</onleft>
			<onright>stop</onright>
			<onclick>stop</onclick>
			<onup>Control.Move(50,-1)</onup>
			<ondown>Control.Move(50,1)</ondown>
			<onleft>PageUp</onleft>
			<onright>PageDown</onright>
		</control>
'''
Footer_Data_XBE	= '''
	</control>
	<include>clock</include>
	</controls>
	</window>
'''
if EMU_Files == 1:
	if xbmc.getCondVisibility('Skin.HasSetting(videolayout)'):
		if os.path.isfile(Custom_Video_Layout):
			Layout_XML_Path			= Custom_Video_Layout
		elif os.path.isfile(Default_Video_Layout):
			Default_Layout_XML_Path	= Default_Video_Layout
		elif os.path.isfile(Default_Synopsis_Layout):
			Default_Layout_XML_Path	= Default_Synopsis_Layout
		else:
			Default_Layout_XML_Path	= Default_No_Video_Layout
	
	elif xbmc.getCondVisibility('Skin.HasSetting(synopsislayout)'):
		if os.path.isfile(Custom_Synopsis_Layout):
			Layout_XML_Path			= Custom_Synopsis_Layout
		elif os.path.isfile(Default_Synopsis_Layout):
			Default_Layout_XML_Path	= Default_Synopsis_Layout
		else:
			Default_Layout_XML_Path	= Default_No_Synopsis_Layout
	
	elif xbmc.getCondVisibility('Skin.HasSetting(thumblayout)'):
		if os.path.isfile(Custom_Thumb_Layout):
			Layout_XML_Path			= Custom_Thumb_Layout
		elif os.path.isfile(Default_Thumb_Layout):
			Default_Layout_XML_Path	= Default_Thumb_Layout
		else:
			Default_Layout_XML_Path	= Default_No_Thumb_Layout
	
	else:
		if os.path.isfile(Custom_Layout):
			Layout_XML_Path	= Custom_Layout
		elif os.path.isfile(Default_Layout):
			Default_Layout_XML_Path		= Default_Layout
		else:
			Default_Layout_XML_Path		= Default_No_Layout

elif FAV_Files == 1:
	if xbmc.getCondVisibility('Skin.HasSetting(videolayout)'):
		if os.path.isfile(Custom_Favs_Video_Layout):
			Layout_XML_Path			= Custom_Video_Layout
		elif os.path.isfile(Default_Favs_Video_Layout):
			Default_Layout_XML_Path	= Default_Favs_Video_Layout
		elif os.path.isfile(Default_Favs_Synopsis_Layout):
			Default_Layout_XML_Path	= Default_Favs_Synopsis_Layout
		else:
			Default_Layout_XML_Path	= Default_No_Favs_Video_Layout
	
	elif xbmc.getCondVisibility('Skin.HasSetting(synopsislayout)'):
		if os.path.isfile(Custom_Favs_Synopsis_Layout):
			Layout_XML_Path			= Custom_Favs_Synopsis_Layout
		elif os.path.isfile(Default_Favs_Synopsis_Layout):
			Default_Layout_XML_Path	= Default_Favs_Synopsis_Layout
		else:
			Default_Layout_XML_Path	= Default_No_Favs_Synopsis_Layout
	
	elif xbmc.getCondVisibility('Skin.HasSetting(thumblayout)'):
		if os.path.isfile(Custom_Favs_Thumb_Layout):
			Layout_XML_Path			= Custom_Favs_Thumb_Layout
		elif os.path.isfile(Default_Favs_Thumb_Layout):
			Default_Layout_XML_Path	= Default_Favs_Thumb_Layout
		else:
			Default_Layout_XML_Path	= Default_No_Favs_Thumb_Layout
	
	else:
		if os.path.isfile(Custom_Favs_Layout):
			Layout_XML_Path	= Custom_Favs_Layout
		elif os.path.isfile(Default_Favs_Layout):
			Default_Layout_XML_Path		= Default_Favs_Layout
		else:
			Default_Layout_XML_Path		= Default_No_Favs_Layout

elif XBE_Files == 1:
	if xbmc.getCondVisibility('Skin.HasSetting(videolayout)'):
		if os.path.isfile(XBE_Default_Video_Layout):
			Default_Layout_XML_Path	= XBE_Default_Video_Layout
		elif os.path.isfile(XBE_Default_Synopsis_Layout):
			Default_Layout_XML_Path	= XBE_Default_Synopsis_Layout
		else:
			Default_Layout_XML_Path	= XBE_Default_No_Video_Layout
	
	elif xbmc.getCondVisibility('Skin.HasSetting(synopsislayout)'):
		if os.path.isfile(XBE_Default_Synopsis_Layout):
			Default_Layout_XML_Path	= XBE_Default_Synopsis_Layout
		else:
			Default_Layout_XML_Path	= XBE_Default_No_Synopsis_Layout
	
	elif xbmc.getCondVisibility('Skin.HasSetting(thumblayout)'):
		if os.path.isfile(XBE_Default_Thumb_Layout):
			Default_Layout_XML_Path	= XBE_Default_Thumb_Layout
		else:
			Default_Layout_XML_Path	= XBE_Default_No_Thumb_Layout
	
	else:
		if os.path.isfile(XBE_Default_Layout):
			Default_Layout_XML_Path		= XBE_Default_Layout
		else:
			Default_Layout_XML_Path		= XBE_Default_No_Layout

if os.path.isfile(Layout_XML_Path):
	Layout_File =  Layout_XML_Path

elif os.path.isfile(Default_Layout_XML_Path):
	Layout_File =  Default_Layout_XML_Path

else:	# default layout is missing so error!
	EMU_Files = 0; FAV_Files = 0; XBE_Files = 0;
	xbmc.executebuiltin('SetFocus(9000)')
	dialog.ok("ERROR","Default layout file is missing.",Default_Layout_XML_Path)

if EMU_Files == 1:
	if os.path.isfile(os.path.join(XML_Files_Path,'gamelist.xml')):
		## this is here so not to mess with the actual menulabel
		if not os.path.isfile(Layout_XML_Path):
			MenuLabel_XML = "default"
		else:
			MenuLabel_XML = MenuLabel
		Header_Data = Header_Data_EMU % (MenuLabel_XML)
		try:
			with open(Layout_File) as layoutfile:
				with open(MyPrograms_Path, "w") as inputfile:
					inputfile.write(Header_Data)
					for code in layoutfile:
						if XBE_Content: code = code.replace('[Media_Path]\\screenshots\\','[Media_Path]\\fanart\\')
						code = code.replace('[ArtworkFolder]',xbmc.getInfoLabel('skin.string(Custom_Media_Path)') + xbmc.getInfoLabel('Skin.String(emuname)') + '\$INFO[Skin.String('+ MenuLabel +'_artworkfolder)]\\')
						code = code.replace('[Artwork_Type]',MenuLabel +'_artworkfolder')
						code = code.replace('[Fanart_Toggle]','Skin.HasSetting(' + xbmc.getInfoLabel('Skin.String(emuname)') + 'fanart)')
						code = code.replace('[Media_Path]',xbmc.getInfoLabel('skin.string(Custom_Media_Path)') + xbmc.getInfoLabel('Skin.String(emuname)'))
						code = code.replace('[CurrentSystem]',MenuLabel)
						if '<!-- video preview mode horizontal -->' in code: xbmc.executebuiltin('Skin.SetBool(videopreviewhorizontal)')
						inputfile.write(code)
					inputfile.write(Footer_Data_EMU)
			with open(os.path.join(XML_Files_Path,'gamelist.xml')) as gamelistfile:
				gamelistfile = gamelistfile.read()
				gamelistfile = gamelistfile.replace('[ArtworkFolder]',xbmc.getInfoLabel('skin.string(Custom_Media_Path)') + xbmc.getInfoLabel('Skin.String(emuname)') + '\$INFO[Skin.String('+ MenuLabel +'_artworkfolder)]\\')
				for line in fileinput.FileInput(MyPrograms_Path,inplace=1):
					if '<!-- content list this label is required -->' in line:
						line = line.replace(line,line+gamelistfile)
					print line,
			with open(_Script_Jump_Path, "w") as inputfile:
				inputfile.write(Jump_File_Data.replace("' + MenuLabel + '",MenuLabel))
			with open(os.path.join(XML_Files_Path,'jumplist.xml')) as jumpfile:
				jumpfile = jumpfile.read()
				for line in fileinput.FileInput(_Script_Jump_Path,inplace=1):
					if '<!-- jumpcode -->' in line:
						line = line.replace(line,line+jumpfile)
					print line,
		except:
			pass
		time.sleep(0.5) # delay to make sure the file is written
		if xbmc.getCondVisibility('Skin.HasSetting(videolayout)'):
			xbmc.executebuiltin('RunScript(special://emustation_scripts/auto_play_preview.py)')
		else:
			xbmc.executebuiltin('ActivateWindow(Programs,Static_Menu,return)')
	else:	# default layout is missing so error!
		xbmc.executebuiltin('SetFocus(9000)')
		if MenuLabel == "xbox":
			dialog.ok("ERROR","No game list found","Rescan your xbox games to fix.",os.path.join(XML_Files_Path,'gamelist.xml'))
		elif MenuLabel == "homebrew":
			dialog.ok("ERROR","No game list found","Rescan your xbox homebrew to fix.",os.path.join(XML_Files_Path,'gamelist.xml'))
		elif MenuLabel == "ports":
			dialog.ok("ERROR","No game list found","Rescan your xbox ports to fix.",os.path.join(XML_Files_Path,'gamelist.xml'))
		else:
			dialog.ok("ERROR","No rom list found","Rescan this emulator for roms to fix.",os.path.join(XML_Files_Path,'gamelist.xml'))
elif XBE_Files == 1:
		## this is here so not to mess with the actual menulabel
		if not os.path.isfile(Layout_XML_Path):
			MenuLabel_XML = "default"
		else:
			MenuLabel_XML = MenuLabel
		Header_Data = Header_Data_XBE % (MenuLabel_XML)
		try:
			with open(Layout_File) as layoutfile:
				with open(MyPrograms_Path, "w") as inputfile:
					inputfile.write(Header_Data)		
					for code in layoutfile:
						inputfile.write(code)
					inputfile.write(Footer_Data_XBE)
		except:
			pass
		time.sleep(0.5) # delay to make sure the file is written
		xbmc.executebuiltin('Dialog.Close(1111,true)')
		xbmc.executebuiltin('ActivateWindow(Programs,'+ MenuLabel +',return)')
elif FAV_Files == 1:
		try:
			with open(Layout_File) as layoutfile:
				with open(FAV_XML_Path, "w") as inputfile:
					inputfile.write(Header_Data_FAVS)
					for code in layoutfile:
						inputfile.write(code)
					inputfile.write(Footer_Data_FAVS)
		except:
			pass
		xbmc.executebuiltin('Skin.SetBool(favsloading)')
		time.sleep(0.5) # delay to make it seem like it loading the menu
		xbmc.executebuiltin('ReplaceWindow(134,return)')
else:
	xbmc.executebuiltin('SetFocus(9000)')
xbmc.executebuiltin('Dialog.Close(1101,true)')