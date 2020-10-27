MednafenX-NES - NES Emulator for XBox v15

What's New:

Check the Latest-NES.txt file for the latest update info.  From now on it will have the latest info and this file will contain the changelog/older update information.

-----------------------------------------------------------------------

MednafenX-NES - NES Emulator for XBox v14

v14 never saw the light of day... 

http://mednafen.com/
http://xport.xbox-scene.com

First off...

-------------------------
Special thanks....
-------------------------

X-port for porting a great collection of emu's over to the xbox, releasing the source code, and answering my stupid questions.

Atariage (Albert in particular) - For providing a place for me to ramble on. For encouragement in general.

Gilou9999 for a new PM3 skin, synopsis, suggestions, rumble setups, etc.

Wimpy for giving us a home and irc channel on the web.

Megaman_? for a mega cheat code database.

BombBloke for scripts that make life easier.

Cbagy for suggestions for the Skin and showing me how to create good quality game previews.  More of that to come, and hopefully some neat skin stuff!

Nate1579 for some XBE Icons.

Kenshiro for ensuing hilariousness.

Waal, Bigby, Carnage By Bob, Stupot for motivating me to get working on lesser known systems.

Comments of support from various interested parties.

If I missed anybody shoot me an email and I'll update this file.


*********************************
* Changes To MednafenX_NES Core *
*********************************

* "Auto Game Configurations (aka Configuration defaults)" added (see below description).

* Support for mappers 2 (Best Of The Best Karate, Paperboy II (no more grey screen)) and 138 (Crimebusters).  Thanks to XTecuterX73.


***************************
* To Do For MednafenX_NES *
***************************

- Get the blarrg NTSC filter going?


*****************************
* Interface Related Changes *
*****************************

* Accurate Screen Pixel Ratio option added (see "http://fancyxbox.info/?doc=1&secao=screen" for more into) per gilou9999's suggestion.  Some numbers are still a WIP.  Go into Game/Text Screen Size Position" and select "Set Game Screen to Accurate Screen Pixel Ratio".  The emu will ask you if you wish to turn off software/hardware filters and flicker filter.  This is recommended for the most accurate screen.  You'll still have to manually adjust the image on the Y axis.  We can't do everything for you, ya lazy bum!

* Added an option to display a "Static" video if no movie found.  Can be set to yes or no.  Static file must be named "Tv Static.xmv" and placed in the emu's "backgrounds" directory.

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

MednafenX-NES - NES Emulator for XBox v13b (Public Beta)

Possibly skipped version number?


-----------------------------------------------------------------------
MednafenX-NES - NES Emulator for XBox v12.02b (Public Beta)


http://mednafen.com/
http://xport.xbox-scene.com

Special thanks..

Gilles9999 for giving the project legs when it needed them.  

Frank Morris for some suggestions.

Cospefogo.. For a spankin' new default keyboard look.

Mega_Man_(?) for being crazy enough too volunteer to enter tons of gamegenie codes.  Only (#-J) right now.

Gilles for some rumble codes.

Nes6502 for the proposal on the Synopsis format

Thanks to all involved for doing the missing movie previews and filling out the Synopsis for the NES.  Rx, Gilles, Justgoonies, and Mega_Man_(?).

XTecuterX73... Where are you man?

Anybody else my brain dead self forgot.

What's New:

****************************
* Changes to Mednafen Core *
****************************

* Modified the rewind controls to use the now standard method of mapping used by all other x-port emus.

* Customized the default mappings for emu (Only NES related mappings are displayed).

* mp3CDDA and CDDA have their own volume control now and are saved with each game configuration (only affects MednafenX_PCE).

- Still waiting on some Mapper changes by XTecuterX73.  But this is beta, so no big hurry.


*****************************
* Interface Related Changes *
*****************************

* Dynamic Skin with Dual Screenshot Movie Previews.

* DYNAMIC MEDNAFENX PM3 skin by Gilou9999 (read the readme.txt in his skin folder).

* There is an alternate synopsis background in the skin directory.  Feel free to try it (just rename it to "synopsis.jpg)

* Lots of interface updates.

* This is mostly an interface update with all the changes I've made over the past few months.  It's basically a public beta to (hopefully) drum up some interest and give everyone a taste of what's ahead.  

If you have any questions head over to that thread, or the official release thread.  I have a few tips for working with the .dat files.


* The much talked about "Game Synopsis!".  See http://forums.xbox-scene.com/index.php?showtopic=663137

* Synopsis.  Press down on right stick to see a description, tips, hints, of the highlighted game. 

* Synopsis background can be stored in the skins "backgrounds" directory or the emulators "background" directory.  Skin directory is searched first.

* Help screen support for game select screen and text browser (try pressing start).  (Graphics provided by Gilou9999)

* The two help menu's and synopsis background are now skin specific. So if the emulator finds the files in a directory called "backgrounds" in the skin directory it will use them. Otherwise it looks in the emulators directory for a "backgrounds" directory. If no synopsis background is discovered the emulator will use the default "other" panel.  The Synopsis background is named "synopsis.jpg".  The help files are named "Game Selection Menu.jpg" and "View Text File.jpg"

* Box/Cart art can be displayed in seperate window. Box/Cart art is autodetected based on size (only in "old screenshots" directory).

* New option to "Force Game Screen Size/Position". There are two configurable screensizes. (To deal with multi-core systems like MekaX and XboyAdvance). This will be useful when switching from HDTV to SDTV or vice versa. It will save the user the trouble of resizing the screens for something that is likely temporary.

* Numerous changes to menu system see below (current menu configuration layout)

* Skin sprites can now be named for easier manipulation. Directory names must be of the format "0_spritename", "1_spritename", etc. Do not use underscores for the spritename. It is a delimiter.

* Added "Select Skin Configuration Used..." and "Save Skin Configuration as..." to the "Configure SKin" menu. This allows multiple skin configurations in one skin allowing the user more "pre-defined" options on how a skin looks. For example the placement of the games list and the preview screens. Gilou's Dynamic skins really take advantage of this, check 'em out!

* Skin previews when selecting a skin or a skin configuration. The files must be in the "preview" directory within the skin directory. "preview.jpg" for the 4-in-1 pic, and "configuration name.jpg" for the rest.

* Removed popup message from "Configure Skin/Select Skin" and replaced the top line with the text "Press Start To Select Directory". This displays on all "change directory" menu screens.

* Changed "Seconds before auto-advancing Screenshot" to "Seconds Before Auto-Advancing Artwork".

* Changed "offset X" and "offset Y" to "Offset X (left/right)" and "Offset Y (up/down)" in the Sprite Settings menu for those who are confused by cartesian coordinates.  ;)  :P

* Sprites now display when sizing the preview screens.

* Screenshot, movie, and gamebox preview transparency's now working properly.

* Removed "Sprite Settings" option from "Pop-up Configure Skin Menu"...  Fixed bug caused by doing this.  :P

* Changed directory browse code so it can be told to "ignore screenshots/streaming media"

* Changed volume increment/decrement on mp3 player and game sound.  Set to 10 for now.

* User can now change music volume in the game select/help/and synopsis screen.

* Zip selection screen now sorts the zip contents. Helpful in Computer emulators in which some zips may contain "multiple disks"!

* Unmapped all the default UI mappings except for "in game menu", "keyboard", and "fast forward".

* Modified the autolaunch (from dash) so that it jumps straight into the emulated game.  Be sure to set the option to "Exit the emulator on game exit after autostart".

* Fixed a bug where the gamescreen would get blurry after changing video options.

* Fixed a bug where the xbox would lock-up when setting 10x11 mode in non 480 modes.

* Improvements to the cheat database system.  Changed menu options to "Search Cheat Database for Codes" and "Save Cheat Codes To Custom DB".

* Search can handle multiple CRC's for games that use same cheat codes but have different CRC's.  (Be careful with this).

* Search and save database options modified to be able to handle GameGenie codes in addition to Gameshark codes.

* Fixed a bug that would cause "Add new code" to default to GameGenie when it should be Gameshark.  Use "Add New Game Genie Code" at the bottom for GameGenie codes.

* completely changed around the screenshot directory structure to accomodate the ability to display both screenshots and cart/box art at the same time.  (Don't worry the old screenshot directories will still work until you are ready to switch).

* Text file directory retired and renamed to "Media" directory.  Screenshots (in the menus) renamed to "old screenshots" to reduce confusion.

Note: Point the media directory to the directory that contains your "artwork" folder.

New format as follows

/usernamedfolder/NES/artwork/box front/
/usernamedfolder/NES/artwork/box back/
/usernamedfolder/NES/artwork/cart/
/usernamedfolder/NES/artwork/titles/
/usernamedfolder/NES/artwork/action/
/usernamedfolder/NES/artwork/misc01/
/usernamedfolder/NES/artwork/misc02/
/usernamedfolder/NES/artwork/misc03/
/usernamedfolder/NES/artwork/misc04/
.......
/usernamedfolder/NES/artwork/misc99/
and so on

Pictures are displayed in the following order. Title, Action, Misc01-Misc??, and then it switches to the old dated ( ) screenshot directory. Be sure to remove your old screenshots once you've switched over or just point the screenshot directory to somewhere else.

It alternates between Boxart and Cartart in the area specified for them.

left/right on left analog to change screenshots.

* Changed the way the movies directory is handled.  The emulator no longer adds the emu name to the path (ex: NES or "f:\movies\NES\").  So you'll either need to move your movies down a directory or just point the movies directory to where the movies are located.

* After changing the media directory the emu will ask the user if they want to point the movies directory to "media\movies".

* Tinkered around with volume control options for mp3 (music), in games sound, and CDDA.  0 (no volume) thru 100 (full volume). Although technically the volume is no longer audible well before it hits 0.

on normal game select menu...

Right analog stick left/right - music volume
Right analog stick up/down - movie volume
Left analog stick left/right - change pictures
Left analog stick up/down - nothing

On favorites menu...

Right analog stick left/right - music volume
Right analog stick up/down - movie volume
Left analog stick left/right - change pictures

In game menu now shows current Game (SFX), mp3CCDA and CDDA volume (if applicable).

Right analog stick left/right - game volume
Right analog stick up/down - music volume
Left analog stick left/right - CDDA volume
Left analog stick up/down - mp3CDDA volume

------------------------------------
Sorta implemented features (hidden).
------------------------------------
(Try selecting .xmv and .jpg/.png files while in the text file browser.)

* Ability to display documentation (.jpg)
* Commercials - Framework put in place for "mediabrowser"

------------------------------------
Current menu configuration layout..
------------------------------------

MAIN MENU

Select Game From Favorites
Select Game
Configure Skin

---->Select Skin
---->Save Skin Configuration As
---->Load Skin Configuration
---->Skin Editor

---->---->Game Select Menu Settings
---->---->---->Screenshot/Movie Preview Settings
---->---->---->---->Show Screenshots? Yes/No
---->---->---->---->Show Movie? Yes/No
---->---->---->---->Play Sound From Movie? Yes/No
---->---->---->---->[Screenshot/movie/boxart] Size/Position
---->---->---->---->[Screenshot/movie/boxart] Transparency
---->---->---->---->Seconds Before Auto-Advancing Artwork
---->---->---->---->Auto-Screenshot Capture Delay - 
---->---->---->---->Show Screenshots While Scrolling

---->---->---->Sprite Settings
---->---->---->Background Settings
---->---->---->Text Settings

---->---->Game Screen Size/Position
---->---->---->Set Game Screen Size/Position
---->---->---->Set Text Screen Size/Position
---->---->---->In Game Options Screen Size/Position
---->---->---->Force Game Screen Size/Pos (0) - Yes/No
---->---->---->Force Text Screen Size/Pos - Yes/No

---->---->General Settings
---->---->Main Menu Settings
---->---->Popup Menu Settings
---->---->Loading Screen Menu Settings
---->---->All 'Other' Menu Settings
---->---->Show Available Memory

---->Video Mode (For setting screen resolution)
---->Start With Music: Yes/No (maybe change to Music: on/off)
---->Favorites Screen: Regular/Enhanced
---->Start Screen: Favorite Select/Game Select/Main Menu 

Configuration

---->Change Default Directories
---->Controller Configuration
---->Video Configuration

---->---->Video Mode - (480i,720i,720p, etc) [or leave/dup this in skin configuration)
---->---->Screenshot/Movie Preview Settings
---->---->---->Show Screenshots? Yes/No
---->---->---->Show Movie? Yes/No
---->---->---->Play Sound From Movie? Yes/No
---->---->---->[Screenshot/movie/boxart] Size/Position
---->---->---->[Screenshot/movie/boxart] Transparency
---->---->---->Seconds before auto-advancing Screenshot -
---->---->---->Auto-Screenshot Capture Delay -
---->---->---->Show Screenshots While Scrolling - Yes/No

---->---->Game Screen Size Position
---->---->---->Set Game Screen Size/Position #
---->---->---->Set Text Screen Size/Position
---->---->---->In Game Options Screen Size/Position
---->---->---->Force Game Screen Size/Pos (0) - Yes/No
---->---->---->Force Text Screen Size/Pos - Yes/No

---->---->Other Video Configurations
---->---->---->Xbox Hardware Filtering -
---->---->---->Software Filter -
---->---->---->Force PAL50 Mode (PAL only) - Yes/No
---->---->---->Flicker Filter Level
---->---->---->Soften Display - Yes/No
---->---->---->10x11 Pixel Aspect Ratio - Yes/No
---->---->---->Move menu text (maybe this should be moved into skin settings)

---->General Settings
---->Network/Netplay Options

Utilities
---->Save Game Management
---->Browse Screenshots
---->View Text File
---->Help

Return to Launcher

------------------------------------
Current menu configuration layout..
------------------------------------

MAIN MENU

Select Game From Favorites
Select Game
Configure Skin

---->Select Skin
---->Save Skin Configuration As
---->Load Skin Configuration
---->Skin Editor

---->---->Game Select Menu Settings
---->---->---->Screenshot/Movie Preview Settings
---->---->---->---->Show Screenshots? Yes/No
---->---->---->---->Show Movie? Yes/No
---->---->---->---->Play Sound From Movie? Yes/No
---->---->---->---->[Screenshot/movie/boxart] Size/Position
---->---->---->---->[Screenshot/movie/boxart] Transparency
---->---->---->---->Seconds Before Auto-Advancing Artwork
---->---->---->---->Auto-Screenshot Capture Delay - 
---->---->---->---->Show Screenshots While Scrolling

---->---->---->Sprite Settings
---->---->---->Background Settings
---->---->---->Text Settings

---->---->Game Screen Size/Position
---->---->---->Set Game Screen Size/Position
---->---->---->Set Text Screen Size/Position
---->---->---->In Game Options Screen Size/Position
---->---->---->Force Game Screen Size/Pos (0) - Yes/No
---->---->---->Force Text Screen Size/Pos - Yes/No

---->---->General Settings
---->---->Main Menu Settings
---->---->Popup Menu Settings
---->---->Loading Screen Menu Settings
---->---->All 'Other' Menu Settings
---->---->Show Available Memory

---->Video Mode (For setting screen resolution)
---->Start With Music: Yes/No (maybe change to Music: on/off)
---->Favorites Screen: Regular/Enhanced
---->Start Screen: Favorite Select/Game Select/Main Menu 

Configuration

---->Change Default Directories
---->Controller Configuration
---->Video Configuration

---->---->Video Mode - (480i,720i,720p, etc) [or leave/dup this in skin configuration)
---->---->Screenshot/Movie Preview Settings
---->---->---->Show Screenshots? Yes/No
---->---->---->Show Movie? Yes/No
---->---->---->Play Sound From Movie? Yes/No
---->---->---->[Screenshot/movie/boxart] Size/Position
---->---->---->[Screenshot/movie/boxart] Transparency
---->---->---->Seconds before auto-advancing Screenshot -
---->---->---->Auto-Screenshot Capture Delay -
---->---->---->Show Screenshots While Scrolling - Yes/No

---->---->Game Screen Size Position
---->---->---->Set Game Screen Size/Position #
---->---->---->Set Text Screen Size/Position
---->---->---->In Game Options Screen Size/Position
---->---->---->Force Game Screen Size/Pos (0) - Yes/No
---->---->---->Force Text Screen Size/Pos - Yes/No

---->---->Other Video Configurations
---->---->---->Xbox Hardware Filtering -
---->---->---->Software Filter -
---->---->---->Force PAL50 Mode (PAL only) - Yes/No
---->---->---->Flicker Filter Level
---->---->---->Soften Display - Yes/No
---->---->---->10x11 Pixel Aspect Ratio - Yes/No
---->---->---->Move menu text (maybe this should be moved into skin settings)

---->General Settings
---->Network/Netplay Options

Utilities
---->Save Game Management
---->Browse Screenshots
---->View Text File
---->Help

Return to Launcher


-----------------------------------------------------------------------

MednafenX-NES - NES Emulator for XBox v10.5pb

Well I released this because it was the one x-port "Medna" emu that didn't make the last round of releases by Nes6502.  Special thanks to Nes6502 for his proof of concept.

----------------

Added support for video previews. Video previews must be in xmv format . Users running at 1080i need to adjust the font for the game select screen to the following:

Game Select Settings
Max Text Width: 220
Number of Lines: 10
Font Size: 20
Line Height: 32 

The Xbox does not have enough CPU power to render several true type
fonts at 1080i and update the video preview. This does not apply to
480i/p or 720p.

----------------

Because of this, though. I had to make numerous changes to the x-port interface. Here is what they were.

Created a new configuration menu called "Screenshot/Movie Preview Configuration". It now contains the new Movie Preview settings as well as all the screenshot related settings that USED to be in "General Settings".

The "Screenshot/Movie Preview Configuration" is as follows.

    * Show Screenshots? No, Screenshots Only, Movies Only, Screenshots 1st- Then Movies, Movies 1st- Then Screenshots.
    * Play Sound From Movie? Yes, No
    * Seconds before auto-advancing screenshot - #
    * Auto-Screenshot Capture Delay - #
    * Show Screenshots While Scrolling? Yes, No

These were removed from the "General Settings Menu" and I shuffled around the "General Settings Menu" to better balance things.

You can set the movie/previews directory in the "Change Default Directories" section. The default location is "D:\VIDEOS\ in order to save confusion with the other two recent Medna releases.  However if you point the movie/previews directory to any drive other than "D:" it changes to the standard x-port emu format of "E:\VIDEOS\EMU_NAME".  That way if you want to you can store all your movies in the same directory and avoid mix-ups with other x-port emu's as they are released with movie preview.

The movie name has to be exactly the same as the ROM name. Only one movie per game.

All settings are saved in the emu_name.ini file.


-----------------------------------------------------------------------

MednafenX-NES - NES Emulator for XBox v9

This is a recompiled version of the latest mednafenx with a correction to a typo in the last release that disabled the ability to load custom palettes.

This version of mednafenx also includes the correct nes color palette. (this is enabled by default) You can always autogenerate your own palette or load your own palette.  Included in this release is the old palette and the RGB palette. The RGB palette is colors that can be output by a svideo modded nes. 

Mednafenx-nesV9 (Fixed)

ENJOY!! please post any issues on the thread located in xport projects. 

Compiled by madmab
brought to you by XtecuterX73 and Madmab :)


-----------------------------------------------------------------------

MednafenX-NES - NES Emulator for XBox v9

http://mednafen.com/
http://xport.xbox-scene.com

What's New:

 - Update UI core to most recent feature set


-----------------------------------------------------------------------

MednafenX-NES - NES Emulator for XBox v8

http://mednafen.com/
http://xport.xbox-scene.com

What's New:

****************************
* EMU Core Related Changes *
****************************

 - Slight speed improvement - about 3-5fps

 - Fixed "Clip sides" bug

 - Screen was missing one line of width and height - fixed

 - More intuitive way to reset the overridden mapper#


*****************************
* Interface Related Changes *
*****************************

 - Test pattern for game screen resizing
   Toggle between game screen and test pattern
   Hide text while resizing
   Change text color on resizing screen
   Change size of test pattern on game screen resizing


-----------------------------------------------------------------

MednafenX-NES - NES Emulator for XBox v8

http://mednafen.com/
http://xport.xbox-scene.com

What's New:

****************************
* EMU Core Related Changes *
****************************

 - Override mapper# and mirroring from game configuration menu

 - Added button definitions for PowerPad 1-12/Family Trainer 1-12

 - Added button definitions for HyperShot 1/2, Run/Jump

 - Added button definitions for QuizKing Buzzers 1-6

 - Mapper fixes :

    43 - Fixed mirroring problem and reset, fixes the buggy games, 
         menu is still little off
   187 - King of Fighters 96 [p1]
         Sonic 3D Blast 6 (Unl) [h1]
         Street Fighter Alpha Zero 97
         Street Fighter Zero 2 [p1]
   196 - Mapped to mapper #4 - for Magical Doropie (J)(TEngl1.00)
   225 - Fixed mirroring problem and reset, fixes the buggy games
   226 - Fixed mirroring problem and reset, fixes the buggy games
   227 - Fixed mirroring problem and reset, fixes the buggy games
   229 - Fixed mirroring problem and reset, fixes the buggy games

 - Mapper additions:

    50 - Super Mario Bros 2 (different levels) (Unl) [p2]
    57 - 54-in-1 (Game Star - GK-54) (Unl)
         6-in-1 (Game Star - GK-L01A) (Unl)
         6-in-1 (SuperGK-L02A) (Unl)
    58 - 68-in-1 (Game Star - HKX5268) (Unl)
    61 - 20-in-1 (Mapper 61) (Unl) [p1]
    62 - Super 700-in-1 (Unl) 
   188 - Karaoke Studio (J)
         Karaoke Studio Senyou Cassette Vol 1 (J)
         Karaoke Studio Senyou Cassette Vol 2 (J)
   200 - 1200-in-1 (Alt Games) [p1]
   230 - 22-in-1 (Unl) [p1]
   231 - 20-in-1 (Mapper 231) (Unl) [p1]
   241 - Study and Game 32-in-1 (Unl) (Keyboard)
         Edu (Asia) (Keyboard)


-----------------------------------------------------------------

MednafenX-NES - NES Emulator for XBox v7

http://mednafen.com/
http://xport.xbox-scene.com

What's New:

****************************
* EMU Core Related Changes *
****************************

 - Added mappers (These are all the mappers that FCEUltraX supported that MednafenX 
                  did not - so MednafenX can now do everything that FCEUltraX did
                  plus much more.)
   40     ( Super Mario Bros 2. J [p1] - Lost Levels FDS converted to INES format)
   43     ( 150-in-1) 
   83     ( dragon ball z 4-in-1) buggy
          ( Fatal Fury 2 ) buggy
          ( World Heroes 2) buggy
   91     ( Street Fighter III [p1])
   161    ( same as mapper #1, MMC1 - Legend of Zelda, Metroid, etc)
   225/255( 64-in-one),  same games buggy buggy (1942), galaga, galaxian
   226    ( 76-in-1) some games buggy
   227    ( 1200-in-1)
   229    ( 43-in-1)
   240    ( Jing Ke Xin Zhuan) 
          ( Sheng Huo Lie Zhuan) 

 - Select a custom palette file


*****************************
* Interface Related Changes *
*****************************

 - Trigger rumble via memory now has the following options:
     + trigger when memory value changes
     + trigger when memory value decreases
     + trigger when memory value increases
     + trigger when memory value =  specified value
     + trigger when memory value != specified value
     + trigger when memory value >  specified value
     + trigger when memory value <  specified value

 - Jump to Memory Dump from cheat code value

 - More searchable memory locations for creating cheat codes

NOTE THAT THE PREVIOUS RUMBLE SETTINGS WILL NEED TO BE REDONE.

The new rumble settings are incompatible with the previous version.
You must redo them.


-----------------------------------------------------------------

MednafenX-NES - NES Emulator for XBox v6


http://mednafen.com/
http://xport.xbox-scene.com

What's New:

*****************************
* Interface Related Changes *
*****************************

 - Trigger rumble when game memory changes
   Idea shamelessly lifted from nes6502  :)

 - Trigger rumble when pressing emulator button

 - View all potential cheat code items
   Cheat Codes -> View Current Potential Matches
   Cheat Codes -> Continue Search for Cheat Code -> View List of Matches

 - View memory dump for cheat codes
   Cheat Codes -> View Memory Dump
   <get to list of potential cheat code items> -> <select an item> -> 
      Jump to this Position in Memory Dump

 - Poke values into memory
   <get to list of potential cheat code items> -> <select an item> -> 
      Poke value into selection
   <get to memory dump> -> <select line> -> <select byte> -> Poke

 - Added analog stick sensitivity configuration.  Use this to 
   custom define your analog stick deadzones if you are experiencing
   drifting:
   Configuration -> Controller Configuration -> Controller # ->
   Change Analog Stick Sensitivity


Important Notes
===============

Trigger Rumble by Pressing Emulator Button
------------------------------------------

To assign rumble to an emulator button, go to Configuration ->
Controller Configuration -> Controller # -> Change Rumble Config

Select the emulator button, then configure the motor intensities and
durations.  "Continuous" means that the motor will stay on for as
long as you have the button pressed.  If "continuous" is not set, then
the motor will stay on for the time specified in the duration fields.


Trigger Rumble when Game Memory Changes
---------------------------------------

This works based off of the cheat-code system.  Let's say you are playing
a beat-em-up type game and your player has 5 slots of health.  First, you
will want to create a code that represents the players health.  Refer to
"Cheating System - How To Make Your Own Cheat Codes" in this document for
an explanation of how to create cheat codes.  Once you have the cheat code
set up that represents the health of the player, go to:

Cheat Codes -> List Cheat Codes -> <select player health code> ->
Configure Rumble

From here, you can set up the rumble values (same as with "Trigger Rumble
by Pressing Emulator Button).  When you're done with that, go to:

Cheat Codes -> List Cheat Codes -> <select player health code> ->
Rumble Enabled On

to select which controller will get the rumble activated.  You can also
choose to have the rumble activate on all of the controllers.  Then go to:

Cheat Codes -> List Cheat Codes -> <select player health code> ->
Rumble When

To select if you want the rumble to trigger when the value changes, decreases
or increases.  In this case, we'll want to set it to "Value Decreases"

Now when your health goes down, the rumble will activate.


-----------------------------------------------------------------

MednafenX-NES - NES Emulator for XBox v5


http://mednafen.com/
http://xport.xbox-scene.com

What's New:

****************************
* EMU Core Related Changes *
****************************

 - Added game configuration option : "Hack Fix"
   If your game is not working, try toggling this.


-----------------------------------------------------------------

MednafenX-NES - NES Emulator for XBox v4

http://mednafen.com/
http://xport.xbox-scene.com

What's New:

*****************************
* Interface Related Changes *
*****************************

 - Yet another possible fix for garbled video on 1.6 xbox's


-----------------------------------------------------------------

MednafenX-NES - NES Emulator for XBox v3

http://mednafen.com/
http://xport.xbox-scene.com

What's New:

****************************
* EMU Core Related Changes *
****************************

 - Games with battery backup RAM (e.g. Zelda) would save the first
   time you exit the game, but then would fail upon subsequent saves
   until the emulator was restarted.  Fixed.

 - When using the USB mouse or joystick to control the light gun,
   pressing one button will fire normally and pressing the other
   button will automatically fire off-screen (cursor automatically
   positioned to upper left corner)


*****************************
* Interface Related Changes *
*****************************

 - Yet another possible fix for garbled video on 1.6 xbox's


-----------------------------------------------------------------

MednafenX-NES - NES Emulator for XBox v2

http://mednafen.com/
http://xport.xbox-scene.com

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

   Furthermore, enabling rewind in FDS games will result in extremely poor
   performance due to the fact that FDS games require a lot of horsepower
   to run.  At least it's full speed in regular and VS UniSystem games.

 - Should no longer crash in 1080i mode (memory limitation issue)

 - Error messages when loading games should provide meaningful feedback
   as to why it has failed.

 - Game Genie implemented.  You don't have to reload the game if you are
   adding or enabling game genie codes, but if you want to disable or
   delete one, you'll have to reload the game.  


*****************************
* Interface Related Changes *
*****************************

 - Made main menu have 7 lines

   Go to Configuration -> Video/Skin Configuration -> Select Skin 
   and reselect the default skin.

   Or, go to Configuration -> Video/Skin Configuration -> Configure Skin ->
   Main Menu Settings -> Text Settings and set 
   Number of Lines Per Page = 7
   Line Height = 19

 - Possible fix to garbled screen upon starting

 - Filename Filter
   Go to Configuration -> General Settings -> Page 2 -> Edit Filename Filter
   The extensions you enter will be the only ones that appear in your
   game listings.  

 - Updated text file viewer :
   Press LTHUMB to change the font height
   Press RTHUMB to bring up the screen-resize menu
   Move LTHUMB left/right, RTHUMB left/right to move the text left/right
   and extend the viewing area
   Move LTHUMB up/down to scroll text up/down

 - Move DPAD left/right on save state slot to inc/dec slot number

 - Use USB mouse to control light gun


-----------------------------------------------------------------

MednafenX-NES - NES Emulator for XBox v1

http://mednafen.com/
http://xport.xbox-scene.com

Thanks to J-Red for an excellent skin! 

Features :

 - Emulates NES/Famicom Disk System/VS UniSystem

 - Excellent compatibility - ported from Mednafen

Default ROM dir is D:\NESROMS

===============
Important Notes
===============

--------
Palettes
--------

Try toggling "Autogenerate NTSC Palette" from the game configuration screen
if you are unhappy with the default palette.

-----------------
Light Gun Support
-----------------

My light gun no longer works for some mysterious reason, so I haven't 
tested the light gun functionality.  It *should* work, though.  

To use the lightgun, first go to Main Menu -> Configuration -> 
Controller Configuration -> Configure Light Gun

From that menu, calibrate the light gun.  You can also choose to have an 
on-screen target to help you while playing lightgun games.

When you select a game to play, you are given the configuration options. 
(You can also press X to select a game to force re-configuration.)
Be sure to change either Controller 1 or Controller 2 from Gamepad to 
Zapper or else you will have no ability to use lightguns in the
game you've selected.

-------------------
Famicom Disk System
-------------------

The WHITE button will Load or Eject the current disk
The BLACK button selects the disk side to use

If you are trying to play an FDS game and it seems to be waiting forever
with some japanese text on the screen, it's probably waiting for you to
flip the disk.  To do so, press WHITE (eject), BLACK (select side), WHITE (load)
and it should continue. 

------------
VS UniSystem
------------

Press the Y button to insert a coin.

Here is a good website to see what the DIP switches do in various VS
UniSystem games:

http://www.solvalou.com/subpage/arcade_dips/V


*****************************
* Interface Related Changes *
*****************************

 - ZIP support

 - Loads of hardware/software filters and video options to tweak

 - Cheat system - Search/Create your own cheat codes (see notes)
 
 - Favorites list

 - Save states

 - Light gun support (see notes)

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
 - Load MednafenX-NES
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

MednafenX-NES can be started with parameters to automatically launch a game
at startup.  Example code can be found in the custom_launch_params.cpp file.

There is also example code in that same file that will show you how to 
make MednafenX-NES load your frontend/dashboard when it exits.

Stella, Gnuboy, SMSPlus, FCEUltra, HUGO, NeoPop, DGen, Bochs, HUGO-CD,
FMSXBox, Bliss, WinSTon, Gens, Z26X, StepmaniaX, PCSXBox, XBoyAdvance,
DOSXBox, AtariXLBox, MirrorMagicX, KoboX, MaelstromX, MarblesX, Vice64X,
Vice20X, VicePETX, KegsX, XPired, AdamX, WonderSwanX, BeatsOfRageX,
PowermangaX, LynxBox, BlueMSXBox, GladiatorX, AmphetamineX, StarfighterX,
PachiX, BlobWarsX, OdysseyX, ArnoldX, X68000X, WinUAEX, MekaX,
MednafenX-NES, MednafenX-PCE, MednafenX-Lynx
what's next?

Enjoy!
