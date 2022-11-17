@Echo off
SetLocal EnableDelayedExpansion
:: this batch is used to generate the menu items from a list of folders.
del /Q "system_list.xml"

md ports
md xbox
md demos

REM for /f "Tokens=*" %%a in ('dir /b /AD /ON "*"') do Echo %%a>>list.txt

(
	Echo ^<content^>
	Echo 		^<item id^="0"^>
	Echo 				^<label^>^$LOCALIZE^[5^]^</label^>
	Echo 				^<label2^>^$LOCALIZE^[5^]^</label2^>
	Echo 				^<onclick^>ActivateWindow^(Settings,return^)^</onclick^>
	Echo 				^<icon^>layouts/settings/art/system_art.png^</icon^>
	Echo 				^<thumb^>layouts/settings/art/logo.png^</thumb^>
	Echo 		^</item^>
	Echo 		^<item id^="1"^>
	Echo 				^<label^>^$LOCALIZE^[518^] ^$LOCALIZE^[427^]^</label^>
	Echo 				^<label2^>^$LOCALIZE^[427^]^</label2^>
	Echo 				^<onclick^>PlayDVD^(^)^</onclick^>
	Echo 				^<icon^>layouts/disc/art/system_art.png^</icon^>
	Echo 				^<thumb^>layouts/disc/art/logo.png^</thumb^>
	Echo 				^<visible^>System.HasMediaDVD^</visible^>
	Echo 		^</item^>
	Echo 		^<item id^="2"^>
	Echo 				^<label^>$INFO^[Skin.String^(favs_games^)^]^</label^>
	Echo 				^<label2^>favs^</label2^>
	Echo 				^<onclick^>RunScript^(special://emustation_scripts/menu_loader.py^)^</onclick^>
	Echo 				^<icon^>layouts/favourites/art/system_art.png^</icon^>
	Echo 				^<thumb^>layouts/favourites/art/logo.png^</thumb^>
	Echo 				^<visible^>^^!Skin.HasSetting^(hide_favs_title^)^</visible^>
	Echo 		^</item^>
)>>"system_list.xml"

Set /a count=3
for /f "Tokens=*" %%a in (system_list.txt) do (
	Echo  %%~na
	if not "%%~na"=="ports" if not "%%~na"=="xbox" if not "%%~na"=="demos" if not "%%~na"=="atarijaguar" if not "%%~na"=="daphne" if not "%%~na"=="neogeocd" (
		Echo 		^<item id^="!count!"^>
		Echo 				^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
		Echo 				^<label2^>%%~na^</label2^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/menu_loader.py^)^</onclick^>
		Echo 				^<icon^>layouts/%%~na/art/system_art.png^</icon^>
		Echo 				^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
		Echo 				^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
		Echo 		^</item^>
	)>>"system_list.xml"

	if "%%~na"=="atarijaguar" (
		Echo 		^<item id^="!count!"^>
		Echo 				^<label^>Launch Emulator: $INFO^[Skin.String^(%%~na_games^)^]^</label^>
		Echo 				^<label2^>%%~na^</label2^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/direct_launch_emulator.py,1,^)^</onclick^>
		Echo 				^<icon^>layouts/%%~na/art/system_art.png^</icon^>
		Echo 				^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
		Echo 				^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
		Echo 		^</item^>
	)>>"system_list.xml"

	if "%%~na"=="daphne" (
		Echo 		^<item id^="!count!"^>
		Echo 				^<label^>Launch Emulator: $INFO^[Skin.String^(%%~na_games^)^]^</label^>
		Echo 				^<label2^>%%~na^</label2^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/direct_launch_emulator.py,1,^)^</onclick^>
		Echo 				^<icon^>layouts/%%~na/art/system_art.png^</icon^>
		Echo 				^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
		Echo 				^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
		Echo 		^</item^>
	)>>"system_list.xml"
	
	REM if "%%~na"=="mame" (
		REM Echo 		^<item id^="!count!"^>
		REM Echo 				^<label^>Launch Emulator: $INFO^[Skin.String^(%%~na_games^)^]^</label^>
		REM Echo 				^<label2^>%%~na^</label2^>
		REM Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		REM Echo 				^<onclick^>RunScript^(special://emustation_scripts/direct_launch_emulator.py,1,^)^</onclick^>
		REM Echo 				^<icon^>layouts/%%~na/art/system_art.png^</icon^>
		REM Echo 				^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
		REM Echo 				^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
		REM Echo 		^</item^>
	REM )>>"system_list.xml"

	if "%%~na"=="neogeocd" (
		Echo 		^<item id^="!count!"^>
		Echo 				^<label^>Launch Emulator: $INFO^[Skin.String^(%%~na_games^)^]^</label^>
		Echo 				^<label2^>%%~na^</label2^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/direct_launch_emulator.py,1,^)^</onclick^>
		Echo 				^<icon^>layouts/%%~na/art/system_art.png^</icon^>
		Echo 				^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
		Echo 				^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
		Echo 		^</item^>
	)>>"system_list.xml"
	
	if "%%~na"=="ports" (
		Echo 		^<item id^="!count!"^>
		Echo 				^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
		Echo 				^<label2^>%%~na^</label2^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/menu_loader.py^)^</onclick^>
		Echo 				^<icon^>layouts/%%~na/art/system_art.png^</icon^>
		Echo 				^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
		Echo 				^<visible^>IntegerGreaterThan^(Skin.String^(ports_games^),0^)^</visible^>
		Echo 		^</item^>
)>>"system_list.xml"

if "%%~na"=="demos" (
		Echo 		^<item id^="!count!"^>
		Echo 				^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
		Echo 				^<label2^>%%~na^</label2^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/menu_loader.py^)^</onclick^>
		Echo 				^<icon^>layouts/%%~na/art/system_art.png^</icon^>
		Echo 				^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
		Echo 				^<visible^>IntegerGreaterThan^(Skin.String^(demos_games^),0^)^</visible^>
		Echo 		^</item^>
)>>"system_list.xml"
	
if "%%~na"=="xbox" (
		Echo 		^<item id^="!count!"^>
		Echo 				^<label^>$INFO^[Skin.String^(%%~na_games^)^]^</label^>
		Echo 				^<label2^>%%~na^</label2^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/menu_loader.py^)^</onclick^>
		Echo 				^<icon^>layouts/%%~na/art/system_art.png^</icon^>
		Echo 				^<thumb^>layouts/%%~na/art/logo.png^</thumb^>
		Echo 				^<visible^>IntegerGreaterThan^(Skin.String^(xbox_games^),0^)^</visible^>
		Echo 		^</item^>
	)>>"system_list.xml"

	Set /a count+=1
)
Set /a countalt=1
:loop
Echo  Direct Launch !countalt!
(
	Echo 		^<item id^="!count!"^>
	Echo 				^<label^>Direct Launch^</label^>
	Echo 				^<label2^>customtile^</label2^>
	Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
	Echo 				^<onclick^>RunScript^(special://emustation_scripts/direct_launch_emulator.py,0,^$INFO^[Skin.String^(CustomHomeTile!countalt!Xbe^)^]^)^</onclick^>
	Echo 				^<icon^>^$INFO^[Skin.String^(CustomHomeTile!countalt!SystemArt^)^]^</icon^>
	Echo 				^<thumb^>^$INFO^[Skin.String^(CustomHomeTile!countalt!Logo^)^]^</thumb^>
	Echo 				^<visible^>Skin.HasSetting^(CustomHomeTile!countalt!Enabled^)^</visible^>
	Echo 		^</item^>
	Set /a count+=1
	Set /a countalt+=1
)>>"system_list.xml"
if not "!countalt!"=="16" goto loop

Echo ^</content^>>>"system_list.xml"

rd ports
rd xbox
rd demos

pause