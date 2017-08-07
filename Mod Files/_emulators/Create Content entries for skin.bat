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
	Echo 		^<icon^>layouts/Settings/art/system_art.png^</icon^>
	Echo 		^<thumb^>layouts/%Settings/art/logo.png^</thumb^>
	Echo 	^</item^>
)>>"Logo.xml"
Set /a count=1
for /f "Tokens=*" %%a in ('dir /b /A:D "*"') do (
	Echo  %%~na
		if not "%%~na"=="ports" if not "%%~na"=="xbox" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^> ^<^^!-- this is the folder name used for layouts, CUT files and emulator files --^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/default.py^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
			Echo 		^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
			Echo 	^</item^>
		)>>"Logo.xml"
		if "%%~na"=="ports" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^> ^<^^!-- this is the folder name used for layouts, CUT files and emulator files --^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/default.py^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
			Echo 	^</item^>
		)>>"Logo.xml"
		if "%%~na"=="xbox" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^> ^<^^!-- this is the folder name used for layouts, CUT files and emulator files --^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/default.py^)^</onclick^>
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
	Echo 		^<icon^>layouts/Settings/art/system_art.png^</icon^>
	Echo 		^<thumb^>layouts/%Settings/art/carousel_logo.png^</thumb^>
	Echo 	^</item^>
)>>"Carousel.xml"
Set /a count=1
for /f "Tokens=*" %%a in ('dir /b /A:D "*"') do (
	Echo  %%~na
		if not "%%~na"=="ports" if not "%%~na"=="xbox" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^> ^<^^!-- this is the folder name used for layouts, CUT files and emulator files --^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/default.py^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/carousel_logo.png^</thumb^>
			Echo 		^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
			Echo 	^</item^>
		)>>"Carousel.xml"
		if "%%~na"=="ports" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^> ^<^^!-- this is the folder name used for layouts, CUT files and emulator files --^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/default.py^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/carousel_logo.png^</thumb^>
			Echo 	^</item^>
		)>>"Carousel.xml"
		if "%%~na"=="xbox" (
			Echo 	^<item id^="!count!"^>
			Echo 		^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
			Echo 		^<label2^>%%~na^</label2^> ^<^^!-- this is the folder name used for layouts, CUT files and emulator files --^>
			Echo 		^<onclick^>RunScript^(Special://xbmc/_scripts/XBMC-Emustation/default.py^)^</onclick^>
			Echo 		^<icon^>layouts/%%~na/art/system_art.png^</icon^>
			Echo 		^<thumb^>layouts/%%~na/art/carousel_logo.png^</thumb^>
			Echo 	^</item^>
		)>>"Carousel.xml"
	Set /a count+=1
)
Echo ^</content^> >>"Carousel.xml"

rd ports
rd xbox