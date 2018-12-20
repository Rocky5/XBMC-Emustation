'''
	Used to check for updates and notify the user.
'''
import os, urllib, urllib2, xbmc, xbmcgui
#####	Start markings for the log file.
print "| update_check.py loaded."
dialog = xbmcgui.Dialog()
# Used to check that you have internet access before letting you do anything.
try:
	home_url = 'http://www.xbmc-emustation.com/downloads/'
	download_path = 'Z:\\temp\\'
	if not os.path.exists( download_path ): os.makedirs( download_path )
	if not os.path.isfile(os.path.join(download_path,"version.bin")):
		if "Test Build" in xbmc.getLocalizedString(39999):
			urllib.urlretrieve(home_url + "/versions/TestBuild.bin",os.path.join(download_path,"version.bin"))
			xbmc.executebuiltin('Notification(Checking for updates,Current version ' + xbmc.getLocalizedString(39999)[-7:] + ')')
			if os.path.isfile( os.path.join(download_path,"version.bin") ):
				with open( os.path.join(download_path,"version.bin"), 'r') as versioncheck:
					versioncheck = versioncheck.readline().rstrip()
				if int(xbmc.getLocalizedString(39999)[-7:].replace(".","")) < int(versioncheck.replace(".","")):
					xbmcgui.Dialog().ok("NOTICE","","New version has been found[CR]Test Build: "+versioncheck)
				else:
					xbmc.executebuiltin('Notification(Checking for updates,No new version found)')
		else:
			urllib.urlretrieve(home_url + "/versions/Release.bin",os.path.join(download_path,"version.bin"))
			xbmc.executebuiltin('Notification(Checking for updates,Current version ' + xbmc.getLocalizedString(39999)[-7:] + ')')
			if os.path.isfile( os.path.join(download_path,"version.bin") ):
				with open( os.path.join(download_path,"version.bin"), 'r') as versioncheck:
					versioncheck = versioncheck.readline().rstrip()
				if int(xbmc.getLocalizedString(39999)[-7:].replace(".","")) < int(versioncheck.replace(".","")):
					xbmcgui.Dialog().ok("NOTICE","","New version has been found[CR]Release Build: "+versioncheck)
				else:
					xbmc.executebuiltin('Notification(Checking for updates,No new version found)')
except: pass