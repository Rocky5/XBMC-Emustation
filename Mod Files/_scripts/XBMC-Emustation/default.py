'''
	Script by Rocky5
	Used to create MyPrograms.xml for different emulators styles
'''

import fileinput, glob, os, shutil, sys, time, xbmc, xbmcgui
from BeautifulSoup import *

#####	Start markings for the log file.
print "================================================================================"
print "| _Scripts\XBMC-Emustation\default.py loaded."
print "| ------------------------------------------------------------------------------"
	
pDialog							= xbmcgui.DialogProgress()
dialog							= xbmcgui.Dialog()

if xbmc.getCondVisibility( '!Skin.HasSetting(althomelayout)' ): MenuLabel = xbmc.getInfoLabel('Container(9001).ListItem.Label2')
if xbmc.getCondVisibility( 'Skin.HasSetting(althomelayout)' ): MenuLabel = xbmc.getInfoLabel('Container(9002).ListItem.Label2')
if str(xbmcgui.getCurrentWindowId()) == "11111": MenuLabel = xbmc.getInfoLabel('Control.GetLabel(99)')
if MenuLabel == "dummy label for python script":	MenuLabel = "apps"
MyPrograms_Path					= xbmc.translatePath( 'special://skin/720p/MyPrograms.xml' )
Layout_XML_Path					= xbmc.translatePath( 'special://xbmc/_layouts/' + MenuLabel + '/layout.xml' )
Default_Layout_XML_Path			= xbmc.translatePath( 'special://xbmc/_layouts/default/layout.xml' )
Content_List_Path				= xbmc.translatePath( "Special://skin/720p/content lists/" )
XBE_Files = 0
if MenuLabel == "apps":	XBE_Files = 1
if MenuLabel == "xbox": XBE_Files = 1
if MenuLabel == "homebrew": XBE_Files = 1
if MenuLabel == "ports": XBE_Files = 1

xbmc.executebuiltin('Skin.SetString(emuname,' + MenuLabel + ')')

if XBE_Files == 0:
	if os.path.isfile( Default_Layout_XML_Path ):
		if os.path.isfile( Content_List_Path + 'merged\\layout_' + MenuLabel + '.xml' ):
			shutil.copy2( Content_List_Path + 'merged\\layout_' + MenuLabel + '.xml', MyPrograms_Path )
			xbmc.executebuiltin( 'ActivateWindow(Programs,dummy,return)' )
	else:	# default layout is missing so error!
		xbmcgui.Dialog().ok( "FATAL ERROR","Reinstall XBMC-Emustation","or reinstall",Layout_XML_Path )

if XBE_Files == 1:
	## this is here so not to mess with the actual menulabel
	if not os.path.isfile( Layout_XML_Path	 ):
		MenuLabel_XML = "default"
	else:
		MenuLabel_XML = MenuLabel
	
	Header_Data						= '<window id="1">\n\
		<defaultcontrol always="true">50</defaultcontrol>\n\
		<allowoverlay>no</allowoverlay>\n\
		<views>50,51,52,53,54,55,56,57,58,59,60</views>\n\
		<layout>' + MenuLabel_XML + '</layout>\n\
		<controls>\n\
		<include>CommonBackground</include>\n\
		<control type="group">\n\
		<animation effect="fade" time="250">WindowOpen</animation>\n\
		<animation effect="fade" time="150">WindowClose</animation>\n\
		<control type="image">\n\
			<posx>0</posx>\n\
			<posy>0</posy>\n\
			<width>1280</width>\n\
			<height>720</height>\n\
			<aspectratio>stretch</aspectratio>\n\
			<texture background="false" fallback="layouts/' + MenuLabel_XML + '/menu_background.png">Special://skin/layouts/' + MenuLabel_XML + '/menu_background.png</texture>\n\
		</control>\n\
	'
	Footer_Data						= '\n\
	<control type="image">\n\
		<posx>0</posx>\n\
		<posy>85r</posy>\n\
		<width>1280</width>\n\
		<height>85</height>\n\
		<aspectratio>stretch</aspectratio>\n\
		<texture background="true">layouts/art/gamelist_help.png</texture>\n\
	</control>\n\
	</control>\n\
	</controls>\n\
	</window>'
	
	if os.path.isfile( Layout_XML_Path ):
		with open( Layout_XML_Path	) as layoutfile:
			with open(MyPrograms_Path, "w") as inputfile:
				inputfile.write( Header_Data )		
				for code in layoutfile:
					inputfile.write( code )			
				inputfile.write( Footer_Data )
				xbmc.executebuiltin('ActivateWindow(Programs,'+ MenuLabel +',return)')
	elif os.path.isfile( Default_Layout_XML_Path ):
		with open( Default_Layout_XML_Path ) as layoutfile:
			with open(MyPrograms_Path, "w") as inputfile:
				inputfile.write( Header_Data )		
				for code in layoutfile:
					inputfile.write( code )			
				inputfile.write( Footer_Data )
				xbmc.executebuiltin( 'ActivateWindow(Programs,'+ MenuLabel +',return)' )
	else:	# default layout is missing so error!
		xbmcgui.Dialog().ok( "FATAL ERROR","Reinstall XBMC-Emustation","or reinstall",Layout_XML_Path )