You do not need the xml header or the window Id.

In the layout.xml is a simple example of how to setup the layout file.

If you want to disable a specific control, you can do the following:

	Example: <control type="image.">
	( this control is now disabled, alternatively you can just delete the hole control :/ )


You can treat the layout folder as its own texture and theming folder.

What I mean is you can have all the images you use inside this folder and just point the texture or diffuse tags to the following:

	<texture background="true" diffuse="Special://skin/layouts/your emulators name/image_diffuse.png">Special://skin/layouts/your emulators name/image.png</texture>

