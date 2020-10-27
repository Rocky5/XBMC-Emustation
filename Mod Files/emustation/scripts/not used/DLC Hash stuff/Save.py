import hashlib, hmac, os, struct, xbmc, xbmcgui, time
dialog	= xbmcgui.Dialog()
hashlibsha1 = hashlib.sha1
inputfile = 'E:\\'
filesize = os.path.getsize(inputfile)
readfile = open(inputfile, 'r+b')
filedata = readfile.read(filesize)
offset = 0
filesize = filesize - offset
XBEKey = "5C0733AE0401F7E8BA7993FDCD2F1FE0".decode('hex') ## This is the same for all Xbox ( other than retail - 5C0733AE0401F7E8BA7993FDCD2F1FE0 debug - 66810D3791FD457FBFA976F8A446A494 )
SIGkey = "".decode('hex') ## This is different for every game
# Compute the HMAC key using the title id and HDD key.
hmacKey = hmac.new(XBEKey, SIGkey, hashlib.sha1).digest()[0:20]
# Compute the content signature.
contentSignature = hmac.new(hmacKey, filedata[offset:filesize], hashlibsha1).digest()[0:20]
readfile.seek(0,0)
#readfile.write(contentSignature)
xbmcgui.Dialog().ok("Hashed","Hashed content.",hmac.new(hmacKey, filedata[offset:filesize], hashlibsha1).hexdigest())