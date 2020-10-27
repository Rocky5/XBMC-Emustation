import os,xbmc,xbmcgui
xbmc.executebuiltin("Skin.SetBool(SelectPreviewMode)") # This is set so the preview is shown in the skin settings menu when required.
Theme_Path = xbmc.translatePath('Special://themes_root/')
ThemeFolder = xbmcgui.Dialog().select("Select Theme",sorted(os.listdir(Theme_Path)),10000)
ThemeFile = os.path.join(sorted(os.listdir(Theme_Path))[ThemeFolder])
if ThemeFolder == -1:
	pass
else:
	xbmc.executehttpapi('SetGUISetting(3;lookandfeel.skintheme;%s.xpr)'%ThemeFile)
	xbmc.executehttpapi('SetGUISetting(3;lookandfeel.skincolors;%s.xml)'%ThemeFile)
	xbmc.executehttpapi('SetGUISetting(3;lookandfeel.font;%s.ttf)'%ThemeFile)
	xbmc.executebuiltin('RunScript(Special://emustation_scripts/home_themer.py)')
xbmc.executebuiltin("Skin.Reset(SelectPreviewMode)") # This is reset so the preview isn't shown in the skin settings menu when not required.