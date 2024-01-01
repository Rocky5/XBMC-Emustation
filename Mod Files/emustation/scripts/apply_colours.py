import glob,os,shutil,xbmc,xbmcgui
xbmc.executebuiltin("Skin.SetBool(SelectPreviewMode)") # This is set so the preview is shown in the skin settings menu when required.

Theme_Path = os.path.join(xbmc.translatePath('Special://themes_root/'),xbmc.getInfoLabel('Skin.CurrentTheme'))
Colours_Path = os.path.join(xbmc.translatePath('Special://themes_root/'),xbmc.getInfoLabel('Skin.CurrentTheme'),'colours/')
if os.path.isfile(os.path.join(Colours_Path,'default.xml')):
	TMP_Theme_Path = 'Z:/temp/colours/'
	if os.path.isdir(TMP_Theme_Path):
		shutil.rmtree(TMP_Theme_Path)
	os.makedirs(TMP_Theme_Path)
	XMLS = [os.path.basename(x) for x in sorted(glob.glob(Colours_Path+"*.xml"))]
	XMLS = [x.lower().replace('default',' default') for x in XMLS]

	try:
		for fn in XMLS:
			with open(os.path.join(TMP_Theme_Path,fn.upper()),"w") as ColourFiles:
				ColourFiles.write('')
	except: pass

	XMLS = sorted(os.listdir(TMP_Theme_Path))
	Filter_XMLS = [os.path.basename(r[0:-4]) for r in XMLS]
	Filter_XMLS = [x.replace(' D','D') for x in Filter_XMLS]
	ColourFolder = xbmcgui.Dialog().select('Select Theme Color',Filter_XMLS,10000)

	if ColourFolder == -1:
		pass
	else:
		SelectedColour = XMLS[ColourFolder]
		if SelectedColour.lower() == ' default.xml':
			ColourFile = 'default.xml'
		else:
			ColourFile = SelectedColour

		shutil.copy2(os.path.join(Colours_Path,ColourFile),os.path.join(Theme_Path,"colors.xml"))
		xbmc.executebuiltin('Skin.Reset(ReloadSkin)')
		xbmc.executebuiltin('ReloadSkin')
		xbmc.executebuiltin('Dialog.Close(all,true)')
	xbmc.executebuiltin("Skin.Reset(SelectPreviewMode)") # This is reset so the preview isn't shown in the skin settings menu when not required.
else:
	xbmcgui.Dialog().ok("ERROR","This theme doesn't support","custom colours as of yet.")