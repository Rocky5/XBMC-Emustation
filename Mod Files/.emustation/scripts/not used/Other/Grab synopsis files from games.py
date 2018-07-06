import operator, os, shutil, struct, xbmc, xbmcgui
def Extract_XBE_TitleID(FileName):
    try :
        XbeDta          =   {}
        if os.path.isfile(FileName) and FileName.endswith('.xbe'):
            xbe         =   open(FileName,'rb')
            # Get Extract_XBE_TitleID Data #
            xbe.seek(0x104)
            tLoadAddr   =   xbe.read(4)
            xbe.seek(0x118)
            tCertLoc    =   xbe.read(4)
            LoadAddr    =   struct.unpack('L',tLoadAddr)
            CertLoc     =   struct.unpack('L',tCertLoc)
            CertBase    =   CertLoc[0] - LoadAddr[0]
            CertBase    +=  8
            IdStart     =   xbe.seek(CertBase)
            tIdData     =   xbe.read(4)
            IdData      =   struct.unpack('L',tIdData)
            XbeDta      =   str(hex(IdData[0])[2:10]).lower().zfill(8)
            xbe.close()
        return XbeDta
    except  :
        xbe.close()
        return {}
pDialog				= xbmcgui.DialogProgress()
dialog				= xbmcgui.Dialog()
Game_Directories	= [ "E:\\Games\\", "F:\\Games\\", "G:\\Games\\", "E:\\Games1\\", "F:\\Games1\\", "G:\\Games1\\", "E:\\Games2\\", "F:\\Games2\\", "G:\\Games2\\" ]
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
for Game_Directories in Game_Directories:
	if os.path.isdir( Game_Directories ):
		pDialog.create( "PARSING XBOX GAMES","Initializing" )
		for Items in sorted( os.listdir( Game_Directories ) ):
			if os.path.isdir(os.path.join( Game_Directories, Items)):
				Game_Directory = os.path.join( Game_Directories, Items )
				pDialog.update(0,"Creating [B][UPPERCASE]Xbox[/UPPERCASE][/B] Synopsis Files.",Items,"This can take some time, please be patient.")
				if os.path.isfile( os.path.join( Game_Directory, "game.xbe" ) ):
					XBEFile = os.path.join( Game_Directory, "game.xbe" )
				elif os.path.isfile( os.path.join( Game_Directory, "tdgame.xbe" ) ):
					XBEFile = os.path.join( Game_Directory, "tdgame.xbe" )
				else:
					XBEFile = os.path.join( Game_Directory, "default.xbe" )
				XMLFile = os.path.join( Game_Directory, "_resources\\default.xml" )
				Extracted_XBE_TitleID = Extract_XBE_TitleID( XBEFile )
				if os.path.isfile( XBEFile ):
					if os.path.isfile( XMLFile ):
						if not os.path.isdir( "E:\\xbox synopsis\\" ): os.makedirs( "E:\\xbox synopsis\\" )
						with open ( XMLFile ) as input:
							input = input.read()
							for line in input.split('\n'):
								if "<synopsis>" in line:
									text_filename = Extracted_XBE_TitleID
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
									
								if "<features_general.>" in line:
									text_players = line.split('>',2)[1]
									text_players = text_players.split('<',1)[0]
									text_players = 'Players: ' + text_players
									if text_players == "Players: ": text_players = "Players: unknown"
									
								with open ( os.path.join( "E:\\xbox synopsis\\",  Extracted_XBE_TitleID + ".txt" ), 'w' ) as output:
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
				else:
					print "Cannot find: " + XBEFile
pDialog.close()
dialog.ok("COMPLETE","synopsis files are in E:\\xbox synopsis\\")