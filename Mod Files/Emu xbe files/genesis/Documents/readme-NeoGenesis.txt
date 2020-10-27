NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v25.14b Madmab Ed (Hybrid)

* Updated to madmab edition interface CFv1b21. See "Interface Changelog.txt"

* Due to an improperly sized array the flicker filter level was resetting to 0 on game load.  Fixed.

* Sound from the genesis plus GX sound engine was being done improperly (incorrect variable types) and was causing weird issues on surround systems.  Fixed.

---------------------------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v25.13b Madmab Ed (Hybrid)

* Updated to madmab edition interface CFv1b18. See "Interface Changelog.txt"

* Added 6 new software filters from GensX and 2 from NeoGeo CD emulator (see interface changelog for more details).

* Based on user feedback removed the following software filters 2xSai Scanline, 4xSai Scanline, Super 2xSai Scanline, Super 4xSai Scanline, Eagle 2x Scanline, Eagle 4x Scanline, Super Eagle2x Scanline, Super Eagle4x Scanline.

* Fixed issue where FPS stop displaying after playing your first game.

---------------------------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v25.12b Madmab Ed (Hybrid)

* Updated to madmab edition interface CFv1b17. See "Interface Changelog.txt"

---------------------------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v25.11b Madmab Ed (Hybrid)

* Updated to madmab edition interface CFv1b16. See "Interface Changelog.txt"

* You can now disable the "Launch Inserted CD" option menu in the "Dummy/Lockdown Mode Settings" menu.

---------------------------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v25.10b Madmab Ed (Hybrid)

Updated to madmab edition interface CFv1b14. See "Interface Changelog.txt"

* Attempt to convert gensx_mk.xbe to use the new sound core.  Untested.


---------------------------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v25.09b Madmab Ed (Hybrid)

Updated to madmab edition interface CFv1b12. See "Interface Changelog.txt"

* Fixed issue where playing CD games across a samba share was not working when the "Root Samba Share Name" contains a value.


---------------------------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v25.08b Madmab Ed (Hybrid)

Updated to madmab edition interface CFv1b09. See "Interface Changelog.txt"

* UMKT loading got foobared somewhere along the way (TitleID issues).  Fixed

* Modified to also be able to run UMKT+Tracks ROM image.  However this uses an extra 3 meg of RAM.  Shouldn't be a problem since a seperate, older, core is launched to support this.

* What happened to v25.07b?  Don't ask... :P

---------------------------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v25.06b Madmab Ed (Hybrid)

Updated to madmab edition interface CFv1b08. See "Interface Changelog.txt"

-----------
Bug Reports
-----------

- Pal games cause screen to be blurry?

- CDDA doesn't loop properly (Sonic CD goes to next song instead of looping)?

-----------------------
Changes to the emu core
-----------------------

* Sound options "DAC Improvement" and "PSG Boost Noise" moved to seperate menu "Sound Configuration".

* Corrected handling of "Redump" Sega CD images.  Sonic CD now works and so should the rest.  Still need to do some more extensive testing.

* Added support for Sega-Mega CD Darkwater Images.

* Fixed some issues with 4-player adapter code.  This has only been tested on port 1 and with the following games.  Gauntlet IV, The Lost Vikings, and NBA Live '95.

* Streaming CD across Samba and Relax now working.  There were a couple bugs related to the new Samba code so it's highly likely this feature worked in my last official release as well as x-port's release.  However on those the load times for a Samba share could be up to 3-4 minutes which is rather ridiculous.

* Streaming over Relax seems better to me.  However both can be a little slow on videos at time, especially Samba shares.

* I managed to improve the startup time for Sega CD over a network to between 20 (best case) to 60 seconds (worst case, some soccer game with 98 tracks) without a cue sheet.

* Sega CD loads over a network share about 4-10 times faster if you use a cuesheet.  So get your hands on the "Sega CUE Maker" and generate yourself some cue files!

* Modified cue sheet reader and iso loading code to be able to handle "Sega CUE Maker" generated "cue" files.

* Preliminary support for "Redump" Sega CD images.  My testing has been limited.  One thing I know for sure is that the "Sonic CD" Redump image does NOT work properly.

***************************************************
Neogenesis now uses the sound core from GensPlusGX.
***************************************************

Yet another feature done for Mega Man (?).  However this is an older version of the GensPlusGX sound core (2011)

This means much better sound/music in alot of games that the GensX sound engine had trouble with.

The biggest fix from the new sound engine is this "implemented Detune overflow (Ariel, Comix Zone, Shaq Fu, Spiderman & many other games using GEMS sound engine)". Plus I suspect some work done in regards to the LFO table may help as well.

The Genesis Plus YM2612 engine was based off of the MAME sound engine and then they went and fixed a bunch of issues with it. Mostly internal tables and other boring junk like that (verified on a real YM chip). So here is a list of the more interesting changes. Please note that since it is a different sound engine I have no idea if any of these affected GensX. The one we DO know about is the "games using GEMS sound engine". So that is a start. Here is a list of "possible" things fixed. If someone feels like verifying.

* .modified LFO behavior when switched off (AM/PM current level is held) and on (LFO step is reseted): fixes intro in Spider-Man & Venom : Separation Anxiety

* .improved LFO timing accuracy: now updated AFTER sample output, like EG/PG updates, and without any precision loss anymore.

* - implemented EG output immediate changes on register writes

* - implemented accurate CSM mode emulation

The big catch is.. interpolation is no longer (at this point). If that even matters (beats me I don't have golden ears).  This is what Neogenesis turned on when the user set "YM2612 Improvement" to yes.

So far Ariel, Shaq Fu, Blood Shot (Battle Frenzy), David Crane's Amazing Tennis, Evander Holyfield's Real Deal Boxing, F1 World Championship Edition (main menu), Greatest Heavyweights of the Ring, and Spider-Man (The Animated Series) are the most obvious examples. If anyone figures out where in Comix Zone the issue is, let me know.

Here is a link with a list of games that use the GEMS sound engine http://gdri.smspower.org/wiki/index.php/Mega_Drive/Genesis_Sound_Engine_List

***************************************************

* One downside to the sound core upgrade.  Old savestates no longer work and the new savestates wont work in any other emu that I know of.  Yes folks this emu is now officially a madmab hybrid!  :lol:

------------------------
Changes to the interface
------------------------

* Updated to the latest madmab edition interface


---------------------------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v25.06b Madmab Ed (Hybrid)

http://xport.xbox-scene.com

What's New:

Check the Latest-NeoGenesis.txt file for the latest update info.  From now on it will have the latest info and this file will contain the changelog/older update information.

-----------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v25

http://xport.xbox-scene.com
goto http://www.emuxtras.net/ for latest cheats, rumbles, synopsis and skin updates.

What's New:

First off...

-------------------------
Special thanks....
-------------------------

X-port for porting a great collection of emu's over to the xbox, releasing the source code, and answering my stupid questions.

Atariage (Albert in particular) - For providing a place for me to ramble on. For encouragement in general.

Gilou9999 for a new PM3 skin, synopsis, suggestions, rumble codes, etc.

Megaman for doing the cheat codes.  Bomb Bloke for creating useful scripts.

Bigby, Du0ph0ne, TheMaster3, Nytmar3 for some beta testing.

Comments of support from various interested parties.

If I missed anybody shoot me an email and I'll update this file.


******************************
* Changes To NeoGenesis Core *
******************************

* Sound no longer stops when saving/loading a save state.

* Memory issues should be no more (mostly).  The UMKT hack was using a nice chunk of memory so now whenever you try to load the rom the emu kicks off a seperate XBE to run it.

* Emu shouldn't hang anymore when perusing the cheat database over and over.  (Whoooops).


*****************************
* Interface Related Changes *
*****************************

* Keep user within ROM directory tree works now.  Honest!


************************
* To Do For NeoGenesis *
************************

* Skin probably needs a few fix-ups.  But they can be found seperately at our website as they become available.

-----------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v24

http://xport.xbox-scene.com
goto http://www.emuxtras.net/ for latest cheats, rumbles, synopsis and skin updates.

What's New:

First off...

------------------
Special thanks....
------------------

X-port for porting a great collection of emu's over to the xbox, releasing the source code, and answering my stupid questions.

Atariage (Albert in particular) - For providing a place for me to ramble on. For encouragement in general.

Gilou9999 for a new PM3 skin, synopsis, suggestions, rumble codes, etc.

Megaman for doing the cheat codes.  Bomb Bloke for creating useful scripts.

Bigby, Du0ph0ne, TheMaster3, Nytmar3 for some beta testing.

Comments of support from various interested parties.

If I missed anybody shoot me an email and I'll update this file.


******************************
* Changes To NeoGenesis Core *
******************************

* Four skins to choose from ( Genesis, Megadrive, 32x, Sega CD)

* "Auto Game Configurations (aka Configuration defaults)" added (see below description).

* Implemented the UMKT patch that someone did a while back.

* Apparently mp3CDDA and CDDA volume were sharing the volume variable for Mp3music. Created seperate volume variables for each. Mp3CDDA and CDDA volume are saved with each game so you can customize this for CD games.

* CD music volume is now saved with each game. That way the user can better balance the sound in games that use CD audio/music.

* Fixed rewind so it no longer locks up when used by implementing my "rewind frameskip" code from atarixlbox.  Bad news is you'll only get rewind in Genesis/Megadrive games.  32x and Sega CD games just use too many resources to make rewind practical.


************************
* To Do For NeoGenesis *
************************

- Eh?


*****************************
* Interface Related Changes *
*****************************

* Given the full "Madmab Edition" treatment.

* New dual-preview skin to support Ressurection Xtra's.  Say thank you to Gilou9999 for the skin.

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

-  NeoGenesis in CD or 32x mode cannot deal with it.  Frameskip had to be activated for it to even work in Genesis mode.

**********************
* End Rewind Changes *
**********************

* Pressing Back while in the the controller settings menu will set the value to "None".

* Hopefully addressed weird issues with "Force Reload D:\\*.ini Settings".

* New option to "Keep user Within ROM Directory Tree".  You can find it in "General Settings, Page Two".  Useful for keeping n00bs from getting lost while selecting games.

* Hopefully cleaned up all instances where the current "game select" directory would get trashed.

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

- Box/Cart art can be displayed in seperate window.

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

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v23

-Added support for video previews. Video previews must be in xmv format 
and placed in the Videos folder. Users running at 1080i need to adjust 
the font for the game select screen to the following:

Game Select Settings
Max Text Width: 220
Number of Lines: 10
Font Size: 20
Line Height: 32 

The Xbox does not have enough CPU power to render several true type
fonts at 1080i and update the video preview. This does not apply to
480i/p or 720p.

This version adds support for Ultimate Mortal Kombat Trilogy


-----------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v22

http://xport.xbox-scene.com

What's new:

 - Brought UI core up to date with most recent feature set


-----------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v21

http://xport.xbox-scene.com

what's new:

****************************
* EMU Core Related Changes *
****************************

 - CUE sheet loading for ISO/MP3 is fixed

 - Loading state from BIN/CUE would not restart the CDDA
   being played.  Fixed.

*****************************
* Interface Related Changes *
*****************************

 - Brought up to date with most recently added features


-----------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v20

http://xport.xbox-scene.com

what's new:

****************************
* EMU Core Related Changes *
****************************

 - Some improvement to sector cacheing when playing real Sega CDs (see notes)

Notes
-----

When playing real Sega CDs discs (not images) the FMV can stutter occasionally.
Previous versions of NeoGenesis would try to intelligently buffer as much as 
possible, but you never know where the next piece of data needs to be read 
from the disc until it's already being requested.  Since this is emulation, 
there's no way to anticipate where the reads will be and store it.  The best 
that can be done is to read ahead a certain amount because usually data is 
read linearly from the disc.  This eliminates a good deal of stutter.  However, 
there is only so much one can do to compensate for scratched discs and the 
XBox's ability to read CD media.  Bear in mind that when (if) you listen to 
audio CDs on your XBox they will not stutter because audio tracks are read
from start to finish and the XBox can buffer lots of data at the beginning.
This results in one pause before the track starts, but while the track plays
the audio data can be read much faster than it needs to be sent to the
audio output.  In emulation, there is a short amount of time in between each
frame to read whatever data is needed from the disc, so only so much can be 
buffered at a time.  Trying to read too much data at once will result in 
stuttering because you're waiting too long for all the data to come back from 
the disc and not reading enough can result in too many individual CD-read 
accesses which can also result in stuttering.  

I did notice during some FMV games that they would requests CD sectors a few
behind what was currently being read (almost like reading backwards).  The 
previous versions of NeoGenesis had buffering designed only for forward-reading.
This one has some backwards buffering as well.  This eliminates some more stutter,
but again, there is only so much that can be done to compensate for CD media.

If your CD games still stutter, I first suggest trying to clean your CDs.  If that
makes no difference, then I suggest you copy the disc to an image file and use that
instead.


*****************************
* Interface Related Changes *
*****************************

 - Added "Soften Display" to video settings configuration options

 - "Sort Directories to top" was not working 100% correctly with items 
   that start with a non-alphabetic character - fixed

Enjoy!


---------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v19

http://xport.xbox-scene.com

what's new:

****************************
* EMU Core Related Changes *
****************************

 - Sometimes CDDA would not stop when it should.  This should now be fixed.


Enjoy!


---------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v18

http://xport.xbox-scene.com

what's new:

****************************
* EMU Core Related Changes *
****************************

 - Fixed CDDA for BIN files read off of HD 


*****************************
* Interface Related Changes *
*****************************

 - Added arrows to menus to indicate items above/below visible lines
   Can be disabled under General Settings

 - Added option to always show screenshots when scrolling.
   Find it under General Settings

 - Default for Sprite Limit set to Yes

 - Settings for last saved game carry over to the next game you configure

 - Added game configuration option to Force 60hz in PAL


Enjoy!


---------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v17

http://xport.xbox-scene.com

what's new:

****************************
* EMU Core Related Changes *
****************************

 - Removed "Fix Screen Tearing" configuration option since it is no longer being used

 - Added option to manually disable SRAM to fix games like Puggsy

 - CDDA plays within BIN files now.  You must have a proper CUE file for the BIN
   and it must be named the same as the BIN file.
   (e.g. MY_SEGA_CD_GAME.BIN and MY_SEGA_CD_GAME.CUE )
   Load the CUE file - not the BIN file.

 - BIN files that are actually ROM images and not SegaCD images should correctly
   load as cartridges now.

 - Added Reset to in-game menu and also as a configurable button


*****************************
* Interface Related Changes *
*****************************

 - GUI brought up to date with most recent 

 - All settings will be reset to a baseline when you start this version.
   This will remove the default mapping of BLACK to the screenshot button
   and will also default the Left Analog stick to act like the DPAD
   during gameplay.  However, any games you have previously played will
   have their button configurations loaded from the previously saved config 
   file and will override the new defaults.  

Enjoy!

---------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v16

http://xport.xbox-scene.com

what's new:

****************************
* EMU Core Related Changes *
****************************

 - New game configuration option : Overclock M68000 CPU feature.
   Prevents slowdown on games like Sonic when lots of sprites are on-screen

================
OVERCLOCKING CPU
================

Now there's yet another reason why NeoGenesis is even better than a real
Genesis/Megadrive machine! :)

Ever notice in lots of games like Sonic and Strider that sometimes things will
slow down when lots of sprites are on the screen?  This happens on the real
hardware, too.  Now there's a way to correct that problem.  

Go to the game selection menu, highlight a game, and press X to bring up the
game configuration menu.  There is a new option called "Overclock M68000".
If you turn it on, you should notice that there is no more slowdown.

You can also turn on/off this overclocking from within the game.  While the
game is playing, press the right thumb stick to bring up the in-game menu.
Select "Configuration", "Configure Controllers", "Controller 1", 
"Change Emulator Definitions" and assign one of the emu buttons to be
"Toggle CPU Speed".  Now go to "Change Joypad Mappings", "Change Game Mappings"
and change the button mapping for "Toggle CPU Speed".  Now you can use that
button mapping to turn the CPU Overclocking on/off in the game so you can
better see the effects.

Most games don't suffer from any slowdown, so the overclocking option is
off by default.  

It also doesn't work well with 32x or SegaCD games. SegaCD games cannot even start
if the overclocking option is on at startup.  You'll need to toggle it on/off from
within the game.

WARNING : It is possible to put the emulator into an undefined state when using
the CPU Overclocking on 32x and/or SegaCD games.  The symptoms of this are 
stuttering music and halted gameplay.  If this happens, you'll need to restart
NeoGenesis.  If you just use the overclocking on regular non-32x, non-segacd games,
everything should stay fine.  


*****************************
* Interface Related Changes *
*****************************

 - New (and very excellent) skin by J-RED


============
INSTALLATION
============

If you are a first-time NeoGenesis user, simply upload all the files to a directory
on your XBox and run the default.xbe file.

If you are a previous user of NeoGenesis, you need to first delete the 
E:\SAVES\NEOGENESIS\SKIN_SETTINGS.INI file.  Then you need to completely
remove your existing EMUSKINS directory and replace it with the new one in
this package.  

If you don't follow those instructions, you will get a very weird looking
display.  If that happens, go to "Configuration" -> "Video/Skin Configuration" ->
"Select Skin" and select the default_neogenesis skin.  Things should then
be back to normal.


-------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v15

http://xport.xbox-scene.com

what's new:

****************************
* EMU Core Related Changes *
****************************

 - Fixed funky sound in Phantasy Star 2

 - Fixed ISO9660 + ISO/MP3 bug


-------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v14

http://xport.xbox-scene.com

what's new:

*****************************
* Interface Related Changes *
*****************************

 - ISO9660 support

 - Simplified menus

 - Help menu

 - New button options from Game Selection menu :
     X     - Configure Game
     BLACK - Delete save files for selected game
     WHITE - Adds/Removes selection as a favorite

 - HQ2X graphics filter

 - Option to startup with background music disabled

 - Option to startup on the favorites game selection screen or the regular game selection screen

 - Option to confirm overwriting save states

Merry Christmas!

-------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v13

http://xport.xbox-scene.com

What's New:

*****************************
* Interface Related Changes *
*****************************

 - Fixed relax+linux bugs

 - If you were having Linux+Relax or Samba issues, then I suggest you try
   this version of NeoGenesis.  If this fixes the problems people have been
   having, then the changes will go into all the ports I've done.  If not, then
   I probably will not bother...so I need to hear feedback.  

-------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v12

http://xport.xbox-scene.com

What's New:

****************************
* EMU Core Related Changes *
****************************

 - Memory corruption fix when loading Sega CD games.  If you were having problems with
   certain SegaCD games not working (e.g. Secret of Monkey Island, or anything, really)
   then this should probably fix it.  Some debugging code was left in and if the
   filename length of your SegaCD files was more than about 65 characters (including the
   path) then there would be a buffer overflow.  So if you had a long filename like
   E:\\GAMES\\SEGA\\SEGACDS\\SECRET_OF_MONKEY_ISLAND\\SECRET_MONKEY_ISLAND_02.MP3
   then things would get screwy.


*****************************
* Interface Related Changes *
*****************************

 - Support for Linux Relax sharing
   At this time, your linux share name must contain the "/" character somewhere
   if you want it to be recognized as a linux share.
   For example :

   rlxshare=/home/player/roms@192.168.1.30:1400

 - Possible Samba fix/improvement : see next item

 - New network configuration parameters : XBox IP, Subnet Mask, Gateway IP.
   Access these through the Configuration -> Network Options menu or change
   them in the INI file :

   [GENERAL]
   LOCAL_IP=192.168.1.30
   SUBNET_MASK=255.255.255.0
   GATEWAY_IP=192.168.1.254
   
   LOCAL_IP is the XBox IP address
   SUBNET_MASK is the subnet mask 
   GATEWAY_IP is your default gateway

   Set these to the same values you use in your XBMP configuration file.
 
   This might help people with Samba issues.

 - If you were having Linux+Relax or Samba issues, then I suggest you try
   this version of NeoGenesis.  If this fixes the problems people have been
   having, then the changes will go into all the ports I've done.  If not, then
   I probably will not bother...so I need to hear feedback.  


-------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v11

http://xport.xbox-scene.com

What's New:

*****************************
* Interface Related Changes *
*****************************

 - Update to current UI bugfixes/features 

 - Music Control Menu - press LTHUMB anywhere to bring up the music control menu.
   This is also a customizable controller action while in-game.  Configure it
   via the Controller Configuration -> UI Mappings menu.

 - Can now save any string setting (like Samba/Relax share names) and directory
   locations via menus.  To change Samba/relax share names, go to Configuration ->
   Network/Netplay Configuration.  To change the default directories, go to
   Configuration -> Change Default Directories 

 - Can enter descriptions for cheat codes using virtual keyboard or real keyboard.

 - Can now wrap backwards from first screenshot to last screenshot


-------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v10

http://xport.xbox-scene.com/

What's New:

*****************************
* Interface Related Changes *
*****************************

 - PAL50 support was broken in v8 and fixed in v9, but v9 broke 4x filters and would hang
   whenever trying to change XBox filters.  This is fixed.

 - 4x Filters removed because most of them ran too slowly to be playable on any game and the
   ones that were playable didn't appear to give much ( if any ) improvement to graphics.
   If anyone objects, I'll listen to arguments for re-installing it.

 - Selectable throttle speed - now you can control how fast the throttle/fast forward
   option behaves.

 - Several new transition effects.  Currently, the transition effect is set to "random".  If you
   want to set the transition effect to a specific setting, then go to Main Menu -> Configuration ->
   Configure Skin -> Transition Effect.  If you don't want to see any transitions, then set
   the Transition Speed to 0 on the same menu.

 - Changed memory management of background textures.  This results in more free memory allowing
   for more/larger skin media.  (This is really only of interest to people making skins.)


-----------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v9


http://xport.xbox-scene.com/


What's New:

****************************
* EMU Core Related Changes *
****************************

 - Re-vamped the 50/60, tearing, jittery sound, etc.  Hopefully this should
   straighten out all the weird, misc bugs a few people have encountered when
   trying to play PAL games on NTSC XBox or vice versa.  


*****************************
* Interface Related Changes *
*****************************

 - PAL50 support was broken in v8 ; fixed

 - Fixed Relax bug - now sharenames like $ROOT$ShareName work

 - Sorting is not case sensitive anymore

 - Forgot to mention - in v8 pressing DPAD Left/Right moves by letter
   on the file selection screens.  Move LTHUMB Left/Right to change
   screenshots.


-----------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v8

http://xport.xbox-scene.com/

What's New:

*****************************
* Interface Related Changes *
*****************************

 - 480p, 720p, 1080i support

 - 4x varieties for all filters
    + Most of these 4x filters make the games run too slow to be enjoyable,
      but the AdvanceMame4x runs well and so do a few others.
    + I also suggest not using the 4x filters unless you can use
      720p or 1080i modes.  Scrunching a 1280x960 picture to half that size
      looks almost exactly the same as the 2x version (and perhaps a little
      worse because of the scrunching.)

 - Hardware filtering options : Point, Bilinear, Trilinear, Anisotropic 

 - Access new video options from Main Menu -> Configuration -> Video Configuration

-----------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v7

http://xport.xbox-scene.com/

What's New:

****************************
* EMU Core Related Changes *
****************************

 - Fixed bug where CDDA music would get turned back ON/OFF incorrectly when
   returning from Options Menu

 - Improved real-CD buffering so if your CD is scratched/damaged, it 
   should still play smoothly

 - Added new Configuration Option : Fix Tearing
    + Default is Auto - which means tearing is always fixed unless the game is playing
      consistently less than max FPS.  Set it to "Always" if you never want to
      see screen tearing.  For certain 32x games, this will result is a slightly
      lower/choppier framerate.  Set it to "Never" to get the best possible speed
      and smooth framerate but you may see screen tearing.  


*****************************
* Interface Related Changes *
*****************************

 - New UI Feature - Auto Load Most Recent Save State
     + Turn this option on via the Main Menu -> Configuration menu
     + If it's on, then when you launch a game, the most recently saved
       state will automatically be loaded.


-----------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v6

http://xport.xbox-scene.com/

What's New:

****************************
* EMU Core Related Changes *
****************************

 - Fixed bug in save states when playing from ISO/MP3.
   If you saved a game while it was playing an MP3, continued playing
   until it loaded another MP3, and then reloaded the save state from the
   other MP3, NeoGenesis would crash.  This is fixed.  


-----------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v5


http://xport.xbox-scene.com/

Sorry about the "two releases in 30 minutes" thing....but I think you'll like this one:

What's New:

****************************
* EMU Core Related Changes *
****************************

 - Save States for CD games are now working (!)
   This is a feature even the windows version of Gens does not have.  :)


-----------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v4

http://xport.xbox-scene.com/

What's New:

****************************
* EMU Core Related Changes *
****************************

 - Fixed video slowdown in 32x games.  Very nice FPS in Virtua Fighter 32x and
   all other 32x games now.

*****************************
* Interface Related Changes *
*****************************

 - Other bugfixes that were fixed in other UI-similar releases.  (E.g. long
   filenames in network shares, etc)

-----------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v3

What's New:

****************************
* EMU Core Related Changes *
****************************

 - Fixed screen tearing


-----------------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v2

What's New:

****************************
* EMU Core Related Changes *
****************************

 - Sound fix for everyone experiencing "fast sound" (i.e. the people running
   50hz games on in 60hz XBox mode.)


*****************************
* Interface Related Changes *
*****************************

 - Bug fix - rompath INI setting was not being read 

 - New Skin options :
    + Continuously loop sprite animations or just loop once
    + Assign motion_x and motion_y variables 
    + Assign a bounding rectangle in which sprites can move
    + Assign a degree of rotation that the sprites should turn when they hit a boundary


-------------------------------------------------------------

NeoGenesis Sega Genesis/Megadrive/32X/SegaCD/MegaCD Emulator for XBox v1

Features :

 - Full sound/video

 - Excellent compatibility - ported from Gens

 - Runs real Sega CDs that you put in your XBox DVD drive or it can
   read ISO/MP3 and BIN image files

 - CUE sheet processing for more accurate CD-MP3 playback

 - CDDISSECT-friendly. Rip with CDDISSECT, upload to XBOX, run CUE

 - Selectable GENS settings : (see notes below feature list)
    + Country code ( Autodetect or force a specific country code )
    + CD Emulation Method - Perfect Synchro or Normal
    + 4-player adaptor on port 1 or port 2
    + Show CD LEDs
    + Fast Blur Effect
    + Sprite Limit
    + YM2612 Improvement
    + DAC Improvement
    + PSG Improvement
    + Selectable MSH2 processor speed
    + Selectable SSH2 processor speed

============
Saving Games
============

This is a common pitfall with XBox emulators of consoles that use SRAM.  
If you are playing, for example, Phantasy Star, then when you have saved the game,
you must go back to the game select menu.  

If you just turn off your XBox while you are still playing the game, then
your saves will not be written to the XBox hard drive and it will be like you
never saved your game.

---------------------------------------------------------------
CUE sheet processing/CDDISSECT friendly
---------------------------------------------------------------

I've improved (IMHO) the original CD track processing by 
allowing for the input of a CUE sheet.  The original GENS source code calculates
CD track lengths by making a best calculation of the length of the MP3 files. 
This, however, is not always accurate.  If you have many MP3 tracks on a CD, the
track offsets grow increasingly incorrect.  Using a CDDISSECT-made CUE sheet
results in 100% accuracy.  (So I suggest you use it.)  Additionally, this port
of GENS is completely CDDISSECT friendly - meaning that you can pop a CD into
your computer, run CDDISSECT, upload all the files (without renaming anything)
and run the CUE sheet on XBox.  If you run the CUE sheet, you do not need to
rename the ISO file to remove the "01" at the end of the name.  However, if
you try to run the ISO file, it will not find the MP3 tracks (unless you first
rename the ISO file to remove the "01".)  If you have existing CD images on your
XBox that worked with another port of GENS, then they will also work with this
one.

============================================
Notes From Gens Documentation About Settings
============================================

Gens now features a custom YM2612 (main sound chip) sound core which
features a "High Quality" mode. The sound output is more accurate
in HQ mode, but it slows things down a bit.  

Gens also features an "improved" DAC (part of the YM2612) sound mode.
This makes the sound in a few games, ( e.g. Street Fighter 2), much better 
than it would be on real hardware.  However, it also causes bugs in other games 
so you should leave it turned off most of the time.

There is optional PSG sound "improvement".  This changes the PSG sound 
output from Square waves to Sine waves which is technically incorrect but can 
make some games sound better. Again you should leave this turned off unless you 
really hate the normal PSG sound.

The 2 SH2 processors can take up to 75% of the emulation time !
To gain some FPS, Gens offers the possibilities to change
MSH2 and SSH2 CPU clocks from 0% to 100%. 

Replace 100 by a lower value to speed up the 32X emulation.
100 means SH2 runs at 23 Mhz and 0 means 0 Mhz... easy :)
Gens doesn't emulate some wait states presents in the real 32X hardware so
you can decrease the master CPU to 60 for almost all games without affecting the
in-game speed.

Slave CPU is mainly used for sound emulation (except for some games with
many 3D calculations such as Virtua Racing), so you can decrease it if you think
PWN sound isn't important.


*****************************
* Interface Related Changes *
*****************************

 - ZIP support

 - Netplay

 - Netplay option to allow for smoother netplay : netplay skip.
   When server starts netplay, you can select a netplay skip value.
   This number specifies how often it should skip checking for network data.
   The higher the number, the less often it checks for network data, but the
   result will be a less responsive controller.

 - Cheat system - Search/Create your own cheat codes or enter Game Genie codes

 - Favorites list

 - Resizable game screen

 - Save Game management - delete save game files

 - Skin-able :
    - Backgrounds
    - Sounds
    - Background Music
    - Sprites
    - Text position (right/left/center, top/bottom/center)
    - Text color, select bar color
    - Font
    - Fading speed
    - Screenshot position
    - Can specify 2 sprites to surround the selected menu option
    - Option to have a transparent select-bar color (from select-color menu)
    - Can flip sprites horizontally/vertically
    - If you want to change the way something looks in this new UI,
      chances are that you can change it via the Configuration menu.

 - Samba/NetBIOS sharing support (read files from your PC)

 - Relax Network Sharing (read files from your PC)

 - Support for filenames > 42 chars from shared directories

 - Play MP3 or M3U playlists in the background
   (Can also read MP3/M3U from across Samba/Relax shares.)

 - User definable save directory.  If you don't like the default of
   E:\SAVES\NEOGENESIS you can change it via the NEOGENESIS.INI file

 - Take in-game screenshots and display them on the game selection list

 - Graphics filters :
     + 2xSai
     + Super 2xSai
     + Eagle
     + Super Eagle
     + SuperScale
     + AdvanceMame 2x
     + Simple 2x
     + 2xSai Scanline
     + Super 2xSai Scanline
     + Eagle Scanline
     + Super Eagle Scanline
     + SuperScale Scanline

 - Record/Playback feature - record your gameplay in the emu and then
   play it back again.  Record up to 10 minutes of gameplay.

 - Every single in-game command is fully customizable on any of the
   four joypad controllers.

 - Map any emulator or UI command to a single button or a combination of
   two buttons.  (e.g. RTrigger+LTrigger = Save State)
   Basically, the controllers are 100% customizable.

 - Autofire capabilities for any emulator button on any controller

 - One-button combos (define a series of emulator commands to be played
   back when you press a user-definable XBox controller combination.)
   (E.g. Press RTrigger+LTrigger to execute the command string
   A,B,A,B,Up,Down,Left,Right)

 - Traverse any directory on any drive ( Continue selecting the parent
   directory entry on the file selection list to get the drive selection
   list.  Selectable drives are C, D, E, F, R, X, Y, Z, and SMB. 
   R is the CDROM drive.  SMB is the samba share you have defined in your
   NEOGENESIS.ini file.  RLX is the relax share you have defined in your
   NEOGENESIS.ini file.)  Press Y from any file-listing screen to go up one
   directory level.

 - Save States with 10 save state slots for each game

 - All UI commands (save state, load state, screenshot, etc) can be
   invoked from the Options/Pause menu as well as in-game via your
   customized joypad mappings.

 - Can be invoked from a command-line to directly run a game from a front-end
   or dashboard and bypass the user-selection screens. (Only if the frontend
   or dashboard supports this feature.)

 - Can return to the launching program *if* the launching program supports this
   feature.  For example, if the custom-launch routines are incorporated into 
   a new frontend, that frontend could launch NeoGenesis and when you exit 
   NeoGenesis, that frontend can be automatically reloaded.  

 - Flapjack and a cigarette


=====================
Relax Network Sharing
=====================

The relax sharing setting goes in the [GENERAL] section as follows:

rlxshare=c:\sgenroms@192.168.123.77:8989

Replace 192.168.123.77 with your computer IP address and replace 8989 with the
port where you have Relax running.


============================
Note on Samba/NetBIOS Shares
============================

There are two INI file settings relating to Samba/NetBIOS sharing and they both
reside in the [GENERAL] section of NeoGenesis.INI:

smbshare=smb://username:password@workgroup:ip_address/computername/sharename
smb_nameserver=192.168.0.1


The smbshare parameter accepts many different formats.  Here are the most 
common:

smbshare=smb://username:password@workgroup/computername/sharename
smbshare=smb://username:password@workgroup:ip_address/computername/sharename
smbshare=smb://username:password@computername/sharename
smbshare=smb://username:password@computername:ip_address/sharename
smbshare=smb://workgroup/computername/sharename
smbshare=smb://workgroup:ip_address/computername/sharename
smbshare=smb://computername/sharename
smbshare=smb://computername:ip_address/sharename

Please try all of the above combinations before deciding it does not work.
Also be aware that some people have to select their SMB drive in NeoGenesis a few
times before any files appear.

If it's still not working, then set the nameserver equal to the IP address of
the computer you are trying to reach or set it equal to your NetBIOS name server.
(If you don't know what a NetBIOS name server is, then just set it to the 
IP address of the computer you are trying to reach.)


Also remember that when you make changes to NeoGenesis.INI, you have to do a 
"Force Reload of D:\*.INI" from the Configuration Menu or else the changes
you made to NeoGenesis.INI will not be loaded.  


=============
Configuration
=============

Almost everything can be changed from the configuration menu.  Here are the
things that require manual modifications to the NeoGenesis.INI file included in
the package: 

Note - you do not need to change the defaults in the INI that comes packaged
with NeoGenesis in order for NeoGenesis to run.  These are all *optional*.

Samba share name - goes in the [GENERAL] section.  Example:

smbshare=SMB://USERNAME:PASSWORD@COMPUTERNAME/SHARENAME


Screenshot directory - default is E:\SCREENSHOTS - goes in [GENERAL] section
Example:

screenshot_dir=E:\SCREENSHOTS


Skin directory - where skins can be found.  Default is D:\EMUSKINS - goes in
[GENERAL] section.  Example:

skin_dir=D:\EMUSKINS


Save directory - this is where you want all your saved games to be stored.
Default is E:\SAVES\NEOGENESIS.  Goes in [GENERAL] section.  Example:

save_dir=E:\SAVES\NEOGENESIS


The default ROM directory INI setting goes in the [GENERAL] section as follows:

rom_dir=d:\sgenroms


If you change any of the above items, then you must upload the new NeoGenesis.INI
file to your XBox, load up NeoGenesis, then select "Force Reload D:\\*.ini 
Settings" from the Configuration menu.  Please note that this will overwrite
any of the setting changes you might have made after you first loaded
NeoGenesis.


===============
Menu Navigation
===============

Select menu options with the DPAD or with R/LTrigger.  The speed of 
R/LTrigger movements can be controlled by :

Configuration -> Menu Scroll Speed

There are some places where you can enter or change values.  This 
can usually be done in a variety of ways include DPAD Left/Right, 
R/L Trigger, and L/R Thumb.  Try all of them if the values are changing
too slowly.

"A" selects the highlighted choice.  "B" cancels/returns.
"Y" from a file-select list will go up one directory.


=====
SKINS
=====

Instructions for making a new skin:

 - Create a new directory off of your SKINS directory (default skins directory
   is D:\EMUSKINS
 - Place your sound/font/graphic media files in this new directory 
 - Load NeoGenesis
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

If you make/configure a skin and NeoGenesis does not load the next time you
play it, then you need to delete the E:\SAVES\NEOGENESIS\NEOGENESIS.INI and
E:\SAVES\NEOGENESIS\SKIN_SETTINGS.INI files.  NeoGenesis should work fine again,
but you'll have to reconfigure your skin.  The problem was probably
that one of your resources (like a WAV or background file) was specified
incorrectly or was never changed from the old skin.  Carefully look at the 
E:\SAVES\NEOGENESIS\SKIN_SETTINGS.INI file to make sure that all filenames exist 
in your skin directory.


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
number like 5 first and them fine-tuning it.


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


================
MP3/M3U Playback
================

Simply select the MP3 or M3U file from the game-selection screen.

The M3U file can also just be a regular file with one songfile per line.
For example:

d:\songs\song1.mp3
e:\moresongs\song2.mp3
smb:\mp3s\song3.mp3

If you are making a playlist of songs on your SMB share, then please note
the format:

smb:\mp3s\song3.mp3

The smb:\ tells NeoGenesis to read from your SMB shared directory.  Do not
put the SMB share definition in the filename.

----------SMB shared filenames are case sensitive!!!---------


=======
Netplay
=======

In order to netplay with someone, follow these steps:

 - Go to the Configuration menu
 - Select Netplay options
 - Turn netplay on
 - Add a server if you are going to connect to someone else
 - Select the game to play
 - If netplay is on, it will ask you if you want to be the client
   or the server.  One person is the client, and the other is the server.
   If you are the server, the game will wait until the client has
   joined.  If you are the client, make sure the server is ready to accept
   your connection before continuing.  
 - When server starts netplay, you can select a netplay skip value.
   This number specifies how often it should skip checking for network data.
   The higher the number, the less often it checks for network data, but the
   result will be a less responsive controller.
 - Once a connection has been made, it should work fine.

NOTE : You both MUST be using the *EXACT* same game.  
I would be *extremely* surprised if the PAL version of a game
worked via netplay with an NTSC version of the same game.  


The server player is always player 1.  The client player is always player 2.

I don't know how well netplay will work across real networks.  Two xbox's 
on the same intranet work very well, though.

If your connection is lost during gameplay, just wait 30 seconds and
you can return to the game select menu.  (Or you can always reboot...)


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

NeoGenesis can be started with parameters to automatically launch a game
at startup.  Example code can be found in the custom_launch_params.cpp file.

There is also example code in that same file that will show you how to 
make NeoGenesis load your frontend/dashboard when it exits.

Enjoy!


Stella, Gnuboy, SMSPlus, FCEUltra, HUGO, NeoPop, DGen, Bochs, HUGO-CD, FMSXBox,
Bliss, WinSTon, Gens/NeoGenesis, Z26, StepmaniaX, PCSXBox, XBoyAdvance....what's next?
