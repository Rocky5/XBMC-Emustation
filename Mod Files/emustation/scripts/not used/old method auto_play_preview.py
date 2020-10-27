'''
	Script by Rocky5
	Used to find and play a preview video for the selected control ID.
'''
import os, xbmc, time
import xml.etree.ElementTree as ET
#####	Start markings for the log file.
print "| auto_play_preview.py loaded."
Root_Directory						= xbmc.translatePath("Special://root/")
Different_Game_Selected 			= 0
Current_System						= xbmc.getInfoLabel('Skin.String(emuname)')
Playback_Delay						= xbmc.getInfoLabel('Skin.String(videodelay)')
Video_Played						= 0
Music_Playing						= 0
if xbmc.getCondVisibility( 'Player.HasAudio' ): Music_Playing = 1
if Music_Playing == 1: xbmc.Player().pause() ## Workaround for music pausing for some reason due to the "while" section below.
xbmc.executebuiltin( 'SetFocus(9000)' )
if Current_System == "ports" or Current_System == "apps" or xbmc.getCondVisibility('Skin.HasSetting(editmode)') == 1: xbmc.executebuiltin( 'SetFocus(50)' )
Current_Label 						= xbmc.getInfoLabel( "Container(9000).ListItem.Label" )
xbmc.executebuiltin('PlayWith(DVDPlayer)')
if xbmc.getCondVisibility( 'Skin.String(Custom_Media_Path)' ) == 1:
	Media_Folder_Path				= xbmc.getInfoLabel( 'Skin.String(Custom_Media_Path)' )
else:
	Media_Folder_Path				= 'Q:\\.emustation\\media\\'
for tag in ET.parse( Root_Directory+'system\\userdata\\guisettings.xml' ).getroot().iter('screensaver'):
	screensaver_enabled				= tag.find('mode').text
	screensaver_time 				= int(tag.find('time').text)
	screensaver_time_min_set		= screensaver_time * 60 - 1
	screensaver_time_min_countd		= screensaver_time_min_set
while True:
	time.sleep(0.1)
	Next_Label =  xbmc.getInfoLabel( "Container(9000).ListItem.Label" ) ## Used to grab the current label so I can see if on next or previous is called.
	
	if xbmc.getCondVisibility('Control.HasFocus(9000)') and xbmc.getCondVisibility('System.IdleTime('+Playback_Delay+')') and Different_Game_Selected == 0 and xbmc.getCondVisibility( 'Skin.HasSetting(videolayout)' ) == 1 and not xbmc.getCondVisibility('Window.IsActive(1120)'):
		Different_Game_Selected		= 1
		Current_Label				=  xbmc.getInfoLabel( "Container(9000).ListItem.Label" )
		FileNameEMU					= xbmc.getInfoLabel('Container(9000).ListItem.Thumb')[:-4].lower()
		FilePath					= os.path.join( Media_Folder_Path, xbmc.getInfoLabel('Skin.String(emuname)'), 'videos\\' )+FileNameEMU
		if os.path.isfile( FilePath+'.mp4' ):
			xbmc.executebuiltin( 'playmedia( ' +FilePath+'.mp4,1,noresume )' )
			Video_Played			= 1
		elif os.path.isfile( FilePath+'.xmv' ):
			xbmc.executebuiltin( 'playmedia( ' +FilePath+'.xmv,1,noresume )' )
			Video_Played			= 1
		else:
			pass
			#xbmc.executebuiltin( 'playmedia( Q:\\system\\media\\static.mp4,1,noresume )' ) ## set above value to 1 if enabling this line.
	
	elif Current_Label != Next_Label: ## If current label doesn't match then we have moved selection, so stop video and play new one.
		if Video_Played == 1: xbmc.Player().stop()
		Different_Game_Selected		= 0
	
	if not xbmc.getCondVisibility('Window.IsActive(1500)') or xbmc.getCondVisibility('Window.IsActive(1101)'): ## Check if current window has changed if it has then break the loop.
		print "script exited due to leaving games list."
		if Music_Playing == 1 and xbmc.getCondVisibility( 'Skin.HasSetting(Use_Startup_Playback)' ) and Video_Played == 1:
			time.sleep(0.1)
			xbmc.executebuiltin('PlayMedia('+xbmc.getInfoLabel('Skin.String(Startup_Playback_Path)')+')')
			xbmc.executebuiltin('playercontrol(RepeatAll)')
		elif xbmc.getCondVisibility( 'Player.HasVideo' ):
			xbmc.Player().stop()
		break
	
	if not screensaver_enabled == "None" and not screensaver_time == "00:10" or not xbmc.getCondVisibility('Window.IsActive(1500)'): ## Check if screensaver is enabled and counting down then break the loop.
		if not xbmc.Player().isPlayingVideo() and xbmc.getCondVisibility('System.IdleTime(1)'):
			mins, secs = divmod(screensaver_time_min_countd, 60)
			screensaver_time 			= '{:02d}:{:02d}'.format(mins, secs)
			#xbmc.executebuiltin('Notification(Count Down,'+screensaver_time+')')
			time.sleep(1)
			screensaver_time_min_countd -= 1
		else:
			screensaver_time_min_countd = screensaver_time_min_set
	else:
		if not screensaver_enabled == "None":
			print "screensaver is about to kick in, so exiting script so not to hang in limbo."
			break