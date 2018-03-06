import hashlib, hmac, os, xbmc, xbmcgui
# xboxkey = "5C0733AE0401F7E8BA7993FDCD2F1FE0".decode('hex')

hddkey = '00000000000000000000000000000000'.decode('hex')

#titleid = '4100534D'.decode('hex')
titleid = '4D530041'.decode('hex')

with open('E:\\contentmeta.xbx', 'rb') as file:
	file.seek(0)
	data = file.read(136)
	#data = file.read(108)
	file.seek(36)
	#titleid = file.read(4)
with open('E:\\contentmeta1.xbx', 'wb') as file:
	file.write(data)

hashkey = hmac.new(hddkey,titleid,hashlib.sha1).hexdigest()

xbmcgui.Dialog().ok("",hashkey,hmac.new(hashkey,data+hashkey,hashlib.sha1).hexdigest())