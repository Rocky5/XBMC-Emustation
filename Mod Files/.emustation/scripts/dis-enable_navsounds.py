import xbmc
#####	Start markings for the log file.
print "| dis-enable_navsounds.py loaded."
if xbmc.getCondVisibility( 'Skin.HasSetting(DisabledSounds)' ):
	xbmc.enableNavSounds(0)
else:
	xbmc.enableNavSounds(1)