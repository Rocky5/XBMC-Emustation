# XBMC-Emustation

### Front end for some emulators, using XBMC

 This is a pet project of mine and its a combination of a skin, python scripts and source edits to XBMC. So don't expect something spectacular.

 I wanted something that looked like EmulationStation on the Xbox and the only way to do that was to make a skin for XBMC and use it's built in feature to launch .cut files.
 
 But it wasn't that simple, I wanted menu loading instant and there was no simple way to do that with over 700 roms or a few hundred games, so I modified the XBMC source to bypass the folder check for xbe files. This worked for games, but not roms, so again had to think outside of the box and came up with a workaround :) I create static menus when you scan your roms. There are also a few other scripts I made to do other tasks, but hopefully you like what I have made and get some use out of it.

## Installation
 * Download [XBMC-Emustation](https://github.com/Rocky5/XBMC-Emustation/archive/master.zip) and extract the **XBMC-Emustation-master** folder to your desktop.
 * Download [XBMC4XBOX-3.5.3.zip](https://drive.google.com/drive/folders/0B9zNhNcNUdDTRVFBbHcwc2JCZFE) and extract the **XBMC** folder to your desktop\\**XBMC-Emustation-master**\\ folder.
 * Now double click the **Build XBMC-Emustation.bat** that's inside the **XBMC-Emustation-master** folder and wait. It will output a new folder named **XBMC-Emustation**
 * FTP this new folder to your Xbox and enjoy.
 
## Roms and Emulators
 * You place your roms in the designated subdirectory in the **_roms** folder.
 * Same exact thing for the emulators, but in the **_emulators** folder.
 
## Scanning Roms
 * Press start on the main screen. Other Settings > Auto Create Cut Files
 
## Updating emulator list
 * Press start on the main screen. Other Settings > Refresh Emulator list.
  ( **note:** If there are no roms present for this emulator it will not show )
  
## Everything else
 * the rest should be self explanatory, its all in the menu.
 
### Acknowledgements:

#### Buzz
 For maintaining XBMC4Xbox over the years.

#### EmulationStation folk for:
 es-theme-simple-master - [GitHub es-theme-simple](https://github.com/RetroPie/es-theme-simple)
 
 es-theme-carbon-master - [GitHub es-theme-carbon](https://github.com/RetroPie/es-theme-carbon)
 
 ( I created a few new images to add to these great svg images )
	
#### MadMab
 For the emulators on the Xbox - [MadMab Emulators](http://www.emuxtras.net/dlsystem/)
 
 [Emuxtras Website](http://www.emuxtras.net)
 
#### Tester
 For feedback and suggestions.