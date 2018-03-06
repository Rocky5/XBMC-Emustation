'''
	Edited to work with XBMC-Emustation and have vars passed to it for downloading files.
'''
import extract, os, hashlib, requests, shutil ,time ,urllib ,urllib2, urlparse, xbmc, xbmcgui
dialog = xbmcgui.Dialog()
dprogress = xbmcgui.DialogProgress()
def check_for_update(url):
	if not os.path.exists( download_path ): os.makedirs( download_path )
	path = os.path.join(download_path,url.split('/')[-1])
	download(url, path, dprogress)
def download_url(url):
	dprogress.create("DOWNLOADING","","Initializing")
	if not os.path.exists( download_path ): os.makedirs( download_path )
	path = os.path.join(download_path,url.split('/')[-1])
	dprogress.update(0,filename,"This can take some time, please be patient.")
	download(url, path, dprogress)
def download(url, dest, dprogress = None):
	dprogress.update(0)
	urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dprogress))
def _pbhook(numblocks, blocksize, filesize, url, dprogress):
	try:
		percent = min((numblocks*blocksize*100)/filesize, 100)
		dprogress.update(percent)
	except:
		percent = 100
		dprogress.update(percent)
	if dprogress.iscanceled():
		if allowcancellation == 1:	raise Exception("Canceled")
def extract_file(file):
	time.sleep(1)
	if not os.path.exists( destination ): os.makedirs( destination )
	dprogress.create("EXTRACTING","","Initializing")
	zippath = destination
	dprogress.update(0,filename,"This can take some time, please be patient." )
	extract.all(file, zippath, dprogress)
	time.sleep(1)
def clear_X():
	try:
		dprogress.create("CACHE","","Initializing")
		for root, dirs, files in os.walk("X:\\", topdown=False):
			for name in files:
				os.remove(os.path.join(root, name))
			for name in dirs:
				os.rmdir(os.path.join(root, name))
			dprogress.update(0,'', 'Prepping Cache')
			time.sleep(0.1)
	except:
		pass
# Used to check that you have internet access before letting you do anything.
try:
	urllib2.urlopen('http://172.217.23.142', timeout=4)
	home_url = 'http://www.xbmc-emustation.com/downloads/'
	# args
	try:
		defaulturl = home_url + sys.argv[1:][0]
		md5hashurl = defaulturl[:-4] + ".md5"
		filename = defaulturl.split("/")[-1]
		exit = 1
	except:
		exit = 0
	try:
		destination = sys.argv[2:][0]
	except:
		destination = ""
	try:
		keyboardmode = sys.argv[3:][0]
	except:
		keyboardmode = ""
	if keyboardmode == "keyboard_mode":
		defaulturl = ''
		keyboard = xbmc.Keyboard('default', 'heading')
		keyboard.setDefault(defaulturl)
		keyboard.setHeading('Formating = URL,md5hash')
		xbmc.executebuiltin('Dialog.Close(1101,true)')
		keyboard.doModal()
		if (keyboard.isConfirmed()):
			defaulturl = keyboard.getText()
			if defaulturl.startswith('https://'): defaulturl = defaulturl.replace('https://','http://')
			if not defaulturl.startswith('ftp://') and not defaulturl.startswith('http://'): defaulturl = 'http://'+defaulturl
			print defaulturl
			dprogress.create("REQUESTING URL","","Please wait...")
			defaulturl = requests.head(defaulturl, allow_redirects=True).url
			dprogress.close()
			md5hash = defaulturl.split(",")[1]
			defaulturl = defaulturl.split(",")[0].replace('%20',' ')
			filename = defaulturl.split("/")[-1]
			exit = 1
		else:
			filename = ""
			exit = 0
	# vars
	if destination == "Emulator_Folder_Path":
		if xbmc.getCondVisibility( 'Skin.String(Custom_Emulator_Path)' ): destination = xbmc.getInfoLabel( 'Skin.String(Custom_Emulator_Path)' )
		else: destination = 'Q:\\.emustation\\emulators\\'
	if destination == "Roms_Folder_Path":
		if xbmc.getCondVisibility( 'Skin.String(Custom_Roms_Path)' ): destination	= xbmc.getInfoLabel( 'Skin.String(Custom_Roms_Path)' )
		else: destination	= 'Q:\\.emustation\\roms\\'
	if destination == "Media_Folder_Path":
		if xbmc.getCondVisibility( 'Skin.String(Custom_Media_Path)' ): destination = xbmc.getInfoLabel( 'Skin.String(Custom_Media_Path)' )
		else: destination = 'Q:\\.emustation\\media\\'
	percent = 0
	allowcancellation = 0
	hashlib = hashlib.md5()
	extensions = [ 'zip' ]
	download_path = 'X:\\downloads\\'
	# Download the check file to see if there is an update.
	check_for_update( home_url + 'versions/URLDownloader.bin' )
	with open( 'Q:\\.emustation\\scripts\\urldownloader\\version.bin', 'r') as verfile:
		local_version = verfile.readline().rstrip()
	with open( 'X:\\downloads\\URLDownloader.bin', 'r') as verfile:
		version = verfile.readline().rstrip()
	os.remove( 'X:\\downloads\\URLDownloader.bin' )
	if version == local_version or filename == "URLDownloader.zip" or xbmc.getInfoLabel('Control.GetLabel(1)') == "Download Assets":
		file = os.path.join(download_path,filename)
		md5hashfile = file[:-4] + ".md5"
		xbmc.executebuiltin('Dialog.Close(1101,true)')
		if os.path.isfile( file ):
			os.remove( file )
		if exit:
			if filename.endswith(tuple(extensions)):
				if dialog.yesno("URLDOWNLOADER","","Would you like to download[CR]" + filename):
					if destination == "":
						destination = dialog.browse( 3,"Select destination folder",'files','' )
					try:
						clear_X()
						global allowcancellation
						allowcancellation = 1
						download_url( defaulturl )
						if keyboardmode == "":
							download_url( md5hashurl )
							with open( md5hashfile, 'r') as md5file:
								md5hash = md5file.readline().rstrip()
							os.remove( md5hashfile )
						# Generate MD5 Hash from downloaded file.
						with open( file, "rb") as inputfile:
							file_content = inputfile.read(1024*1024)
							dprogress.create("CHECKING CONSISTENCY","","Initializing")
							while file_content:
								dprogress.update(( percent * 100 ) / os.path.getsize( file ),"Calculating MD5 Hash","This can take some time, please be patient." )
								hashlib.update( file_content )
								file_content = inputfile.read(1024*1024)
								percent = percent+1024*1024
						if md5hash == hashlib.hexdigest():
							extract_file( file )
							os.remove( file )
							dprogress.close()
							if filename == "XBMC-Emustation-update-files.zip" and os.path.isfile( 'Q:\\updater\\default.xbe'):
								xbmc.executebuiltin('RunXBE(Q:\\updater\\default.xbe)')
							elif filename == "URLDownloader.zip" and os.path.isdir( 'Q:\\system\\scripts\\urldownloader'):
								xbmc.executebuiltin('RunScript(Q:\\system\\scripts\\autoexec.py)')
							else:
								dialog.ok("SUCCESS","",filename + " Installed")
								if filename == "Download Lists.zip": xbmc.executebuiltin('ReloadSkin')
						else:
							dialog.ok("ERROR","MD5Hash Mismatch","Server Hash: " + md5hash,"Local Hash: " + hashlib.hexdigest())
							os.remove( file )
					except:
						if dprogress.iscanceled():
							dprogress.close()
							dialog.ok("URLDOWNLOADER","You cancelled the download of",filename)
						else:
							dprogress.close()
							dialog.ok("ERROR","","Server or local network issue")
			else:
				dialog.ok("ERROR","Supported files",extensions)
		else:
			if keyboardmode == "": dialog.ok("ERROR","Missing required information.")
	else:
		xbmc.executebuiltin('Dialog.Close(1101,true)')
		xbmcgui.Dialog().ok("UPDATE","Please update","[B]URLDownloader[/B] then the [B]Download Lists[/B]")
except urllib2.URLError as err:
	xbmc.executebuiltin('Dialog.Close(1101,true)')
	xbmcgui.Dialog().ok("ERROR","No network access","Please check your ethernet cable")