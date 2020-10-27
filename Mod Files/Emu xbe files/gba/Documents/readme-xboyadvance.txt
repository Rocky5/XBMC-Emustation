XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v24b3

What's New:

Check the Latest-xboyadvance.txt file for the latest update info.  From now on it will have the latest info and this file will contain the changelog/older update information.


-----------------------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v24

http://xport.xbox-scene.com
goto http://www.emuxtras.net/ for latest cheats, rumbles, synopsis and skin updates.

recent changes..

* Whoops didn't quite have "auto configuration" working right.  Fixed now.  ;)  :P

* Keep user within ROM directory tree works now.  Honest!


-----------------------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v23

http://xport.xbox-scene.com
goto http://www.emuxtras.net/ for latest cheats, rumbles, synopsis and skin updates.

recent changes..

*****************************
* Interface Related Changes *
*****************************

* New feature "Seconds before playing movie" determines how long the emu will wait before playing a movie.  The default is half a second.  This will help speed up rom browsing.  Especially useful for people streaming stuff (like movies) across the network.

* If streaming movies from across the network and the user press on the dpad or a, b, x or y the emulator will abort the transfer.  This should help speed up rom browsing and allow the user an "out" especially for the larger movies.

* Fixed an issue with the software filters displaying garbage.

* Activated the "Keep user Within ROM Directory Tree?" which I somehow missed.

* Fixed up the box/cart art position on a few skins.

* Fixed a problem where setting the box/cart orientation was screwed up.

* Fixed the bug that screwed up Gilou's skin to begin with (too weird to explain).  :P


-----------------------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v22

First off...

------------------
Special thanks....
------------------

X-port for porting a great collection of emu's over to the xbox, releasing the source code, and answering my stupid questions.

Atariage (Albert in particular) - For providing a place for me to ramble on. For encouragement in general.

Gilou9999 for a new PM3 skin, synopsis, suggestions, etc.

Comments of support from various interested parties.

If I missed anybody shoot me an email and I'll update this file.


*******************************
* Changes To XboyAdvance Core *
*******************************

* Well none really... :P


*************************
* To Do For XboyAdvance *
*************************
- Eh?


*****************************
* Interface Related Changes *
*****************************

* Given the full "Madmab Edition" treatment.

* New dual-preview skin to support Ressurection Xtra's.  Say thank you to Gilou9999 for the skin.

* Three yummy skins to choose from.  GB, GBA, or GBC.

* "Auto Game Configurations (aka Configuration defaults)" added (see below description).  Use with caution.

* Hopefully addressed weird issues with "Force Reload D:\\*.ini Settings".

* New option to "Keep user Within ROM Directory Tree".  You can find it in "General Settings, Page Two".  Useful for keeping n00bs from getting lost while selecting games.

* Hopefully cleaned up all instances where the current "game select" directory would get trashed.

* Transparency control for keypad and keyboard should now function properly.

* Tightened up the Synopsis parsing code (sorry RessX :( )

* Fixed issue where cycling thru screenshots when non-available would create an infinite loop.


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

* Skin can now have a "Startup Movie" on loading menu. Please use with discretion (no long movies)

* "Startup Movie" can be displayed full screen or in a window. If fullscreen is used the loading menu will not be displayed.

* Transparency for "Startup Movie" can be set as well.

* Moved the network initialization code to run before the loading menu. This moves the delay caused by network init to before the display of the loading menu, not after.

* Files when selecting within a zip are sorted.

* Added a seperate timer for alternating Box/Cart art.

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

* Sprites can now be named for easier manipulation. Directory names must be of the format "0_spritename", "1_spritename", etc. Do not use underscores for the spritename. It is a delimiter.

* Added "Select Skin Configuration Used" and "Save Skin Configuration as" to the "Configure SKin" menu in place of the above moved options. This allows multiple skin configurations in one skin allowing the user more "pre-defined" options on how a skin looks. For example the placement of the games list and the preview screens. Gilou's Dynamic skins really take advantage of this, check 'em out!

* Sprites now show when sizing the preview screens.

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

* select save state screen tells you whether your "loading" or "saving", it also now displays whether a save file has a record session ( R ) associated with it.

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

* (internal) Modified YesNoMenu so it doesn't clear m_menuText.

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

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v21

What's new :

****************************
* EMU Core Related Changes *
****************************

 - Fixed reading of battery saves in GBC games for MBC1, MBC3, MBC5

 - Rewind is too taxing for GBA - it makes it slow down a lot
   Rewind on GB is a little stuttery while rewinding, but the
   gameplay should be fairly smooth while it's storing rewind data.


*****************************
* Interface Related Changes *
*****************************

 - Updated UI core to most recent feature set (rewind, etc)


-----------------------------------------------------------------------


XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v20

What's new :

****************************
* EMU Core Related Changes *
****************************

 - Reverted back to 1.7.2 core

 - Implemented relevant portions of VBAsmooth code

 - Delayed auto-load save states to avoid strange slowdown
   Sometimes when the auto-loading of save states happened, 
   the GBA emulation would be very very sluggish, like the timing
   is off.  Seems the GBA emulation needs to "warm-up" for a second
   before loading the save state.

Notes
-----

Usually newer cores mean better cores, but this does not seem to be the case
with the last 2 releases.  I haven't seen any information that indicates
any games play better with the 1.8 core, (quite the contrary actually) so
I've backported to 1.7.2.

In the last version, I stated that I wouldn't do this, but I was talking
about 1.7 since that seems to be the fastest one.  This version, however,
now appears to be faster than even version 9 thanks to the vbasmooth additions.


-----------------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v19

What's new :


****************************
* EMU Core Related Changes *
****************************

 - Save files are now only moved to their new location once.
   If you wish to use your save games on a previous version of XBoyAdvance, 
   then do the following:

      + Run this version of XBoyAdvance once and then exit back to the dashboard.
      + Copy the save games from their new location back to the old location
        Default new location is E:\SAVES\XBOYADVANCE\<gamename>
        Default old location is E:\SAVES\XBOYADVANCE\
      + Run any previous version of XBoyAdvance and your saves should work again
        and they will never be moved again.

Notes regarding speed/sound stuttering:

The most recent core updates resulted in better compatibility at the expense of
speed.  Full speed GBA emulation on XBox will not be possible unless the
core gets a major overhaul (like coding a highly optimized ASM GBA emulation routine)
which would obviously be very difficult.  Don't expect it from me.

If you are happier with the speed of previous versions, then I suggest you use them.
If there is a feature that you absolutely cannot do without in the newer ones,
then bump up your frameskip setting.  I know you probably don't want to hear that,
but that's the way it is.

No, it's not feasible to implement both old and new core simultaneously.
Trying to compile the old core with all the recent changes would be less work,
but would still be an enormous amount.  This is not something that I'm going to be
doing.


*****************************
* Interface Related Changes *
*****************************

 - Added an option to display FPS on the General Settings page.


-----------------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v18

What's new :

****************************
* EMU Core Related Changes *
****************************

 - Updated to v1.8.0b sources

 - Video lines shifted up to fix problem with lines getting cut off on the bottom.

 - Fixed white strip in upper left corner when emulator plays first game.

 - When you change the save type for GBA, the SRAM file will automatically be deleted.
   Previously, if you did not delete the save file if one was already created,
   it would get read in which caused problems.  This is useful for when you select the
   wrong initial SRAM type for certain games (like Dragon Ball Z).

 - Added locked-aspect-ratio mode when resizing the game screen

 - Implemented a few misc GBA bugfixes from various other sources


*****************************
* Interface Related Changes *
*****************************

 - GUI brought up to date with any missing features

 - Much more robust mp3 playlist features

 - People who cannot display 480i should be able to see something now

 - 480p, 720p  should work fine now

 - Previously, all save state files, config files, sram files were stored in one
   directory.  Now each game gets its own directory.  This will allow for 4096
   games.  4096 is the maximum number of files/subdirectories that can exist in one
   directory on the XBox.  Existing files are moved automatically.

 - Fixed bug with ISO9660 DVD images where information could not be read past the first
   2GB of data on the disc.  The directory would be displayed fine, but when you 
   selected a game that existed past the first half of the disc, it would fail.

 - New option to autoload the last game you played upon launching the emulator
   Find it on the second page of Configuration->General


-----------------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v17

What's new :

****************************
* EMU Core Related Changes *
****************************

 - GBA sound got screwed up again.  Fixed.

-----------------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v16

What's new :

****************************
* EMU Core Related Changes *
****************************

 - Fixed some sound timings in GBMono/GBColor mode.  Frameskip 0 should no longer
   cause the sound to jump from time to time.

 - Fixed a bug where Gameshark/Codebreaker codes were not being reloaded/reinitialized
   when you reload a game image.


-----------------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v15

What's new :

****************************
* EMU Core Related Changes *
****************************

 - Fixed system link emulation
   Games using high-speed transfer like Metal Gear, Zelda, and Mario Tennis
   should work fine now.  (And hopefully all link games work fine now.)

 - Fixed graphics glitches in dual-mode.


-----------------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v14

What's new :

****************************
* EMU Core Related Changes *
****************************

 - Added GB-Mono palettes


*****************************
* Interface Related Changes *
*****************************

 - Fixed bug where screenshots for save states were not being displayed
   on save state menu when the screenshot directory and save game
   directory are on different volumes.  Screenshots that are created
   with save states should only appear on the save/load state menus.
   They should not appear in your regular screenshots directory
   and should not appear on the game-selection menu with the normal
   screenshots.  

 - Added option to disable screenshots with save states

 - Fixed some invalid chars and network issues

 - If you had the option to always bring up the Save/Load state menu
   on and you tried to save/load a state from the Game Utilities menu
   you would be presented with the save/load state menu twice.  This
   is fixed.  ( People using the Game Utilities menu to save/load states
   should probably turn off the "Always show save/load state menu"
   option from the General Configuration settings.)


-----------------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v13

What's new :

****************************
* EMU Core Related Changes *
****************************

 - OK, save states fixed (for real) (well, I'm pretty sure)

 - Sound problems fixed

 - Controller problems fixed

 - Added option to only hear sound from Gameboy #2
   Full set of choices is now "Only #1, Mixed, and Only #2"

 - Changed way saves are stored for Gameboy #2 in dual-gameboy mode.
   You can now, for example, play Pokemon Red and Blue in solo mode
   and when you decide to link them together in dual-mode the 
   solo-mode saves for Gameboy #2 will load up instead of a new set of
   save files.


-----------------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v12

What's new :

****************************
* EMU Core Related Changes *
****************************

 - Fixed bug where loading save states for certain configurations was causing
   XBoyAdvance to crash.


-----------------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v11

What's new :

****************************
* EMU Core Related Changes *
****************************

 - GB/GBC System-Link - Select "Dual Gameboys" from the game configuration screen
   * THIS DOES NOT WORK WITH GBA - ONLY GBMono/GBColor *

 - Rumble support for GBC-Rumble carts - select "Rumble Force" from game
   configuration screen

 - Performed some optimizations to get an average of 5 FPS more on GBA emulation

===============
Important Notes
===============

For system-link games, You can either play the same cart (e.g. Top Gear Pocket) or 
different carts (e.g. Pokemon Blue and Pokemon Red).  If you want to play two different
carts, press X on the first game which will bring up the game configuration menu.
From there, select "Dual Gameboys", then select "Other Gameboy Filename" to select
the second cart image.

Throttle/Fast forward is somewhat jumpy in system-link mode.  This is normal.

Please bear in mind that some system link games (like Pokemon Red/Blue) are a little
flakey when it comes to establishing a connection.  Sometimes if the timing is off
during the initiation, one of the gameboys will freeze on the connection menu.  This
happens with real gameboys, too, so it's actually behaving correctly.  You just need
to be sure to initiate the connection at the same time on both ends.

If you want to try out the new features, Top Gear Pocket supports both rumble and
system link.  


*****************************
* Interface Related Changes *
*****************************

 - Option to select your own flicker filter level 0-5 (default is 5 - max enabled)

 - Added 720x480 and 720x576 modes to Video Configuration menu

 - Added "Force PAL50" option to Video Configuration menu

 - Added option to hide filename extensions - find it on General Settings menu

 - Added option to always bring up save/load state menu on General Settings menu
   If this option is turned on, then whenever you press the in-game button-combo 
   to save/load a state it will display the load/save state menu from which you
   can select the state.  
   If the option is off, then the normal default behavior of immediately
   loading/saving the current state slot will occur.

 - Screenshot saved with each save state

 - Added option to configure text screen size/position for viewing text files

 - Added default text-viewing dir.  Set it via the default directories section.

 - If you select the same text file to view you will be placed back at the position
   you left it.

 - Added Controller -> Joypad Mappings -> UI Mappings option for "Text Browser"
   Assign a key-combo to this function and when invoked, it will take you back
   to the last text file you were browsing at the position you left it.  
   This makes it much easier to jump back and forth from game <-> doc.
   Note - you must first manually select a file to browse from the "Game Utilities"
   menu off of the "In Game Options" menu.

 - When you go up a directory, the cursor is positioned over the directory you just
   exited.


-----------------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v10

http://xport.xbox-scene.com

Thanks to J-Red for a nifty new default skin! (read below)

what's new:

****************************
* EMU Core Related Changes *
****************************

 - Merged in VisualBoy Advance 1.7.2 sources

 - Yes, Hamtaro works now

*****************************
* Interface Related Changes *
*****************************

 - Filenames are no longer converted to all lowercase

 - Option to sort directories to the top or mixed in with the files

 - Fixed bug when selecting multiple buttons in combos

 - Customizable delay between screenshots (e.g. show new screenshot every 3 seconds)

 - View text files - access via Main Menu -> Utilities or during gameplay from
   In-game options -> Game Utilities

 - When the user has edited their INI files (which you should NOT do anymore
   since everything is editable through the menus) and their save directory is
   invalid, they will now be told so when XBoyAdvance starts.

 - Hardware filters (point filtering, bi/tri linear, etc) are now re-initalized
   before each game starts.  The filter was possibly being overridden and never
   enforced after the first time a game is played.

 - Returning to favorites list maintains current position in list

 - Separated "General Settings" into two pages

 - Can now have hi-res modes (e.g. 1080i) initialized at startup

You can overwrite the entire XBoyAdvance tree with this new package, but when you start
it up for the first time, the skin will probably look/behave screwy.  Just go to
Configuration -> Video/Skin Configuration -> Select Skin and reselect the 
default_xboyadvance directory.  Then exit back to the main menu (important to exit to
main menu first) and then restart the emulator.

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


----------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v9

http://xport.xbox-scene.com

what's new:

****************************
* EMU Core Related Changes *
****************************

 - Merged in VisualBoy Advance 1.7 sources

 - Added support for Gameshark v3 codes - not sure if it works 100% though
   (only tested on Castlevania Circle of the Moon and worked fine.)


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

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v8


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

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v7

http://xport.xbox-scene.com

What's New:

****************************
* EMU Core Related Changes *
****************************

 - Fix for Banjo Kazooie - Grunty's Revenge


*****************************
* Interface Related Changes *
*****************************

 - Fixed hiccuping BGM in menus

 - Other UI updates/bugfixes to make it current with standard UI


------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v6

http://xport.xbox-scene.com

What's New:

****************************
* EMU Core Related Changes *
****************************

 - Implemented VisualBoy Advance 1.6a sources


*****************************
* Interface Related Changes *
*****************************

 - 480p, 720p, 1080i support

 - Hardware filtering options : Point, Bilinear, Trilinear, Anisotropic 
    
 - Screen size/position saved with each game

 - Selectable throttle speed

 - Other UI updates/bugfixes to make it current with standard UI


------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v5

http://xport.xbox-scene.com

What's New:

****************************
* EMU Core Related Changes *
****************************

  - Fixed bug with save types.  If you selected a specific save type
    (e.g. EEPROM, etc) it was not being picked up by XBoyAdvance.
    This was previnting the playing of games like DBZ:Goku among others.
    

------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v4

what's New :

*****************************
* Interface Related Changes *
*****************************

 - Fixed support for long filenames (some games would load, e.g. off CD media,
   but save games would not save.  Or some games wouldn't load from network
   share at all.)

 - Bugfixed screenshot display from favorites listing

 - Other bugfixes/UI/Skin changes to bring it up to date with other emu releases


------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v3

What's New :

****************************
* EMU Core Related Changes *
****************************

 - Tactics Ogre now works

 - Reflect mini-game in Wario Ware now works

 - Jumpy graphics in games like Doom and Duke Nukem is fixed

 - Borders now display on Super Gameboy games

 - GB/GBC Cheating now works

 - Cheat code searching in GBA now searches all GBA memory instead of just the
   main portion.  

 - Added Gameshark/Codebreaker Support


*****************************
* Interface Related Changes *
*****************************

 - Won't crash when reading many,many files via Relax share

 - Fixed greater than/less than bug in cheat code searching (they were reversed)


------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v2

What's New :

****************************
* EMU Core Related Changes *
****************************

 - Removed the FPS text (ooops!)

That FPS stuff is actually slightly impacting the actual FPS of the games.
I was using it for testing purposes and I completely forgot about it.

I am aware that certain games like Tactics Ogre crash in XBox and not PC
version.  I'm looking into it.


------------------------------------------------------

XBoyAdvance - GBA/GBC/GB/SGB/SGB2 Emulator for XBox v1

Features :

 - Emulates the Gameboy Advance, Gameboy Color, Gameboy Mono, SuperGameboy 1 and 2

 - Excellent compatibility - ported from VisualBoy Advance v1.5.1

Various Important Notes:

============
Saving Games
============

This is a common pitfall with XBox emulators of consoles that use SRAM.  
If you are playing, for example, Zelda, then when you have saved the game,
you must go back to the game select menu.  

If you just turn off your XBox while you are still playing the game, then
your saves will not be written to the XBox hard drive and it will be like you
never saved your game.


*****************************
* Interface Related Changes *
*****************************

 - ZIP support 

 - Cheat system - Search/Create your own cheat codes 
 
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

 - Samba/NetBIOS sharing support (read NES roms from your PC)

 - Relax Network Sharing 

 - Play MP3 or M3U playlists in the background
   (Can also read MP3/M3U from across Samba shares.)

 - User definable save directory.  If you don't like the default of
   E:\SAVES\XBOYADVANCE you can change it via the XBOYADVANCE.INI file

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

 - Autofire capabilities for any emulator button on any controller

 - One-button combos (define a series of emulator commands to be played
   back when you press a user-definable XBox controller combination.)
   (E.g. Press RTrigger+LTrigger to execute the command string
   A,B,A,B,Up,Down,Left,Right)

 - Traverse any directory on any drive ( Continue selecting the parent
   directory entry on the file selection list to get the drive selection
   list.  Selectable drives are C, D, E, F, R, X, Y, Z, and SMB. 
   R is the CDROM drive.  SMB is the samba share you have defined in your
   XBOYADVANCE.ini file.)  Press Y from any file-listing screen to go up one
   directory level.

 - Save States with 10 save state slots

 - All UI commands (save state, load state, screenshot, etc) can be
   invoked from the Options/Pause menu as well as in-game via your
   customized joypad mappings.

 - Can be invoked from a command-line to directly run a game from a front-end
   or dashboard and bypass the user-selection screens. (Only if the frontend
   or dashboard supports this feature.)

 - Can return to the launching program *if* the launching program supports this
   feature.  For example, if the custom-launch routines are incorporated into 
   a new frontend, that frontend could launch XBoyAdvance and when you exit 
   XBoyAdvance, that frontend can be automatically reloaded.  

 - Cigar and a waffle


=====================
Relax Network Sharing
=====================

The relax sharing setting goes in the [GENERAL] section as follows:

rlxshare=c:\gbaroms@192.168.123.77:8989

Replace 192.168.123.77 with your computer IP address and replace 8989 with the
port where you have Relax running.


============================
Note on Samba/NetBIOS Shares
============================

There are two INI file settings relating to Samba/NetBIOS sharing and they both
reside in the [GENERAL] section of XBoyAdvance.INI:

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
Also be aware that some people have to select their SMB drive in XBoyAdvance a few
times before any files appear.

If it's still not working, then set the nameserver equal to the IP address of
the computer you are trying to reach or set it equal to your NetBIOS name server.
(If you don't know what a NetBIOS name server is, then just set it to the 
IP address of the computer you are trying to reach.)


Also remember that when you make changes to XBoyAdvance.INI, you have to do a 
"Force Reload of D:\*.INI" from the Configuration Menu or else the changes
you made to XBoyAdvance.INI will not be loaded.  


=============
Configuration
=============

Almost everything can be changed from the configuration menu.  Here are the
things that require manual modifications to the XBoyAdvance.INI file included in
the package:

Samba share name - goes in the [GENERAL] section.  Example:

smbshare=SMB://USERNAME:PASSWORD@COMPUTERNAME/SHARENAME


Screenshot directory - default is E:\SCREENSHOTS - goes in [GENERAL] section
Example:

screenshot_dir=E:\SCREENSHOTS


Skin directory - where skins can be found.  Default is D:\EMUSKINS - goes in
[GENERAL] section.  Example:

skin_dir=D:\EMUSKINS


Save directory - this is where you want all your saved games to be stored.
Default is E:\SAVES\XBOYADVANCE.  Goes in [GENERAL] section.  Example:

save_dir=E:\SAVES\XBOYADVANCE


The default ROM directory INI setting goes in the [GENERAL] section as follows:

rom_dir=e:\games\gbaroms


If you change any of the above items, then you must upload the new XBoyAdvance.INI
file to your XBox, load up XBoyAdvance, then select "Force Reload D:\\*.ini 
Settings" from the Configuration menu.  Please note that this will overwrite
any of the setting changes you might have made after you first loaded
XBoyAdvance.


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
 - Load XBoyAdvance
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

If you make/configure a skin and XBoyAdvance does not load the next time you
play it, then you need to delete the E:\SAVES\XBOYADVANCE\XBOYADVANCE.INI and
E:\SAVES\XBOYADVANCE\SKIN_SETTINGS.INI files.  XBoyAdvance should work fine again,
but you'll have to reconfigure your skin.  The problem was probably
that one of your resources (like a WAV or background file) was specified
incorrectly or was never changed from the old skin.  Carefully look at the 
E:\SAVES\XBOYADVANCE\SKIN_SETTINGS.INI file to make sure that all filenames exist 
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

The smb:\ tells XBoyAdvance to read from your SMB shared directory.  Do not
put the SMB share definition in the filename.

----------SMB shared filenames are case sensitive!!!---------


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

XBoyAdvance can be started with parameters to automatically launch a game
at startup.  Example code can be found in the custom_launch_params.cpp file.

There is also example code in that same file that will show you how to 
make XBoyAdvance load your frontend/dashboard when it exits.


Stella, Gnuboy, SMSPlus, FCEUltra, HUGO, NeoPop, DGen, Bochs, HUGO-CD, FMSXBox,
Bliss, WinSTon, Gens, Z26, StepmaniaX, PCSXBox, XBoyAdvance....what's next?


Enjoy!
