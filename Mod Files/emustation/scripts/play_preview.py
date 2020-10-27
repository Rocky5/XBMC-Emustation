import os, xbmc, urllib2, xbmcgui, time
dialog	= xbmcgui.Dialog()
Focus	= "9000"
if xbmc.getCondVisibility('Skin.HasSetting(synopsislayout)') or xbmc.getCondVisibility('Skin.HasSetting(videolayout)'):
	if str(xbmc.getCondVisibility('Skin.String(Custom_Media_Path)')) == "1":
		Media_Folder_Path	= xbmc.getInfoLabel('Skin.String(Custom_Media_Path)')
	else:
		Media_Folder_Path	= 'Q:\\emustation\\media\\'
	Current_System	= xbmc.getInfoLabel('Skin.String(emuname)')
	Current_Memory	= xbmc.getInfoLabel("system.freememory")[:-2]
	# XBE Files
	PathXBE			= xbmc.getInfoLabel('listitem.path')
	PathXBEAlt		= os.path.join(PathXBE, '_resources\\media\\')
	# Emulators
	FileNameEMU		= xbmc.getInfoLabel('Container(9000).ListItem.Thumb')[:-4].lower()
	PathEmu			= os.path.join(Media_Folder_Path, Current_System, 'videos\\')
	Network_Valid	= 1
	Loop_Counter	= 0
	#xbmc.executebuiltin('ActivateWindow(1101)')
	#time.sleep(1)
	def Check_Network():
		global Network_Valid
		try:
			xbmc.executebuiltin('Notification(STRM preview found, Checking for internet access...)')
			urllib2.urlopen('http://www.google.com', timeout=3)
			xbmc.executebuiltin('Notification(WOOHOO!, Internet access successful)')
			time.sleep(2)
		except urllib2.URLError as err:
			xbmc.executebuiltin('Notification(OOPS!,No internet access found)')
			Network_Valid = 0
	if xbmc.Player().isPlayingVideo():
		xbmc.executebuiltin('SetFocus(9100)')
		xbmc.executebuiltin('Dialog.Close(1101,true)')
	else:
		try:
			if int(Current_Memory) >= 8:
				# Find video using supported extensions
				XBEVideo = ""
				if os.path.isfile(PathXBE+"preview.mp4"): XBEVideo = PathXBE+"preview.mp4"
				elif os.path.isfile(PathXBE+"preview.xmv"): XBEVideo = PathXBE+"preview.xmv"
				elif os.path.isfile(PathXBE+"preview.strm"): XBEVideo = PathXBE+"preview.strm"
				if os.path.isdir(PathXBEAlt):
					for XBEVideo in sorted(os.listdir(PathXBEAlt)):
						if XBEVideo.endswith(tuple(Extensions)):
							XBEVideo = PathXBEAlt+XBEVideo.lower()
				# Find video using supported extensions
				EmuVideo = ""
				if os.path.isfile(PathEmu+FileNameEMU+'.mp4'): EmuVideo = PathEmu+FileNameEMU+'.mp4'
				elif os.path.isfile(PathEmu+FileNameEMU+'.strm'): EmuVideo = PathEmu+FileNameEMU+'.strm'
				elif os.path.isfile(PathEmu+FileNameEMU+'.xmv'): EmuVideo = PathEmu+FileNameEMU+'.xmv'
				if Current_System == "apps" or xbmc.getCondVisibility('Skin.HasSetting(editmode)') == 1:
					VideoFile	= XBEVideo
				else:
					VideoFile	= EmuVideo
				if os.path.isfile(VideoFile):
					if VideoFile.endswith("xmv") or VideoFile.endswith("mp4"):
						xbmc.executebuiltin('PlayWith(DVDPlayer)')
						xbmc.executebuiltin('playmedia(' + VideoFile + ',1,noresume)')
						xbmc.executebuiltin('Dialog.Close(1101,true)')
					elif VideoFile.endswith("strm"):
						Check_Network()
						if Network_Valid:
							xbmc.executebuiltin('PlayWith(MPlayer)')
							xbmc.executebuiltin('playmedia(' + VideoFile + ',1,noresume)')
							xbmc.executebuiltin('Dialog.Close(1101,true)')
							while True:
								if xbmc.Player().isPlayingVideo(): break
								Loop_Counter += 1
								time.sleep(1)
								if Loop_Counter == 6: break
					xbmc.executebuiltin('SetFocus(9100)')
					xbmc.executebuiltin('Dialog.Close(1101,true)')
				else:
					# xbmc.executebuiltin('playmedia(Q:\\system\\media\\static.mp4,1,noresume)')
					# xbmc.executebuiltin('SetFocus(9100)')
					xbmc.executebuiltin('Dialog.Close(1101,true)')
					xbmc.executebuiltin('SetFocus(' + Focus + ')')
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