'''
	Script by Rocky5
	Run different loaders if a button is held down

KEY_BUTTON_A		=	256
KEY_BUTTON_B		=	257
KEY_BUTTON_X		=	258
KEY_BUTTON_Y		=	259
KEY_BUTTON_BLACK	=	260
KEY_BUTTON_WHITE	=	261

'''

import os, sys, time, xbmc, xbmcgui

if xbmc.getCondVisibility( 'Skin.String(Custom_XBELoader_1)' ):
	Custom_XBELoader_1 = xbmc.getInfoLabel( 'Skin.String(Custom_XBELoader_1)' )
else:
	Custom_XBELoader_1 = 0

if xbmc.getCondVisibility( 'Skin.String(Custom_XBELoader_2)' ):
	Custom_XBELoader_2 = xbmc.getInfoLabel( 'Skin.String(Custom_XBELoader_2)' )
else:
	Custom_XBELoader_2 = 0

if xbmc.getCondVisibility( 'Skin.String(Custom_XBELoader_3)' ):
	Custom_XBELoader_3 = xbmc.getInfoLabel( 'Skin.String(Custom_XBELoader_3)' )
else:
	Custom_XBELoader_3 = 0

if xbmc.getCondVisibility( 'Skin.String(Custom_XBELoader_4)' ):
	Custom_XBELoader_4 = xbmc.getInfoLabel( 'Skin.String(Custom_XBELoader_4)' )
else:
	Custom_XBELoader_4 = 0

if xbmc.getCondVisibility( 'Skin.String(Custom_XBELoader_5)' ):
	Custom_XBELoader_5 = xbmc.getInfoLabel( 'Skin.String(Custom_XBELoader_5)' )
else:
	Custom_XBELoader_5 = 0

if xbmc.getCondVisibility( 'Skin.String(Custom_XBELoader_6)' ):
	Custom_XBELoader_6 = xbmc.getInfoLabel( 'Skin.String(Custom_XBELoader_6)' )
else:
	Custom_XBELoader_6 = 0

print Custom_XBELoader_1

class KeyboardListener(WindowDialog):

	def __init__(self):
		self.key = None
		WindowDialog.doModal(self)
		self.urlChaines = urlChaines

	def onAction(self, action):
		## A Button
		if action.getButtonCode() == 256:
			if not Custom_XBELoader_1 == 0:
				xbmc.executebuiltin('RunXBE('+ Custom_XBELoader_1 +')')
			
			
			
			
			
			
			
			