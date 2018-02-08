import os, shutil, sys, xbmc, xbmcgui
pDialog	= xbmcgui.DialogProgress()
dialog	= xbmcgui.Dialog()
if xbmc.getCondVisibility( 'Skin.String(Custom_Emulator_Path)' ):
	Emulator_Folder_Path = xbmc.getInfoLabel( 'Skin.String(Custom_Emulator_Path)' )
else:
	Emulator_Folder_Path = 'Q:\\emustation\\emulators\\'
text_filename = "tmp"
text_filename_ext = ""
text_name = ""
text_description = ""
text_rating = ""
text_releasedate = ""
text_developer = ""
text_publisher = ""
text_genre = ""
text_players = ""

Select_Emu_Folder = dialog.select( "SELECT A SYSTEM",sorted( os.listdir( Emulator_Folder_Path ) ) )
Emu_Path = os.path.join( Emulator_Folder_Path, sorted( os.listdir( Emulator_Folder_Path ) )[Select_Emu_Folder] )
Emu_Path = os.path.split(Emu_Path)[1]
destination = os.path.join( os.getcwd(), Emu_Path )
if not Select_Emu_Folder == -1:
	if not os.path.isdir( destination ): os.makedirs( destination )
	pDialog.create( "SYNOPSIS MAKER","Initializing" )
	with open ( os.path.join( os.getcwd(), "gamelist.xml" ) ) as input:
		input = input.read()
		for line in input.split('\n'):
			if "<path>" in line:
				text_filename = line.split('/',2)[1]
				text_filename = text_filename.split('<',1)[0]
				text_filename = text_filename.replace('&#39;',"'")
				text_filename = text_filename.replace('&amp;','&')
				text_filename_ext = "Filename: " + text_filename
				text_filename = text_filename[:-4] # remove extension
				text_name = "Name: unknown"
				text_description = "_________________________\n"
				text_rating = "Rating: unknown"
				text_releasedate = "Released: unknown"
				text_developer = "Developer: unknown"
				text_publisher = "Publisher: unknown"
				text_genre = "Genre: unknown"
				text_players = "Players: at least 1"
				
			if "<name>" in line:
				text_name = line.split('>',2)[1]
				text_name = text_name.split('<',1)[0]
				text_name = text_name.replace('&#39;',"'")
				text_name = text_name.replace('&amp;','&')
				text_name = 'Name: ' + text_name
				if text_name == "Name: ": text_name = "Name: " + text_filename
				
			if "<desc>" in line:
				text_description = line.split('>',2)[1]
				text_description = text_description.split('<',1)[0]
				text_description = text_description.replace('&amp;quot;','"')
				text_description = text_description.replace('&#39;',"'")
				text_description = text_description.replace('&amp;','&')
				text_description = text_description.replace('quot;','"')
				text_description = text_description.replace('&#xD;&#xA;','[CR]')
				text_description = text_description.replace('&#xA;&#xA;','[CR]')
				text_description = text_description.replace('&#xD;&#xD;','[CR]')
				text_description = text_description.replace('&#xA;','[CR]')
				text_description = text_description.replace('&#xD;','[CR]')
				text_description = '_________________________\n' + text_description
				
			if "<rating>" in line:
				text_rating = line.split('>',2)[1]
				text_rating = text_rating.split('<',1)[0]
				text_rating = 'Rating: ' + text_rating
				if text_rating == "Rating: ": text_rating = "Rating: unknown"
				
			if "<releasedate>" in line:
				text_releasedate = line.split('>',2)[1]
				text_releasedate = text_releasedate.split('<',1)[0]
				text_releasedate = text_releasedate[:-7] # remove time stamp that's not used
				# now to reorder the date and time into rest of the world standards
				text_releasedate_day = text_releasedate[6:] 
				text_releasedate_month = text_releasedate[4:-2]
				text_releasedate_year = text_releasedate[:-4]
				#text_releasedate = 'Release Year: ' + text_releasedate_day + '.' + text_releasedate_month + '.' + text_releasedate_year
				text_releasedate = 'Release Year: ' + text_releasedate_year
				if text_releasedate == "Release Year: .." or text_releasedate == "Release Year: ": text_releasedate = "Released: unknown"
				
			if "<developer>" in line:
				text_developer = line.split('>',2)[1]
				text_developer = text_developer.split('<',1)[0]
				text_developer = text_developer.replace('&#39;',"'")
				text_developer = text_developer.replace('&amp;','&')
				text_developer = 'Developer: ' + text_developer
				if text_developer == "Developer: ": text_developer = "Developer: unknown"
				
			if "<publisher>" in line:
				text_publisher = line.split('>',2)[1]
				text_publisher = text_publisher.split('<',1)[0]
				text_publisher = text_publisher.replace('&#39;',"'")
				text_publisher = text_publisher.replace('&amp;','&')
				text_publisher = 'Publisher: ' + text_publisher
				if text_publisher == "Publisher: ": text_publisher = "Publisher: unknown"
				
			if "<genre>" in line:
				text_genre = line.split('>',2)[1]
				text_genre = text_genre.split('<',1)[0]
				text_genre = text_genre.replace('&#39;',"'")
				text_genre = text_genre.replace('&amp;','&')
				text_genre = 'Genre: ' + text_genre
				if text_genre == "Genre: ": text_genre = "Genre: unknown"
				
			if "<players>" in line:
				text_players = line.split('>',2)[1]
				text_players = text_players.split('<',1)[0]
				text_players = 'Players: ' + text_players
				if text_players == "Players: ": text_players = "Players: unknown"
				
			with open ( os.path.join( destination,text_filename + '.txt' ), 'w' ) as output:
				output.write(text_filename_ext + '\n')
				output.write(text_name + '\n')
				output.write(text_rating + '\n')
				output.write(text_releasedate + '\n')
				output.write(text_developer + '\n')
				output.write(text_publisher + '\n')
				output.write(text_genre + '\n')
				output.write(text_players + '\n')
				output.write(text_description + '\n')
			
			pDialog.update(0,"Creating synopisis files.","[B][UPPERCASE]" + text_filename + "[/UPPERCASE][/B]","This can take some time, please be patient." )
			
	if os.path.isfile( os.path.join( destination,'tmp.txt' ) ): os.remove( os.path.join( destination,'tmp.txt' ) )

	if not os.path.isdir( os.path.join( destination,'gamelist' ) ):
		os.makedirs( os.path.join( destination,'gamelist' ) )
		shutil.copyfile( os.path.join( os.getcwd(), "gamelist.xml" ),os.path.join( destination,'gamelist','gamelist.xml' ) )
	else:
		shutil.copyfile( os.path.join( os.getcwd(), "gamelist.xml" ),os.path.join( destination,'gamelist','gamelist.xml' ) )