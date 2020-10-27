import os, time, xbmc, xbmcgui
working_directory = os.getcwd() + '/'
dprogress = xbmcgui.DialogProgress()
xbmc.executebuiltin('Skin.SetString(DisableCancel,Disabled)')
xbmc.executebuiltin('Skin.SetString(DisableProgress,Disabled)')
dprogress.update(0)
dprogress.create("URLDOWNLOADER","","Loading...")
# Get args and pass them to run script
defaulturl = sys.argv[1:][0]
filename = sys.argv[2:][0]
try:
	zipsize = sys.argv[3:][0]
except:
	zipsize = ""
try:
	destination = sys.argv[4:][0]
except:
	destination = ""
try:
	keyboardmode = sys.argv[5:][0]
except:
	keyboardmode = ""
xbmcgui.Window(xbmcgui.getCurrentWindowId()).setProperty("MyScript.ExternalRunning", "True")
xbmc.executebuiltin('RunScript(' + xbmc.translatePath('Special://urldownloader/') + 'downloader.py'+','+defaulturl+','+filename+','+zipsize+','+destination+','+keyboardmode+')' )
while (xbmcgui.Window(xbmcgui.getCurrentWindowId()).getProperty("MyScript.ExternalRunning") == "True"):
	time.sleep(1)
dprogress.close()
xbmc.executebuiltin('Skin.SetString(DisableCancel,)')
xbmc.executebuiltin('Skin.SetString(DisableProgress,)')