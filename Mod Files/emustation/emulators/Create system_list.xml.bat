@Echo off
SetLocal EnableDelayedExpansion
:: this batch is used to generate the menu items from a list of folders.
if exist "system_list.xml" del /Q "system_list.xml"

REM md homebrew
REM md ports
REM md xbox
REM md demos

REM for /f "Tokens=*" %%a in ('dir /b /AD /ON "*"') do Echo %%a>>list.txt

(
	Echo ^<content^>
	Echo 		^<item id^="0"^>
	Echo 				^<name^>^$LOCALIZE^[5^]^</name^>
	Echo 				^<systemid^>^$LOCALIZE^[5^]^</systemid^>
	Echo 				^<onclick^>ActivateWindow^(Settings,return^)^</onclick^>
	Echo 				^<systemart^>layouts/settings/art/system_art.png^</systemart^>
	Echo 				^<logo^>layouts/settings/art/logo.png^</logo^>
	Echo 		^</item^>
	Echo 		^<item id^="1"^>
	Echo 				^<name^>^$LOCALIZE^[518^] ^$LOCALIZE^[427^]^</name^>
	Echo 				^<systemid^>^$LOCALIZE^[427^]^</systemid^>
	Echo 				^<onclick^>PlayDVD^(^)^</onclick^>
	Echo 				^<systemart^>layouts/disc/art/system_art.png^</systemart^>
	Echo 				^<logo^>layouts/disc/art/logo.png^</logo^>
	Echo 				^<visible^>System.HasMediaDVD^</visible^>
	Echo 		^</item^>
	Echo 		^<item id^="2"^>
	Echo 				^<name^>$INFO^[Skin.String^(favs_games^)^]^</name^>
	Echo 				^<systemid^>favs^</systemid^>
	Echo 				^<onclick^>RunScript^(special://emustation_scripts/menu_loader.py^)^</onclick^>
	Echo 				^<systemart^>layouts/favourites/art/system_art.png^</systemart^>
	Echo 				^<logo^>layouts/favourites/art/logo.png^</logo^>
	Echo 				^<visible^>IntegerGreaterThan^(Skin.String^(favs_games^),0^) ^+ ^^!Skin.HasSetting^(hide_favs_title^)^</visible^>
	Echo 		^</item^>
)>>"system_list.xml"

Set /a count=3
for /f "Tokens=1,2 delims=~" %%a in (system_list.txt) do (
	Echo  %%~na
	Echo  %%~nb
	if not "%%~na"=="demos" if not "%%~na"=="homebrew" if not "%%~na"=="ports" if not "%%~na"=="xbox" if not "%%~na"=="atarijaguar" if not "%%~na"=="daphne" if not "%%~na"=="neogeocd" (
		Echo 		^<item id^="!count!"^>
		Echo 				^<name^>$INFO^[Skin.String^(%%~na_games^)^]^</name^>
		Echo 				^<systemid^>%%~na^</systemid^>
		Echo 				^<fullname^>%%~nb^</fullname^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/menu_loader.py^)^</onclick^>
		Echo 				^<systemart^>layouts/%%~na/art/system_art.png^</systemart^>
		Echo 				^<logo^>layouts/%%~na/art/logo.png^</logo^>
		Echo 				^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
		Echo 		^</item^>
	)>>"system_list.xml"

	if "%%~na"=="atarijaguar" (
		Echo 		^<item id^="!count!"^>
		Echo 				^<name^>Launch Emulator: $INFO^[Skin.String^(%%~na_games^)^]^</name^>
		Echo 				^<systemid^>%%~na^</systemid^>
		Echo 				^<fullname^>%%~nb^</fullname^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/direct_launch_emulator.py,1,^)^</onclick^>
		Echo 				^<systemart^>layouts/%%~na/art/system_art.png^</systemart^>
		Echo 				^<logo^>layouts/%%~na/art/logo.png^</logo^>
		Echo 				^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
		Echo 		^</item^>
	)>>"system_list.xml"

	if "%%~na"=="daphne" (
		Echo 		^<item id^="!count!"^>
		Echo 				^<name^>Launch Emulator: $INFO^[Skin.String^(%%~na_games^)^]^</name^>
		Echo 				^<systemid^>%%~na^</systemid^>
		Echo 				^<fullname^>%%~nb^</fullname^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/direct_launch_emulator.py,1,^)^</onclick^>
		Echo 				^<systemart^>layouts/%%~na/art/system_art.png^</systemart^>
		Echo 				^<logo^>layouts/%%~na/art/logo.png^</logo^>
		Echo 				^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
		Echo 		^</item^>
	)>>"system_list.xml"

	if "%%~na"=="neogeocd" (
		Echo 		^<item id^="!count!"^>
		Echo 				^<name^>Launch Emulator: $INFO^[Skin.String^(%%~na_games^)^]^</name^>
		Echo 				^<systemid^>%%~na^</systemid^>
		Echo 				^<fullname^>%%~nb^</fullname^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/direct_launch_emulator.py,1,^)^</onclick^>
		Echo 				^<systemart^>layouts/%%~na/art/system_art.png^</systemart^>
		Echo 				^<logo^>layouts/%%~na/art/logo.png^</logo^>
		Echo 				^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
		Echo 		^</item^>
	)>>"system_list.xml"
	
	if "%%~na"=="ports" (
		Echo 		^<item id^="!count!"^>
		Echo 				^<name^>$INFO^[Skin.String^(%%~na_games^)^]^</name^>
		Echo 				^<systemid^>%%~na^</systemid^>
		Echo 				^<fullname^>%%~nb^</fullname^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/menu_loader.py^)^</onclick^>
		Echo 				^<systemart^>layouts/%%~na/art/system_art.png^</systemart^>
		Echo 				^<logo^>layouts/%%~na/art/logo.png^</logo^>
		Echo 				^<visible^>IntegerGreaterThan^(Skin.String^(ports_games^),0^)^</visible^>
		Echo 		^</item^>
	)>>"system_list.xml"

if "%%~na"=="homebrew" (
		Echo 		^<item id^="!count!"^>
		Echo 				^<name^>$INFO^[Skin.String^(%%~na_games^)^]^</name^>
		Echo 				^<systemid^>%%~na^</systemid^>
		Echo 				^<fullname^>%%~nb^</fullname^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/menu_loader.py^)^</onclick^>
		Echo 				^<systemart^>layouts/%%~na/art/system_art.png^</systemart^>
		Echo 				^<logo^>layouts/%%~na/art/logo.png^</logo^>
		Echo 				^<visible^>IntegerGreaterThan^(Skin.String^(homebrew_games^),0^)^</visible^>
		Echo 		^</item^>
	)>>"system_list.xml"

if "%%~na"=="demos" (
		Echo 		^<item id^="!count!"^>
		Echo 				^<name^>$INFO^[Skin.String^(%%~na_games^)^]^</name^>
		Echo 				^<systemid^>%%~na^</systemid^>
		Echo 				^<fullname^>%%~nb^</fullname^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/menu_loader.py^)^</onclick^>
		Echo 				^<systemart^>layouts/%%~na/art/system_art.png^</systemart^>
		Echo 				^<logo^>layouts/%%~na/art/logo.png^</logo^>
		Echo 				^<visible^>IntegerGreaterThan^(Skin.String^(demos_games^),0^)^</visible^>
		Echo 		^</item^>
	)>>"system_list.xml"
	
if "%%~na"=="xbox" (
		Echo 		^<item id^="!count!"^>
		Echo 				^<name^>$INFO^[Skin.String^(%%~na_games^)^]^</name^>
		Echo 				^<systemid^>%%~na^</systemid^>
		Echo 				^<fullname^>%%~nb^</fullname^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/menu_loader.py^)^</onclick^>
		Echo 				^<systemart^>layouts/%%~na/art/system_art.png^</systemart^>
		Echo 				^<logo^>layouts/%%~na/art/logo.png^</logo^>
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
	Echo 				^<name^>Direct Launch^</name^>
	Echo 				^<systemid^>customtile^</systemid^>
	Echo 				^<fullname^>customtile^</fullname^>
	Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
	Echo 				^<onclick^>RunScript^(special://emustation_scripts/direct_launch_emulator.py,0,^$INFO^[Skin.String^(CustomHomeTile!countalt!Xbe^)^]^)^</onclick^>
	Echo 				^<systemart^>^$INFO^[Skin.String^(CustomHomeTile!countalt!SystemArt^)^]^</systemart^>
	Echo 				^<logo^>^$INFO^[Skin.String^(CustomHomeTile!countalt!Logo^)^]^</logo^>
	Echo 				^<visible^>Skin.HasSetting^(CustomHomeTile!countalt!Enabled^)^</visible^>
	Echo 		^</item^>
	Set /a count+=1
	Set /a countalt+=1
)>>"system_list.xml"
if not "!countalt!"=="16" goto loop

Echo ^</content^>>>"system_list.xml"

REM rd homebrew
REM rd ports
REM rd xbox
REM rd demos

pause