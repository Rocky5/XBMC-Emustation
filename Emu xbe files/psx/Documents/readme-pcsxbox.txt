PCSXBox - PSX Emulator for XBox v21 (redux)


http://xport.xbox-scene.com
goto http://www.emuxtras.net/ for latest cheats, rumbles, synopsis and skin updates.

What's New:

Check the Latest-pcsxbox.txt file for the latest update info.  From now on it will have the latest info and this file will contain the changelog/older update information.


-----------------------------------------------------------------------

PCSXBox - PSX Emulator for XBox v21


First off...

------------------
Special thanks....
------------------

X-port for porting a great collection of emu's over to the xbox, releasing the source code, and answering my stupid questions.

Atariage (Albert in particular) - For providing a place for me to ramble on. For encouragement in general.

Gilou9999 for a new PM3 skin, synopsis, suggestions, etc.

Bigby, Du0ph0ne, TheMaster3, Nytmar3 for some beta testing.

Comments of support from various interested parties.

If I missed anybody shoot me an email and I'll update this file.


***************************
* Changes To PcsXbox Core *
***************************

* Changed so all versions (1.14-1.16) use same configurations for ease of use and to save confusion

* Directory information is passed when changing PSX versions so that when user exits a game he is still on the same game in the game select screen (again to save confusion).


*********************
* To Do For PcsXbox *
*********************

- Fix some lockups on exit?


*****************************
* Interface Related Changes *
*****************************

* Given the full "Madmab Edition" treatment.

* New dual-preview skin to support Ressurection Xtra's.  Say thank you to Gilou9999 for the skin.

* "Move Selected to the Garbage Folder?" now has a new option.. "Never Move".  So "Yes" will ask before moving the selected file to the Garbage folder.  "No" will just move the file and "Never Move" won't move the file at all.

* New feature "Seconds before playing movie" determines how long the emu will wait before playing a movie.  The default is half a second.  This will help speed up rom browsing.  Especially useful for people streaming stuff (like movies) across the network.

* If streaming movies from across the network and the user press on the dpad or a, b, x or y the emulator will abort the transfer.  This should help speed up rom browsing and allow the user an "out" especially for the larger movies.

* Pressing the back key while viewing a games synopsis will toggle between a fixed font and the skins proportional font.

* Fixed an issue with the software filters displaying garbage.

* Activated the "Keep user Within ROM Directory Tree?" which I somehow missed.

* Fixed up the box/cart art position on a few skins.

* Fixed a problem where setting the box/cart orientation was screwed up.

* Fixed the bug that screwed up Gilou's skin to begin with (too weird to explain).  :P

* Accurate Screen Pixel Ratio option added (see "http://fancyxbox.info/?doc=1&secao=screen" for more into) per gilou9999's suggestion.  Some numbers are still a WIP.  Go into Game/Text Screen Size Position" and select "Set Game Screen to Accurate Screen Pixel Ratio".  The emu will ask you if you wish to turn off software/hardware filters and flicker filter.  This is recommended for the most accurate screen.  You'll still have to manually adjust the image on the Y axis.  We can't do everything for you, ya lazy bum!

* Added an option to display a "Static" video if no movie found.  Can be set to yes or no.  Static file must be named "Tv Static.xmv" and placed in the emu's "backgrounds" directory.

* Rewind is a bit of a memory hog.  On some emu's at 720p it is barely useful.  Some emu's can't even handle it.  Here is what I did.

* Tweaked around with the rewind system fixed a couple potential xbox lockers.

******************
* Rewind changes *
******************

* Rewind is a bit of a memory hog.  On some emu's at 720p it is barely useful.  Some emu's can't even handle it.  Here is what I did.

* Tweaked around with the rewind system fixed a couple potential xbox lockers.

* Modified the rewind system so if memory runs low it clears half the buffer, if that doesn't work it clears the entire buffer.  What this means is that on memory intensive emu's you'll have a rewind system that mostly works.  It's pretty much a "better than nothing" set-up.

* Known emu's to have rewind issues.  

-  NeoGenesis in CD or 32x mode cannot deal with it.  Frameskip had to be activated for it to even work in Genesis mode.

-  Snes9xBox works almost 100% in 480i/480p.  At 720p I relied on two things clearing the buffer when it's full and saving memory when filters are not used (see above)

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

* Modified YesNoMenu so it doesn't clear m_menuText.

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

PCSXBox - PSX Emulator for XBox v20

http://xport.xbox-scene.com/
http://home.t-online.de/home/PeteBernert/
http://www.pcsx.net

What's new:

 - Shortcuts work again.
   For reference:
   http://xbmc.org/wiki/?title=HOW-TO:_Create_shortcuts_to_.xbe_files


Just a small tweak by Bomb Bloke.
Who doesn't have a great big long list of achievements to put here... ;)

Enjoy!


-----------------------------------------------------------------------

PCSXBox - PSX Emulator for XBox v19

http://xport.xbox-scene.com/
http://home.t-online.de/home/PeteBernert/
http://www.pcsx.net

What's new:

 - Updated UI core to most recent feature set


-----------------------------------------------------------------------

PCSXBox - PSX Emulator for XBox v18

http://xport.xbox-scene.com/
http://home.t-online.de/home/PeteBernert/
http://www.pcsx.net

Many thanks to Neverwill for the great new skins!
There is a full-color version also included.  To change to it, go to
Configuration -> Video/Skin Configuration -> Select Skin

What's new:

****************************
* EMU Core Related Changes *
****************************

 - Added buttons for L3/R3/Mode
   "Mode" only functions in Dual Shock mode.

 - Fixed Right Thumbstick X-Axis (was inverted)

 - There is now a single directory for saves.  If you were using
   the 1.4 or 1.6 cores to play games, then you should move all of your
   files/directories from E:\SAVES\PCSXBOX_1.4 and E:\SAVES\PCSXBOX_1.6
   to E:\SAVES\PCSXBOX

 - Implemented true Dual Shock+rumble support.  From the game configuration
   menu change the "Controller #" to "Dual Shock" to enable it.
   No, Ape Escape still does not work - it's a core issue, not a
   Dual Shock issue.

 - You cannot use Dual Shock and multitap simultaneously.

 - Added option to enable/disable rumble for controllers 1/2   

 - Added option to increase the rumble amount for controllers 1/2
   if the rumble is too light.

 - Instructions included on how to set up your own website which can
   store/serve configuration files:
   upload_download_configurations_instructions.txt


--------------------------------------------------------------------

PCSXBox - PSX Emulator for XBox v17

http://xport.xbox-scene.com/
http://home.t-online.de/home/PeteBernert/
http://www.pcsx.net

Many thanks to Neverwill for the great new skins!
There is a full-color version also included.  To change to it, go to
Configuration -> Video/Skin Configuration -> Select Skin

What's new:

****************************
* EMU Core Related Changes *
****************************

 - Analog support ( tested on Medievil )
   Go to the game configuration screen, and toggle the controller type
   for controller 1 through 4.

 - Multitap support ( tested on MicroMachines v3 )
   Go to the game configuration screen and toggle "Multitap".


--------------------------------------------------------------------

PCSXBox - PSX Emulator for XBox v16

http://xport.xbox-scene.com/
http://home.t-online.de/home/PeteBernert/
http://www.pcsx.net

Many thanks to Neverwill for the great new skins!
There is a full-color version also included.  To change to it, go to
Configuration -> Video/Skin Configuration -> Select Skin

What's new:

****************************
* EMU Core Related Changes *
****************************

 - Save state loading caused crashes under certain circumstances.
   This has been fixed.  

 - Defaulted "Auto load most recent save state" to off since this
   seems to be causing lots of problems.

   If this is not disabled automatically for you, I suggest
   making sure it's always off unless you know what you're doing.


--------------------------------------------------------------------

PCSXBox - PSX Emulator for XBox v15

http://xport.xbox-scene.com/
http://home.t-online.de/home/PeteBernert/
http://www.pcsx.net

Many thanks to Neverwill for the great new skins!
There is a full-color version also included.  To change to it, go to
Configuration -> Video/Skin Configuration -> Select Skin

What's new:

****************************
* EMU Core Related Changes *
****************************

 - Added "Throttle Method" option to game configuration screen.
   The original way that throttling was handled in all versions
   prior to v14 is that once you hit the throttle/FF button once, it 
   would set a flag that would never get cleared, even after you 
   release the throttle/FF button.  In v14, I "fixed" this bug, but
   apparently people liked the bug - so now they have the option of
   making use of it.
   It defaults to the way things were before v14.  

 - Select the core on the game configuration screen.  If the core
   you wish to use is not the current XBE that is running, the
   appropriate XBE will be launched with the game you selected as
   the parameter.  

   The 1.4core XBE must be called "DEFAULT14.XBE"
   The 1.5core XBE must be called "DEFAULT.XBE"
   The 1.6core XBE must be called "DEFAULT16.XBE"
   
   All of the XBEs must be in the same directory.

 - Possibly improved load state.  I'm pretty sure that in this version
   of PCSXBox some variables are set up more correctly than in previous
   versions when completing a load state.  The default is to have this new
   load state method on by default, but if you find that your saved states
   no longer load, then turn off the "Use Newer Restore State" option on the
   game configuration menu. 

 - Somewhat reduced the frequency/duration of the brief pauses during gameplay.

 - Included game configuration option to save the memory card data with the
   save states.

 - New SPU option "Sound Timer".  Originally the sound code was executed
   synchronously with the CPU emulation.  Putting it in threaded mode seems
   to give a few extra FPS on average, so it is the new default.  If your
   games sound different and you want to go back to an original setting, 
   go to your game configuration -> Set SPU Fixes -> Sound Timer Method and
   set it to "Original" instead of "Threaded". 


--------------------------------------------------------------------

PCSXBox - PSX Emulator for XBox v14

http://xport.xbox-scene.com/
http://home.t-online.de/home/PeteBernert/
http://www.pcsx.net

Many thanks to Neverwill for the great new skins!
There is a full-color version also included.  To change to it, go to
Configuration -> Video/Skin Configuration -> Select Skin

what's new:

****************************
* EMU Core Related Changes *
****************************

 - Brought up to date with core UI features

 - Multiple XBEs for PCSX cores :
   1.4 : PCSXBox version 1
   1.5 : PCSXBox versions 2-13
   1.6 : new as of version 14

 - Selectable SPU cores:
     1.6 : PCSXBox versions 1-11
     1.9 : PCSXBox versions 12-13

 - Selectable GPU cores:
     1.12 : PCSXBox versions 1-7
     1.15 : PCSXBox versions 8-11
     1.16 : PCSXBox versions 12-13

 - Bugfix recMTC2 : Medievil works now in the recompiler instead of just the 
   CPU interpreter mode (possibly other games as well)
   Medievil actually always worked if you enabled "Use CPU interpreter" from the
   CPU fixes menu, but it was unbearably slow.  
   Set Frameskip and Framelimit off and set the SPU settings to the fastest possible.
   It's still far from fullspeed, but it's playable now.

 - Each game gets its own set of memory cards

 - Added new game configuration section "Set SPU Fixes"

    + XA Sound - disable/enable (disable to speed up performance), default was on

    + XA Speed Fix - if XA sound is too fast, try enabling this, default was off

    + Reverb - better reverb effects at the expense of performance, default was Best/Slowest

    + Interpolations - better sound effects at the expense of performance, default was Gaussian/Good

    + Wait for CPU Action - Fixes games like Valkyrie Profile (tested) and Metal Gear Solid (untested)

    + IRQ in Decoded Sound Buf - Fixes Crash Team Racing (untested)

    (Setting Reverb and Interpolations to None/Fastest can give noticeable FPS increases
    since all prior versions had them set to better/slower values.)

 - See notes about Memory Cards

 - Rewinding does not work (not that it ever did anyway)


Memory Cards
------------

I've noticed that memory cards are somewhat glitchy in some games.  For example,
in Valkyrie Profile, when you try and save, it will sometimes say it cannot
read the memory cards or that it fails.  Similarly, when trying to reload, it
will not show any save slots.  I've found that retrying will result in success
(eventually.)

I recommend using both memory cards and save states while playing, just in case.


*****************************
* Interface Related Changes *
*****************************

 - ISO9660 support 

 - Save state selection menu now has timestamp next to each used state.


--------------------------------------------------------------------

PCSXBox - PSX Emulator for XBox v13

http://xport.xbox-scene.com/
http://home.t-online.de/home/PeteBernert/
http://www.pcsx.net

what's new:


****************************
* EMU Core Related Changes *
****************************

 - Fixed sound


--------------------------------------------------------------------

PCSXBox - PSX Emulator for XBox v12

http://xport.xbox-scene.com/
http://home.t-online.de/home/PeteBernert/
http://www.pcsx.net

what's new:


****************************
* EMU Core Related Changes *
****************************

 - Improved speed 5-10% on average

 - Fixed problem where it was impossible to return to main menu

 - Changing discs now works (tested with Chrono Cross)

 - Upload/Download configurations to/from xport.xbox-scene.com via GUI

 - Implemented FF9 movie fix - select the option from the CPU fixes menu

 - Diablo works now (?) see notes

 - Support for simultaneous shared memory cards and game-specific memory cards.
   To select a game-specific memory card, change the Memory Card number to 10
   via the Game Configuration menus.
   
 - Memory card settings saved per game

 - Merged in PEOPS SPU v1.9
   * speed optimized ADSR mixing

 - Merged in PEOPS GPU v1.16
   * Dark Forces fix - set it on the Graphics Fixes Menu
   * Skullmonkeys y-coordinate fix


==============================
Upload/Download Configurations
==============================

This is a new GUI feature that allows you to share your configuration files with
the rest of the world.  

At the time of this version, there are only a few configuration files available 
on the website.  Once you have a game tweaked and working well, please take a few 
moments to upload the configuration.  This is as simple as selecting the "Upload" 
option on the Game Configuration menu.  Downloading a configuration can be 
accomplished in very much the same manner by selecting the "Download" option.


============
Diablo Works
============

This is rather strange.  I remember trying Diablo (US version) a long time ago and 
noting that things seemed like they would be OK except that the controls did not 
work.  Later, someone else confirmed this on the PCSXBox compatibility list.  However,
now it works in BIOS mode.  I cannot recall what version was the last time I tested
it or if anything changed or perhaps I tried BIOS mode when there was no actual
BIOS file and it defaulted to HLE mode.  (This would be before I put in the check
that informs the user if the BIOS is not actually present.)

Compatibility has most likely not changed, but I thought this was worth mentioning.


===========
Save States
===========

I've noticed that save states work seemingly randomly, but if you are
persistent in loading them, they will eventually work.  There may be certain 
games where save states simply do not ever work, but I strongly suggest that
you try loading them over and over several different ways (e.g. via Autoload
most recent savestate, via the on-screen menus, and via the button combo in-game).
Chances are they will work eventually.  This has always been the case - nothing
has changed with save states in this release.  I just thought it was noteworthy.


============
Memory Cards
============

In addition to the 10 shared memory cards, there is now an option to use a 
game-specific memory card.  This is a memory card that is unique to the game
you are playing.  You can have 2 of them per game (slot 1 and slot 2). 

To enable the feature, change the Memory Card number to 10 in the Game 
Configuration menus.


*****************************
* Interface Related Changes *
*****************************

 - Most recent version of standard GUI (lots of updates since last version)

 - Fixed a bug with loading save states 

 - Fixed default ROM path not being set at startup


--------------------------------------------------------------------

PCSXBox - PSX Emulator for XBox v11

http://xport.xbox-scene.com/
http://home.t-online.de/home/PeteBernert/
http://www.pcsx.net

what's new:

*****************************
* Interface Related Changes *
*****************************

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

Merry Christmas!


------------------------------------------------------------

PCSXBox - PSX Emulator for XBox v10

http://xport.xbox-scene.com/
http://home.t-online.de/home/PeteBernert/
http://www.pcsx.net

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

PCSXBox - PSX Emulator for XBox v9

http://xport.xbox-scene.com/
http://home.t-online.de/home/PeteBernert/
http://www.pcsx.net

What's New:

*****************************
* Interface Related Changes *
*****************************

 - Relax sharing works now

 - Turning off background music option works now 

 - Fixed little bug that was making everything very quiet


----------------------------------------------

PCSXBox - PSX Emulator for XBox v8

http://xport.xbox-scene.com/
http://home.t-online.de/home/PeteBernert/
http://www.pcsx.net

What's New:

****************************
* EMU Core Related Changes *
****************************

 - Cleaned up video handling and rewrote some video routines resulting in
   about 10-20% framerate improvement.  For example, Castlevania SOTN
   ran at about 52 fps before, and now it runs at over 60fps with dips to 58fps
   from time to time.  

 - Implemented P.E.Op.S. PSX Soft GPU v1.15 - relevant changes :
    + Fixed frame limitation if "old skipping method" is used
    + Added sprite x coord wrap (skullmonkey)


*****************************
* Interface Related Changes *
*****************************

 - Many miscellaneous bug fixes that were applied to the other recent emu releases

 - Relax support

 - Basically the same set of features as the most recent other emu ports I've done


----------------------------------------------

PCSXBox - PSX Emulator for XBox v7

What's New:

*****************************
* Interface Related Changes *
*****************************

 - Fixed freezing during loading of XBE (see below)

 - Fixed freezing during loading of game (see below)

 - Press Y from any file listing to go up one directory

 - Settings files (STG) will be saved with graphics filter now.
   The settings file format should remain static.  

 - Background Music should stay stopped or stay started when
   entering/exiting a game now.

 - New Configure Skin menu option - Show Available Memory
   Shows how much memory is currently available.
   Please remember that sometimes an emulator will allocate memory the
   first time it is run - so when you are making a skin be sure to run
   the emulator at least once before determining how much memory you have
   left for your skin.

 - Small change to Samba routine - but it's not likely it changes much.

=====
Samba
=====

moneyshotz has reported that the following SMB share format worked for him:

smbshare=smb://MSHOME/moneyshotz/PSXRoms
smb_nameserver=192.168.2.242

MSHOME = workgroup name
moneyshotz = computer name
PSXRoms = share name
192.168.2.242 = IP address of the computer which is sharing PSXRoms

So please try that method as well as those listed below.


==================================================================
If PCSXBox was freezing on you before it even got to the Main Menu
==================================================================

 - Remove the E:/UDATA/ffff051f/0FC41366546E/ directory as well as 
   everything inside it.  (There should only be one SaveMeta.XBX file
   in that directory and it is probably 0-length.)  Be sure that you
   remove the 0FC41366546E directory completely.  Don't just delete the 
   SaveMeta.XBX file.

 - Delete E:/SAVES/PCSXBOX/PCSX.INI and E:/SAVES/PCSXBOX/SKIN_SETTINGS.INI

 - Install PCSXBox v7


=================================================================
If PCSXBox was freezing on games that worked in previous versions
=================================================================

 - Remove the E:/UDATA/ffff051f/0FC41366546E/ directory as well as 
   everything inside it.  (There should only be one SaveMeta.XBX file
   in that directory and it is probably 0-length.)  Be sure that you
   remove the 0FC41366546E directory completely.  Don't just delete the 
   SaveMeta.XBX file.

 - Delete E:/SAVES/PCSXBOX/PCSX.INI and E:/SAVES/PCSXBOX/SKIN_SETTINGS.INI

 - Delete the STG and KEY files associated with the game you are trying to play.
   For example, if your game is called CASTLE.BIN, then delete the following
   files : E:/SAVES/PCSXBOX/CASTLE.STG and E:/SAVES/PCSXBOX/CASTLE.KEY

 - Install PCSXBox v7


-----------------------------------------------------------------------

PCSXBox - PSX Emulator for XBox v6


What's New:

*****************************
* Interface Related Changes *
*****************************

 - Samba/NetBIOS fix.  This should hopefully fix the problems that some people
   have been having with Samba/NetBIOS shares.

 - New SKIN features :
     + Can specify 2 sprites to surround the selected menu option
       Be sure to re-install the PCSXBOX_DEFAULT skin in this package
       to see an example.
     + Option to have a transparent select-bar color (from select-color menu)

 - Fixed bug where MP3 would start up again after game ends even if it was stopped.

 - All *.PNG screenshots in screenshots dir will be displayed on game select
   screen regardless of filename now.

 - Fixed bug where fade speed of 0 resulted in game-loading screen not displaying

 - New graphics filters :
     + 2xSai Scanline
     + Super 2xSai Scanline
     + Eagle Scanline
     + Super Eagle Scanline
     + SuperScale Scanline

 - New netplay option to allow for smoother netplay : netplay skip.
   When server starts netplay, you can select a netplay skip value.
   This number specifies how often it should skip checking for network data.
   The higher the number, the less often it checks for network data, but the
   result will be a less responsive controller.


-----------------------------------------------------------------------

PCSXBox - PSX Emulator for XBox v5

What's New:

*****************************
* Interface Related Changes *
*****************************

 - Fixed bug when reloading favorites list containing files with spaces in them

 - Fixed bug where screenshots were not displaying on favorites list

 - Samba/NetBIOS library updated and added option for a nameserver

 - XBE should now load regardless of any screwy settings

 - New option - see full path or just filename on favorites list

 - Changed location of save files to E:\SAVES\PCSXBOX
   Existing save files will be moved there.

 - User definable save directory.  If you don't like the default of
   E:\SAVES\PCSXBOX you can change it via the PCSX.INI file

 - New option - overwrite D:\PCSX.INI and D:\EMUSKINS\SKINNAME\SETTINGS.INI
   files with current settings.  Makes it easier to package up your custom
   skins.

 - Loading a new skin should work correctly now

 - Record/Playback feature - record your gameplay in the emu and then
   play it back again.  Record up to 10 minutes of gameplay.

 - New main menu option "Configure Game"  Set all configuration for a game
   from the main menu so you can just click on the game to play it.

============================
Note on Samba/NetBIOS Shares
============================

There are two INI file settings relating to Samba/NetBIOS sharing and they both
reside in the [GENERAL] section of PCSX.INI:

smbshare=smb://username:password@workgroup:ip_address/computername/sharename
smb_nameserver=192.168.0.1

The smbshare parameter accepts many different formats.  Here are the most 
common:

smbshare=smb://username:password@workgroup/computername/sharename
smbshare=smb://username:password@workgroup:ip_address/computername/sharename
smbshare=smb://username:password@computername/sharename
smbshare=smb://username:password@computername:ip_address/sharename

Please try all of the above combinations before deciding it does not work.
Also be aware that some people have to select their SMB drive in PCSXBox a few
times before any files appear.

If it's still not working, then set the nameserver equal to the IP address of
the computer you are trying to reach or set it equal to your NetBIOS name server.
(If you don't know what a NetBIOS name server is, then just set it to the 
IP address of the computer you are trying to reach.)


Also remember that when you make changes to PCSX.INI, you have to do a 
"Force Reload of D:\*.INI" from the Configuration Menu or else the changes
you made to PCSX.INI will not be loaded.  


=============================
User Definable Save Directory
=============================

There is another new INI file setting that can be placed in the PCSX.INI 
[GENERAL] section :

save_dir=E:\SAVES\PCSXBOX

This specifies the directory where you want PCSXBox to save your files.  Please
note that the PCSX.INI and SKIN_SETTINGS.INI files that reflect your actual
PCSXbox settings and skin settings will *always* reside in the default save
directory which is E:\SAVeS\PCSXBOX    

If you already have saved games, don't worry.  PCSXBox will move those save
game files to the new directory automatically the first time you run v5.


-----------------------------------------------------------------------

PCSXBox - PSX Emulator for XBox v4

This is a completely new UI which I plan on incorporating into most of my other 
releases.  I tried to include as much customization and as many features as 
possible, but I'm sure there will still be changes and additions that people 
will want to see.  Please provide feedback on the xbox-scene.com emulation 
forums so that this UI can be refined and then placed into the other ports.

What's New :

 - Customizable skins
    - Backgrounds
    - Sounds
    - Background Music
    - Sprites
    - Text position (right/left/center, top/bottom/center)
    - Text color, select bar color
    - Font
    - Fading speed
    - Screenshot position
    - If you want to change the way something looks in this new UI,
      chances are that you can change it via the Configuration menu.

 - Default Castlevania:SOTN skin gives example of what you can do.

 - Netplay (2 players)

 - Samba/NetBIOS support (read CD images from your PC)

 - Every single in-game command is fully customizable on any of the
   four joypad controllers.

 - Map any emulator or UI command to a single button or a combination of
   two buttons.  (e.g. RTrigger+LTrigger = Save State)

 - Autofire capabilities for any emulator button on any controller

 - One-button combos (define a series of emulator commands to be played
   back when you press a user-definable XBox controller combination.)
   (E.g. Press RTrigger+LTrigger to run the series of commands that
   will cast Soul Steal in Castlevania)

 - Traverse any directory on any drive ( Continue selecting the parent
   directory entry on the file selection list to get the drive selection
   list.  Selectable drives are C, D, E, F, R, X, Y, Z, and SMB. 
   R is the CDROM drive.  SMB is the samba share you have defined in your
   pcsx.ini file.)

 - 10 save state slots

 - Take in-game screenshots which can later be browsed and can also
   be viewed on the game-selection list.

 - All UI commands (save state, load state, screenshot, etc) can be
   invoked from the Options/Pause menu as well as in-game via your
   customized joypad mappings.

 - New graphics filters :
    - 2xSai
    - Super 2xSai
    - Eagle
    - Super Eagle
    - SuperScale
    - AdvanceMame 2x
    - Simple 2x

 - Can be invoked from a command-line to directly run a game from a front-end
   or dashboard and bypass the user-selection screens. (Only if the frontend
   or dashboard supports this feature.)

 - Can return to the launching program *if* the launching program supports this
   feature.  For example, if the custom-launch routines are incorporated into 
   a new frontend, that frontend could launch PCSXBox and when you exit 
   PCSXBox, that frontend can be automatically reloaded.  

 - Support for M3U playlists of MP3 files.  (Currently only supports MP3 files)
   (Can also read MP3/M3U from across Samba shares.)

 - Favorites list

 - Save Game management - delete save game files

 - CD-Changing should hopefully be fixed

 - Schmoke and a pancake

What's Not New:

 - Compatibility - this version does not fix or break any games from v2/v3.


Various Important Notes:

=============
Configuration
=============

Almost everything can be changed from the configuration menu.  Here are the
things that require manual modifications to the PCSX.INI file included in
the package:

Samba share name - goes in the [GENERAL] section.  Example:

smbshare=SMB://USERNAME:PASSWORD@COMPUTERNAME/SHARENAME


Screenshot directory - default is E:\SCREENSHOTS - goes in [GENERAL] section
Example:

screenshot_dir=E:\SCREENSHOTS


Skin directory - where skins can be found.  Default is D:\EMUSKINS - goes in
[GENERAL] section.  Example:

skin_dir=D:\EMUSKINS

If you change any of the above items, then you must upload the new PCSX.INI
file to your XBox, load up PCSXBox, then select "Force Reload D:\\*.ini 
Settings" from the Configuration menu.  Please note that this will overwrite
any of the setting changes you might have made after you first loaded
PCSXBox.  


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
 - Once a connection has been made, it should work fine.

NOTE : You both MUST be using the *EXACT* same game and the *EXACT* same
settings.  I would be *extremely* surprised if the PAL version of a game
worked via netplay with an NTSC version of the same game.  Make sure
you are also using the same emulation method (HLE or BIOS).  The CPU
and Graphics settings all must be the same.

The server player is always player 1.  The client player is always player 2.

I don't know how well netplay will work across real networks.  Two xbox's 
on the same intranet work very well, though.

If your connection is lost during gameplay, just wait 30 seconds and
you can return to the game select menu.  (Or you can always reboot...)


=====
SKINS
=====

Instructions for making a new skin:

 - Create a new directory off of your SKINS directory (default skins directory
   is D:\EMUSKINS
 - Place your sound/font/graphic media files in this new directory 
 - Load PCSXBox
 - Select Configuration
 - select Configure Skin
 - Use the menus to select your new media files and change your settings

If you wish to use sprites in your new skin, then read the following:

 - Create a subdirectory off of your new skin directory called SPRITES
   e.g. D:\EMUSKINS\NEWSKIN\SPRITES
 - In this new SPRITES directory create a 0-based numeric directory for
   each sprite you wish to make.  This means that if you have 4 sprites
   you wish to load, the directory names *must* be called 0, 1, 2, and 3.

   Do not call them 1, 2, 3, and 4.  
   Do not call them 0, 3, 5, 6.  
   Do not call them SPRITE1, SPRITE2, SPRITE3, SPRITE4.  

   Inside each of these new directories, you must place the sprite frames.
   Each frame is represented by a BMP, PNG, or JPG file.  The order of the
   frames is given by the filenames.  These filenames must also be named
   with 0-based numbers.  For example, 0.png, 1.png, 2.png.  Look at the
   sprites directory of the included SOTN default skin to see how it works.

Also be aware of memory constraints.  Let's say you have a frame of a sprite
called 0.png.  This picture file is 90 pixels wide and 130 pixels high.
This will get rounded up to a 256x256 pixel 32bit picture.  This means
that it will consume 256x256x4 bytes (256KB) of memory.  If your sprite has
10 frames of animation, that's around 2.5MB of memory.  Keep this in mind
before you make ultra-smooth moving sprites with hundreds of frames of
animation.

If you make/configure a skin and PCSXbox does not load the next time you
play it, then you need to go to the E:\UDATA\ffff051f directory and
search for the PCSX.INI and SKIN_SETTINGS.INI files in one of the
subdirectories.  When you have found them, delete them and PCSXBox should
run fine again, but you'll have to configure your skin again.  The problem
was probably that one of your resources (like a WAV or background file)
was specified incorrectly or was never changed from the old skin.
Carefully look at the SKIN_SETTINGS.INI file in the subdirectory off
of UDATA to make sure that all filenames exist in your skin directory.


=============
Samba/NetBIOS
=============

You'll need a fast network.  :)

I've run some tests, and it seems that if you can transfer data to your
XBox at a rate of 1.5 megabytes per second or faster, then reading
a CD image from across your network should work fine.  If the games
are running really crappy, then your network is probably not fast enough.

To access your Samba share that you defined in your PCSX.INI file (see
configuration section above), first choose "Select a Game" from the main
menu.  Then continue to select the parent directory (always the first
entry in the list) until you get to the screen that displays the 
drives you can access (C, D, E, F, R, X, Y, Z, SMB).  Select the SMB
item and you should now be browsing your Samba shared files.

If you get no items in the SMB listing, then your share is probably not
defined correctly in PCSX.INI. (Did you remember to "Force Reload
of *.ini files" ?  See configuration section.


====================
Controller Remapping
====================

Configuration -> Configure Controllers

There are 32 general/all-purpose emulator "buttons" or actions.  Each of these
buttons can be assigned a specific emulator action.  For example, Emu Button 1
can be Cross, or Square, or L1, or Start, or DPad Down, etc.  These "emu 
buttons" can then be assigned XBox triggers.  For example, Emu Button 1
(which you have mapped to, for example, SQUARE) can be triggered by 
XBox controller button B.  The default button mappings should provide
enough information on how the system works and how it can be used.  


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

D, DR, R, X

D = Down, DR = Down+Right, R = Right, X = Cross button

First, set the delay to a number like 2 or 3.  Then set up the moves.  In
this case, any (or none) of the following might work:

Down
Down+Right
Right
Right+X
Right

OR

Down
Down+Right
Right+x

OR

Down
Down+Right
Right
Right+X
Right+X
Right+X

You will probably need to fine-tune each combo move before it works, but
you'll soon get the knack of it.


================
Graphics Filters
================

As mentioned above, the new filters are :

    - 2xSai
    - Super 2xSai
    - Eagle
    - Super Eagle
    - SuperScale
    - AdvanceMame 2x
    - Simple 2x

Some of them are faster than others, but they're all noticeably slower
than "no filtering".  I am not responsible for your favorite filter
making your game run slower than you'd like.  Turn on frameskipping and be
happy.  :P


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

The smb:\ tells PCSXBox to read from your SMB shared directory.  Do not
put the SMB share definition in the filename.

----------SMB shared filenames are case sensitive!!!---------

==================================================
Command-Line/Auto-Launching and Return to Launcher
==================================================

This section is for the developers of frontends, dashboards, etc.

PCSXBox can be started with parameters to automatically launch a game
at startup.  Example code can be found in the custom_launch_params.cpp file.

There is also example code in that same file that will show you how to 
make PCSXBox load your frontend/dashboard when it exits.


-----------------------------------------------------------------------

PCSXBox - PSX Emulator for XBox v3


What's New :

****************************
* EMU Core Related Changes *
****************************

 - Saves graphics/CPU settings for each game


-----------------------------------------------------------------------

PCSXBox - PSX Emulator for XBox v2

What's New :

****************************
* EMU Core Related Changes *
****************************

 - Used new PCSX 1.5 source code

 - CDDA playback

 - Multi-disc support (go to options menu, then press Y to load new disc)

 - Added more CPU options :
    + Disable XA sound processing
    + Always enable SIO IRQ
    + Black and White movies (speed up movies)
    + Disable CDDA
    + Use CPU interpreter (slower, but possibly more compatible)
    + Always enable SPU IRQ
    + InuYasha Sengoku Battle fix (might fix other games as well)
   

Here's What's New from the v1.5 PCSX sources :
   * Added translation support, thanks to Zydio. 
   * Fixed several compatibility issues. 
   * Improved NetPlay code, added NETsetInfo, thanks to JNS. 
   * Fixed SW Ints, thanks to Xeven. 
   * Fixed Mdecs timing issues, thanks to Xeven. 
   * Fixed a bug related to Memcards in Xenogears. 
   * Decode_XA.c now uses fixed point, 
   * added NEGCON type to plugins.c/PsxBios.c
   * added a mingw32 port (yokota). 
   * Added preliminary MacOSX code (Stefhane Conversy). 
   * Fixed bug in CreateMcd (kitaro). 
   * Added a 'NO PIC' image. 
   * Pcsx now compiles without a recompiler. 
   * Same small speedups. 
   * Fixed RTPS/RTPT SXYP fifo issue, thanks to Xeven. 
   * VSync now has a Start and a End ;), thanks to Pete. 

If anyone is able to successfully fiddle with all the options to get Ape Escape
working on PCSX for Windows (or Linux or any other non-XBox platform), then please 
let me know and I'll look into adding analog support.  

Thanks again to Linuzappz and Pete Bernert for making the source available.
Obviously this port would not exist without these people.  


-----------------------------------------------------------------------

PCSXBox - PSX Emulator for XBox v1

http://xport.xb-power.com
http://www.pcsx.net/

What's New :

****************************
* EMU Core Related Changes *
****************************

 - Emulates Playstation

 - Memory Card manager (select from 10 memory cards)

 - Gameshark code-compatible

 - Gameshark cheat code database with codes for over 1700 games

 - Remappable PSX buttons

 - Supports BIN files or GZIP'd BIN files.  (GZIP is not the same as ZIP)


*****************************
* Interface Related Changes *
*****************************

 - Throttle/speed-up

 - Save states (LTRIGGER+BLACK and LTRIGGER+WHITE)

 - Cheat code searching

 - Background - Thanks to CandyISO for the background image 

 - True Type Font - Thanks to CandyISO for this PSX font

 - MP3 support

 - XPort's Configurable PlayThing :)

-----------------------------------------------------------------------

Press Y from the main menu for help.
Press LTHUMB from main menu for Configuration
Press RTHUMB from main menu to switch between CDROM Drive and Hard Drive
Press LTHUMB during gameplay for the options menu


-----------------------------------------------------------------------


Many thanks go out to the PCSX team for this great emulator and also to
Jens Duttke for his Gameshark cheat code database.

Also thanks to Lantus for helping me with the PAL issues I was having.  
Hopefully PAL users will be able to enjoy this just as much as NTSC users.

Further thanks to CandyISO for providing the background and TTF font.


-----------------------------------------------------------------------


This version does not support real CDs.  There are a different set of technical
hurdles involved with PSX cds than with SegaCD and PCE CD/SCD.  I was finally
able to get the XBox to read XA sectors, but it reads them much too slowly
for anyone to want to play games using it.  (Reads about 2.5KB per second)

For now, create BIN/CUE's of your PSX games and either copy them to your HD or
burn them to DVDR/CDRW.  Your BIN and CUE files should have the same names:

For example:

GAMENAME.BIN
GAMENAME.CUE

is a valid combination and

GAMENAME01.BIN
GAMENAME.CUE

is not.

Furthermore, if you use GZIP to compress your BIN image, you will end up with
a filename like

GAMENAME.BIN.GZ

This means that you need to rename your CUE file to be:

GAMENAME.BIN.CUE

or you could rename the GZ file so that the two files are:

GAMENAME.GZ
GAMENAME.CUE

make sense?


-----------------------------------------------------------------------


A note about GZIP'ing your images.  Yes, they will work, but you will suffer
a performance hit because there's no "true" direct access to any position in
the file.  Let's say the game is reading sectors 1 to 100 - it'll read them
lickity-split, but then when it requests, say, sector 30000 is has to scan through
and do some processing on sectors 100 to 30000 before it can read the data instead
of just jumping directly to that spot and reading.  This is the nature of compression.
No, cacheing of data does not help in this case.  So, in a nutshell, compression
is supported, but I advise against it unless you run from the HD and have replaced
the standard XBox HD with a faster one.

You can make an XBox ISO with a BIN/CUE image on it, burn it to a disc, run PCSXBox 
from the HD, then press the RTHUMB button to get a listing of files on the disc.
This is to make upgrading easier for those who prefer to keep BIN/CUE images
on disc instead of on the HD.  


-----------------------------------------------------------------------


When you select the BIN file to load, you will be presented with an options menu.
You can start the game using one of two different BIOS methods.  Using an actual
BIOS file for the emulation is the most compatible, however it's a little slower
than HLE.  Try both and see which one works best for the game you're playing.


-----------------------------------------------------------------------


There is also a section for changing the graphics options.  If the game you want
to play has graphics problems or isn't displaying graphics (but you can hear sound)
then you might want to try fiddling with some of the graphics options.  There is
also a specific CPU option in this section for fixing Parasite Eve and Vandal 
Hearts 1 and 2.


-----------------------------------------------------------------------


Also on this options menu is the memory card manager.  From this section,
you can change the memory cards that are in slots one and two.  You have ten
different cards you can use.  Please note that changing the card number
while playing a game *does not* switch the actual memory card that the game is
using.  


------------------------------
XPort's Configurable PlayThing
------------------------------

This is part of a project I did many years ago that fiddles with 
curves and trajectories.  I thought it would look nice on the XBox.  You
be the judge.  :)  Move the character with the Left Analog stick and fire
using the B button.
(Hint - fiddle with the X and Y Multipliers on the "Squiggle" effect.)


Stella, Gnuboy, SMSPlus, FCEUltra, HUGO, NeoPop, DGen, Bochs, HUGO-CD, FMSXBox,
Bliss, WinSTon, Gens, Z26, StepmaniaX, PCSXBox....what's next?


Enjoy!
