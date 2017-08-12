'''
	Script by Rocky5
	Used to create merged layout files that are used to replace MyPrograms.xml for different emulators styles
'''

import fileinput, glob, os, re, shutil, sys, time, xbmc, xbmcgui
from BeautifulSoup import *

#####	Start markings for the log file.
print "================================================================================"
print "| _Scripts\XBMC-Emustation\create layouts.py loaded."
print "| ------------------------------------------------------------------------------"
	
pDialog							= xbmcgui.DialogProgress()
dialog							= xbmcgui.Dialog()
MyPrograms_Path					= xbmc.translatePath( 'special://skin/720p/MyPrograms.xml' )
ThemeType						= xbmc.getInfoLabel( 'Skin.CurrentTheme' )
Default_Layout_XML_Path			= xbmc.translatePath( 'special://xbmc/_layouts/default/' + ThemeType + '/layout.xml' )
Content_List_Path				= xbmc.translatePath( "Special://skin/720p/content lists/" )

for Items in sorted( os.listdir( Content_List_Path ) ):
	if os.path.isfile( os.path.join( Content_List_Path,Items ) ):
		#####	Sets variables.
		Emu_Name			= Items[:-4]
		Layout_XML_Path		= xbmc.translatePath( 'special://xbmc/_layouts/' + Emu_Name + '/' + ThemeType + '/layout.xml' )
		###########

		## this is here so not to mess with the actual menulabel
		if not os.path.isfile( Layout_XML_Path ):
			MenuLabel_XML = "default"
		else:
			MenuLabel_XML = Emu_Name
			
		Header_Data				= '<window id="1">\n\
			<defaultcontrol always="false">9000</defaultcontrol>\n\
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
				<texture background="false" fallback="layouts/' + MenuLabel_XML + '/menu_background.png">Special://xbmc/_layouts/' + MenuLabel_XML + '/menu_background.png</texture>\n\
			</control>\n\
		'
		Footer_Data				= '\n\
			<control type="image">\n\
				<posx>0</posx>\n\
				<posy>85r</posy>\n\
				<width>1280</width>\n\
				<height>85</height>\n\
				<aspectratio>stretch</aspectratio>\n\
				<texture background="true">layouts/art/gamelist_help_emus.png</texture>\n\
			</control>\n\
			</control>\n\
		</controls>\n\
	</window>'

		if not os.path.isdir( Content_List_Path + 'merged' ): os.makedirs( Content_List_Path + 'merged' )
		
		if os.path.isfile( Layout_XML_Path ):
			try:
				with open( Layout_XML_Path ) as layoutfile:
					with open(Content_List_Path + 'merged\\layout_' + Emu_Name + '.xml', "w") as inputfile:		
						inputfile.write(Header_Data)
						for code in layoutfile:
							inputfile.write( code )
						inputfile.write(Footer_Data)
						inputfile.close()

				with open( Content_List_Path + Emu_Name + '.xml' ) as countfile:
					countfile = countfile.read()
					for line in fileinput.FileInput(Content_List_Path + 'merged\\layout_' + Emu_Name + '.xml',inplace=1):
						if '</focusedlayout>' in line:
							line = line.replace(line,line+countfile)
						print line,
					countfile.close()
			except:
				pass

		elif os.path.isfile( Default_Layout_XML_Path ):
			try:
				with open( Default_Layout_XML_Path ) as layoutfile:
					with open(Content_List_Path + 'merged\\layout_' + Emu_Name + '.xml', "w") as inputfile:		
						inputfile.write(Header_Data)
						for code in layoutfile:
							inputfile.write( code )
						inputfile.write(Footer_Data)	
						inputfile.close()

				with open( Content_List_Path + Emu_Name + '.xml' ) as countfile:
					countfile = countfile.read()
					for line in fileinput.FileInput(Content_List_Path + 'merged\\layout_' + Emu_Name + '.xml',inplace=1):
						if '</focusedlayout>' in line:
							line = line.replace(line,line+countfile)
						print line,
					countfile.close()
			except:
				pass
		else:	# default layout is missing so error!
			dialog.ok("FATAL ERROR","Reinstall XBMC-Emustation","or reinstall",Layout_XML_Path)
			
xbmc.executebuiltin("Notification(Complete,All layouts refreshed)")