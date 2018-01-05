'''
	Script by Rocky5 (original idea headphone)
	Used to create a favourites.xml from your games/roms.
'''
import fileinput, os, xbmc, xbmcgui
#####	Start markings for the log file.
print "| _Scripts\XBMC-Emustation\generate_favourites.py loaded."
Current_name 	= xbmc.getInfoLabel('Container(9000).ListItem.Label')
Emulator_name	= xbmc.getInfoLabel('Skin.String(emuname)')
# Gets current XBMC-Emustation directory.
CharCount = 100 # How many characters you want after 'The executable running is: '
with open( xbmc.translatePath( "special://xbmc/system/" ) + "xbmc.log", "r" ) as XBMCLOG:
	for line in XBMCLOG:
		left,found,right = line.partition("The executable running is: ")
		if found:
			Working_Directory			= ( right[:CharCount] )
			XBMCLOG.close
			Root_Directory       		 = os.path.dirname( Working_Directory ) + '\\'
			if str( xbmc.getCondVisibility( 'Skin.String(Custom_Emulator_Path)' ) ) == "1":
				Emulator_Path			= xbmc.getInfoLabel( 'Skin.String(Custom_Emulator_Path)' )
			else:
				Emulator_Path			= Root_Directory + '_emulators\\'.replace( '\\','\\\\' )
			if str( xbmc.getCondVisibility( 'Skin.String(Custom_Roms_Path)' ) ) == "1":
				Roms_Path				= xbmc.getInfoLabel( 'Skin.String(Custom_Roms_Path)' ).replace( '\\','\\\\' )
			else:
				Roms_Path				= Root_Directory + '_roms\\'
			Current_Profile_Directory	= xbmc.translatePath( 'special://profile/' )
			Favourites_XML				= xbmc.translatePath( "special://Profile/favourites.xml")
			Scripts_Path 				= Root_Directory + '_scripts\\xbmc-emustation\\'
			Rom_List_File				= Root_Directory + '_scripts\\xbmc-emustation\\rom lists\\'
			Emulators_Location 			= os.path.join( Emulator_Path, Emulator_name, 'default.xbe' )
			with open(Rom_List_File + Emulator_name + '_favs.xml') as file:
				for line in file:
					if '<favourites>' + Current_name + ',' in line:
						Rom_Path = line.split(',', 1)[1]
						Rom_Path = Rom_Path.split('<', 1)[0]
				file.close
			#Favourite_String = '<favourite name="[' + Emulator_name + '] ' + Current_name + '\" thumb=\"' + xbmc.getInfoLabel( 'Container(9000).ListItem.Thumb' ) + '\">RunScript(&quot;' + Scripts_Path + 'launcher.py&quot;,&quot;' + Emulators_Location + '&quot;,&quot;' + Rom_Path +'&quot;,1)</favourite>\n</favourites>'
			Favourite_String = '<favourite name="' + Current_name + '\" thumb=\"' + xbmc.getInfoLabel( 'Container(9000).ListItem.Thumb' ) + '\">RunScript(&quot;' + Scripts_Path + 'launcher.py&quot;,&quot;' + Emulators_Location + '&quot;,&quot;' + Rom_Path +'&quot;,1)</favourite>\n</favourites>'
if not os.path.isfile( Favourites_XML ):
	f = open(Favourites_XML,"w")
	f.write("<favourites>\n")
	f.write("</favourites>")
	f.close()
if Rom_Path in open(Favourites_XML).read():
	xbmc.executebuiltin("Notification(DOH!,This rom has already been added.)")
else:
	for line in fileinput.input(Favourites_XML, inplace=1):
		line = line.replace('</favourites>', Favourite_String)
		line = line.replace('<favourites />', '<favourites>\n' + Favourite_String)
		print line,
	xbmc.executebuiltin("Notification(" + Current_name + ",Has been added to your favourites.)")
	xbmc.executebuiltin('RunScript(' + Scripts_Path + 'update_favs_counter.py)' )
xbmc.executebuiltin('SetFocus(9000)')