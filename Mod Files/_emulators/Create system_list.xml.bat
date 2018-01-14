@Echo off
SetLocal EnableDelayedExpansion
:: this batch is used to generate the menu items from a list of folders.

md ports
md xbox

(
	Echo ^<content^>
	Echo 	^<item id^="0"^>
	Echo 		^<label^>^$LOCALIZE^[5^]^</label^>
	Echo 		^<label2^>^$LOCALIZE^[5^]^</label2^>
	Echo 		^<onclick^>ActivateWindow^(Settings,return^)^</onclick^>
	Echo 		^<icon^>layouts/settings/art/system_art.png^</icon^>
	Echo 		^<thumb^>layouts/settings/art/logo.png^</thumb^>
	Echo 	^</item^>
	Echo 	^<item id^="1"^>
	Echo 		^<label^>^$LOCALIZE^[518^] ^$LOCALIZE^[427^]^</label^>
	Echo 		^<label2^>^$LOCALIZE^[427^]^</label2^>
	Echo 		^<onclick^>PlayDVD^(^)^</onclick^>
	Echo 		^<icon^>layouts/disc/art/system_art.png^</icon^>
	Echo 		^<thumb^>layouts/disc/art/logo.png^</thumb^>
	Echo 		^<visible^>System.HasMediaDVD^</visible^>
	Echo 	^</item^>
	Echo 	^<item id^="2"^>
	Echo 		^<label^>$INFO^[Skin.String^(favs_games^)^]^</label^>
	Echo 		^<label2^>favs^</label2^>
	Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/menu_loader.py^)^</onclick^>
	Echo 		^<icon^>layouts/favourites/art/system_art.png^</icon^>
	Echo 		^<thumb^>layouts/favourites/art/logo.png^</thumb^>
	Echo 	^</item^>
)>>"system_list.xml"
Set /a count=3
for /f "Tokens=*" %%a in ('dir /b /A:D "*"') do (
	Echo  %%~na
		if not "%%~na"=="ports" if not "%%~na"=="xbox" if not "%%~na"=="atarijaguar" if not "%%~na"=="atarijaguarcd" if not "%%~na"=="mame" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^>
			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/menu_loader.py^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
			Echo 		^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
			Echo 	^</item^>
		)>>"system_list.xml"
		if "%%~na"=="atarijaguar" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>Direct Launch Only: $INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^>
			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/direct_launch_emulator.py,1^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
			Echo 		^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
			Echo 	^</item^>
		)>>"system_list.xml"
		if "%%~na"=="atarijaguarcd" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>Direct Launch Only: $INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^>
			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/direct_launch_emulator.py,1^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
			Echo 		^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
			Echo 	^</item^>
		)>>"system_list.xml"
		if "%%~na"=="mame" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>Direct Launch Only: $INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^>
			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/direct_launch_emulator.py,1^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
			Echo 		^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
			Echo 	^</item^>
		)>>"system_list.xml"
		if "%%~na"=="ports" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^>
			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/menu_loader.py^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
			Echo 	^</item^>
		)>>"system_list.xml"
		if "%%~na"=="xbox" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^>
			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/menu_loader.py^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
			Echo 	^</item^>
		)>>"system_list.xml"
	Set /a count+=1
)
(
			Echo 	^<item id^="90"^>
			Echo 		^<label^>Direct Launch Only^</label^>
			Echo 		^<label2^>customtile1^</label2^>
 			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
 			Echo 		^<onclick^>RunXBE^(^$INFO^[Skin.String^(CustomHomeTile1Xbe^)^]^)^</onclick^>
 			Echo 		^<icon^>^$INFO^[Skin.String^(CustomHomeTile1SystemArt^)^]^</icon^>
 			Echo 		^<thumb^>^$INFO^[Skin.String^(CustomHomeTile1Logo^)^]^</thumb^>
 			Echo 		^<visible^>Skin.HasSetting^(CustomHomeTile1Enabled^)^</visible^>
 			Echo 	^</item^>
 			Echo 	^<item id^="91"^>
 			Echo 		^<label^>Direct Launch Only^</label^>
 			Echo 		^<label2^>customtile2^</label2^>
 			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
 			Echo 		^<onclick^>RunXBE^(^$INFO^[Skin.String^(CustomHomeTile2Xbe^)^]^)^</onclick^>
 			Echo 		^<icon^>^$INFO^[Skin.String^(CustomHomeTile2SystemArt^)^]^</icon^>
 			Echo 		^<thumb^>^$INFO^[Skin.String^(CustomHomeTile2Logo^)^]^</thumb^>
 			Echo 		^<visible^>Skin.HasSetting^(CustomHomeTile2Enabled^)^</visible^>
 			Echo 	^</item^>
 			Echo 	^<item id^="92"^>
 			Echo 		^<label^>Direct Launch Only^</label^>
 			Echo 		^<label2^>customtile3^</label2^>
 			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
 			Echo 		^<onclick^>RunXBE^(^$INFO^[Skin.String^(CustomHomeTile3Xbe^)^]^)^</onclick^>
 			Echo 		^<icon^>^$INFO^[Skin.String^(CustomHomeTile3SystemArt^)^]^</icon^>
 			Echo 		^<thumb^>^$INFO^[Skin.String^(CustomHomeTile3Logo^)^]^</thumb^>
 			Echo 		^<visible^>Skin.HasSetting^(CustomHomeTile3Enabled^)^</visible^>
 			Echo 	^</item^>
)>>"system_list.xml"

Echo ^</content^> >>"system_list.xml"

rd ports
rd xbox