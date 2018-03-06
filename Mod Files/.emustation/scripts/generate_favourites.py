'''
	Script by Rocky5 (original idea headphone)
	Used to create a favourites.xml from your games/roms.
'''
import fileinput, os, xbmc, xbmcgui
#####	Start markings for the log file.
print "| .emustation\Scripts\generate_favourites.py loaded."
Current_name 	= xbmc.getInfoLabel('Container(9000).ListItem.Label')
Emulator_name	= xbmc.getInfoLabel('Skin.String(emuname)')
# Gets current XBMC-Emustation directory.
CharCount = 100 # How many characters you want after 'The executable running is: '
with open( xbmc.translatePath( 'special://xbmc/system/' ) + 'xbmc.log', 'r' ) as XBMCLOG:
	for line in XBMCLOG:
		left,found,right = line.partition('The executable running is: ')
		if found:
			Working_Directory			= ( right[:CharCount] )
			XBMCLOG.close
			Root_Directory       		 = os.path.dirname( Working_Directory ) + '\\'
			if str( xbmc.getCondVisibility( 'Skin.String(Custom_Emulator_Path)' ) ) == '1':
				Emulator_Folder_Path			= xbmc.getInfoLabel( 'Skin.String(Custom_Emulator_Path)' )
			else:
				Emulator_Folder_Path			= Root_Directory + '.emustation\\emulators\\'.replace( '\\','\\\\' )
			Current_Profile_Directory	= xbmc.translatePath( 'special://profile/' )
			Favourites_XML				= xbmc.translatePath( 'special://Profile/favourites.xml')
			Scripts_Path 				= Root_Directory + '.emustation\\scripts\\'
			Favs_List_XML				= os.path.join( Root_Directory, '.emustation\\gamelists', Emulator_name, 'favslist.xml')
if not os.path.isfile( Favourites_XML ):
	f = open(Favourites_XML,'w')
	f.write('<favourites>\n')
	f.write('</favourites>')
	f.close()
if os.path.isfile( Favs_List_XML ):
	with open( Favs_List_XML ) as file:
		for line in file:
			if '<favourites>' + Current_name in line:
				Emu_Path = line.split(',',1)[1]; Emu_Path = line.split(',',1)[1]; Emu_Path = Emu_Path.split(',',1)[0];
				Rom_Path = line.split(',',1)[1]; Rom_Path = Rom_Path.split(',',1)[1]; Rom_Path = Rom_Path.split('<',1)[0];
	Favourite_String_Emuname = '<favourite name="[' + Emulator_name + '] ' + Current_name + '\" thumb=\"' + xbmc.getInfoLabel( 'Container(9000).ListItem.Thumb' ) + '\">RunScript(&quot;' + Scripts_Path + 'launcher.py&quot;,&quot;' + Emu_Path + '&quot;,&quot;' + Rom_Path + '&quot;,1)</favourite>\n</favourites>'
	Favourite_String = '<favourite name="' + Current_name + '\" thumb=\"' + xbmc.getInfoLabel( 'Container(9000).ListItem.Thumb' ) + '\">RunScript(&quot;' + Scripts_Path + 'launcher.py&quot;,&quot;' + Emu_Path + '&quot;,&quot;' + Rom_Path + '&quot;,1,0)</favourite>\n</favourites>'
	if Rom_Path in open(Favourites_XML).read():
		xbmc.executebuiltin('Notification(DOH!,This rom has already been added.)')
	else:
		for line in fileinput.input(Favourites_XML, inplace=1):
			line = line.replace('</favourites>', Favourite_String)
			line = line.replace('<favourites />', '<favourites>\n' + Favourite_String)
			print line,
		xbmc.executebuiltin("Notification(" + Current_name.upper().replace(',',' ') + ",Has been added to your favourites.)")
		xbmc.executebuiltin('RunScript(' + Scripts_Path + 'update_favs_counter.py)' )
else:
	xbmc.executebuiltin('Notification(ERROR,Please rescan your roms.)')
xbmc.executebuiltin('SetFocus(9000)')