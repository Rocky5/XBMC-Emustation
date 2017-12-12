'''
	Script by Rocky5
	Used to build the home menu system.
'''
import fileinput, os, sys, time, xbmc, xbmcgui
#####	Start markings for the log file.
print "| _Scripts\XBMC-Emustation\home_themer.py loaded."
pDialog					= xbmcgui.DialogProgress()
dialog					= xbmcgui.Dialog()
## Not used now as I changed the source code to reload almost instantly.
#Select_Theme		= sys.argv[1:][0]
# try:
	# if Select_Theme == "1":
		# xbmc.executebuiltin( 'Skin.Theme(1)' )
# except: pass

# try:
	# if Select_Theme == "0":
		# xbmc.executebuiltin( 'Skin.Theme(-1)' )
# except: pass

# Delay to it gives the system time to update the current theme entry.
# time.sleep(0.2)

dialog			= xbmcgui.Dialog()
time.sleep(1)
HomeLayout 		= xbmc.getInfoLabel( 'Skin.CurrentTheme' )
Home_XML_Path	= xbmc.translatePath( 'special://skin/720p/home.xml' )
Layout_File		= xbmc.translatePath( 'special://xbmc/_layouts/home/' + HomeLayout + '.xml' )
System_List		= xbmc.translatePath( 'special://xbmc/_layouts/home/other/system_list.xml' )
Header_Data		= '<window id="0">\n\
	<defaultcontrol always="true">9000</defaultcontrol>\n\
	<controls>\n\
		<control type="button" id="9100">\n\
			<posx>-500</posx>\n\
			<onclick>-</onclick>\n\
		</control>\n\
		<include>CommonBackground</include>\n\
	'
Footer_Data				= '\n\
	</controls>\n\
</window>'
if os.path.isfile( Layout_File ):
	try:
		os.remove(Home_XML_Path)
		with open( Layout_File ) as layoutfile:
			with open(Home_XML_Path, "w") as inputfile:
				inputfile.write( Header_Data )
				for code in layoutfile:
					inputfile.write( code )
				inputfile.write( Footer_Data )
				inputfile.close()
			layoutfile.close()
	except:
		pass
else:
	dialog.ok("ERROR!",HomeLayout + ".xml is missing from","Q:\\_layouts\\home\\","Reinstall this file to fix the issue.")
if os.path.isfile( System_List ):
	try:
		with open( System_List ) as fin:
				fin = fin.read()
				for line in fileinput.FileInput(Home_XML_Path,inplace=1):
					if '</focusedlayout>' in line:
						line = line.replace(line,line+fin)
					print line,
				fin.close()
	except:
		pass
else:
	dialog.ok("ERROR!","system_list.xml is missing from","Q:\\_layouts\\home\\other\\","Reinstall this file to fix the issue.")
xbmc.executebuiltin( 'ReloadSkin' ) # required for the custom them selector to reload the skin and apply the new theme.