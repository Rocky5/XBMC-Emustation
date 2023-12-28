import os,xbmc,xbmcgui
xbmc.executebuiltin("Skin.SetBool(SelectPreviewMode)") # This is set so the preview is shown in the skin settings menu when required.
Error = 0
Theme_Path = xbmc.translatePath('Special://themes_root/')
ThemeFolder = xbmcgui.Dialog().select("Select Theme",sorted(os.listdir(Theme_Path)),10000)
ThemeFile = os.path.join(sorted(os.listdir(Theme_Path))[ThemeFolder])
if ThemeFolder == -1:
	pass
else:
	# Check if it's a v1.5+ theme.
	if os.path.isfile(os.path.join(Theme_Path,ThemeFile,"colors.xml")):
		with open(os.path.join(Theme_Path,ThemeFile,"colors.xml")) as read_file:
			if "XBMC-Emustation v1.5+" in read_file.read():
				xbmc.executehttpapi('SetGUISetting(3;lookandfeel.skintheme;%s.xpr)'%ThemeFile)
				xbmc.executehttpapi('SetGUISetting(3;lookandfeel.skincolors;%s.xml)'%ThemeFile)
				xbmc.executehttpapi('SetGUISetting(3;lookandfeel.font;%s.ttf)'%ThemeFile)
				xbmc.executebuiltin('RunScript(Special://emustation_scripts/home_themer.py)')
			else:
				Error = 1
			# with open(os.path.join(Theme_Path,ThemeFile,"colors.xml")) as read_file:
				# for line in read_file.readlines():
					# if 'instant=' in line:
						# xbmc.executebuiltin('Skin.SetString(custom_theme_instant_label,%s))'%line.split('=',1)[1].split(' --',1)[0])
					# if 'fade=' in line:
						# xbmc.executebuiltin('Skin.SetString(custom_theme_fade_label,%s))'%line.split('=',1)[1].split(' --',1)[0])
					# if 'slide=' in line:
						# xbmc.executebuiltin('Skin.SetString(custom_theme_slide_label,%s))'%line.split('=',1)[1].split(' --',1)[0])
	else:
		Error = 1
if Error: xbmcgui.Dialog().ok('ERROR','','This theme is not compatible with this version[CR]of XBMC-Emustation.','')
xbmc.executebuiltin("Skin.Reset(SelectPreviewMode)") # This is reset so the preview isn't shown in the skin settings menu when not required.