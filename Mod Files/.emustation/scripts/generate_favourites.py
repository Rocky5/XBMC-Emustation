'''
	Script by Rocky5 (original idea headphone)
	Used to create a favourites.xml from your games/roms.
'''
import fileinput,os,shutil,xbmc,xbmcgui
#####	Start markings for the log file.
print "| .emustation\Scripts\generate_favourites.py loaded."
Current_name 	= xbmc.getInfoLabel('Container(9000).ListItem.Label')
Emu_Name		= xbmc.getInfoLabel('Skin.String(emuname)')
Root_Directory 	= xbmc.translatePath("Special://root/")
if str( xbmc.getCondVisibility( 'Skin.String(Custom_Emulator_Path)' ) ) == '1':
	Emulator_Folder_Path	= xbmc.getInfoLabel( 'Skin.String(Custom_Emulator_Path)' )
else:
	Emulator_Folder_Path	= Root_Directory + '.emustation\\emulators\\'.replace( '\\','\\\\' )
Current_Profile_Directory	= xbmc.translatePath( 'special://profile/' )
Favourites_XML				= xbmc.translatePath( 'special://Profile/favourites.xml')
Favourites_XML_Backup		= xbmc.translatePath( 'special://Profile/favourites.backup')
Scripts_Path 				= Root_Directory + '.emustation\\scripts\\'
Favs_List_XML				= os.path.join( Root_Directory, '.emustation\\gamelists', Emu_Name, 'favslist.xml')
if not os.path.isfile( Favourites_XML ):
	f = open(Favourites_XML,'w')
	f.write('<favourites>\n')
	f.write('</favourites>')
	f.close()
if os.path.isfile( Favs_List_XML ):
	with open( Favs_List_XML ) as file:
		for line in file:
			## Disabled as it causes issues with 007 games, so don't use Unicode characters in synopsis names and you will be fine.
			# try:
				# line = line.decode('unicode_escape').encode('utf-8')
			# except:
				# pass
			if '<favourites>' + Current_name in line:
				TMP = line.replace('<favourites>',''); TMP = TMP.replace('</favourites>',''); TMP = TMP.split('|');
				Display_Name = TMP[0]; Emu_Path = TMP[1]; Rom_Path = TMP[2];
				Emu_Path = os.path.join( '$INFO[skin.string(custom_emulator_path)]', Emu_Name, Emu_Path )
				if Emu_Name == "fba" or Emu_Name == "fbl" or Emu_Name == "fblc" or Emu_Name == "fbaxxx":
					pass
				else:
					Rom_Path = os.path.join( '$INFO[skin.string(custom_roms_path)]', Emu_Name, Rom_Path )
	if Emu_Path.startswith("Q:\\"): Emu_Path = Emu_Path.replace( "Q:\\", Root_Directory )
	if Rom_Path.startswith("Q:\\"): Rom_Path = Rom_Path.replace( "Q:\\", Root_Directory )
	Favourite_String = '	<favourite name="' + Display_Name + '\" thumb=\"' + os.path.join(xbmc.getInfoLabel( 'skin.string(Custom_Media_Path)' ), Emu_Name, xbmc.getInfoLabel( 'Skin.String(' + Emu_Name + '_artworkfolder)' ), xbmc.getInfoLabel( 'Container(9000).ListItem.Thumb' ))  + '\">RunScript(&quot;' + Scripts_Path + 'launcher.py&quot;,&quot;' + Emu_Path + '&quot;,&quot;' + Rom_Path + '&quot;,1,0)</favourite>'
	if Emu_Path in open(Favourites_XML).read():
		xbmc.executebuiltin('Notification(DOH!,This rom has already been added.)')
	else:
		for line in fileinput.input(Favourites_XML, inplace=1):
			line = line.replace('<favourites />', '<favourites>\n' + Favourite_String.replace('\n','') + '\n</favourites>')
			line = line.replace('</favourites>', Favourite_String.replace('\n','') + '\n</favourites>')
			print line,
		shutil.copy2(Favourites_XML,Favourites_XML_Backup)
		xbmc.executebuiltin("Notification(" + Display_Name.upper().replace(',',' ') + ",Has been added to your favourites.)")
		xbmc.executebuiltin('RunScript(' + Scripts_Path + 'update_favs_counter.py)' )
else:
	xbmc.executebuiltin('Notification(ERROR,Please rescan your roms.)')
xbmc.executebuiltin('SetFocus(9000)')