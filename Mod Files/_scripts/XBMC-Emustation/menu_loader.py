'''
	Script by Rocky5
	Used to create MyPrograms.xml for different emulators styles
'''

import fileinput, glob, os, shutil, sys, time, xbmc, xbmcgui

#####	Start markings for the log file.
print "| _Scripts\XBMC-Emustation\menu_loader.py loaded."
	
pDialog							= xbmcgui.DialogProgress()
dialog							= xbmcgui.Dialog()
XBE_Files						= 0

if xbmc.getCondVisibility( '!Skin.HasSetting(althomelayout)' ): MenuLabel = xbmc.getInfoLabel('Container(9001).ListItem.Label2')
if xbmc.getCondVisibility( 'Skin.HasSetting(althomelayout)' ): MenuLabel = xbmc.getInfoLabel('Container(9002).ListItem.Label2')
if str(xbmcgui.getCurrentWindowId()) == "11111": MenuLabel = xbmc.getInfoLabel('Control.GetLabel(99)')
if MenuLabel == "dummy label for python script":	MenuLabel = "apps"
MyPrograms_Path					= xbmc.translatePath( 'special://skin/720p/MyPrograms.xml' )
ThemeType						= xbmc.getInfoLabel( 'Skin.CurrentTheme' )
Default_Layout_XML_Path			= xbmc.translatePath( 'special://xbmc/_layouts/default/' + ThemeType + '/layout.xml' )
Layout_XML_Path					= xbmc.translatePath( 'special://xbmc/_layouts/' + MenuLabel + '/' + ThemeType + '/layout.xml' )
Content_List_Path				= xbmc.translatePath( "Special://skin/720p/content lists/" )

if MenuLabel == "apps":	XBE_Files = 1
if MenuLabel == "xbox": XBE_Files = 1
if MenuLabel == "homebrew": XBE_Files = 1
if MenuLabel == "ports": XBE_Files = 1

xbmc.executebuiltin('Skin.SetString(emuname,' + MenuLabel + ')')

if XBE_Files == 0:
	if os.path.isfile( os.path.join( Content_List_Path,MenuLabel + '.xml' ) ):
		## this is here so not to mess with the actual menulabel
		if not os.path.isfile( Layout_XML_Path ):
			MenuLabel_XML = "default"
		else:
			MenuLabel_XML = MenuLabel
			
		Header_Data				= '<window id="1">\n\
			<defaultcontrol always="true">9000</defaultcontrol>\n\
			<allowoverlay>no</allowoverlay>\n\
			<views>50</views>\n\
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
				<texture background="false" fallback="layouts/' + MenuLabel_XML + '/menu_background.png">Special://xbmc/_layouts/' + MenuLabel_XML + '/' + ThemeType + '/menu_background.png</texture>\n\
			</control>\n\
		'
		Footer_Data				= '\n\
			<control type="image">\n\
				<posx>0</posx>\n\
				<posy>635</posy>\n\
				<width>1280</width>\n\
				<height>85</height>\n\
				<aspectratio>stretch</aspectratio>\n\
				<texture background="true">layouts/art/gamelist_help_emus.png</texture>\n\
			</control>\n\
			</control>\n\
		</controls>\n\
	</window>'

		if os.path.isfile( Layout_XML_Path ):
			try:
				with open( Layout_XML_Path ) as layoutfile:
					with open(MyPrograms_Path, "w") as inputfile:
						inputfile.write(Header_Data)
						for code in layoutfile:
							inputfile.write( code )
						inputfile.write(Footer_Data)
						inputfile.close()

				with open( Content_List_Path + MenuLabel + '.xml' ) as countfile:
					countfile = countfile.read()
					for line in fileinput.FileInput(MyPrograms_Path,inplace=1):
						if '</focusedlayout>' in line:
							line = line.replace(line,line+countfile)
						print line,
					countfile.close()
			except:
				pass

			xbmc.executebuiltin( 'ActivateWindow(Programs,'+ MenuLabel +',return)' )

		elif os.path.isfile( Default_Layout_XML_Path ):
			try:
				with open( Default_Layout_XML_Path ) as layoutfile:
					with open(MyPrograms_Path, "w") as inputfile:
						inputfile.write(Header_Data)
						for code in layoutfile:
							inputfile.write( code )
						inputfile.write(Footer_Data)	
						inputfile.close()

				with open( Content_List_Path + MenuLabel + '.xml' ) as countfile:
					countfile = countfile.read()
					for line in fileinput.FileInput(MyPrograms_Path,inplace=1):
						if '</focusedlayout>' in line:
							line = line.replace(line,line+countfile)
						print line,
					countfile.close()
			except:
				pass
			xbmc.executebuiltin( 'ActivateWindow(Programs,'+ MenuLabel +',return)' )

		else:	# default layout is missing so error!
			dialog.ok( "ERROR","Default layout file is missing.",Default_Layout_XML_Path )

	else:	# default layout is missing so error!
		dialog.ok("ERROR","No content list found","Rescan this emulator for CUT files to fix.",os.path.join( Content_List_Path,MenuLabel + '.xml' ))
else:		
	xbmc.executebuiltin( 'SetFocus(9000)' )

if XBE_Files == 1:
	Default_Layout_XML_Path		= xbmc.translatePath( 'special://xbmc/_layouts/default/' + ThemeType + '/XBE files/layout.xml' )
	## this is here so not to mess with the actual menulabel
	if not os.path.isfile( Layout_XML_Path	 ):
		MenuLabel_XML = "default"
	else:
		MenuLabel_XML = MenuLabel
	
	Header_Data					= '<window id="1">\n\
		<defaultcontrol always="true">50</defaultcontrol>\n\
		<allowoverlay>no</allowoverlay>\n\
		<views>50</views>\n\
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
			<texture background="false" fallback="layouts/' + MenuLabel_XML + '/menu_background.png">Special://skin/layouts/' + MenuLabel_XML + '/' + ThemeType + '/menu_background.png</texture>\n\
		</control>\n\
	'
	Footer_Data					= '\n\
	<control type="image">\n\
		<posx>0</posx>\n\
		<posy>635</posy>\n\
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
		dialog.ok( "ERROR","Default layout file is missing.",Default_Layout_XML_Path )
else:		
	xbmc.executebuiltin( 'SetFocus(9000)' )