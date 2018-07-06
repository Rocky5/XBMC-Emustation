import xbmc
if xbmc.getCondVisibility( 'Skin.HasSetting(DisabledSounds)' ):
	xbmc.enableNavSounds(0)
else:
	xbmc.enableNavSounds(1)