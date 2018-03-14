'''
	Script by Rocky5
	Used to enter the current version into the skins string.po file
'''
import fileinput, os, xbmc, xbmcgui
print "| .emustation\Scripts\versioner.py loaded."
try:
	with open( 'Q:\\system\\version.bin','r' ) as version:
		current_version = version.read().rstrip()
	for line in fileinput.input( os.path.join( 'Q:\\default skin\\language\\English\\strings.po' ), inplace=1):
		if line.strip().startswith('msgid "XBMC-Emustation '):
			line = 'msgid "XBMC-Emustation %s"\n' % ( current_version )
		print line,
except:
	pass