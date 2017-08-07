You do not need the xml header or the window Id.

In the layout.xml is a simple example of how to setup the layout file.

If you want to disable a specific control, you can do the following:

	Example: <control type="image.">
	( this control is now disabled, alternatively you can just delete the hole control :/ )


You can treat the layout folder as its own texture and theming folder.

What I mean is you can have all the images you use inside this folder and just point the texture or diffuse tags to the following:

	<texture background="true" diffuse="Special://skin/layouts/$INFO[Skin.String(emuname)]/image_diffuse.png">Special://skin/layouts/$INFO[Skin.String(emuname)]/image.png</texture>
	
Screenshots or synopsis for emulators.

	Screenshot image:
		<texture background="true">special://xbmc/_tbns/$INFO[Skin.String(emuname)]/$INFO[Skin.CurrentTheme]/$INFO[Container(9000).listitem.Label].jpg</texture>

	Synopsis image:
		<texture background="true">special://xbmc/_tbns/$INFO[Skin.String(emuname)]/$INFO[Skin.CurrentTheme]/$INFO[Container(9000).listitem.Label].png</texture>
	

Fanart, screenshot or synopsis for xbe files.

	Fanart image:
		<texture background="true" diffuse="background diffuse.png">$INFO[listitem.path,,fanart.jpg]</texture>
	
	Screenshot image:
		<texture background="true">$INFO[listitem.path,,screenshot.jpg]</texture>
	
	Synopsis image:
		<texture background="true">$INFO[listitem.path,,synopsis.png]</texture>
		
	Carbon theme:
	
	Screenshot image:
		<texture background="true">$INFO[listitem.path,,screenshot_carbon.jpg]</texture>
	
	Synopsis image:
		<texture background="true">$INFO[listitem.path,,synopsis_carbon.png]</texture>



Currently there are two layouts in each layout.xml one for the stock theme and one for the carbon theme.
XBE layouts must use different ID for the lists, you can use from 52 to 60 )

