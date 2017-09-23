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
)>"Logo.xml"
(
	Echo 	^<item id^="1"^>
	Echo 		^<label^>^$LOCALIZE^[518^] ^$LOCALIZE^[427^]^</label^>
	Echo 		^<label2^>^$LOCALIZE^[427^]^</label2^>
	Echo 		^<onclick^>PlayDVD^(^)^</onclick^>
	Echo 		^<icon^>layouts/disc/art/system_art.png^</icon^>
	Echo 		^<thumb^>layouts/disc/art/logo.png^</thumb^>
	Echo 		^<visible^>System.HasMediaDVD^</visible^>
	Echo 	^</item^>
)>>"Logo.xml"
Set /a count=2
for /f "Tokens=*" %%a in ('dir /b /A:D "*"') do (
	Echo  %%~na
		if not "%%~na"=="ports" if not "%%~na"=="xbox" if not "%%~na"=="atarijaguar" if not "%%~na"=="atarijaguarcd" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^> ^<^^!-- this is the folder name used for layouts, CUT files and emulator files --^>
			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/menu_loader.py^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
			Echo 		^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
			Echo 	^</item^>
		)>>"Logo.xml"
		if "%%~na"=="atarijaguar" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>Direct Launch Only $INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^> ^<^^!-- this is the folder name used for layouts, CUT files and emulator files --^>
			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/direct_launch_emulator.py^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
			Echo 		^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
			Echo 	^</item^>
		)>>"Logo.xml"
		if "%%~na"=="atarijaguarcd" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>Direct Launch Only $INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^> ^<^^!-- this is the folder name used for layouts, CUT files and emulator files --^>
			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/direct_launch_emulator.py^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
			Echo 		^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
			Echo 	^</item^>
		)>>"Logo.xml"
		if "%%~na"=="ports" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^> ^<^^!-- this is the folder name used for layouts, CUT files and emulator files --^>
			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/menu_loader.py^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
			Echo 	^</item^>
		)>>"Logo.xml"
		if "%%~na"=="xbox" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^> ^<^^!-- this is the folder name used for layouts, CUT files and emulator files --^>
			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/menu_loader.py^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
			Echo 	^</item^>
		)>>"Logo.xml"
	Set /a count+=1
)
Echo ^</content^> >>"Logo.xml"

(
	Echo ^<content^>
	Echo 	^<item id^="0"^>
	Echo 		^<label^>^$LOCALIZE^[5^]^</label^>
	Echo 		^<label2^>^$LOCALIZE^[5^]^</label2^>
	Echo 		^<onclick^>ActivateWindow^(Settings,return^)^</onclick^>
	Echo 		^<icon^>layouts/settings/art/system_art.png^</icon^>
	Echo 		^<thumb^>layouts/settings/art/carousel_logo.png^</thumb^>
	Echo 	^</item^>
)>"Carousel.xml"
(
	Echo 	^<item id^="1"^>
	Echo 		^<label^>^$LOCALIZE^[518^] ^$LOCALIZE^[427^]^</label^>
	Echo 		^<label2^>^$LOCALIZE^[427^]^</label2^>
	Echo 		^<onclick^>PlayDVD^(^)^</onclick^>
	Echo 		^<icon^>layouts/disc/art/system_art.png^</icon^>
	Echo 		^<thumb^>layouts/disc/art/carousel_logo.png^</thumb^>
	Echo 		^<visible^>System.HasMediaDVD^</visible^>
	Echo 	^</item^>
)>>"Carousel.xml"
Set /a count=2
for /f "Tokens=*" %%a in ('dir /b /A:D "*"') do (
	Echo  %%~na
		if not "%%~na"=="ports" if not "%%~na"=="xbox" if not "%%~na"=="atarijaguar" if not "%%~na"=="atarijaguarcd" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^> ^<^^!-- this is the folder name used for layouts, CUT files and emulator files --^>
			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/menu_loader.py^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/carousel_logo.png^</thumb^>
			Echo 		^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
			Echo 	^</item^>
		)>>"Carousel.xml"
		if "%%~na"=="atarijaguar" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>Direct Launch Only $INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^> ^<^^!-- this is the folder name used for layouts, CUT files and emulator files --^>
			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/direct_launch_emulator.py^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/carousel_logo.png^</thumb^>
			Echo 		^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
			Echo 	^</item^>
		)>>"Carousel.xml"
		if "%%~na"=="atarijaguarcd" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>Direct Launch Only $INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^> ^<^^!-- this is the folder name used for layouts, CUT files and emulator files --^>
			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/direct_launch_emulator.py^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/carousel_logo.png^</thumb^>
			Echo 		^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
			Echo 	^</item^>
		)>>"Carousel.xml"
		if "%%~na"=="ports" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^> ^<^^!-- this is the folder name used for layouts, CUT files and emulator files --^>
			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/menu_loader.py^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/carousel_logo.png^</thumb^>
			Echo 	^</item^>
		)>>"Carousel.xml"
		if "%%~na"=="xbox" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^> ^<^^!-- this is the folder name used for layouts, CUT files and emulator files --^>
			Echo 		^<onclick^>SetFocus^(9100^)^</onclick^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/menu_loader.py^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/carousel_logo.png^</thumb^>
			Echo 	^</item^>
		)>>"Carousel.xml"
	Set /a count+=1
)
Echo ^</content^> >>"Carousel.xml"

rd ports
rd xbox