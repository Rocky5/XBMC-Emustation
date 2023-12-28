import os, xbmc, xbmcgui, time
class GUI(xbmcgui.WindowXML):
	def onInit(self):
		global Moved_Selection
		Moved_Selection = 0
		if xbmc.getCondVisibility('Skin.HasSetting(gameloaded)') and xbmc.getCondVisibility('Skin.HasSetting(lastromlist)'):
			xbmc.executebuiltin('Skin.Reset(gameloaded)')
			xbmc.executebuiltin('SetFocus(9000,'+xbmc.getInfoLabel('skin.string(lastrompos)')+')')
		time.sleep(int(Playback_Delay))
		if Moved_Selection == 0:
			FilePath = Media_Folder_Path+Current_System+'/videos/'+xbmc.getInfoLabel('Container(9000).ListItem.Thumb')[:-4].lower()
			if os.path.isfile(FilePath+'.mp4'):
				xbmc.executebuiltin('playmedia(' +FilePath+'.mp4,1,noresume)')
			elif os.path.isfile(FilePath+'.xmv'):
				xbmc.executebuiltin('playmedia(' +FilePath+'.xmv,1,noresume)')
			if xbmc.Player().isPlayingVideo(): xbmc.PlayList(0).clear()
	def onFocus(self, controlID): pass	
	def onClick(self, controlID): pass
	def onAction(self, action):
		global Moved_Selection
		Moved_Selection = 0
		loop = 0
		if action.getButtonCode() == 256:
			if xbmc.Player().isPlayingVideo(): xbmc.Player().stop()
			self.close()
		if action.getButtonCode() == 257 or action.getButtonCode() == 275:
			if xbmc.Player().isPlayingVideo(): xbmc.Player().stop()
			self.close()
		if action.getButtonCode() == 261:
			if xbmc.Player().isPlayingVideo(): xbmc.Player().stop()
			xbmc.executebuiltin('SetFocus(9990)')
		if action.getButtonCode() == 270 or action.getButtonCode() == 271 or action.getButtonCode() == 272 or action.getButtonCode() == 273 or action.getButtonCode() == 262 or action.getButtonCode() == 263:
			if xbmc.Player().isPlayingVideo():
				xbmc.Player().stop()
				xbmc.PlayList(0).clear()
			while True:
				if xbmc.getCondVisibility('Window.IsVisible(1101)') or xbmc.getCondVisibility('Window.IsVisible(10000)') or xbmc.getCondVisibility('Skin.HasSettings(editmode)'):
					xbmc.Player().stop()
					break
				loop += 1
				time.sleep(0.05)
				if xbmc.getCondVisibility('System.IdleTime('+Playback_Delay+')') and Moved_Selection == 0 and not xbmc.getCondVisibility('Window.IsActive(1120)') and not xbmc.getCondVisibility('Window.IsActive(1101)'):
					Moved_Selection = 1
					FilePath = Media_Folder_Path+Current_System+'/videos/'+xbmc.getInfoLabel('Container(9000).ListItem.Thumb')[:-4].lower()
					if os.path.isfile(FilePath+'.mp4'):
						xbmc.executebuiltin('playmedia(' +FilePath+'.mp4,1,noresume)')
						break
					elif os.path.isfile(FilePath+'.xmv'):
						xbmc.executebuiltin('playmedia(' +FilePath+'.xmv,1,noresume)')
						break
					else:
						break
				if loop == 110: # used to break the loop if nothing has happened within the delay time
					break
if (__name__ == '__main__'):
	Root_Directory				= xbmc.translatePath("Special://root/")
	Current_System				= xbmc.getInfoLabel('Skin.String(emuname)')
	Playback_Delay				= xbmc.getInfoLabel('Skin.String(videodelay)')
	Music_Playing				= 0
	if xbmc.getCondVisibility('Skin.HasSetting(gameloaded)') and xbmc.getCondVisibility('Skin.HasSetting(lastromlist)'):
		xbmc.executebuiltin('ActivateWindow(Home)') # loaded so back works
		time.sleep(0.1)
	xbmc.executebuiltin('PlayWith(DVDPlayer)')
	if xbmc.getCondVisibility('Skin.String(Custom_Media_Path)') == 1:
		Media_Folder_Path		= xbmc.getInfoLabel('Skin.String(Custom_Media_Path)')
	else:
		Media_Folder_Path		= 'Q:/emustation/media/'
	if xbmc.Player().isPlayingAudio(): Music_Playing = 1
	try:
		ui = GUI('MyPrograms.xml', os.getcwd())
		ui.doModal()
		del ui
		print "Auto video playback script exited properly"
	except:
		pass
	if Music_Playing == 1 and xbmc.getCondVisibility('Skin.HasSetting(Use_Startup_Playback)') and not xbmc.Player().isPlayingAudio():
		xbmc.executebuiltin('PlayMedia('+xbmc.getInfoLabel('Skin.String(Startup_Playback_Path)')+')')

### KEY_BUTTON_A                        256
### KEY_BUTTON_B                        257
### KEY_BUTTON_X                        258
### KEY_BUTTON_Y                        259
### KEY_BUTTON_BLACK                    260
### KEY_BUTTON_WHITE                    261
### KEY_BUTTON_LEFT_TRIGGER             262
### KEY_BUTTON_RIGHT_TRIGGER            263
### KEY_BUTTON_LEFT_THUMB_STICK         264
### KEY_BUTTON_RIGHT_THUMB_STICK        265
### KEY_BUTTON_RIGHT_THUMB_STICK_UP     266
### KEY_BUTTON_RIGHT_THUMB_STICK_DOWN   267
### KEY_BUTTON_RIGHT_THUMB_STICK_LEFT   268
### KEY_BUTTON_RIGHT_THUMB_STICK_RIGHT  269
### KEY_BUTTON_DPAD_UP                  270
### KEY_BUTTON_DPAD_DOWN                271
### KEY_BUTTON_DPAD_LEFT                272
### KEY_BUTTON_DPAD_RIGHT               273
### KEY_BUTTON_START                    274
### KEY_BUTTON_BACK                     275
### KEY_BUTTON_LEFT_THUMB_BUTTON        276
### KEY_BUTTON_RIGHT_THUMB_BUTTON       277
### KEY_BUTTON_LEFT_ANALOG_TRIGGER      278
### KEY_BUTTON_RIGHT_ANALOG_TRIGGER     279
### KEY_BUTTON_LEFT_THUMB_STICK_UP      280
### KEY_BUTTON_LEFT_THUMB_STICK_DOWN    281
### KEY_BUTTON_LEFT_THUMB_STICK_LEFT    282
### KEY_BUTTON_LEFT_THUMB_STICK_RIGHT   283