'''
	Script by Rocky5
	Used to create MyPrograms.xml for different emulators styles
'''

import fileinput, os, time, xbmc, xbmcgui

#####	Start markings for the log file.
print "| .emustation\Scripts\menu_loader.py loaded."

try:
	XBE_Edit_Mode	= sys.argv[1:][0]
except:
	XBE_Edit_Mode	= "0"

pDialog							= xbmcgui.DialogProgress()
dialog							= xbmcgui.Dialog()
XBE_Files						= 0
EMU_Files						= 0
FAV_Files						= 0
Default_Layout_XML_Path			= "0"
Layout_XML_Path					= "0"

MenuLabel = xbmc.getInfoLabel('Container(9000).ListItem.Label2')
if str(xbmcgui.getCurrentWindowDialogId()) == "11111": MenuLabel = xbmc.getInfoLabel('Control.GetLabel(99)')
if MenuLabel == "dummy label for python script":	MenuLabel = "apps"
MyPrograms_Path					= xbmc.translatePath( 'special://skin/720p/MyPrograms.xml' )
_Script_Jump_Path				= xbmc.translatePath( 'special://skin/720p/_script_jumpList.xml' )
FAV_XML_Path					= xbmc.translatePath( 'special://skin/720p/DialogFavourites.xml' )
ThemeType						= xbmc.getInfoLabel( 'Skin.CurrentTheme' )
Favs_List_Path					= xbmc.translatePath( 'special://xbmc/.emustation/gamelists/' + MenuLabel )

Default_No_Layout				= xbmc.translatePath( 'special://xbmc/.emustation/layouts/default/skindefault/layout.xml' )
Default_No_Synopsis_Layout		= xbmc.translatePath( 'special://xbmc/.emustation/layouts/default/skindefault/synopsis_layout.xml' )
Default_No_Thumb_Layout			= xbmc.translatePath( 'special://xbmc/.emustation/layouts/default/skindefault/thumb_layout.xml' )
XBE_Default_No_Layout			= xbmc.translatePath( 'special://xbmc/.emustation/layouts/default/skindefault/XBE files/layout.xml' )
XBE_Default_No_Synopsis_Layout	= xbmc.translatePath( 'special://xbmc/.emustation/layouts/default/skindefault/XBE files/synopsis_layout.xml' )
XBE_Default_No_Thumb_Layout		= xbmc.translatePath( 'special://xbmc/.emustation/layouts/default/skindefault/XBE files/thumb_layout.xml' )


Default_Layout					= xbmc.translatePath( 'special://xbmc/.emustation/layouts/default/' + ThemeType + '/layout.xml' )
Default_Synopsis_Layout			= xbmc.translatePath( 'special://xbmc/.emustation/layouts/default/' + ThemeType + '/synopsis_layout.xml' )
Default_Thumb_Layout			= xbmc.translatePath( 'special://xbmc/.emustation/layouts/default/' + ThemeType + '/thumb_layout.xml' )
XBE_Default_Layout				= xbmc.translatePath( 'special://xbmc/.emustation/layouts/default/' + ThemeType + '/XBE files/layout.xml' )
XBE_Default_Synopsis_Layout		= xbmc.translatePath( 'special://xbmc/.emustation/layouts/default/' + ThemeType + '/XBE files/synopsis_layout.xml' )
XBE_Default_Thumb_Layout		= xbmc.translatePath( 'special://xbmc/.emustation/layouts/default/' + ThemeType + '/XBE files/thumb_layout.xml' )
Custom_Layout					= xbmc.translatePath( 'special://xbmc/.emustation/layouts/' + MenuLabel + '/' + ThemeType + '/layout.xml' )
Custom_Synopsis_Layout			= xbmc.translatePath( 'special://xbmc/.emustation/layouts/' + MenuLabel + '/' + ThemeType + '/synopsis_layout.xml' )
Custom_Thumb_Layout				= xbmc.translatePath( 'special://xbmc/.emustation/layouts/' + MenuLabel + '/' + ThemeType + '/thumb_layout.xml' )

if XBE_Edit_Mode == "editmode" or MenuLabel == "apps" or MenuLabel == "homebrew" or MenuLabel == "ports":
	XBE_Files = 1
	if XBE_Edit_Mode == "editmode": MenuLabel = "xbox"
elif MenuLabel == "favs":
	FAV_Files = 1
else:
	EMU_Files = 1

xbmc.executebuiltin('Skin.SetString(emuname,' + MenuLabel + ')')
	
Header_Data_EMU					= '<window id="1">\n\
		<onunload condition="Player.HasVideo">Stop</onunload>\n\
		<defaultcontrol always="true">9000</defaultcontrol>\n\
		<allowoverlay>no</allowoverlay>\n\
		<view>50</view>\n\
		<layout>%s</layout>\n\
		<controls>\n\
		<include>CommonBackground</include>\n\
		<control type="group">\n\
		<animation effect="fade" time="150">WindowOpen</animation>\n\
		<animation effect="fade" time="150">WindowClose</animation>\n\
		<!-- Used to run the script and stop folk moving the list forward or backwards -->\n\
		<control type="button" id="9999">\n\
			<posx>-500</posx>\n\
			<onfocus>RunScript(Special://XBMC/.emustation/scripts/play_preview.py)</onfocus>\n\
		</control>\n\
		<control type="button" id="9990">\n\
			<posx>-500</posx>\n\
			<onfocus>SetFocus(9000)</onfocus>\n\
			<onfocus>ActivateWindow(1120)</onfocus>\n\
		</control>\n\
		<!-- Used to stop playback if one of the direction buttons are pressed or the (A) button -->\n\
		<control type="button" id="9100">\n\
			<posx>-500</posx>\n\
			<onup>setfocus(9000)</onup>\n\
			<onup>stop</onup>\n\
			<onup>setfocus(9000)</onup>\n\
			<ondown>setfocus(9000)</ondown>\n\
			<ondown>stop</ondown>\n\
			<ondown>setfocus(9000)</ondown>\n\
			<onleft>stop</onleft>\n\
			<onleft>setfocus(9000)</onleft>\n\
			<onright>stop</onright>\n\
			<onright>setfocus(9000)</onright>\n\
			<onclick>setfocus(9000)</onclick>\n\
			<onclick>stop</onclick>\n\
		</control>\n\
		<!-- Used to stop folk moving when the script is run, it shouldnt matter but it may do on slow drives. So its added. -->\n\
		<control type="button" id="9200">\n\
			<posx>-500</posx>\n\
			<onclick>-</onclick>\n\
		</control>\n\
	'
Footer_Data_EMU					= '\n\
	</control>\n\
	</controls>\n\
	</window>'

	
Header_Data_FAVS				= '<window type="dialog" id="134">\n\
	<defaultcontrol always="true">450</defaultcontrol>\n\
	<onunload>Skin.Reset(favsloading)</onunload>\n\
	<include>dialogeffect</include>\n\
	<controls>\n'

Footer_Data_FAVS				= '\n\
	</controls>\n\
	</window>'
	
Jump_File_Data					= '<window type="dialog" id="1120">\n\
	<defaultcontrol always="true">9000</defaultcontrol>\n\
	<controls>\n\
		<control type="group" id="jump section">\n\
			<posy>90</posy>\n\
			<animation effect="slide" reversable="true" start="0,0" end="0,-25" time="0" condition="StringCompare(Skin.String(emuname),xbox) + Skin.HasSetting(synopsislayout) + !Skin.HasSetting(KioskMode)">conditional</animation>\n\
			<!-- Normal -->\n\
			<control type="group">\n\
				<visible>!Skin.HasSetting(KioskMode) + [!StringCompare(Skin.String(emuname),xbox) | !Skin.HasSetting(synopsislayout)]</visible>\n\
				<control type="image">\n\
					<description>background image</description>\n\
					<posx>165</posx>\n\
					<posy>10</posy>\n\
					<width>950</width>\n\
					<height>530</height>\n\
					<texture>menu_back_shadow.png</texture>\n\
				</control>\n\
				<control type="image">\n\
					<description>background image</description>\n\
					<posx>320</posx>\n\
					<posy>100</posy>\n\
					<width>640</width>\n\
					<height>350</height>\n\
					<texture border="20,20,20,20">menu_back.png</texture>\n\
				</control>\n\
			</control>\n\
			<!-- kiosk mode -->\n\
			<control type="group">\n\
				<visible>Skin.HasSetting(KioskMode) + [!StringCompare(Skin.String(emuname),xbox) | !Skin.HasSetting(synopsislayout)]</visible>\n\
				<control type="image">\n\
					<description>background image</description>\n\
					<posx>165</posx>\n\
					<posy>60</posy>\n\
					<width>950</width>\n\
					<height>280</height>\n\
					<texture>menu_back_shadow.png</texture>\n\
				</control>\n\
				<control type="image">\n\
					<description>background image</description>\n\
					<posx>320</posx>\n\
					<posy>100</posy>\n\
					<width>640</width>\n\
					<height>200</height>\n\
					<texture border="20,20,20,20">menu_back.png</texture>\n\
				</control>\n\
			</control>\n\
			<!-- Normal -->\n\
			<control type="group">\n\
				<visible>StringCompare(Skin.String(emuname),xbox) + Skin.HasSetting(synopsislayout) + !Skin.HasSetting(KioskMode)</visible>\n\
				<control type="image">\n\
					<description>background image</description>\n\
					<posx>165</posx>\n\
					<posy>10</posy>\n\
					<width>950</width>\n\
					<height>580</height>\n\
					<texture>menu_back_shadow.png</texture>\n\
				</control>\n\
				<control type="image">\n\
					<description>background image</description>\n\
					<posx>320</posx>\n\
					<posy>100</posy>\n\
					<width>640</width>\n\
					<height>400</height>\n\
					<texture border="20,20,20,20">menu_back.png</texture>\n\
				</control>\n\
			</control>\n\
			<!-- kiosk mode -->\n\
			<control type="group">\n\
				<visible>StringCompare(Skin.String(emuname),xbox) + Skin.HasSetting(synopsislayout) + Skin.HasSetting(KioskMode)</visible>\n\
				<control type="image">\n\
					<description>background image</description>\n\
					<posx>165</posx>\n\
					<posy>60</posy>\n\
					<width>950</width>\n\
					<height>280</height>\n\
					<texture>menu_back_shadow.png</texture>\n\
				</control>\n\
				<control type="image">\n\
					<description>background image</description>\n\
					<posx>320</posx>\n\
					<posy>100</posy>\n\
					<width>640</width>\n\
					<height>200</height>\n\
					<texture border="20,20,20,20">menu_back.png</texture>\n\
				</control>\n\
			</control>\n\
			<control type="label">\n\
				<description>heading label</description>\n\
				<posx>320</posx>\n\
				<posy>130</posy>\n\
				<width>640</width>\n\
				<height>50</height>\n\
				<align>center</align>\n\
				<aligny>center</aligny>\n\
				<font>size_50</font>\n\
				<label>$LOCALIZE[32073]</label>\n\
				<textcolor>menu_header_label</textcolor>\n\
			</control>\n\
			<control type="grouplist" id="9000">\n\
				<posx>320</posx>\n\
				<posy>201</posy>\n\
				<width>640</width>\n\
				<height>50</height>\n\
				<onleft>9000</onleft>\n\
				<onright>9000</onright>\n\
				<onup>9004</onup>\n\
				<ondown>9001</ondown>\n\
				<itemgap>-1</itemgap>\n\
				<scrolltime>0</scrolltime>\n\
				<orientation>horizontal</orientation>\n\
				<!-- jumpcode -->\n\
			</control>\n\
			<control type="grouplist" id="9001">\n\
				<posx>320</posx>\n\
				<posy>250</posy>\n\
				<width>640</width>\n\
				<height>200</height>\n\
				<onleft>-</onleft>\n\
				<onright>-</onright>\n\
				<onup>9000</onup>\n\
				<ondown>9002</ondown>\n\
				<itemgap>-1</itemgap>\n\
				<scrolltime>0</scrolltime>\n\
				<orientation>vertical</orientation>\n\
				<control type="button" id="8050">\n\
					<label>[UPPERCASE]Add current rom to $LOCALIZE[1036][/UPPERCASE]</label>\n\
					<include>MenuButtonCommonValues</include>\n\
					<onclick>Dialog.Close(1120)</onclick>\n\
					<onclick>SetFocus(9200)</onclick>\n\
					<onclick>RunScript(Special://XBMC/.emustation/scripts/generate_favourites.py)</onclick>\n\
					<visible>!StringCompare(Skin.String(emuname),xbox) + !Skin.HasSetting(KioskMode)</visible>\n\
				</control>\n\
				<control type="button" id="8051">\n\
					<label>[UPPERCASE]Add current game to $LOCALIZE[1036][/UPPERCASE]</label>\n\
					<include>MenuButtonCommonValues</include>\n\
					<onclick>Dialog.Close(1120)</onclick>\n\
					<onclick>SetFocus(9200)</onclick>\n\
					<onclick>RunScript(Special://XBMC/.emustation/scripts/generate_favourites.py)</onclick>\n\
					<visible>StringCompare(Skin.String(emuname),xbox) + !Skin.HasSetting(KioskMode)</visible>\n\
				</control>\n\
			</control>\n\
			<control type="grouplist" id="9002">\n\
				<posx>320</posx>\n\
				<posy>299</posy>\n\
				<width>640</width>\n\
				<height>200</height>\n\
				<onleft>9002</onleft>\n\
				<onright>9002</onright>\n\
				<onup>9001</onup>\n\
				<ondown>9003</ondown>\n\
				<itemgap>-1</itemgap>\n\
				<scrolltime>0</scrolltime>\n\
				<orientation>horizontal</orientation>\n\
				<visible>!StringCompare(Skin.String(emuname),xbox) + !Skin.HasSetting(KioskMode)</visible>\n\
				<control type="button" id="8040">\n\
					<label>[UPPERCASE]Artwork Type[/UPPERCASE]</label>\n\
					<label2>&lt; [UPPERCASE]2d[/UPPERCASE] &gt;</label2>\n\
					<include>MenuButtonCommonValues</include>\n\
					<onfocus>Skin.SetString(' + MenuLabel + '_artworkfolder,boxart)</onfocus>\n\
					<visible allowhiddenfocus="true">StringCompare(Skin.String(' + MenuLabel + '_artworkfolder),boxart)</visible>\n\
				</control>\n\
				<visible>!StringCompare(Skin.String(emuname),xbox)</visible>\n\
				<control type="button" id="8041">\n\
					<label>[UPPERCASE]Artwork Type[/UPPERCASE]</label>\n\
					<label2>&lt; [UPPERCASE]3d[/UPPERCASE] &gt;</label2>\n\
					<include>MenuButtonCommonValues</include>\n\
					<onfocus>Skin.SetString(' + MenuLabel + '_artworkfolder,boxart3d)</onfocus>\n\
					<visible allowhiddenfocus="true">StringCompare(Skin.String(' + MenuLabel + '_artworkfolder),boxart3d)</visible>\n\
				</control>\n\
				<control type="button" id="8042">\n\
					<label>[UPPERCASE]Artwork Type[/UPPERCASE]</label>\n\
					<label2>&lt; [UPPERCASE]logos[/UPPERCASE] &gt;</label2>\n\
					<include>MenuButtonCommonValues</include>\n\
					<onfocus>Skin.SetString(' + MenuLabel + '_artworkfolder,logo)</onfocus>\n\
					<visible allowhiddenfocus="true">StringCompare(Skin.String(' + MenuLabel + '_artworkfolder),logo)</visible>\n\
				</control>\n\
				<control type="button" id="8043">\n\
					<label>[UPPERCASE]Artwork Type[/UPPERCASE]</label>\n\
					<label2>&lt; [UPPERCASE]mix[/UPPERCASE] &gt;</label2>\n\
					<include>MenuButtonCommonValues</include>\n\
					<onfocus>Skin.SetString(' + MenuLabel + '_artworkfolder,mix)</onfocus>\n\
					<visible allowhiddenfocus="true">StringCompare(Skin.String(' + MenuLabel + '_artworkfolder),mix)</visible>\n\
				</control>\n\
				<control type="button" id="8044">\n\
					<label>[UPPERCASE]Artwork Type[/UPPERCASE]</label>\n\
					<label2>&lt; [UPPERCASE]screenshots[/UPPERCASE] &gt;</label2>\n\
					<include>MenuButtonCommonValues</include>\n\
					<onfocus>Skin.SetString(' + MenuLabel + '_artworkfolder,screenshots)</onfocus>\n\
					<visible allowhiddenfocus="true">StringCompare(Skin.String(' + MenuLabel + '_artworkfolder),screenshots)</visible>\n\
				</control>\n\
			</control>\n\
			<control type="grouplist" id="9002">\n\
				<posx>320</posx>\n\
				<posy>299</posy>\n\
				<width>640</width>\n\
				<height>200</height>\n\
				<onleft>9002</onleft>\n\
				<onright>9002</onright>\n\
				<onup>9001</onup>\n\
				<ondown>9003</ondown>\n\
				<itemgap>-1</itemgap>\n\
				<scrolltime>0</scrolltime>\n\
				<orientation>horizontal</orientation>\n\
				<visible>StringCompare(Skin.String(emuname),xbox) + !Skin.HasSetting(KioskMode)</visible>\n\
				<control type="button" id="8040">\n\
					<label>[UPPERCASE]Artwork Type[/UPPERCASE]</label>\n\
					<label2>&lt; [UPPERCASE]2d[/UPPERCASE] &gt;</label2>\n\
					<include>MenuButtonCommonValues</include>\n\
					<onfocus>Skin.SetString(' + MenuLabel + '_artworkfolder,boxart)</onfocus>\n\
					<visible allowhiddenfocus="true">StringCompare(Skin.String(' + MenuLabel + '_artworkfolder),boxart)</visible>\n\
				</control>\n\
				<control type="button" id="8041">\n\
					<label>[UPPERCASE]Artwork Type[/UPPERCASE]</label>\n\
					<label2>&lt; [UPPERCASE]3d[/UPPERCASE] &gt;</label2>\n\
					<include>MenuButtonCommonValues</include>\n\
					<onfocus>Skin.SetString(' + MenuLabel + '_artworkfolder,boxart3d)</onfocus>\n\
					<visible allowhiddenfocus="true">StringCompare(Skin.String(' + MenuLabel + '_artworkfolder),boxart3d)</visible>\n\
				</control>\n\
				<control type="button" id="8042">\n\
					<label>[UPPERCASE]Artwork Type[/UPPERCASE]</label>\n\
					<label2>&lt; [UPPERCASE]cd poster[/UPPERCASE] &gt;</label2>\n\
					<include>MenuButtonCommonValues</include>\n\
					<onfocus>Skin.SetString(' + MenuLabel + '_artworkfolder,cdposter)</onfocus>\n\
					<visible allowhiddenfocus="true">StringCompare(Skin.String(' + MenuLabel + '_artworkfolder),cdposter)</visible>\n\
				</control>\n\
				<control type="button" id="8043">\n\
					<label>[UPPERCASE]Artwork Type[/UPPERCASE]</label>\n\
					<label2>&lt; [UPPERCASE]disc[/UPPERCASE] &gt;</label2>\n\
					<include>MenuButtonCommonValues</include>\n\
					<onfocus>Skin.SetString(' + MenuLabel + '_artworkfolder,disc)</onfocus>\n\
					<visible allowhiddenfocus="true">StringCompare(Skin.String(' + MenuLabel + '_artworkfolder),disc)</visible>\n\
				</control>\n\
				<control type="button" id="8044">\n\
					<label>[UPPERCASE]Artwork Type[/UPPERCASE]</label>\n\
					<label2>&lt; [UPPERCASE]dual[/UPPERCASE] &gt;</label2>\n\
					<include>MenuButtonCommonValues</include>\n\
					<onfocus>Skin.SetString(' + MenuLabel + '_artworkfolder,dual)</onfocus>\n\
					<visible allowhiddenfocus="true">StringCompare(Skin.String(' + MenuLabel + '_artworkfolder),dual)</visible>\n\
				</control>\n\
				<control type="button" id="8045">\n\
					<label>[UPPERCASE]Artwork Type[/UPPERCASE]</label>\n\
					<label2>&lt; [UPPERCASE]open case[/UPPERCASE] &gt;</label2>\n\
					<include>MenuButtonCommonValues</include>\n\
					<onfocus>Skin.SetString(' + MenuLabel + '_artworkfolder,opencase)</onfocus>\n\
					<visible allowhiddenfocus="true">StringCompare(Skin.String(' + MenuLabel + '_artworkfolder),opencase)</visible>\n\
				</control>\n\
				<control type="button" id="8046">\n\
					<label>[UPPERCASE]Artwork Type[/UPPERCASE]</label>\n\
					<label2>&lt; [UPPERCASE]screenshots[/UPPERCASE] &gt;</label2>\n\
					<include>MenuButtonCommonValues</include>\n\
					<onfocus>Skin.SetString(' + MenuLabel + '_artworkfolder,screenshots)</onfocus>\n\
					<visible allowhiddenfocus="true">StringCompare(Skin.String(' + MenuLabel + '_artworkfolder),screenshots)</visible>\n\
				</control>\n\
			</control>\n\
			<control type="grouplist" id="9003">\n\
				<posx>320</posx>\n\
				<posy>348</posy>\n\
				<width>640</width>\n\
				<height>200</height>\n\
				<onleft>-</onleft>\n\
				<onright>-</onright>\n\
				<onup>9002</onup>\n\
				<ondown>9004</ondown>\n\
				<itemgap>-1</itemgap>\n\
				<scrolltime>0</scrolltime>\n\
				<orientation>vertical</orientation>\n\
				<visible>Skin.HasSetting(synopsislayout) + !Skin.HasSetting(KioskMode)</visible>\n\
				<control type="radiobutton" id="8060">\n\
					<label>[UPPERCASE]Enable Fanart[/UPPERCASE]</label>\n\
					<include>MenuButtonCommonValues</include>\n\
					<onclick>Skin.ToggleSetting(' + MenuLabel + 'fanart)</onclick>\n\
					<selected>Skin.HasSetting(' + MenuLabel + 'fanart)</selected>\n\
				</control>\n\
			</control>\n\
			<control type="grouplist" id="9004">\n\
				<posx>320</posx>\n\
				<posy>348</posy>\n\
				<width>640</width>\n\
				<height>200</height>\n\
				<onleft>-</onleft>\n\
				<onright>-</onright>\n\
				<onup>9003</onup>\n\
				<ondown>9000</ondown>\n\
				<itemgap>-1</itemgap>\n\
				<scrolltime>0</scrolltime>\n\
				<orientation>vertical</orientation>\n\
				<animation effect="slide" reversable="true" start="0,0" end="0,49" time="0" condition="Skin.HasSetting(synopsislayout)">conditional</animation>\n\
				<visible>StringCompare(Skin.String(emuname),xbox) + !Skin.HasSetting(KioskMode)</visible>\n\
				<control type="button" id="8070">\n\
					<label>[UPPERCASE]Xbox Games Edit Mode[/UPPERCASE]</label>\n\
					<include>MenuButtonCommonValues</include>\n\
					<onclick>Dialog.Close(1120)</onclick>\n\
					<onclick>RunScript(Special://XBMC/.emustation/scripts/menu_loader.py,editmode)</onclick>\n\
				</control>\n\
			</control>\n\
		</control>\n\
	</controls>\n\
</window>'

Header_Data_XBE					= '<window id="1">\n\
		<onunload condition="Player.HasVideo">Stop</onunload>\n\
		<defaultcontrol always="true">50</defaultcontrol>\n\
		<allowoverlay>no</allowoverlay>\n\
		<view>50</view>\n\
		<layout>%s</layout>\n\
		<controls>\n\
		<include>CommonBackground</include>\n\
		<control type="group">\n\
		<animation effect="fade" time="150">WindowOpen</animation>\n\
		<animation effect="fade" time="150">WindowClose</animation>\n\
		<control type="button" id="9990">\n\
			<posx>-500</posx>\n\
			<onfocus>SetFocus(50)</onfocus>\n\
			<onfocus>ContextMenu</onfocus>\n\
		</control>\n\
		<!-- Used to run the script and stop folk moving the list forward or backwards -->\n\
		<control type="button" id="9999">\n\
			<posx>-500</posx>\n\
			<onfocus>RunScript(Special://XBMC/.emustation/scripts/play_preview.py)</onfocus>\n\
		</control>\n\
		<!-- Used to stop playback if one of the direction buttons are pressed or the (A) button -->\n\
		<control type="button" id="9100">\n\
			<posx>-500</posx>\n\
			<onup>setfocus(50)</onup>\n\
			<onup>stop</onup>\n\
			<onup>setfocus(50)</onup>\n\
			<ondown>setfocus(50)</ondown>\n\
			<ondown>stop</ondown>\n\
			<ondown>setfocus(50)</ondown>\n\
			<onleft>stop</onleft>\n\
			<onleft>setfocus(50)</onleft>\n\
			<onright>stop</onright>\n\
			<onright>setfocus(50)</onright>\n\
			<onclick>setfocus(50)</onclick>\n\
			<onclick>stop</onclick>\n\
		</control>\n\
	'
Footer_Data_XBE					= '\n\
	</control>\n\
	</controls>\n\
	</window>'
	
if EMU_Files == 1 or FAV_Files == 1:
	if xbmc.getCondVisibility( 'Skin.HasSetting(synopsislayout)' ):
		if os.path.isfile( Custom_Synopsis_Layout ):
			Layout_XML_Path				= Custom_Synopsis_Layout
		else:
			if os.path.isfile( Default_Synopsis_Layout ):
				Default_Layout_XML_Path	= Default_Synopsis_Layout
			else:
				Default_Layout_XML_Path	= Default_No_Synopsis_Layout
	elif xbmc.getCondVisibility( 'Skin.HasSetting(thumblayout)' ):
		if os.path.isfile( Custom_Thumb_Layout ):
			Layout_XML_Path				= Custom_Thumb_Layout
		else:
			if os.path.isfile( Default_Thumb_Layout ):
				Default_Layout_XML_Path	= Default_Thumb_Layout
			else:
				Default_Layout_XML_Path	= Default_No_Thumb_Layout
	else:
		if os.path.isfile( Custom_Layout ):
			Layout_XML_Path				= Custom_Layout
		elif os.path.isfile( Default_Layout ):
			Default_Layout_XML_Path		= Default_Layout
		else:
			Default_Layout_XML_Path		= Default_No_Layout
else:
	if xbmc.getCondVisibility( 'Skin.HasSetting(synopsislayout)' ):
		if os.path.isfile( Custom_Synopsis_Layout ):
			Layout_XML_Path				= Custom_Synopsis_Layout
		else:
			if os.path.isfile( XBE_Default_Synopsis_Layout ):
				Default_Layout_XML_Path	= XBE_Default_Synopsis_Layout
			else:
				Default_Layout_XML_Path	= XBE_Default_No_Synopsis_Layout
	elif xbmc.getCondVisibility( 'Skin.HasSetting(thumblayout)' ):
		if os.path.isfile( Custom_Thumb_Layout ):
			Layout_XML_Path				= Custom_Thumb_Layout
		else:
			if os.path.isfile( XBE_Default_Thumb_Layout ):
				Default_Layout_XML_Path	= XBE_Default_Thumb_Layout
			else:
				Default_Layout_XML_Path	= XBE_Default_No_Thumb_Layout
	else:
		if os.path.isfile( Custom_Layout ):
			Layout_XML_Path				= Custom_Layout
		elif os.path.isfile( XBE_Default_Layout ):
			Default_Layout_XML_Path		= XBE_Default_Layout
		else:
			Default_Layout_XML_Path		= XBE_Default_No_Layout
	
if os.path.isfile( Layout_XML_Path ):
	Layout_File =  Layout_XML_Path
elif os.path.isfile( Default_Layout_XML_Path ):
	Layout_File =  Default_Layout_XML_Path
else:	# default layout is missing so error!
	EMU_Files = 0; FAV_Files = 0; XBE_Files = 0;
	xbmc.executebuiltin('SetFocus(9000)')
	dialog.ok( "ERROR","Default layout file is missing.",Default_Layout_XML_Path )
	
if EMU_Files == 1:
	if os.path.isfile( os.path.join( Favs_List_Path,'gamelist.xml' ) ):
		## this is here so not to mess with the actual menulabel
		if not os.path.isfile( Layout_XML_Path ):
			MenuLabel_XML = "default"
		else:
			MenuLabel_XML = MenuLabel
		Header_Data = Header_Data_EMU % ( MenuLabel_XML  )
		try:
			with open( Layout_File ) as layoutfile:
				with open(MyPrograms_Path, "w") as inputfile:
					inputfile.write( Header_Data )
					for code in layoutfile:
						code = code.replace('[ArtworkFolder]',xbmc.getInfoLabel( 'skin.string(Custom_Media_Path)' ) + xbmc.getInfoLabel( 'Skin.String(emuname)' ) + '\$INFO[Skin.String('+ MenuLabel +'_artworkfolder)]\\')
						code = code.replace('[Fanart_Toggle]','Skin.HasSetting(' + xbmc.getInfoLabel( 'Skin.String(emuname)' ) + 'fanart)')
						code = code.replace('[Media_Path]',xbmc.getInfoLabel( 'skin.string(Custom_Media_Path)' ) + xbmc.getInfoLabel( 'Skin.String(emuname)' ))
						code = code.replace('[CurrentSystem]',MenuLabel)
						inputfile.write( code )
					inputfile.write( Footer_Data_EMU )
			with open( os.path.join( Favs_List_Path,'gamelist.xml' ) ) as gamelistfile:
				gamelistfile = gamelistfile.read()
				gamelistfile = gamelistfile.replace('[ArtworkFolder]',xbmc.getInfoLabel( 'skin.string(Custom_Media_Path)' ) + xbmc.getInfoLabel( 'Skin.String(emuname)' ) + '\$INFO[Skin.String('+ MenuLabel +'_artworkfolder)]\\')
				for line in fileinput.FileInput(MyPrograms_Path,inplace=1):
					if '<!-- content list this label is required -->' in line:
						line = line.replace(line,line+gamelistfile)
					print line,
			with open(_Script_Jump_Path, "w") as inputfile:
				inputfile.write( Jump_File_Data )
			with open( os.path.join( Favs_List_Path,'jumplist.xml' ) ) as jumpfile:
				jumpfile = jumpfile.read()
				for line in fileinput.FileInput(_Script_Jump_Path,inplace=1):
					if '<!-- jumpcode -->' in line:
						line = line.replace(line,line+jumpfile)
					print line,
		except:
			pass
		time.sleep(0.5) # delay to make sure the file is written
		xbmc.executebuiltin( 'ActivateWindow(Programs,Static_Menu,return)' )
	else:	# default layout is missing so error!
		xbmc.executebuiltin('SetFocus(9000)')
		if MenuLabel == "xbox":
			dialog.ok("ERROR","No game list found","Rescan your xbox games to fix.",os.path.join( Favs_List_Path,'gamelist.xml' ))
		else:
			dialog.ok("ERROR","No rom list found","Rescan this emulator for roms to fix.",os.path.join( Favs_List_Path,'gamelist.xml' ))
elif XBE_Files == 1:
		## this is here so not to mess with the actual menulabel
		if not os.path.isfile( Layout_XML_Path ):
			MenuLabel_XML = "default"
		else:
			MenuLabel_XML = MenuLabel
		Header_Data = Header_Data_XBE % ( MenuLabel_XML  )
		try:
			with open( Layout_File	) as layoutfile:
				with open(MyPrograms_Path, "w") as inputfile:
					inputfile.write( Header_Data )		
					for code in layoutfile:
						inputfile.write( code )
					inputfile.write( Footer_Data_XBE )
		except:
			pass
		time.sleep(0.5) # delay to make sure the file is written
		xbmc.executebuiltin( 'Dialog.Close(1111,true)' )
		xbmc.executebuiltin( 'ActivateWindow(Programs,'+ MenuLabel +',return)' )
elif FAV_Files == 1:
		try:
			with open( Layout_File ) as layoutfile:
				with open(FAV_XML_Path, "w") as inputfile:
					inputfile.write( Header_Data_FAVS )
					for code in layoutfile:
						inputfile.write( code )
					inputfile.write( Footer_Data_FAVS )
		except:
			pass
		xbmc.executebuiltin( 'Skin.SetBool(favsloading)' )
		time.sleep(0.5) # delay to make it seem like it loading the menu
		xbmc.executebuiltin( 'ReplaceWindow(favourites)' )
else:
	xbmc.executebuiltin( 'SetFocus(9000)' )