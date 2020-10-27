SNES9XBox Super Nintendo Emulator for XBox v3

http://xport.xbox-scene.com
http://www.emuxtras.net

What's New:

Check the Latest-Snes9x.txt file for the latest update info.  From now on it will have the latest info and this file will contain the changelog/older update information.


-----------------------------------------------------------------------

SNES9XBox Super Nintendo Emulator for XBox v2


*****************************
* Changes To Snes9Xbox Core *
*****************************

* Fixed the issue with the black border at the bottom of the screen.. The emu likes to force the vertical resolution to 239 even on NTSC games which causes the black border at the bottom.  Most games even PAL run at 224.  The emu will be nice and tell you if the game you are currently playing is using 239 pixels.  Thanks to Cbagy for help on this.

* Hopefully any PAL xbox speed issues are fixed.  I'm sure you'll let me know if they ain't.  :P

* Added multiplayer5 support for games that use more than 2 controllers (aka Bomberman)

* PAL ROMS now supported.  In the game configuration screen you can select "Automatic", "Force PAL" or "Force NTSC".  Let me know if you run into any PAL games with scratchy sound.  Because of this I had to change the perfect pixel screen to have two options. One for PAL and one for NTSC

* Screen memory allocated depends on whether filters are active or not.  This is done to help relieve memory issues when running at 720p and higher.

* Snes9xbox now has support for AR (Action Replay) and GG (Game Gear) codes.  Check them out!

* Software filters should work now (I think I got it right).


***********************
* To Do For Snes9Xbox *
***********************

* lightgun support, PAR, loading of external data files for certain games, SNES mouse support.

* Memory issues may be no longer and I might be able to take out the above mentioned screen filter code..  Just have not got around to it.

* Anything else I happen to think of...


*****************************
* Interface Related Changes *
*****************************

* Tweaked around with the rewind system fixed a couple potential xbox lockers.  Rewind works well in 480i/p and fair in 720p.  See below.

* Given the full "Madmab Edition" treatment.

* New dual-preview skin.  Say thank you to Gilou9999 for the skin.

* Two skins to choose from.  Snes and Snes 2.0.

* "Auto Game Configurations (aka Configuration defaults)" added (see below description).

* Background Music now stops when you start a game..

* Fixed a long standing bug in the favorites system.  This one goes waaaaay back. (Thanks to Hyper_Eye for reporting it)

* Emulator should now work with 1.6 Xbox's super big thanks to FreakDave.  1.6 users let me know how this works for you.

* Fixed a problem where the media directory selected by the user replaced the wrong media directory.  Again.  Double Doi on me!  :P

* Fixed the problem where the wrong synopsis description was showing when selecting a game in the favorites menu.

* Fixed odd bug where the opening movie and movies played full screen in the media browser would not display properly at 1080i

* Fixed a couple goofs that prevented loading ROMS over a samba share.

* "Ask Before Moving To Garbage Dir?" now has a new option.. "Never Move".  So "Yes" will ask before moving the selected file to the Garbage folder.  "No" will just move the file and "Never Move" won't move the file at all.

* New feature "Seconds before playing movie" determines how long the emu will wait before playing a movie.  The default is half a second.  This will help speed up rom browsing.  Especially useful for people streaming stuff (like movies) across the network.

* Pick -1 on "Seconds before playing movie" to set to 0 seconds.  0 will equal half a second..  1 one second, and so on.

* If streaming movies from across the network and the user press on the dpad or a, b, x or y the emulator will abort the transfer.  This should help speed up rom browsing and allow the user an "out" especially for the larger movies.

* User can now select which "cheat code database" they wan't to load since it seemed silly to mix the many AR and GG codes into one file for Snes9xbox.

* Select file function now has an option to not display directories.  First menu to use this is the cheat code database select screen.

* Pressing the back key while viewing a games synopsis will toggle between a fixed font and the skins proportional font.

* Fixed long standing bug of YesNo Menu pop-up graphic not centering properly.

* Fixed an issue with the software filters displaying garbage.

* Activated the "Keep user Within ROM Directory Tree?" which I somehow missed.

* Fixed up the box/cart art position on a few skins.

* Fixed a problem where setting the box/cart orientation was screwed up.

* Fixed the bug that screwed up Gilou's skin to begin with (too weird to explain).  :P

--------------
New SAMBA code
--------------

* Old SAMBA library replaced.  You should now have more luck connecting to your SAMBA shares (including a NAS).  Especially shares with passwords which NEVER worked under the old code.

* Renamed "Enter Samba Share Name" to "Enter Root Samba Share Name" since it acts more as a shortcut now that you can "Browse" SMB shares.

* "Samba Server Name" doesn't really serve any purpose at the moment but I left it in there just in case.

* SMB shares can now be browsed.  As a result how you use Samba shares has changed slightly...  Try these steps..

1) Clear out your "Samba Share Name"

2) Use either the ROM browser or the "Change default directories" to browse to your share (Press "Y" until you see the drive list and select "SMB:\\").

3) If it doesn't work, try it again a couple times.  For some silly reason sometimes it times out.

4) If the emu thinks your share needs a password a window will pop-up asking you if you want to enter in a username and password.  Enter it as "username:password".

5) As a result of this change you can set all your definable directories to any share with any password.

6) If for some reason browsing doesn't work try entering your Samba server name in the "Enter Root Samba Share Name" under "Network/Netplay Options" format is "smb://servername_or_ip/sharename" or "smb://username:password@servername_or_ip/sharename" if the share is password protected.  Browsing once within a share is much more reliable.

7) If you enter anything into the "Root Samba Share Name" then you are stuck with that and cant use other servers for media streaming unless they are on a Relax share.

8) If steps 1-5 don't work for you but step 6 works you might wanna consider deleting your emu_name.ini file in the SAVES directory.  I was told by one user that this cleared up his problem.

* Some suggestions if you decide to "stream" stuff over the network.

1) Try splitting the workload.  Setup a Relax and Samba share (or even seperate servers) and divy up the workload.  They both have seperate caches so it's more efficient.

2) Roms, Screenshots, Box/Cart art, Manuals, Commercials, preview movies and the like are great candidates for streaming.

3) If you do stream Screenshots and Box/Cart art set the timers a little higher and not the same.  For example 5 seconds on screenshots, 10 on Box/Cart art.  Or just set them to 0 (manual advance).

4) Streaming movies really depends on how good of a network you have  For example streaming movies over a wireless network aint gonna be so hot.  To me relax seems faster but that may have changed with the new SMB code.  You might also wanna consider bumping up the movie delay a couple seconds. (only applies if "Movie Streaming Style" is set to "Copy Then Play (slower?)".  Pseudo streaming does not have this limitation.

An example of how I have mine set up.  Screenshots and Box/Cart art on the xbox 5/10 sec delay respectivaly (or 0).  ROMS, GameFaqs, VGMaps, etc on a Samba share to my NAS, as well as all of the commercials and manuals.  Movies on NAS using samba and pseudo streaming.  

The possibilities are endless.  Experimentation is worthwhile.  Or you could just slap a super big hard drive in your Xbox and forget all this silliness.  :P

------------------
End New SAMBA Code
------------------

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


----------------------------------------------------------------------

SNES9XBox Super Nintendo Emulator for XBox v1

http://xport.xbox-scene.com
http://www.snes9x.com

Features:

 - Excellent compatibility - ported from SNES9X v1.43

*****************************
* Interface Related Changes *
*****************************

 - All the usual XPort features ( ZIP support, save states, rewind, autofire,
   cheat codes, fast forward, graphic filters, etc, etc.)

 - If you leave rewind on it will crash after a few minutes.
   Best to just turn it on when you need it.


IMPORTANT NOTES
---------------

Yes, I know I said I'd never release a SNES port - and I never really intended to do so.
This has been sitting around for a long time, though, and I have been keeping it
updated with the changes to the UI feature set (rewinding, rumble, slowdown, etc)
because the SNES gets a lot of playtime in the house here.  I figure that since all
the source is now available, it would only be a matter of time before someone wrapped
my core around a port of SNES9X - so I'm saving them some time.  

There is still a lot that needs to be done with this port like lightgun support, PAR,
loading of external data files for certain games, SNES mouse support, fixing up 
the rewinding, and some other stuff that I don't recall right now.  There is also 
no skin for it.  These are all things that are left for someone else to implement.
