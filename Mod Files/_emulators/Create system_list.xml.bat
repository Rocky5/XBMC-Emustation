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
)>"system_list.xml"
(
	Echo 	^<item id^="1"^>
	Echo 		^<label^>^$LOCALIZE^[518^] ^$LOCALIZE^[427^]^</label^>
	Echo 		^<label2^>^$LOCALIZE^[427^]^</label2^>
	Echo 		^<onclick^>PlayDVD^(^)^</onclick^>
	Echo 		^<icon^>layouts/disc/art/system_art.png^</icon^>
	Echo 		^<thumb^>layouts/disc/art/logo.png^</thumb^>
	Echo 		^<visible^>System.HasMediaDVD^</visible^>
	Echo 	^</item^>
)>>"system_list.xml"
(
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
Echo ^</content^> >>"system_list.xml"

REM (
	REM Echo ^<content^>
	REM Echo 	^<item id^="0"^>
	REM Echo 		^<label^>^$LOCALIZE^[5^]^</label^>
	REM Echo 		^<label2^>^$LOCALIZE^[5^]^</label2^>
	REM Echo 		^<onclick^>ActivateWindow^(Settings,return^)^</onclick^>
	REM Echo 		^<icon^>layouts/settings/art/system_art.png^</icon^>
	REM Echo 		^<thumb^>layouts/settings/art/carousel_logo.png^</thumb^>
	REM Echo 	^</item^>
REM )>"Carousel.xml"
REM (
	REM Echo 	^<item id^="1"^>
	REM Echo 		^<label^>^$LOCALIZE^[518^] ^$LOCALIZE^[427^]^</label^>
	REM Echo 		^<label2^>^$LOCALIZE^[427^]^</label2^>
	REM Echo 		^<onclick^>PlayDVD^(^)^</onclick^>
	REM Echo 		^<icon^>layouts/disc/art/system_art.png^</icon^>
	REM Echo 		^<thumb^>layouts/disc/art/carousel_logo.png^</thumb^>
	REM Echo 		^<visible^>System.HasMediaDVD^</visible^>
	REM Echo 	^</item^>
REM )>>"Carousel.xml"
REM Set /a count=2
REM for /f "Tokens=*" %%a in ('dir /b /A:D "*"') do (
	REM Echo  %%~na
		REM if not "%%~na"=="ports" if not "%%~na"=="xbox" if not "%%~na"=="atarijaguar" if not "%%~na"=="atarijaguarcd" (
			REM Echo 	^<item id^="!count!"^>
			REM Echo 		^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
			REM Echo 		^<label2^>%%~na^</label2^>
			REM Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			REM Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/menu_loader.py^)^</onclick^>
			REM Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			REM Echo 		^<thumb^>layouts/%%~na/art/carousel_logo.png^</thumb^>
			REM Echo 		^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
			REM Echo 	^</item^>
		REM )>>"Carousel.xml"
		REM if "%%~na"=="atarijaguar" (
			REM Echo 	^<item id^="!count!"^>
			REM Echo 		^<label^>Direct Launch Only $INFO^[Skin.String^(%%~na_games^)^]^</label^>
			REM Echo 		^<label2^>%%~na^</label2^>
			REM Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			REM Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/direct_launch_emulator.py^)^</onclick^>
			REM Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			REM Echo 		^<thumb^>layouts/%%~na/art/carousel_logo.png^</thumb^>
			REM Echo 		^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
			REM Echo 	^</item^>
		REM )>>"Carousel.xml"
		REM if "%%~na"=="atarijaguarcd" (
			REM Echo 	^<item id^="!count!"^>
			REM Echo 		^<label^>Direct Launch Only $INFO^[Skin.String^(%%~na_games^)^]^</label^>
			REM Echo 		^<label2^>%%~na^</label2^>
			REM Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			REM Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/direct_launch_emulator.py^)^</onclick^>
			REM Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			REM Echo 		^<thumb^>layouts/%%~na/art/carousel_logo.png^</thumb^>
			REM Echo 		^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
			REM Echo 	^</item^>
		REM )>>"Carousel.xml"
		REM if "%%~na"=="ports" (
			REM Echo 	^<item id^="!count!"^>
			REM Echo 		^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
			REM Echo 		^<label2^>%%~na^</label2^>
			REM Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			REM Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/menu_loader.py^)^</onclick^>
			REM Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			REM Echo 		^<thumb^>layouts/%%~na/art/carousel_logo.png^</thumb^>
			REM Echo 	^</item^>
		REM )>>"Carousel.xml"
		REM if "%%~na"=="xbox" (
			REM Echo 	^<item id^="!count!"^>
			REM Echo 		^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
			REM Echo 		^<label2^>%%~na^</label2^>
			REM Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			REM Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/menu_loader.py^)^</onclick^>
			REM Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			REM Echo 		^<thumb^>layouts/%%~na/art/carousel_logo.png^</thumb^>
			REM Echo 	^</item^>
		REM )>>"Carousel.xml"
	REM Set /a count+=1
REM )
REM Echo ^</content^> >>"Carousel.xml"

rd ports
rd xbox