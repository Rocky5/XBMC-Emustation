import hashlib, hmac, os, struct, xbmc, xbmcgui, time
# Had to use this while loop to get the HDD key as it will be Busy for a second or two.
dialog	= xbmcgui.Dialog()
hashlibsha1 = hashlib.sha1
Select_Folder = dialog.browse( 3,"Select folder to hash",'files','' )
contextmetafile = os.path.join( Select_Folder,'contentmeta.xbx' )
filesize = os.path.getsize(contextmetafile)
readxbx = open(contextmetafile, 'r+b')
filedata = readxbx.read(filesize)
while True:
	key = xbmc.getInfoLabel('system.hddlockkey')
	time.sleep(1)
	if key != 'Busy':
		break
hddkey = key.decode('hex')
# Check the header fields.
headersize = struct.unpack('I', filedata[24:28])[0]
titleid = filedata[36:40]
# Compute the HMAC key using the title id and HDD key.
hmacKey = hmac.new(hddkey, titleid, hashlib.sha1).digest()[0:20]
# Compute the content signature.
contentSignature = hmac.new(hmacKey, filedata[20:headersize], hashlibsha1).digest()[0:20]
readxbx.seek(0,0)
readxbx.write(contentSignature)

xbmcgui.Dialog().ok("Hashed","Hashed content.")