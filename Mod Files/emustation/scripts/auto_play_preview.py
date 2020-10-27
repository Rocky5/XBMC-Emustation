import os, xbmc, xbmcgui, time
import xml.etree.ElementTree as ET
class GUI(xbmcgui.WindowXML):
	def onInit(self):
		global Video_Played
		if xbmc.getCondVisibility('Skin.HasSetting(gameloaded)') and xbmc.getCondVisibility('Skin.HasSetting(lastromlist)'):
			xbmc.executebuiltin('SetFocus(9000,'+xbmc.getInfoLabel('skin.string(lastrompos)')+')')
			xbmc.executebuiltin('Skin.Reset(gameloaded)')
		time.sleep(int(Playback_Delay))
		FilePath = Media_Folder_Path+Current_System+'/videos/'+xbmc.getInfoLabel('Container(9000).ListItem.Thumb')[:-4].lower()
		if os.path.isfile(FilePath+'.mp4'):
			xbmc.executebuiltin('playmedia(' +FilePath+'.mp4,1,noresume)')
			Video_Played = 1
		elif os.path.isfile(FilePath+'.xmv'):
			xbmc.executebuiltin('playmedia(' +FilePath+'.xmv,1,noresume)')
			Video_Played = 1
		if Video_Played == 1 and Music_Playing == 1: xbmc.PlayList(0).clear()
	def onFocus(self, controlID):
		if xbmc.getCondVisibility('Player.HasVideo'): xbmc.Player().stop()
	def onClick(self, controlID): pass
	def onAction(self, action):
		global Moved_Selection
		global loop
		global Video_Played
		Moved_Selection = 0
		if action.getButtonCode() == 256:
			xbmc.Player().stop()
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
				if xbmc.getCondVisibility('Window.IsVisible(1101)') or xbmc.getCondVisibility('Window.IsVisible(10000)') or xbmc.getCondVisibility('Skin.HasSettings(editmode)'):
					xbmc.Player().stop()
					break
				loop += 1
				time.sleep(0.05)
				if xbmc.getCondVisibility('System.IdleTime('+Playback_Delay+')') and Moved_Selection == 0 and not xbmc.getCondVisibility('Window.IsActive(1120)') and not xbmc.getCondVisibility('Window.IsActive(1101)'):
					Moved_Selection = 1
					FilePath = Media_Folder_Path+Current_System+'/videos/'+xbmc.getInfoLabel('Container(9000).ListItem.Thumb')[:-4].lower()
					if os.path.isfile(FilePath+'.mp4'):
						if Music_Playing == 1: xbmc.PlayList(0).clear()
						xbmc.executebuiltin('playmedia(' +FilePath+'.mp4,1,noresume)')
						Video_Played = 1
					elif os.path.isfile(FilePath+'.xmv'):
						if Music_Playing == 1: xbmc.PlayList(0).clear()
						xbmc.executebuiltin('playmedia(' +FilePath+'.xmv,1,noresume)')
						Video_Played = 1
				if loop == 120:
					break
if (__name__ == '__main__'):
	global Music_Playing
	Root_Directory						= xbmc.translatePath("Special://root/")
	Current_System						= xbmc.getInfoLabel('Skin.String(emuname)')
	Playback_Delay						= xbmc.getInfoLabel('Skin.String(videodelay)')
	Music_Playing						= 0
	Video_Played						= 0
	if xbmc.getCondVisibility('Skin.String(Custom_Media_Path)') == 1:
		Media_Folder_Path				= xbmc.getInfoLabel('Skin.String(Custom_Media_Path)')
	else:
		Media_Folder_Path				= 'Q:/emustation/media/'
	if xbmc.Player().isPlayingAudio():
		Music_Playing = 1
	try:
		ui = GUI('MyPrograms.xml', os.getcwd())
		ui.doModal()
		del ui
		print "Auto video playback script exited properly"
	except: pass
	if Music_Playing == 1 and xbmc.getCondVisibility('Skin.HasSetting(Use_Startup_Playback)') and Video_Played == 1:
		xbmc.executebuiltin('PlayMedia('+xbmc.getInfoLabel('Skin.String(Startup_Playback_Path)')+')')