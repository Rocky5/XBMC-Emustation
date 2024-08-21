import time, xbmc
if xbmc.getCondVisibility('Skin.HasSetting(Use_Startup_Playback)'):
	time.sleep(0.5)
	xbmc.executebuiltin('PlayMedia('+xbmc.getInfoLabel('Skin.String(Startup_Playback_Path)')+')')
	xbmc.PlayList(0).shuffle()
	xbmc.executebuiltin('playercontrol(RepeatAll)')