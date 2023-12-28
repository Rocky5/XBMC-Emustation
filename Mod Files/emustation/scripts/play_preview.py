import os, xbmc, xbmcgui, time
dialog	= xbmcgui.Dialog()
if not xbmc.Player().isPlayingVideo():
	Focus = "9000"
	Music_Playing = 0
	Played_Video = 0
	if xbmc.Player().isPlayingAudio():
		Music_Playing = 1
		
	if xbmc.getCondVisibility('Skin.HasSetting(synopsislayout)') or xbmc.getCondVisibility('Skin.HasSetting(videolayout)'):
		if str(xbmc.getCondVisibility('Skin.String(Custom_Media_Path)')) == "1":
			Media_Folder_Path	= xbmc.getInfoLabel('Skin.String(Custom_Media_Path)')
		else:
			Media_Folder_Path	= 'Q:/emustation/media/'
		Current_System	= xbmc.getInfoLabel('Skin.String(emuname)')
		Current_Memory	= xbmc.getInfoLabel("system.freememory")[:-2]
		# XBE Files
		PathXBE			= xbmc.getInfoLabel('listitem.path')
		PathXBEAlt		= os.path.join(PathXBE, '_resources/media/')
		# Emulators
		FileNameEMU		= xbmc.getInfoLabel('Container(9000).ListItem.Thumb')[:-4].lower()
		PathEmu			= os.path.join(Media_Folder_Path, Current_System, 'videos/')
		try:
			if int(Current_Memory) >= 8:
				EmuMP4Video = PathEmu+FileNameEMU+'.mp4'
				EmuXMVVideo = PathEmu+FileNameEMU+'.xmv'
				if os.path.isfile(EmuMP4Video):
					xbmc.executebuiltin('PlayWith(DVDPlayer)')
					xbmc.executebuiltin('playmedia(' +EmuMP4Video+',1,noresume)')
					Played_Video = 1
				elif os.path.isfile(EmuXMVVideo):
					xbmc.executebuiltin('PlayWith(DVDPlayer)')
					xbmc.executebuiltin('playmedia(' +EmuXMVVideo+',1,noresume)')
					Played_Video = 1
				if Played_Video == 1:
					xbmc.executebuiltin('SetFocus(9100)')
				else:
					xbmc.executebuiltin('SetFocus(9000)')
				xbmc.executebuiltin('Dialog.Close(1101,true)')
				if Music_Playing == 1 and Played_Video == 1 and xbmc.getCondVisibility('Skin.HasSetting(Use_Startup_Playback)'):
					time.sleep(1)
					while True:
						if not xbmc.Player().isPlayingVideo():
							xbmc.executebuiltin('SetFocus(9000)')
							xbmc.PlayList(0).clear()
							time.sleep(1)
							xbmc.executebuiltin('PlayMedia('+xbmc.getInfoLabel('Skin.String(Startup_Playback_Path)')+')')
							break
			else:
				dialog.ok("OOPS!","There isn't enough free ram to play this video.","Current free ram = " + xbmc.getInfoLabel("system.freememory"))
				xbmc.executebuiltin('SetFocus(' + Focus + ')')
				xbmc.executebuiltin('Dialog.Close(1101,true)')
		except:
			xbmc.executebuiltin('SetFocus(' + Focus + ')')
			xbmc.executebuiltin('Dialog.Close(1101,true)')
	else:
		xbmc.executebuiltin('SetFocus(' + Focus + ')')
		xbmc.executebuiltin('Dialog.Close(1101,true)')