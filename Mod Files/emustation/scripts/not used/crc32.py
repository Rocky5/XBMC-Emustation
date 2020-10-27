import os, zlib, sys, xbmc, xbmcgui
dialog = xbmcgui.Dialog()
dialogprogress = xbmcgui.DialogProgress()
filesize = os.path.getsize( "E:\\testfile.zip" )
prev = 0
percent = 0
dialogprogress.create("CHECKING FILE INTEGRITY","","Initializing")
for eachLine in open( str("E:\\testfile.zip"), "rb"):
	dialogprogress.update( (100*percent)/filesize,"Calculating CRC32","This can take some time, please be patient." )
	prev = zlib.crc32(eachLine, prev)
	crc = "%08X"%(prev & 0xFFFFFFFF)
	percent = percent - (filesize/1)
dialogprogress.close()
xbmcgui.Dialog().ok("CRC32",crc)
