import os, xbmc, xbmcgui, time
import xml.etree.ElementTree as ET
class GUI(xbmcgui.WindowXML):
	def onInit(self):
		global Video_Played
		if xbmc.getCondVisibility('Skin.HasSetting(gameloaded)') and xbmc.getCondVisibility('Skin.HasSetting(lastromlist)'):
			xbmc.executebuiltin('SetFocus(9000,'+xbmc.getInfoLabel('skin.string(lastrompos)')+')')
			xbmc.executebuiltin('Skin.Reset(gameloaded)')
		time.sleep(int(Playback_Delay))
		Current_System		= xbmc.getInfoLabel("Container(9000).ListItem.Label2")
		FilePath = Media_Folder_Path+'/'+Current_System
		if os.path.isfile(FilePath+'.mp4'):
			if xbmc.getCondVisibility('Player.HasAudio'): xbmc.PlayList(0).clear()
			xbmc.executebuiltin('playmedia(' +FilePath+'.mp4,1,noresume)')
			Video_Played = 1
		elif os.path.isfile(FilePath+'.xmv'):
			if xbmc.getCondVisibility('Player.HasAudio'): xbmc.PlayList(0).clear()
			xbmc.executebuiltin('playmedia(' +FilePath+'.xmv,1,noresume)')
			Video_Played = 1
	def onFocus(self, controlID):
		if xbmc.getCondVisibility('Player.HasVideo'): xbmc.Player().stop()
	def onClick(self, controlID): pass
	def onAction(self, action):
		global Different_Game_Selected
		global Current_Label
		global Next_Label
		global loop
		global Video_Played
		Different_Game_Selected = 0
		Current_Label = xbmc.getInfoLabel("Container(9000).ListItem.Label")
		if action.getButtonCode() == 256:
			time.sleep(0.1)
			self.close()
		if action.getButtonCode() == 257 or action.getButtonCode() == 275:
			if xbmc.getCondVisibility('Player.HasVideo'): xbmc.Player().stop()
			time.sleep(0.1)
			self.close()
		if action.getButtonCode() == 261:
			if xbmc.getCondVisibility('Player.HasVideo'): xbmc.Player().stop()
			xbmc.executebuiltin('SetFocus(9990)')
		if action.getButtonCode() == 270 or action.getButtonCode() == 271 or action.getButtonCode() == 272 or action.getButtonCode() == 273 or action.getButtonCode() == 262 or action.getButtonCode() == 263:
			if xbmc.getCondVisibility('Player.HasVideo'): xbmc.Player().stop()
			loop = 0
			while True:
				if xbmc.getCondVisibility('Skin.HasSettings(editmode)'): break
				loop += 1
				time.sleep(0.05)
				Next_Label =  xbmc.getInfoLabel("Container(9000).ListItem.Label") ## Used to grab the current label so I can see if on next or previous is called.
				if xbmc.getCondVisibility('System.IdleTime('+Playback_Delay+')') and Different_Game_Selected == 0 and not xbmc.getCondVisibility('Window.IsActive(1120)') and not xbmc.getCondVisibility('Window.IsActive(1101)'):
					Different_Game_Selected	= 1
					Current_System		= xbmc.getInfoLabel("Container(9000).ListItem.Label2")
					Current_Label =  xbmc.getInfoLabel("Container(9000).ListItem.Label")
					FilePath = Media_Folder_Path+'/'+Current_System
					if os.path.isfile(FilePath+'.mp4'):
						if xbmc.getCondVisibility('Player.HasAudio'): xbmc.PlayList(0).clear()
						# playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
						# playlist.clear()
						# playlist.add(FilePath+'.mp4')
						# xbmc.Player().play(playlist,0,1)
						xbmc.executebuiltin('playmedia(' +FilePath+'.mp4,1,noresume)')
						Video_Played = 1
					elif os.path.isfile(FilePath+'.xmv'):
						if xbmc.getCondVisibility('Player.HasAudio'): xbmc.PlayList(0).clear()
						xbmc.executebuiltin('playmedia(' +FilePath+'.xmv,1,noresume)')
						Video_Played = 1
					break
				elif Current_Label != Next_Label: ## If current label doesn't match then we have moved selection, so stop video and play new one.
					Different_Game_Selected	= 0
				if loop == 350:
					break
if (__name__ == '__main__'):
	Root_Directory		= xbmc.translatePath("Special://root/")
	Playback_Delay		= "1"
	Music_Playing		= 0
	Video_Played		= 0
	Media_Folder_Path	= 'Q:/emustation/attract/'
	if xbmc.Player().isPlayingAudio():
		# CurrentPlaylistOffSet = xbmc.PlayList(0).getposition()
		# CurrentPlaylistTimeOffSet = xbmc.Player().getTime()
		# xbmc.PlayList(0).unshuffle()
		Music_Playing = 1
	try:
		ui = GUI('home.xml', os.getcwd())
		ui.doModal()
		del ui
		print "Auto video playback script exited properly"
	except: pass
if Music_Playing == 1 and xbmc.getCondVisibility('Skin.HasSetting(Use_Startup_Playback)') and Video_Played == 1:
	xbmc.executebuiltin('PlayMedia('+xbmc.getInfoLabel('Skin.String(Startup_Playback_Path)')+')')
	# xbmc.PlayList(0).unshuffle()
	# xbmc.executebuiltin('Playlist.PlayOffset('+str(CurrentPlaylistOffSet)+')')
	# while True:
		# try:
			# time.sleep(0.1)
			# xbmc.Player().seekTime(CurrentPlaylistTimeOffSet)
			# break
		# except: pass
	# xbmc.PlayList(0).shuffle()