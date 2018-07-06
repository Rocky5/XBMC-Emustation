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
pDialog	= xbmcgui.DialogProgress()
dialog	= xbmcgui.Dialog()
Game_Directories = [ "E:\\Games\\", "F:\\Games\\", "G:\\Games\\", "E:\\Games1\\", "F:\\Games1\\", "G:\\Games1\\", "E:\\Games2\\", "F:\\Games2\\", "G:\\Games2\\" ]
for Game_Directories in Game_Directories:
	if os.path.isdir( Game_Directories ):
		pDialog.create( "PARSING XBOX GAMES","Initializing" )
		for Items in sorted( os.listdir( Game_Directories ) ):
			if os.path.isdir(os.path.join( Game_Directories, Items)):
				Game_Directory = os.path.join( Game_Directories, Items )
				pDialog.update(0,"Copying [B][UPPERCASE]Xbox[/UPPERCASE][/B] Images.",Items,"This can take some time, please be patient.")
				if os.path.isfile( os.path.join( Game_Directory, "game.xbe" ) ):
					XBEFile = os.path.join( Game_Directory, "game.xbe" )
				elif os.path.isfile( os.path.join( Game_Directory, "tdgame.xbe" ) ):
					XBEFile = os.path.join( Game_Directory, "tdgame.xbe" )
				else:
					XBEFile = os.path.join( Game_Directory, "default.xbe" )
				TBNFile = os.path.join( Game_Directory, "default.tbn" )
				Extracted_XBE_TitleID = Extract_XBE_TitleID( XBEFile )
				if os.path.isfile( XBEFile ):
					if os.path.isfile( TBNFile ):
						if not os.path.isdir( "E:\\xbox artwork\\" ): os.makedirs( "E:\\xbox artwork\\" )
						shutil.copy2( TBNFile, "E:\\xbox artwork\\" + Extracted_XBE_TitleID + ".jpg" )
					else:
						print "Cannot find: " + TBNFile
				else:
					print "Cannot find: " + XBEFile
pDialog.close()
dialog.ok("COMPLETE","Done, images are in E:\\xbox artwork\\")