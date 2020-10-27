'''
	Edited to work with XBMC-Emustation and have vars passed to it for downloading files.
'''
import extract, hashlib, hmac, logging, math, operator, os, requests, shutil, struct, time, traceback, urllib2, urlparse, xbmc, xbmcgui, warnings
dialog = xbmcgui.Dialog()
dprogress = xbmcgui.DialogProgress()
working_directory = os.getcwd() + '/'
class GoogleDriveDownloader:
	CHUNK_SIZE = 32768
	DOWNLOAD_URL = "https://docs.google.com/uc?export=download"
	@staticmethod
	def download_file_from_google_drive(file_id, dest_path, zipsize, filename, overwrite=False, unzip=False, showsize=False):
		destination_directory = os.path.dirname(dest_path)
		if not os.path.exists(destination_directory):
			makedirs(destination_directory)
		if not os.path.exists(dest_path) or overwrite:
			if filename == "Update":
				dprogress.create("URLDOWNLOADER","","Checking for update")
			else:
				dprogress.create("URLDOWNLOADER","","Resolving Google Drive link")
			session = requests.Session()
			response = session.get(GoogleDriveDownloader.DOWNLOAD_URL, params={'id': file_id}, stream=True)
			token = GoogleDriveDownloader._get_confirm_token(response)
			if token:
				params = {'id': file_id, 'confirm': token}
				response = session.get(GoogleDriveDownloader.DOWNLOAD_URL, params=params, stream=True)
			current_download_size = [0]
			GoogleDriveDownloader._save_response_content(response, dest_path, showsize, current_download_size, zipsize, filename)
			if unzip:
				try:
					with zipfile.ZipFile(dest_path, 'r') as z:
						z.extractall(destination_directory)
				except zipfile.BadZipfile:
					warnings.warn('Ignoring `unzip` since "{}" does not look like a valid zip file'.format(file_id))
	@staticmethod
	def _get_confirm_token(response):
		for key, value in response.cookies.items():
			if key.startswith('download_warning'):
				return value
		return None
	@staticmethod # 
	def _save_response_content(response, destination, showsize, current_size, zipsize, filename):
		percent = 0
		global allowcancellation
		allowcancellation = 1
		try:
			with open(destination, 'wb') as f:
				for chunk in response.iter_content(GoogleDriveDownloader.CHUNK_SIZE):
					if chunk:  # filter out keep-alive new chunks
						f.write(chunk)
						if showsize:
							percent = int(str(current_size).strip('[]'))*101/zipsize
							current_size[0] += GoogleDriveDownloader.CHUNK_SIZE
							dprogress.update(percent,filename,"This can take some time, please be patient.")
							if dprogress.iscanceled():
								if allowcancellation == 1:	raise Exception("Cancelled")
		except Exception as err:
			pass
def check_for_update(url):
	if not os.path.exists( update_path ): os.makedirs( update_path )
	path = os.path.join(update_path,url.split('/')[-1])
	filename = updatename
	GoogleDriveDownloader.download_file_from_google_drive(file_id=str(url), dest_path=str(update_path+filename), zipsize=int(zipsize), filename="Update", unzip=False, showsize=False, overwrite=True)
def download_url(url):
	dprogress.create("DOWNLOADING","","Initializing")
	if not os.path.exists( download_path ): os.makedirs( download_path )
	path = os.path.join(download_path,url.split('/')[-1])
	GoogleDriveDownloader.download_file_from_google_drive(file_id=str(url), dest_path=str(file), zipsize=int(zipsize), filename=filename, unzip=False, showsize=True, overwrite=True)
def extract_file(file):
	time.sleep(1)
	if not os.path.exists( xbmc.translatePath(destination) ): os.makedirs( xbmc.translatePath(destination) )
	dprogress.create("EXTRACTING","","Initializing")
	zippath = xbmc.translatePath(destination)
	dprogress.update(0,filename,"This can take some time, please be patient." )
	extract.all(file, zippath, dprogress)
	time.sleep(1)
def clear_X():
	try:
		dprogress.create("CACHE","","Initializing")
		for root, dirs, files in os.walk("X:/", topdown=False):
			for name in files:
				os.remove(os.path.join(root, name))
			for name in dirs:
				os.rmdir(os.path.join(root, name))
			dprogress.update(0,'', 'Prepping Cache')
			time.sleep(0.1)
	except:
		pass
def convert_size(size_bytes):
	if size_bytes == 0:
		return "0B"
	size_name = ("B", "KB", "MB")
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p, 2)
	return "%s %s" % (s, size_name[i])
# Used to check that you have internet access before letting you do anything.
try:
	urllib2.urlopen('http://51.255.141.154', timeout=1)
	# args
	try:
		defaulturl = sys.argv[1:][0]
		filename = sys.argv[2:][0]
		exit = 1
	except:
		exit = 0
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
	# vars
	if destination == "Emulator_Folder_Path":
		if xbmc.getCondVisibility( 'Skin.String(Custom_Emulator_Path)' ): destination = xbmc.getInfoLabel( 'Skin.String(Custom_Emulator_Path)' )
		else: destination = ""
	if destination == "Roms_Folder_Path":
		if xbmc.getCondVisibility( 'Skin.String(Custom_Roms_Path)' ): destination	= xbmc.getInfoLabel( 'Skin.String(Custom_Roms_Path)' )
		else: destination = ""
	if destination == "Media_Folder_Path":
		if xbmc.getCondVisibility( 'Skin.String(Custom_Media_Path)' ): destination = xbmc.getInfoLabel( 'Skin.String(Custom_Media_Path)' )
		else: destination = ""
	global updatename
	global allowcancellation
	allowcancellation = 0
	udhashlibmd5 = hashlib.md5()
	hashlibsha1 = hashlib.sha1
	extensions = [ 'zip' ]
	download_path = 'X:/downloads/'
	update_path = 'Z:/temp/'
	dlcmode = 0
	xmlinvalid = 0
	urldinvalid = 0
	exit = 1
	zipsizediag = convert_size(float(zipsize))
	try:
		current_skin_version = int(xbmc.getLocalizedString(31000)[-7:].replace(".",""))
	except:
		current_skin_version = int(xbmc.getLocalizedString(31000)[-7:].replace(".",""))
	# Download the check file to see if there is an update. Doing it this way speeds up the loading after you download 1 files ad the files are kept until a reboot.
	if not filename == "URLDownloader.zip" and not filename == "XBMC-Emustation-update-files.zip" and not filename == "XBMC-Emustation-test-build.zip" and not filename == "XBMC4Gamers-update-files.zip" and not filename == "XBMC4Gamers-test-build.zip":
		if not os.path.isfile( 'Z:/temp/URLDownloader.bin' ):
			updatename = 'URLDownloader.bin'
			check_for_update( '1Hw02Uwn1izByJhcsWTNzgtJfUdTPk1TG' )
			with open( working_directory + 'version.bin', 'r') as verfile:
				local_version = verfile.readline().rstrip()
			with open( 'Z:/temp/URLDownloader.bin', 'r') as verfile:
				urldversion = verfile.readline().rstrip()
			if int(local_version.replace(".","")) < int(urldversion.replace(".","")):
				os.remove( 'Z:/temp/URLDownloader.bin' )
				urldinvalid = 1
		if not os.path.isfile( 'Z:/temp/DownloadList.bin' ):
			updatename = 'DownloadList.bin'
			check_for_update( '1udJy_7OfVES0iV2g5Q3TVT1Afobu0lYb' )
			with open( 'Z:/temp/DownloadList.bin', 'r') as verfile:
				dlsversion = verfile.readline().rstrip()
			with open( xbmc.translatePath('Special://skin/720p/_Script_URLDownloader.xml'), "rb") as updatefile:
				udhashlibmd5.update( updatefile.read() )
			if udhashlibmd5.hexdigest() != dlsversion:
				os.remove( 'Z:/temp/DownloadList.bin' )
				xmlinvalid = 1
		dprogress.close()
	# If hash doesn't match tell user to update, also if filename is the urldownloader.zip bypass.
	if xmlinvalid == 0 and urldinvalid == 0 or filename == "URLDownloader.zip" or xbmc.getInfoLabel('Control.GetLabel(1)') == "Download Assets":
		# This is here to fix compatibility issues with previous builds.
		file = os.path.join(download_path,filename)
		# Truncate the filename to look cleaner and also get the titleid for DLC installation.
		if keyboardmode == "DLC":
			titleid = filename[-12:]; titleid = titleid[:-4]
			filename = filename[:-13]+'.zip'
			dlcmode = 1
		xbmc.executebuiltin('Dialog.Close(1101,true)')
		if os.path.isfile( file ):
			os.remove( file )
		# Check to see if we need the newer version of Emustation or Gamers, v1.2.000 or later.
		if current_skin_version >= int(12000) or filename == "URLDownloader.zip" or filename == "XBMC-Emustation-update-files.zip" or filename == "XBMC-Emustation-test-build.zip" or filename == "XBMC4Gamers-update-files.zip" or filename == "XBMC4Gamers-test-build.zip":
			pass
		else:
			xbmcgui.Dialog().ok("WARNING","Please update to the latest versions of","XBMC-Emustation or XBMC4Gamers","v1.2 or later is required to use the downloader")
			keyboardmode = "empty"
			exit = 0
		if exit:
			xbmcgui.Window(xbmcgui.getCurrentWindowId()).setProperty("MyScript.ExternalRunning", "False")
			if dialog.yesno("DOWNLOAD","",filename+"[CR]Install size "+zipsizediag):
				if destination == "":
					destination = dialog.browse( 3,"Select destination folder",'files','' )
					if keyboardmode == "MOD":
						if os.path.isfile( os.path.join( destination, 'default.xbe' ) ):
							pass
						else:
							dialog.ok("ERROR","Cant find a default.xbe","Did you select the proper folder?")
							destination = 0
				if destination:
					destinationsizecheck = destination
					if destinationsizecheck.startswith('Special:'): destinationsizecheck = xbmc.translatePath('Special://root/')[:2]
					if destinationsizecheck.startswith('Q:'): destinationsizecheck = xbmc.translatePath('Special://root/')[:2]
					partition_free_space = xbmc.getInfoLabel('System.Freespace('+destinationsizecheck[:1]+')').replace(destinationsizecheck[:2]+' ','').split(' ')[0]
					if int(zipsize) <= int(partition_free_space)*1024*1024:
						try:
							clear_X()
							download_url( defaulturl )
							xbmc.executebuiltin('Skin.SetString(DisableCancel,Disabled)')
							extract_file( file )
							os.remove( file )
							if dlcmode:
								dprogress.update(0)
								dprogress.create("DLC SIGNER","","Initializing" )
								# Had to use this while loop to get the HDD key as it will be Busy for a second or two.
								while True:
									key = xbmc.getInfoLabel('system.hddlockkey')
									time.sleep(1)
									if key != 'Busy':
										hddkey = key.decode('hex')
										filecount = 1
										countlist = 0
										break
								for folder, subfolder, file in os.walk('E:/TDATA/'+titleid):
									filecount += len(file)
								for folder, subfolder, file in os.walk('E:/TDATA/'+titleid):
									for xbxfile in file:
										xbxfile = xbxfile.lower()
										if xbxfile == "contentmeta.xbx":
											contextmetafile = os.path.join( folder, xbxfile )
											filesize = os.path.getsize(contextmetafile)
											readxbx = open(contextmetafile, 'r+b')
											filedata = readxbx.read(filesize)
											# Check the header fields.
											headersize = struct.unpack('I', filedata[24:28])[0]
											titleid = filedata[36:40]
											# Compute the HMAC key using the title id and HDD key.
											hmacKey = hmac.new(hddkey, titleid, hashlibsha1).digest()[0:20]
											# Compute the content signature.
											contentSignature = hmac.new(hmacKey, filedata[20:headersize], hashlibsha1).digest()[0:20]
											readxbx.seek(0,0)
											readxbx.write(contentSignature)
											countlist = countlist + 1
										dprogress.update(( countlist * 100 ) / filecount,"Signing ContextMeta.xbx","This can take some time, please be patient." )
										countlist = countlist + 1
							xbmc.executebuiltin('Skin.SetString(DisableCancel,)')
							if filename == "XBMC-Emustation-update-files.zip" or filename == "XBMC-Emustation-test-build.zip" or filename == "XBMC4Gamers-update-files.zip" or filename == "XBMC4Gamers-test-build.zip" and os.path.isfile( xbmc.translatePath('Special://xbmc/updater/default.xbe') ):
								xbmc.executebuiltin( 'RunXBE( ' + xbmc.translatePath( 'Special://xbmc/updater/default.xbe' ) + ')' )
							elif filename == "Cache Formatter.zip" and os.path.isfile( xbmc.translatePath('Special://xbmc/Cache Formatter/default.xbe') ):
								xbmc.executebuiltin( 'RunXBE( ' + xbmc.translatePath( 'Special://xbmc/Cache Formatter/default.xbe') + ')' )
							elif filename == "URLDownloader.zip" and os.path.isdir( xbmc.translatePath('Special://xbmc/system/scripts/tmp/urldownloader') ):
								xbmc.executebuiltin( 'RunScript( ' + xbmc.translatePath( 'Special://xbmc/system/scripts/autoexec.py') + ')' )
							else:
								dprogress.close()
								dialog.ok("SUCCESS","",filename + " Installed")
						except Exception as err:
							print "Error 2:"; logging.error(traceback.format_exc())
							if allowcancellation == 1:
								dprogress.close()
								dialog.ok("URLDOWNLOADER","You cancelled the download of",filename)
							else:
								dprogress.close()
								dialog.ok("ERROR","","Server or local network issue")
					else:
						dialog.ok("ERROR","","Insufficient space on "+destinationsizecheck)
	else:
		xbmc.executebuiltin('Dialog.Close(1101,true)')
		xbmcgui.Dialog().ok("UPDATE AVAILABLE","Please update the","[B]URLDownloader[/B]")
except urllib2.URLError as err:
	print "Error 3:"; logging.error(traceback.format_exc())
	xbmc.executebuiltin('Dialog.Close(1101,true)')
	xbmcgui.Dialog().ok("ERROR","No network access","Please check your ethernet cable")

# Used to zero the progress bar after everything is done
try:
	dprogress.update(0)
except:
	pass