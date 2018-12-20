'''
	Script by Rocky5
	Used to find and play a preview video for the selected control ID.
'''
import glob, os, xbmc, xbmcgui, time
#####	Start markings for the log file.
print "| play_preview.py loaded."
dialog			= xbmcgui.Dialog()
if str( xbmc.getCondVisibility( 'Skin.String(Custom_Media_Path)' ) ) == "1":
	Media_Folder_Path		= xbmc.getInfoLabel( 'Skin.String(Custom_Media_Path)' )
else:
	Media_Folder_Path		= 'Q:\\.emustation\\media\\'
Extensions		= ["mp4","strm","xmv"]
Current_System	= xbmc.getInfoLabel('Skin.String(emuname)')
Current_Memory	= xbmc.getInfoLabel( "system.freememory" )[:-2]
# XBE Files
PathXBE			= xbmc.getInfoLabel('listitem.path')
PathXBEAlt		= os.path.join( PathXBE, '_resources\\media' )
# Find video using supported extensions
XBEVideo = []
for ext in ('preview.mp4','preview.strm','preview.xmv'):
	XBEVideo.extend(glob.glob(os.path.join(PathXBE, ext)))
XBEVideo = ''.join(XBEVideo)
if XBEVideo == "":
	if os.path.isdir(PathXBEAlt):
		for VideoFile in sorted(os.listdir(PathXBEAlt)):
			if VideoFile.endswith(tuple(Extensions)):
				XBEVideo = VideoFile.lower()
	else:
		XBEVideo = ""
# Emulators
FileNameEMU		= xbmc.getInfoLabel('Container(9000).ListItem.Thumb')[:-4].lower()
PathEmu			= os.path.join( Media_Folder_Path, Current_System, 'videos' )
# Find video using supported extensions
EmuVideo = []
for ext in (''+FileNameEMU+'.mp4',''+FileNameEMU+'.strm',''+FileNameEMU+'.xmv'):
	EmuVideo.extend(glob.glob(os.path.join(PathEmu, ext)))
if Current_System == "ports" or Current_System == "apps" or xbmc.getCondVisibility('Skin.HasSetting(editmode)') == 1:
	Focus		= "50"
	VideoFile	= os.path.join(PathXBEAlt,XBEVideo)
else:
	Focus		= "9000"
	VideoFile	= ''.join(EmuVideo)
try:
	if int(Current_Memory) >= 8:
		if xbmc.getCondVisibility( 'Skin.HasSetting(synopsislayout)' ):
			if xbmc.Player().isPlayingVideo():
				xbmc.executebuiltin( 'SetFocus(9100)' )
			else:
				if os.path.isfile( VideoFile ):
					if VideoFile.endswith("xmv") or VideoFile.endswith("mp4"):
						xbmc.executebuiltin('PlayWith(DVDPlayer)')
						xbmc.executebuiltin( 'playmedia( ' + VideoFile + ',1,noresume )' )
					elif VideoFile.endswith("strm"):
						xbmc.executebuiltin('PlayWith(MPlayer)')
						xbmc.executebuiltin( 'playmedia( ' + VideoFile + ',1,noresume )' )
					else:
						xbmc.executebuiltin('PlayWith(MPlayer)')
						xbmc.executebuiltin( 'playmedia( ' + VideoFile + ',1,noresume )' )
					while True:
						if xbmc.Player().isPlayingVideo(): break
					xbmc.executebuiltin( 'SetFocus(9100)' )
				else:
					xbmc.executebuiltin( 'playmedia( Q:\\system\\media\\static.mp4,1,noresume )' )
					while True:
						if xbmc.Player().isPlayingVideo(): break
					xbmc.executebuiltin( 'SetFocus(9100)' )
		else:
			xbmc.executebuiltin( 'SetFocus(' + Focus + ')' )
	else:
		dialog.ok("OOPS!","There isn't enough free ram to play this video.","Current free ram = " + xbmc.getInfoLabel( "system.freememory" ) )
		xbmc.executebuiltin( 'SetFocus(' + Focus + ')' )
except:
	dialog.ok("ERROR","","Please rescan your roms to fix this issue." )
	xbmc.executebuiltin( 'SetFocus(' + Focus + ')' )