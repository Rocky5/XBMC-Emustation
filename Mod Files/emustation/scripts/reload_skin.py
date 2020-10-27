import xbmc, xbmcgui
xbmcgui.Dialog().ok("ANIMATIONS ALTERED","","I need to reload the skin for these[CR]changes to take effect.")
xbmc.executebuiltin('Skin.Reset(ReloadSkin)')
xbmc.executebuiltin('ActivateWindow(10000)')
xbmc.executebuiltin('ReloadSkin')