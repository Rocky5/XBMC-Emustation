'''
	Script by Rocky5
	Used to select a random menu item.
'''
import random, xbmc
MenuLabel		= xbmc.getInfoLabel('Skin.String(emuname)')
XBE_Files		= "0"
if MenuLabel == "apps" or MenuLabel == "xbox" or MenuLabel == "homebrew" or MenuLabel == "ports": XBE_Files = "1"
if XBE_Files == "0": ID			= "9000"
if XBE_Files == "1": ID			= "50"	
Get_Rom_Count	= int(xbmc.getInfoLabel('Container(' + ID + ').NumItems'))
xbmc.executebuiltin('SetFocus('+ID+ ','+str(random.randrange(0,Get_Rom_Count,1))+')')
