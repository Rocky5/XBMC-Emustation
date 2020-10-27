import operator, os, shutil, struct, xbmc, xbmcgui
pDialog				= xbmcgui.DialogProgress()
dialog				= xbmcgui.Dialog()
Game_Directories	= [ "E:\\Synopsis Folders\\Output - Artwork - Homebrew\\", "E:\\Synopsis Folders\\Output - Artwork - Xbox Specials-Others\\", "E:\\Synopsis Folders\\Output - Artwork - Xbox JPN Games\\", "E:\\Synopsis Folders\\Output - Artwork - Xbox Other\\", "E:\\Synopsis Folders\\Output - Artwork - Xbox PAL Games\\", "E:\\Synopsis Folders\\Output - Artwork - Xbox NTSC Games\\", ]
text_filename		= "tmp"
text_filename_ext	= ""
text_name			= ""
text_description	= ""
text_rating			= ""
text_releasedate	= ""
text_developer		= ""
text_publisher		= ""
text_genre			= ""
text_players		= ""
text_titleid		= ""
for Game_Directories in Game_Directories:
	if os.path.isdir( Game_Directories ):
		pDialog.create( "PARSING XBOX GAMES","Initializing" )
		for Items in sorted( os.listdir( Game_Directories ) ):
			if os.path.isdir(os.path.join( Game_Directories, Items)):
				Game_Directory = os.path.join( Game_Directories, Items )
				pDialog.update(0,"Creating [B][UPPERCASE]Xbox[/UPPERCASE][/B] Synopsis Files.",Items,"This can take some time, please be patient.")
				XMLFile = os.path.join( Game_Directory, "_resources\\default.xml" )
				if os.path.isfile( XMLFile ):
					if Game_Directories.endswith('Homebrew\\'): OutputFolder = "_Homebrew Synopsis"
					if Game_Directories.endswith('Specials-Others\\'): OutputFolder = "_Xbox Games Synopsis\\Specials-Others"
					if Game_Directories.endswith('NTSC Games\\'): OutputFolder = "_Xbox Games Synopsis\\NTSC Games"
					if Game_Directories.endswith('PAL Games\\'): OutputFolder = "_Xbox Games Synopsis\\PAL Games"
					if Game_Directories.endswith('JPN Games\\'): OutputFolder = "_Xbox Games Synopsis\\JPN Games"
					if Game_Directories.endswith('Xbox Other\\'): OutputFolder = "_Xbox Games Synopsis\\Xbox Other"
					if not os.path.isdir( "E:\\"+OutputFolder+"\\" ): os.makedirs( "E:\\"+OutputFolder+"\\" )
					with open ( XMLFile ) as input:
						input = input.read()
						for line in input.split('\n'):
							if "<synopsis>" in line:
								text_filename = Items
								text_filename_ext = "Filename: " + text_filename
								text_filename = text_filename[:38] # truncate to fit 42 character limit - extension
								text_name = "Name: unknown"
								text_description = "_________________________\n"
								text_rating = "Rating: unknown"
								text_releasedate = "Released: unknown"
								text_developer = "Developer: unknown"
								text_publisher = "Publisher: unknown"
								text_genre = "Genre: unknown"
								text_players = "Players: at least 1"
								text_titleid = "Not found"
								
							if "<title>" in line:
								text_name = line.split('>',2)[1]
								text_name = text_name.split('<',1)[0]
								text_name = text_name.replace('&#39;',"'")
								text_name = text_name.replace('&amp;','&')
								text_name = 'Name: ' + text_name
								if text_name == "Name: ": text_name = "Name: " + text_filename
								
							if "<overview>" in line:
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
								
							if "<release_date>" in line:
								text_releasedate = line.split('>',2)[1]
								text_releasedate = text_releasedate.split('<',1)[0]
								text_releasedate = 'Release Year: ' + text_releasedate
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

							if "<features_general>" in line:
								text_players = line.split('>',2)[1]
								text_players = text_players.split('<',1)[0]
								text_players = text_players.split(',',1)[0]
								text_players = text_players.replace('Players','Players:')
								if text_players == "": text_players = "Players: unknown"

							if "<titleid>" in line:
								text_titleid = line.split('>',2)[1]
								text_titleid = text_titleid.split('<',1)[0]
								text_filename_ext = "Filename: " + text_titleid

					txt_output = os.path.join( "E:\\"+OutputFolder+"\\",  text_titleid + ".txt")
					if os.path.isfile(txt_output):
						if not os.path.isdir("E:\\"+OutputFolder+"\\Dups"): os.makedirs("E:\\"+OutputFolder+"\\Dups")
						txt_output = os.path.join( "E:\\"+OutputFolder+"\\Dups\\",  text_titleid + ".txt")
					with open ( txt_output , 'w' ) as output:
						output.write(text_filename_ext + '\n')
						output.write(text_name + '\n')
						output.write(text_rating + '\n')
						output.write(text_releasedate + '\n')
						output.write(text_developer + '\n')
						output.write(text_publisher + '\n')
						output.write(text_genre + '\n')
						output.write(text_players + '\n')
						output.write(text_description + '\n')
				else:
					print "Cannot find: " + XMLFile
pDialog.close()
dialog.ok("COMPLETE","synopsis files converted")