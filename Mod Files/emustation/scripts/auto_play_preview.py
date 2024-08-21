import os
import xbmc
import xbmcgui
import time

class GUI(xbmcgui.WindowXML):
	def onInit(self):
		self.Moved_Selection = True
		if xbmc.getCondVisibility('Skin.HasSetting(gameloaded)') and xbmc.getCondVisibility('Skin.HasSetting(lastromlist)'):
			xbmc.executebuiltin('Skin.Reset(gameloaded)')
			xbmc.executebuiltin('SetFocus(9000,' + xbmc.getInfoLabel('skin.string(lastrompos)') + ')')
		time.sleep(int(Playback_Delay))
		self.play_video()

	def play_video(self):
		if self.Moved_Selection:
			thumb = xbmc.getInfoLabel('Container(9000).ListItem.Thumb')[:-4].lower()
			video_extensions = ['.mp4', '.xmv']
			for ext in video_extensions:
				video_path = os.path.join(Media_Folder_Path, Current_System, 'videos', thumb + ext)
				if os.path.isfile(video_path):
					if not xbmc.getCondVisibility('Window.IsActive(1120)') and not xbmc.getCondVisibility('Window.IsActive(1101)'):
						xbmc.executebuiltin('playmedia(' + video_path + ',1,noresume)')
						xbmc.PlayList(0).clear()
						break
					
	def loop_check(self,timeout):
		if xbmc.Player().isPlayingVideo():
			xbmc.Player().stop()
			xbmc.PlayList(0).clear()
		loop = 0
		time.sleep(timeout)
		while True:
			if xbmc.getCondVisibility('Window.IsVisible(1101)') or xbmc.getCondVisibility('Window.IsVisible(10000)') or xbmc.getCondVisibility('Skin.HasSettings(editmode)'):
				xbmc.Player().stop()
				break

			loop += 1
			time.sleep(0.05)
			
			if not self.Moved_Selection and xbmc.getCondVisibility('System.IdleTime('+Playback_Delay+')'):
				self.Moved_Selection = True
				self.play_video()

			if loop == 110: # Break the loop if nothing has happened within the delay time
				break
	def onFocus(self, controlID): pass	
	def onClick(self, controlID): pass
	def onAction(self, action):
		self.Moved_Selection = False
		if action.getButtonCode() in [256, 257, 275]:
			xbmc.Player().stop()
			self.close()
		elif action.getButtonCode() == 258:
			time.sleep(0.1)
			self.loop_check(1)
		elif action.getButtonCode() == 261:
			xbmc.Player().stop()
			xbmc.executebuiltin('SetFocus(9990)')
		elif action.getButtonCode() in [270, 271, 272, 273, 262, 263]:
			self.loop_check(0)

if __name__ == '__main__':
	Root_Directory = xbmc.translatePath("Special://root/")
	Current_System = xbmc.getInfoLabel('Skin.String(emuname)')
	Playback_Delay = xbmc.getInfoLabel('Skin.String(videodelay)')
	Music_Playing = int(xbmc.Player().isPlayingAudio())
	Media_Folder_Path = xbmc.getInfoLabel('Skin.String(Custom_Media_Path)') or 'Q:/emustation/media/'

	if xbmc.getCondVisibility('Skin.HasSetting(gameloaded)') and xbmc.getCondVisibility('Skin.HasSetting(lastromlist)'):
		xbmc.executebuiltin('ActivateWindow(Home)')
		time.sleep(0.1)

	xbmc.executebuiltin('PlayWith(DVDPlayer)')

	try:
		ui = GUI('MyPrograms.xml', os.getcwd())
		ui.doModal()
		del ui
		print("Auto video playback script exited properly")
	except:
		pass

	if Music_Playing and xbmc.getCondVisibility('Skin.HasSetting(Use_Startup_Playback)') and not xbmc.Player().isPlayingAudio():
		startup_path = xbmc.getInfoLabel('Skin.String(Startup_Playback_Path)')
		xbmc.executebuiltin('PlayMedia(' + startup_path + ')')

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