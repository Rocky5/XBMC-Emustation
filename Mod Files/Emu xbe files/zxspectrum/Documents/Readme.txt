First off...

------------------
Special thanks....
------------------

X-port for porting a great collection of emu's over to the xbox, releasing the source code, and answering my stupid questions.
Atariage (Albert in particular) - For providing a place for me to ramble on. For encouragement in general.
RessurectionX for all that Xtra's stuff, synopsis, suggestions, etc.
Gilou9999 for a new PM3 skin, synopsis, suggestions, etc.
Stupot for making lotsa game preview videos.
Comments of support from various interested parties.
If I missed anybody shoot me an email and I'll update this file.
Here's to the two people out there that use this emulator.

***********************************************
*** Changes To DidntxSpectrum Core ***
***********************************************

* Given the full "Madmab Edition" treatment.
* New dual-preview skin to support Ressurection Xtra's.  Say thank you to Gilou9999 for the skin.  Music provied by Carnage By Bob.
* Smart loading of Cartridge images from zip files and across the network.  So feel free to ZIP those suckers up now!

**************************************
*** To Do For DidntxSpectrum ***
**************************************

* Hopefully some form of an Xtra's collection from stupot.

**************************************
*** Interface Related Changes ***
**************************************
* Hopefully addressed weird issues with "Force Reload D:\\*.ini Settings".
* New option to "Keep user Within ROM Directory Tree".  You can find it in "General Settings, Page Two".  Useful for keeping n00bs from getting lost while selecting games.
* Hoperfully cleaned up all instances where the current "game select" directory would get trashed.
* Transparency control for keypad and keyboard should now function properly.
* Tightened up the Synopsis parsing code (sorry RessX :( )
* Fixed issue where cycling thru screenshots when non-available would create an infinite loop.

Fixes to the keyboard/keypad including. These affect emu's that use a keyboard/keypad (Winuaex, AdamX, Atarixlbox)
* Keyboard/keypad no longer corrupts portions of the screen when being moved.
* Keyboard/keypad can be moved diagonally in ALL directions now
* Keyboard/keypad transparency now works properly when "Pause game while using Keyboard/Pad" is set to ON.
* Fixed issue with screen blurring when Keyboard/keypad is activated.  I'm surprised I did not notice this earlier. 

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
You can set the movie/previews directory in the "Change Default Directories" section.
The movie name has to be exactly the same as the ROM name. Only one movie per game. 

* Display order can be set to. None, Screenshots Only, Movies Only, Screenshots 1st- Then Movies, Movies 1st- Then Screenshots.
* Sound for movies can be turned on/off
* Box/Cart art can be displayed in seperate window.
* Skin author can now designate two locations where Boxart or Cartart will display based on width vs height.
* Movies display over screenshots so if you want you can see screenshots when no movie exists.
* Can now stream videos and screenshots from Samba or Relax.
* Old Screenshots are now sorted and displayed in proper order.
* Old Screenshots can be named anything (as long as it has .png extension)
* In Game Options Screen can be sized and positioned now.

* New option to "Force Game Screen Size/Position". There are two configurable screensizes. (To deal with multi-core systems like MekaX and XboyAdvance). This will be useful when switching from HDTV to SDTV or vice versa. It will save the user the trouble of resizing the screens for something that is likely temporary.

* Numerous changes to menu system see above (current menu configuration layout)
* Sprites can now be named for easier manipulation. Directory names must be of the format "0_spritename", "1_spritename", etc. Do not use underscores for the spritename. It is a delimiter.
* Added "Select Skin Configuration Used" and "Save Skin Configuration as" to the "Configure SKin" menu in place of the above moved options. This allows multiple skin configurations in one skin allowing the user more "pre-defined" options on how a skin looks. For example the placement of the games list and the preview screens. Gilou's Dynamic skins really take advantage of this, check 'em out!
* Sprites now show when sizing the preview screens.
* Changed "Seconds before auto-advancing Screenshot" to "Seconds Before Auto-Advancing Artwork".
* Changed "offset X" and "offset Y" to "Offset X (left/right)" and "Offset Y (up/down)" in the Sprite Settings menu.
* New Option to pause or not pause emulation when keyboard or keypad is up.

------------------------------------------
Finished the "Media browser"
------------------------------------------
* Ability to display documentation (text or graphic) and commercials.
* Assigned buttons (white/black) to go to next/previous files when viewing documentation. See below graphic/text file viewer controls.
* Once the user opens a document - the emulator remember this document as long as the game session is running.
* View settings for each document viewed are now stored in a "bookmark" file so next time you view a file your settings are restored.  Back to "reset" as if reading document for first time.
* "View Text File" changed to "Browse Manuals/Videos"

* In screenshot viewer. If the image is smaller than your text file screensize settings it will work as follows. 
a) If the image is taller than it is wide it will continue expanding the image ( based on aspect ratio) until the width fits within the width of your text file screensize width. (Most normal manuals)
b) If the image is wider than it is tall it will continue expanding the image ( based on aspect ratio) until the height fits within the height of your text file screensize height. (For example NES manuals).

This seems to effectively stretch the image in the best manner possible for scanned manual reading.

* Browsing manuals/videos should dump you into the media directory correctly.
* Unmapped controls that allow you to move the screen around since word wrap should work correctly now.
* Change Fixed Width font controls are mapped to the right analog stick (left/right) like the help screen says it should be. :lol:
* Set font size keeps seperate settings for Fixed Width fonts and proportional fonts since they produce different results.
* Graphic documentation can now be stored in a ZIP file and still work with the media browser functions (next/previous and bookmarks).
* Music no longer starts playing after viewing text file in game.
* Number of lines displayed in the text file viewer now properly match user set text screen size.
* Number of lines displayed updates properly if user modifies text screen size within text file viewer
* Text file viewer functions turn off FixedWidth before displaying any menu.

* Added a fixed width font for the text file viewer. If you wanna use it you have to make sure that a file named (included in zip) "FixedFont.ttf" is located in the emulator directory. Press "Y" in the text file viewer to switch to the fixed font.

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

B -> Exit
Y -> Delete file (Utilities-> browse screenshots only)

White -> Previous file
Black -> Next file

Back -> Reset image to default settings/view.

Dpad -> Up/Down/Left/Right -> Move image 1/4th the total size of the image.
Left Analog button -> Music Control Menu
Left Analog up/down -> Move screen up/down.
Right Analog left/right -> decrease/increase screen size.  Size changes proportional to distance the stick is pressed.

------------------------------------------

********************************************
**** Carryovers from Atarixlbox ****
********************************************
* Ability to pick a file from within a zip file.
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

* (cheat codes)When "adding a code" from the "edit code" screen the current code is copied as a template.
* You can activate/deactivate a code from the "cheat code list" menu by pressing start.

* Deleting a cheat code now asks you if you are sure (I got tired of accidently deleting my codes ).

* Fixed up the problem created from using multiple files in a Zip file.
* Fixed problem when a filename inside a zip contains too many characters. While I was at it I fixed the space as the last character when trimming to 42 characters behavior. Zip files where the path was saved now unzip correctly.

* Rewind and Fastforward are de-activated during record/playback and netplay mode. It even tells you so when you try!!
* Modified YesNoMenu so it doesn't clear m_menuText.

* Added ability to add in cheat codes from a Gameshark compatible database (see description below). This includes the ability to export the cheat codes in a game to "share" with your friends. Cheat/rumble codes are included for most games. When "adding" codes from the gameshark DB it will move you to the entries with a matching CRC. If not you'll have to manually find the game.

***********************************************************************************************
*** "Auto Game Configurations (aka Configuration defaults) for select emulators ***
***********************************************************************************************
In the "General settings" menu there will be a new option.

"Automatically Use Default Game Configuration - Yes/No"

If the user sets it to "Yes" it will bring up the game configuration screen and let the user define the default (if no default.stg and default.key file exists).

In the "Configuration" menu there will be a new option... "Set default game configuration"

The user can go in anytime thru the "Configuration" menu to change these "defaults" to something else if they wish.

Once set to "Automatically use Default Game Configuration" the user will not see the game configuration screen again unless they... a) press X when selecting a game. Change "Use Default Game Configuration" back to "No".

Keep in mind when it is set to "Yes" the game will use your "Default game settings" and not the normal x-port behavior. If set to "No" the emulator will behave like it usually does. Each emu is typically different. But all, at the very least carry the controller settings over.

This feature will only be added to emulators in which it is feasible to use.
