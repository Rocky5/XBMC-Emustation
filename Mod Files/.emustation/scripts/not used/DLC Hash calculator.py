import hashlib, hmac, os, struct, xbmc, xbmcgui, time
# Had to use this while loop to get the HDD key as it will be Busy for a second or two.
while True:
	key = xbmc.getInfoLabel('system.hddlockkey')
	time.sleep(1)
	if key != 'Busy':
		break
hddkey = key.decode('hex')
for folder, subfolder, file in os.walk('E:\\TDATA\\'+titleid):
	for filename in file:
		if filename == "contentmeta.xbx":
			contextmetafile = os.path.join( folder, filename )
filesize = os.path.getsize(contextmetafile)
readxbx = open(contextmetafile, 'r+b')
filedata = readxbx.read(filesize)
# Check the header fields.
headersize = struct.unpack('I', filedata[24:28])[0]
titleid = filedata[36:40]
# Compute the HMAC key using the title id and HDD key.
hmacKey = hmac.new(hddkey, titleid, hashlib.sha1).digest()[0:20]
# Compute the content signature.
contentSignature = hmac.new(hmacKey, filedata[20:headersize], hashlib.sha1).digest()[0:20]
contentSignaturealt = hmac.new(hmacKey, filedata[20:headersize], hashlib.sha1).hexdigest()
readxbx.seek(0, 0)
readxbx.write(contentSignature)
xbmcgui.Dialog().ok("",contentSignature,contentSignaturealt)