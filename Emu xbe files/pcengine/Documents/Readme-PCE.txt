MednafenX-PCE - PCE/TG16 Emulator for XBox v6b02

http://mednafen.com/
http://xport.xbox-scene.com
goto http://www.emuxtras.net/ for latest cheats, rumbles, synopsis and skin updates.

What's New:

Check the Latest-PCE.txt file for the latest update info.  From now on it will have the latest info and this file will contain the changelog/older update information.

-----------------------------------------------------------------------

MednafenX-PCE - PCE/TG16 Emulator for XBox v5

http://mednafen.com/
http://xport.xbox-scene.com
goto http://www.emuxtras.net/ for latest cheats, rumbles, synopsis and skin updates.


First off...

-------------------------
Special thanks....
-------------------------

X-port for porting a great collection of emu's over to the xbox, releasing the source code, and answering my stupid questions.

Atariage (Albert in particular) - For providing a place for me to ramble on. For encouragement in general.

Gilou9999 for a new PM3 skin, synopsis, suggestions, rumble codes, etc.

Comments of support from various interested parties.

If I missed anybody shoot me an email and I'll update this file.


*********************************
* Changes To MednafenX_PCE Core *
*********************************

* Fixed an issue where the screen was not displaying correctly in Mednafen_PCE when in debug mode.

* CD music volume is now saved with each game. That way the user can better balance the sound in games that use CD audio/music.


***************************
* To Do For MednafenX_PCE *
***************************

- Eh?


*****************************
* Interface Related Changes *
*****************************

* Given the full "Madmab Edition" treatment.

* New dual-preview skin to support Ressurection Xtra's.  Say thank you to Gilou9999 for the skin.

* "Auto Game Configurations (aka Configuration defaults)" added (see below description).

* Apparently mp3CDDA and CDDA volume were sharing the volume variable for Mp3music. Created seperate volume variables for each. Mp3CDDA and CDDA volume are saved with each game so you can customize this for CD games.

* New feature "Seconds before playing movie" determines how long the emu will wait before playing a movie.  The default is half a second.  This will help speed up rom browsing.  Especially useful for people streaming stuff (like movies) across the network.

* If streaming movies from across the network and the user press on the dpad or a, b, x or y the emulator will abort the transfer.  This should help speed up rom browsing and allow the user an "out" especially for the larger movies.

* Fixed an issue with the software filters displaying garbage.

* Activated the "Keep user Within ROM Directory Tree?" which I somehow missed.

* Fixed up the box/cart art position on a few skins.

* Fixed a problem where setting the box/cart orientation was screwed up.

* Fixed the bug that screwed up Gilou's skin to begin with (too weird to explain).  :P

* Accurate Screen Pixel Ratio option added (see "http://fancyxbox.info/?doc=1&secao=screen" for more into) per gilou9999's suggestion.  Some numbers are still a WIP.  Go into Game/Text Screen Size Position" and select "Set Game Screen to Accurate Screen Pixel Ratio".  The emu will ask you if you wish to turn off software/hardware filters and flicker filter.  This is recommended for the most accurate screen.  You'll still have to manually adjust the image on the Y axis.  We can't do everything for you, ya lazy bum!

* Added an option to display a "Static" video if no movie found.  Can be set to yes or no.  Static file must be named "Tv Static.xmv" and placed in the emu's "backgrounds" directory.

******************
* Rewind changes *
******************

* Rewind is a bit of a memory hog.  On some emu's at 720p it is barely useful.  Some emu's can't even handle it.  Here is what I did.

* Tweaked around with the rewind system fixed a couple potential xbox lockers.

* Modified the rewind system so if memory runs low it clears half the buffer, if that doesn't work it clears the entire buffer.  What this means is that on memory intensive emu's you'll have a rewind system that mostly works.  It's pretty much a "better than nothing" set-up.

**********************
* End Rewind Changes *
**********************

* Pressing Back while in the the controller settings menu will set the value to "None".

* Hopefully addressed weird issues with "Force Reload D:\\*.ini Settings".

* New option to "Keep user Within ROM Directory Tree".  You can find it in "General Settings, Page Two".  Useful for keeping n00bs from getting lost while selecting games.

* Hoperfully cleaned up all instances where the current "game select" directory would get trashed.

* Transparency control for keypad and keyboard should now function properly.

* Tightened up the Synopsis parsing code (sorry RessX :( )

* Fixed issue where cycling thru screenshots when non-available would create an infinite loop.

* Fixed two bugs that would cause the game select screen to slow down massively.  One related to having Box/Cart art timer set to 0.  The other related to the rather large size of the Xtra's.  You dirty pirate you!  :P


* Fixes to the keyboard/keypad including. These affect emu's that use a keyboard/keypad (Winuaex, AdamX, Atarixlbox)

- Keyboard/keypad no longer corrupts portions of the screen when being moved.

- Keyboard/keypad can be moved diagonally in ALL directions now

- Keyboard/keypad transparency now works properly when "Pause game while using Keyboard/Pad" is set to ON.

- Fixed issue with screen blurring when Keyboard/keypad is activated.  I'm surprised I did not notice this earlier. 


* Created a new overlay system. The file "overlay.ini" contains configuration information for each overlay, including the color of the transparent button.

* Fixed issue with the "Music Control Menu" where the "Go to next/previous song" options were not working.

* Fixed issue where "View playlist" did not show the first two songs.

* Fixed issue where "pause" would still display even after changing songs while viewing the playlist in "clear screen" mode.

* Add song to playlist now functions correctly.

* Added a seperate "Volume Control Menu". It can be accessed by pressing "Y" in the "In Game Options" menu, or from the "Game Configuration" menu. It lets the user set the volume for in game sound, mp3_cdda, cdda, movie and mp3 music player from 0-100.

* Fixed issue where games that had more than 48 CRCs in the cheat code database would cause a crash when game is selected while searching for cheat codes.

* Rumble codes and cheat codes are now stored in seperate files. ( "rumblelist.inf" and "codelist.inf" respectively).  To make it easier to search for "rumble codes" only.  Note to cheat code makers: be sure to make your cheat codes and rumble codes seperately now.  For those importing rumbles, the rumble does not have to be "activated" in order to work, it just works.  Remove it from the list if you no longer wish to use it, or set it to "Rumble Enabled On - Nothing".

* Cheat code menus moved around.  In-Game menu option "Cheat Codes" was moved into "Game Utilities" and replaced with "Cheat Code Database" to make it easier for the gamer to use codes in the database.  Cheat code creators just need to go into "Game Utilities" to get to their stuff.

* Skin can now have a "Startup Movie" on loading menu. Please use with discretion (no long movies).  User can press B to skip the movie.

* "Startup Movie" can be displayed full screen or in a window. If fullscreen is used the loading menu will not be displayed.

* Transparency for "Startup Movie" can be set as well.

* Moved the network initialization code to run before the loading menu. This moves the delay caused by network init to before the display of the loading menu, not after.

* Files when selecting within a zip are sorted.

* Added a seperate timer for alternating Box/Cart art.

* LThumb-Down - Go to next Box/Cart.  LThumb-Up - Go to previous Box/Cart.

* Ability to view synopsis from within game. (press right analog stick down).


* Movies! The ability to display movie previews!

- You can set the movie/previews directory in the "Change Default Directories" section.

- The movie name has to be exactly the same as the ROM name. Only one movie per game. 

- Display order can be set to. None, Screenshots Only, Movies Only, Screenshots 1st- Then Movies, Movies 1st- Then Screenshots.

- Movies display over screenshots so if you want you can see screenshots when no movie exists.

- Can now stream videos and screenshots from Samba or Relax.

- Sound for movies can be turned on/off

- Box/Cart art can be displayed in seperate window.  Box/Cart art is autodetected based on size (only in "old screenshots" directory).

- Transparencies for Box/Cart art (and screenshots) is now supported  Check out some of the 3d Box/Cart art floating around!

- Skin author can now designate two locations where Boxart or Cartart will display based on width vs height.

- Old Screenshots are now sorted and displayed in proper order.

- Old Screenshots can be named anything (as long as it has .png extension)

- In Game Options Screen can be sized and positioned now.


* New option to "Force Game Screen Size/Position". There are two configurable screensizes. (To deal with multi-core systems like MekaX and XboyAdvance). This will be useful when switching from HDTV to SDTV or vice versa. It will save the user the trouble of resizing the screens for something that is likely temporary.

* Numerous changes to menu system see above (current menu configuration layout)

* Skin Sprites can now be named for easier manipulation. Directory names must be of the format "0_spritename", "1_spritename", etc. Do not use underscores for the spritename. It is a delimiter.

* Added "Select Skin Configuration Used" and "Save Skin Configuration as" to the "Configure SKin" menu in place of the above moved options. This allows multiple skin configurations in one skin allowing the user more "pre-defined" options on how a skin looks. For example the placement of the games list and the preview screens. Gilou's Dynamic skins really take advantage of this, check 'em out!

* Sprites now display when sizing the preview screens.

* Changed "Seconds before auto-advancing Screenshot" to "Seconds Before Auto-Advancing Artwork".

* Changed "offset X" and "offset Y" to "Offset X (left/right)" and "Offset Y (up/down)" in the Sprite Settings menu.

* New Option to pause or not pause emulation when keyboard or keypad is up.

----------------------------
Finished the "Media browser"
----------------------------

* Be sure to use the RessurectionXtras or Xtras for maximum enjoyment!  "http://www.emuxtras.net"

* Ability to display documentation (text or graphic) and commercials (xmv format only).

* Assigned buttons (white/black) to go to next/previous files when viewing documentation. See below graphic/text file viewer controls.

* Once the user opens a document - the emulator remembers this document as long as the game session is running.

* View settings for each document viewed are now stored in a "bookmark" file so next time you view a file your settings are restored.  Press Back to "reset" as if reading document for first time.

* "View Text File" changed to "Browse Manuals/Videos"

* Support added for different kinds of documentation in the media browser.  Including "Manuals", "Game FAQs", "Game Maps", "Commercials", and "Other".  The user can also specify where these directories are located.  Defaults are "Manuals", "GameFAQs", "VGMAPS", "Commercials", and "Other".  "Other" is in the media root directory (typically "x:\media\Other") for non emu specific stuff.

* User can specify whether manual is displayed "Full Size" or be "Sized to fit screen" when loaded.  Keep in mind any saved bookmarks override this.  Press Back to toggle between "Full Size" and "Size to fit screen".

* Commercials can be displayed either full screen, at the size of the video with black background, or same size of the video with synopsis background.

* NOTE: Some emulators are tight on memory (eg: NeoGenesis) and not all the Xtra's will load.  If you have trouble with an image loading you might have to resize it.

* In screenshot viewer. If the image is smaller than your text file screensize settings it will work as follows. 

a) If the image is taller than it is wide it will continue expanding the image ( based on aspect ratio) until the width fits within the width of your text file screensize width. (Most normal manuals)

b) If the image is wider than it is tall it will continue expanding the image ( based on aspect ratio) until the height fits within the height of your text file screensize height. (For example NES manuals).

This seems to effectively stretch the image in the best manner possible for scanned manual reading.

* Browsing manuals/videos should auto select any file matching your ROM name exactly.  Select "View Media Directory" for manual browsing.

* Unmapped controls that allow you to move the screen around since word wrap should work correctly now.

* Change Fixed Width font controls are now mapped to the right analog stick (left/right) like the help screen says it should be.  Doh!

* Set font size keeps seperate settings for Fixed Width fonts and proportional fonts since they produce different results.

* Graphic documentation can now be stored in a ZIP file and still work with the media browser functions (next/previous and bookmarks).

* Music no longer starts playing after viewing text file in game.

* Number of lines displayed in the text file viewer now properly match user set text screen size.

* Number of lines displayed updates properly if user modifies text screen size within text file viewer.

* Text file viewer functions turn off FixedWidth before displaying any menu.

* Added a fixed width font for the text file viewer. If you wanna use it you have to make sure that a file named "FixedFont.ttf" is located in the emulator directory. Press "Y" in the text file viewer to switch to the fixed font.

------------------------------------
Controls for text browser

A -> Start Search
B -> Exit
X -> Continue Last Search
Y -> Simulate width font

White -> Previous file
Black -> Next file

Start -> Help screen
Back -> Reset view as if document was loaded for first time.

Dpad -> Up/down, Left-> Up Page, Right-> Down Page
Left Analog button -> Set font size
Left Analog Up -> Top of file
Left Analog Down -> End of file
Right Analog button -> Set text screen size
Right Analog left/right -> decrease/increase fixed-width font size

Left/Right triggers - Move up/down text file.

----------------------------------------------
Controls for screenshot browser

A -> Lock/Unlock Aspect Ratio
B -> Exit
Y -> Delete file (Utilities-> browse screenshots only)

White -> Previous file
Black -> Next file

Start -> Help screen
Back -> Toggle between "Full Size" and "Size to fit screen".

Dpad -> Up/Down/Left/Right -> Move image 1/4th the total size of the image.
Left Analog button -> Music Control Menu
Left Analog up/down -> Move screen up/down.
Right Analog left/right -> decrease/increase screen size.  Size changes proportional to distance the stick is pressed.

------------------------------------------

*********************
* End Media Browser *
*********************

******************************
* Carryovers from Atarixlbox *
******************************

* Ability to pick a file from within a zip file.  That way on computer based emu's multi-disk games can be zipped now. Keep in mind that if you play any game that "saves" to a floppy, that disk has to be a seperate UNZIPPED file.

* Fixed a few interface "quirks" regarding playing game sounds while emu is paused.

* Select save state screen tells you whether your "loading" or "saving", it also now displays whether a save file has a record session ( R ) associated with it.

* When a new save state is created it deletes any recordings. If you press the "back" button while in the save state select screen it will allow you to delete that save state (as well as it's recording).

* Utilities menu display modifed to state "stop or start recording/playback" depending on whether they are turned on or off. It also displays total minutes remaining or played so far.

* Record/Playback turn off when exiting a game. Boy that sure caused some confusion. 

* Switched positioning control of sprites in the skin menu to the left analog stick, that way you don't have to worry about unintentionally lowering the volume.

* Savestate load screen is a little more informational when sent to it from the save/record option. 

* When you save a picture it removes the screenshot save path making it easier to see long names.

* Changed order of some of the entries in the "Music Control Menu". 

* Playlist repeat mode, and View Name setting is saved in INI file. Although song name only shows in the music control menu.

* (cheat codes) When "adding a code" from the "edit code" screen the current code is copied as a template.

* You can activate/deactivate a code from the "cheat code list" menu by pressing start.

* Deleting a cheat code now asks you if you are sure (I got tired of accidently deleting my codes ).

* Fixed up the problem created from using multiple files in a Zip file.

* Fixed problem when a filename inside a zip contains too many characters. While I was at it I fixed the space as the last character when trimming to 42 characters behavior. Zip files where the path was saved now unzip correctly.

* Rewind and Fastforward are de-activated during record/playback and netplay mode. It even tells you so when you try!!

* (Internal) Modified YesNoMenu so it doesn't clear m_menuText.

* Added ability to add in cheat codes from a Gameshark compatible database (see description below). This includes the ability to export the cheat codes in a game to "share" with your friends. Cheat/rumble codes are included for most games. When "adding" codes from the gameshark DB it will move you to the entries with a matching CRC. If not you'll have to manually find the game.

*******************************************************************************
* "Auto Game Configurations (aka Configuration defaults) for select emulators *
*******************************************************************************

In the "General settings" menu there will be a new option.

"Automatically Use Default Game Configuration - Yes/No"

If the user sets it to "Yes" it will bring up the game configuration screen and let the user define the default (if no default.stg and default.key file exists).

In the "Configuration" menu there will be a new option... "Set default game configuration"

The user can go in anytime thru the "Configuration" menu to change these "defaults" to something else if they wish.

Once set to "Automatically use Default Game Configuration" the user will not see the game configuration screen again unless they... a) press X when selecting a game. Change "Use Default Game Configuration" back to "No".

Keep in mind when it is set to "Yes" the game will use your "Default game settings" and not the normal x-port behavior. If set to "No" the emulator will behave like it usually does. Each emu is typically different. But all, at the very least carry the controller settings over.

This feature will only be added to emulators in which it is feasible to use.


-----------------------------------------------------------------------
MednafenX-PCE - PCE/TG16 Emulator for XBox v4

http://mednafen.com/
http://xport.xbox-scene.com
http://necstasy.emunova.net/

What's New:

 - Updated UI core to most recent feature set

 - Added Sherlock 1&2 hack to options menu (untested)


-----------------------------------------------------------------------

MednafenX-PCE - PCE/TG16 Emulator for XBox v3

http://mednafen.com/
http://xport.xbox-scene.com
http://necstasy.emunova.net/

What's New:

****************************
* EMU Core Related Changes *
****************************

 - Fixed autofire in games like Dragon Spirit
   For Dragon Spirit, set autofire to 3.  If mapping both A and B
   to the same XBox button, then set A autofire to 3 and B to 4.
   Dragon Spirit seems to intentionally try to disable autofire and
   having both buttons pressed simultaneously.  If both are pressed
   at the exact same time, only one will function.  This is why
   different autofire values are needed if mapping both emu buttons
   to the same XBox button.

Important Notes
===============

Perfect CUE
-----------

I believe there is some misunderstanding about how the Perfect CUE
system is to be used.  You should *not* select "Use My Selected CUE File."
when it asks you to select the perfect CUE sheet.  Find the game
you're playing in the list and use that selection.  This will ensure
that you will have the most accurate CUE information.  The CUE file
you selected to launch the game will still be read to obtain the filenames.
The track locations, gaps, etc are obtained from the perfect CUE system.

The only reason I left the "Use My Selected CUE File" in the list is
because it's possible that there are discs that have not been cataloged
yet.  That is the only time you should select "Use My Selected CUE File" -
when the game you're looking for is not in the list.  Check the list
carefully, though, because unless you have something extremely rare,
it's going to be in the list somewhere.  

Here's a tip - if you downloaded the game, then it's not rare and it's in 
the list somewhere.


-----------------------------------------------------------------

MednafenX-PCE - PCE/TG16 Emulator for XBox v2

http://mednafen.com/
http://xport.xbox-scene.com
http://necstasy.emunova.net/

What's New:

****************************
* EMU Core Related Changes *
****************************

 - Rewind support enabled
   Two new button definitions: "Turn On/Off Rewind" and "Rewind"
   Map them to whatever buttons you want in controller configuration

   If you're playing in 720p or 1080i mode, the amount of time available
   for rewinding is decreased due to memory constraints.  (720p and 1080i
   require much more memory than 480i/p)

   Furthermore, enabling rewind in CD games will result in extremely poor
   performance due to the fact that saving a state in CD games take a lot
   more memory (and therefore more processing time) than in HuCard games.  
   That's just the way it goes.  At least it's full speed in HuCard games.

 - Implemented 6-button pad 

   Toggle it on the game configuration menu.

   You'll also need to configure the buttons under Controller Configuration
   before they'll be usable.  You can do this once on the main menu
   and the configuration can be copied to all your existing save games.

   List of games that use 6-button pad: (incomplete I'm sure)

   Advanced V.G.
   Fire Pro Wrestling Female
   Mahjong Sword Princess Quest Gaiden
   Strip Fighter II
   Battlefield '94 In Super Battle Dream
   Garou Densetsu Special
   Street Fighter II - Champion Edition
   Super Real Mahjong P V Custom
   World Heroes 2
   Kakutou Haou Densetsu Algunos
   Garou Densetsu 2
   Linda Cube
   Super Real Mahjong P II & III Custom
   Ryuuko No Ken
   Flash Hiders

 - PCE mouse support

   Toggle it from game configuration.

   Use the Left Analog stick or a real USB mouse to control it.

   Brandish, Lemmings, A.III, and possibly some others can make use of it.
   Artist Tool does not - it uses a different peripheral.

 - Error messages when loading games should provide meaningful feedback
   as to why it has failed.

 - Audio tracks read from WAV, OGG, or inside BIN files had some distortion
   and were making the gameplay choppy in certain parts.  This is now fixed.

 - Games that play a specific range of audio sectors from inside an audio
   track were not starting/stopping at the correct locations when played
   from an MP3 file.  This is fixed, but it will only work correctly if
   your MP3 files are *not* VBR.  They should be constant bitrate.

 - OGG/WAV/PCM files cannot be read across a network or from ISO9660 files
   (i.e. your S:\, RLX:\ or SMB:\ drives).  An error message will tell
   you this now instead of the program crashing.

*****************************
* Interface Related Changes *
*****************************

 - Should no longer crash in 1080i mode (memory limitation issue)

 - Made main menu have 8 lines

   Go to Configuration -> Video/Skin Configuration -> Select Skin 
   and reselect the default skin.

   Or, go to Configuration -> Video/Skin Configuration -> Configure Skin ->
   Main Menu Settings -> Text Settings and set 
   Number of Lines Per Page = 8
   Line Height = 19

 - Possible fix to garbled screen upon starting

 - Filename Filter
   Go to Configuration -> General Settings -> Page 2 -> Edit Filename Filter
   The extensions you enter will be the only ones that appear in your
   game listings.  

 - Improved support for ZIP files that have more than one file in them.

 - Updated text file viewer :
   Press LTHUMB to change the font height
   Press RTHUMB to bring up the screen-resize menu
   Move LTHUMB left/right, RTHUMB left/right to move the text left/right
   and extend the viewing area
   Move LTHUMB up/down to scroll text up/down

 - Move DPAD left/right on save state slot to inc/dec slot number

Enjoy!


-----------------------------------------------------------------

MednafenX-PCE - PCE/TG16 Emulator for XBox v1

http://mednafen.com/
http://xport.xbox-scene.com
http://necstasy.emunova.net/

Thanks to J-Red for an excellent skin! 

Features :

 - Emulates PC-Engine/TurboGrafx-16/SuperGrafx/Arcade Card CD/CD/SCD

 - Excellent, stupendous, fanshmabulous compatibility - ported from Mednafen

Default ROM dir is D:\PCEROMS

===============
Important Notes
===============

If you like PCE, you're going to love this one.  Out of the 100+ CDs I tried
and the dozens of HUCard images, it played them all perfectly with just a 
handful of ones with minor issues.

------------------
Perfect CUE System
------------------

Thanks to the great people at http://necstasy.emunova.net/, you should no
longer have to worry if your CUE sheet has the right indices, gaps, layout, etc.

The PCE TOC database is a compilation of verified TOCs from just about every
single PCE CD game in existence.  I have incorporated all of that data into
MednafenX-PCE.  The only thing you need to be concerned with is making sure
your CUE sheet points to the correct ISO/MP3 files for each track.  You
can still use CDDissect to rip your PCE games:

http://xport.xbox-scene.com/cddissect.php

As long as you have all the ISO/MP3 files and your CUE sheet points to them
correctly, you'll be all set.

Please note the following examples of CUE sheet "FILE" lines:

This is good:

FILE "dynastic_hero02.iso" BINARY


This is bad:

FILE "c:\pcecds\dynastic hero\dynastic_hero02.iso" BINARY

You should not have any paths in your FILE lines.  It should simply be the 
filename.  

--------
CD Games
--------

To play a CD game, select the CUE sheet.  You will then be prompted to select
the name of the game so that MednafenX-PCE can load the correct TOC information.
If you are looking for a specific name but cannot find it, then load up 
pcetoc_names.txt in notepad or some other text viewer and search for the name of
the game.  (Or some portion of the name.)  

The game you are trying to play *does* have an entry in the list.  You just have to
find it.

----------------
US Encoded Games
----------------

Almost all games will load without issue, but if you just get a black screen 
then go to the game configuration menu for that game and toggle the "Force US"
option.  That will probably fix the problem.  If not, you most likely have a bad
dump.

*****************************
* Interface Related Changes *
*****************************

 - ZIP support

 - Launch original PCEngine CDs from your XBox DVDROM drive

 - Loads of hardware/software filters and video options to tweak

 - Cheat system - Search/Create your own cheat codes (see notes)
 
 - Favorites list

 - Save states

 - Fast forward/throttle 

 - Resizable game screen

 - Text file viewer

 - ISO9660, Relax, Samba support

 - Take in-game screenshots and display them on the game selection list

 - Record/Playback feature - record your gameplay in the emu and then
   play it back again.  Record up to 10 minutes of gameplay.

 - Every single in-game command is fully customizable on any of the
   four joypad controllers.

 - Map any emulator or UI command to a single button or a combination of
   two buttons.  (e.g. RTrigger+LTrigger = Save State)

 - Autofire capabilities for any emulator button on any controller

 - One-button combos (define a series of emulator commands to be played
   back when you press a user-definable XBox controller combination.)
   (E.g. Press RTrigger+LTrigger to execute the command string
   A,B,A,B,Up,Down,Left,Right)

 - Traverse any directory on any drive ( Continue selecting the parent
   directory entry on the file selection list to get the drive selection
   list.  Selectable drives are C, D, E, F, R, X, Y, Z, RLX, and SMB. 
   R is the CDROM drive.  SMB is your samba share, RLX is your relax share.
   Press Y from any file-listing screen to go up one directory level.

 - All UI commands (save state, load state, screenshot, etc) can be
   invoked from the Options/Pause menu as well as in-game via your
   customized joypad mappings.

 - All the other standard features found in XPort ports.


=============
Configuration
=============

Everything can be changed from the configuration menu.  

If you have never used one of my ports before, I highly suggest you go 
through all of the various configuration screens (particularly 
"General Settings") to see what you can do.

Even if you are already familiar with the standard XPort interface,
I suggest you at least take another look at "General Settings" because
there may be options you have not seen before.


===============
Menu Navigation
===============

Select menu options with the DPAD or with R/LTrigger.  The speed of 
R/LTrigger movements can be controlled by :

Configuration -> General Settings -> Page 2 -> Menu Scroll Speed

There are some places where you can enter or change values.  This 
can usually be done in a variety of ways include DPAD Left/Right, 
R/L Trigger, and L/R Thumb.  Try all of them if the values are changing
too slowly.

"A" selects the highlighted choice.  "B" cancels/returns.
"Y" from a file-select list will go up one directory.
"X" to select a game brings up the game configuration screen
"WHITE" to select a game adds it to your favorites.
"BLACK" to select a game (on your favorites list) deletes it from the list.

================
Text File Viewer
================

DPAD Up     - Up one line
DPAD Down   - Down one line
DPad Left   - Up one page
DPAD Right  - Down one page
R Trigger   - Scroll down
L Trigger   - Scroll up
A           - Start search
X           - Continue last search
White       - Top of file
Black       - End of file
Y           - Simulate fixed-width font
Back        - Decrease width of simulated fixed-width font
Start       - Increase width of simulated fixed-width font
B           - Exit


=====
SKINS
=====

Instructions for making a new skin:

 - Create a new directory off of your SKINS directory (default skins directory
   is D:\EMUSKINS
 - Place your sound/font/graphic media files in this new directory 
 - Load MednafenX-PCE
 - "Select Skin" from the main menu and select your new directory.
 - Select Configuration
 - select Configure Skin
 - Use the menus to select your new media files and change your settings
 - When you are satisfied with what you have, go back to the main menu.
 - Select "Configuration"
 - Select "Overwrite D:\*.ini and D:\emuskins\\<skin>\\settings.ini"
   This will write the skin settings in your skin directory (if your skin
   directory is on the hard drive.)
 - You're done!  You can package up the directory and share it with your friends.

If you wish to use sprites in your new skin, then read the following:

 - Create a subdirectory off of your new skin directory called SPRITES
   e.g. D:\EMUSKINS\NEWSKIN\SPRITES
 - In this new SPRITES directory create a 0-based numeric directory for
   each sprite you wish to make.  This means that if you have 4 sprites
   you wish to load, the directory names *must* be called 0, 1, 2, and 3.

   Do not call them 1, 2, 3, and 4.  
   Do not call them 0, 3, 5, 6.  
   Do not call them SPRITE1, SPRITE2, SPRITE3, SPRITE4.  

 - Inside each of these new directories, you must place the sprite frames.
   Each frame is represented by a BMP, PNG, or JPG file.  The order of the
   frames is given by the filenames.  These filenames must also be named
   with 0-based numbers.  For example, 0.png, 1.png, 2.png.  Look at the
   sprites directory of the included default skin to see how it works.

 - Do not skip numbers when naming sprite directories or sprite frame 
   filenames.  A list of directories called 0,1,2,5,7 is *INVALID*.
   Similarly, a list of files called 0.png, 1.png, 4.png, 5.png is also
   *INVALID*.

Also be aware of memory constraints.  Let's say you have a frame of a sprite
called 0.png.  This picture file is 90 pixels wide and 130 pixels high.
This will get rounded up to a 256x256 pixel 32bit picture.  This means
that it will consume 256x256x4 bytes (256KB) of memory.  If your sprite has
10 frames of animation, that's around 2.5MB of memory.  Keep this in mind
before you make ultra-smooth moving sprites with hundreds of frames of
animation.

You can check your available memory by going to Configuration -> Configure Skin
-> Show Available Memory


====================
Controller Remapping
====================

Configuration -> Configure Controllers

There are 32 general/all-purpose emulator "buttons" or actions.  Each of these
buttons can be assigned a specific emulator action.  For example, Emu Button 1
can be A, or B, or DPad Down, etc.  These "emu buttons" can then be assigned 
XBox triggers.  For example, Emu Button 1 (which you have mapped to, for 
example, A) can be triggered by  XBox controller button B.  The default button 
mappings should provide enough information on how the system works and 
how it can be used.  

==========
Autofiring
==========

Configuration -> Configure Controllers -> Controller # -> Change Autofire

Each "Emu Button" can be set up for autofiring.  Simply set the autofire
variable to a non-zero value.  This value indicates how long the emulator
should wait before releasing and re-pressing the button.  A value of 1
might be too fast to register on some games.  I suggest setting it to a
number like 5 first and then fine-tuning it.


======
Combos
======

Setting up a combo can be kind of tricky because you need to know exactly
what the game expects to have happen on the joypads to execute the special
move.  For example, let's say that we want to map a standard move that is
described like this : 

D, DR, R, A

D = Down, DR = Down+Right, R = Right, A = A button

First, set the delay to a number like 2 or 3.  Then set up the moves.  In
this case, any (or none) of the following might work:

Down
Down+Right
Right
Right+A
Right

OR

Down
Down+Right
Right+A

OR

Down
Down+Right
Right
Right+A
Right+A
Right+A

You will probably need to fine-tune each combo move before it works, but
you'll soon get the hang of it.


==================================================
Cheating System - How To Make Your Own Cheat Codes
==================================================

Just about every single port I've released has this feature, and I 
occasionally hear people asking "how does it work?" This is easiest to 
explain by example:

 1) Start playing a game. 

 2) Go to Options Menu and select "Start Search for Cheat Code"

 3) Go back to game and lose a life

 4) Go to Options Menu and select "Continue Search For Cheat Code"

 5) Select "Search For Values Less Than Before" because when you
    first selected "Start Search For Cheat Codes" you had one more
    life than you do now.  You will see the number of matches go down.

 6) If the number of matches is greater than 10, then perform actions
    3, 4 and 5 continually until the number of matches is less than 10.
    If you run out of lives, then just start playing the game again.
    (Do not exit the emulator and select the game again - just start another
    game from within the emulator.)  Now you will have a full stock of lives,
    which is *more* than the last time you checked your values.  So when you
    continue searching, you'll want to select "Search For Values Greater Than
    Before."  Then go through steps 3-5 over and over until you have less than
    10 matches.

 7) Now that you have less than 10 matches, you can add the codes to your
    list.  If the search narrowed the list down to 1 possible match, it
    will automatically add it to your list.  Now you can "List Cheat Codes"
    and selectively turn on/off the cheat codes to try them out and see
    which on is the right one.

Alternately, you can use the "Search For An Exact Value" option if you
already know the number you wish to change.  Example:

Let's say you are playing Dragon Warrior and your character currently has
25 Hit Points.  Follow these instructions:

 1) Go to Options Menu and select "Start Search for Cheat Code"

 2) Select "Continue Search For Cheat Code"

 3) Select "Search For an Exact Value" and enter 25 as the number.
    The number of matches should decrease very quickly.  

 4) Go back to the game and do something to change your Hit Points amount.
    For example, let's say you drink a potion and your Hit Points are now 35.

 5) Go to options menu and select "Continue Search For Cheat Code"

 6) Select "Search For an Exact Value" and enter 35 as the number.
    Chances are very good that the number of matches will be down to 
    one or two.  Just try out the codes to see which one gives you infinite 
    Hit Points!

Advanced Cheat Code Usage:

Cheat codes have the following format:

TT AAAAAA VVVV

TT     = Type
AAAAAA = Address
VVVV   = Value

You can hand-edit the cheat codes you've created.  Go to the Cheat Code list,
select a code, and select Edit.  Let's say you've already created a cheat code
that keeps your hit points at 25.  The last four hex digits of your code will be
0019 (which is hexidecimal for 25.)  You can change the last two digits to, for 
example, FF which will give you 255 hit points instead of 25.  More sophisticated
codes can be made by altering the Type:

Type Table

80 - Means set the 16-bit value (0-65535) pointed to by the cheat code address 
     to the cheat code value.

30 - Means set the 8-bit value (0-255) pointed to by the cheat code address 
     to the cheat code value.

10 - Means increase the 16-bit value pointed to by the cheat code address
     by the cheat code value.

11 - Means decrease the 16-bit value pointed to by the cheat code address
     by the cheat code value.

20 - Means increase the 8-bit value pointed to by the cheat code address
     by the cheat code value.

21 - Means decrease the 8-bit value pointed to by the cheat code address
     by the cheat code value.

D0 - Means only execute the next code in the list if the 16-bit value pointed
     to by the cheat code address is equal to the cheat code value

D1 - Means only execute the next code in the list if the 16-bit value pointed
     to by the cheat code address is not equal to the cheat code value

D2 - Means only execute the next code in the list if the 16-bit value pointed
     to by the cheat code address is less than the cheat code value

D3 - Means only execute the next code in the list if the 16-bit value pointed
     to by the cheat code address is greater than the cheat code value

E0 - Means only execute the next code in the list if the 8-bit value pointed
     to by the cheat code address is equal to the cheat code value

E1 - Means only execute the next code in the list if the 8-bit value pointed
     to by the cheat code address is not equal to the cheat code value

E2 - Means only execute the next code in the list if the 8-bit value pointed
     to by the cheat code address is less than the cheat code value

E3 - Means only execute the next code in the list if the 8-bit value pointed
     to by the cheat code address is greater than the cheat code value

If you are familiar with cheat codes, you'll notice that these are standard
Gameshark types.  With enough experience you could make some seriously
interesting codes with this system.  

For example, I played around with Super Mario Bros (NES) and found out that
address 0007EE stores the number of coins and address 0007FA is the
one's digit in the timer.  Here are two codes:

E0 0007FA 03
20 0007EE 01

Those codes mean that while the ones timer digit is equal to three, increase the 
number of coins by one.  You won't see the coins updated on the overhead
display in the game, but if you start a game, wait until the timer one's
digit is a three and then collect a coin, you'll see that your coin value
is actually much higher than one, now.  Fun useless stuff.  :P


==================================================
Command-Line/Auto-Launching and Return to Launcher
==================================================

This section is for the developers of frontends, dashboards, etc.

MednafenX-PCE can be started with parameters to automatically launch a game
at startup.  Example code can be found in the custom_launch_params.cpp file.

There is also example code in that same file that will show you how to 
make MednafenX-PCE load your frontend/dashboard when it exits.


Stella, Gnuboy, SMSPlus, FCEUltra, HUGO, NeoPop, DGen, Bochs, HUGO-CD,
FMSXBox, Bliss, WinSTon, Gens, Z26X, StepmaniaX, PCSXBox, XBoyAdvance,
DOSXBox, AtariXLBox, MirrorMagicX, KoboX, MaelstromX, MarblesX, Vice64X,
Vice20X, VicePETX, KegsX, XPired, AdamX, WonderSwanX, BeatsOfRageX,
PowermangaX, LynxBox, BlueMSXBox, GladiatorX, AmphetamineX, StarfighterX,
PachiX, BlobWarsX, OdysseyX, ArnoldX, X68000X, WinUAEX, MekaX,
MednafenX-NES, MednafenX-PCE, MednafenX-Lynx
what's next?

Enjoy!
