@Echo off
CHCP 65001
SetLocal EnableDelayedExpansion
:: this batch is used to generate the menu items from a list of folders.
if exist "system_list.xml" del /Q "system_list.xml"

Set "output=_sort_id"

md %output%

(
	Echo 		^<item id^="0"^>
	Echo 				^<name^>^$LOCALIZE^[5^]^</name^>
	Echo 				^<fullname^>Adjust System Settings^</fullname^>
	Echo 				^<systemid^>^$LOCALIZE^[5^]^</systemid^>
	Echo 				^<systemart^>layouts/settings/art/system_art.png^</systemart^>
	Echo 				^<onclick^>ActivateWindow^(Settings,return^)^</onclick^>
	Echo 				^<logo^>layouts/settings/art/logo.png^</logo^>
	Echo 		^</item^>
)>>"!output!\00_settings.xml"
(
	Echo 		^<item id^="1"^>
	Echo 				^<name^>^$LOCALIZE^[518^] ^$LOCALIZE^[427^]^</name^>
	Echo 				^<systemid^>^$LOCALIZE^[427^]^</systemid^>
	Echo 				^<systemart^>layouts/disc/art/system_art.png^</systemart^>
	Echo 				^<logo^>layouts/disc/art/logo.png^</logo^>
	Echo 				^<onclick^>PlayDVD^(^)^</onclick^>
	Echo 				^<visible^>System.HasMediaDVD^</visible^>
	Echo 		^</item^>
)>>"!output!\01_disc.xml"
(
	Echo 		^<item id^="2"^>
	Echo 				^<name^>$INFO^[Skin.String^(favs_games^)^]^</name^>
	Echo 				^<fullname^>Your Favorite Games^</fullname^>
	Echo 				^<systemid^>favs^</systemid^>
	Echo 				^<systemart^>layouts/favourites/art/system_art.png^</systemart^>
	Echo 				^<logo^>layouts/favourites/art/logo.png^</logo^>
	Echo 				^<onclick^>RunScript^(special://emustation_scripts/menu_loader.py^)^</onclick^>
	Echo 				^<visible^>IntegerGreaterThan^(Skin.String^(favs_games^),0^) ^+ ^^!Skin.HasSetting^(hide_favs_title^)^</visible^>
	Echo 		^</item^>
)>>"!output!\02_favourites.xml"

Set /a count=3
for /f "Tokens=1,2 delims=~" %%a in (system_list.txt) do (
	Echo  %%~na	
	Echo  %%~nb	
	
	if not "%%~na"=="demos" if not "%%~na"=="homebrew" if not "%%~na"=="ports" if not "%%~na"=="xbox" if not "%%~na"=="atarijaguar" if not "%%~na"=="daphne" if not "%%~na"=="neogeocd" (
		Echo 		^<item id^=""^>
		Echo 				^<name^>$INFO^[Skin.String^(%%~na_games^)^]^</name^>
		Echo 				^<systemid^>%%~na^</systemid^>
		Echo 				^<fullname^>%%~nb^</fullname^>
		Echo 				^<systemart^>layouts/%%~na/art/system_art.png^</systemart^>
		Echo 				^<logo^>layouts/%%~na/art/logo.png^</logo^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/menu_loader.py^)^</onclick^>
		Echo 				^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
		Echo 		^</item^>
	)>>"!output!\%%~na.xml"

	if "%%~na"=="atarijaguar" (
		Echo 		^<item id^=""^>
		Echo 				^<name^>Launch Emulator: $INFO^[Skin.String^(%%~na_games^)^]^</name^>
		Echo 				^<systemid^>%%~na^</systemid^>
		Echo 				^<fullname^>%%~nb^</fullname^>
		Echo 				^<systemart^>layouts/%%~na/art/system_art.png^</systemart^>
		Echo 				^<logo^>layouts/%%~na/art/logo.png^</logo^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/direct_launch_emulator.py,1,^)^</onclick^>
		Echo 				^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
		Echo 		^</item^>
	)>>"!output!\%%~na.xml"

	if "%%~na"=="daphne" (
		Echo 		^<item id^=""^>
		Echo 				^<name^>Launch Emulator: $INFO^[Skin.String^(%%~na_games^)^]^</name^>
		Echo 				^<systemid^>%%~na^</systemid^>
		Echo 				^<fullname^>%%~nb^</fullname^>
		Echo 				^<systemart^>layouts/%%~na/art/system_art.png^</systemart^>
		Echo 				^<logo^>layouts/%%~na/art/logo.png^</logo^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/direct_launch_emulator.py,1,^)^</onclick^>
		Echo 				^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
		Echo 		^</item^>
	)>>"!output!\%%~na.xml"

	if "%%~na"=="neogeocd" (
		Echo 		^<item id^=""^>
		Echo 				^<name^>Launch Emulator: $INFO^[Skin.String^(%%~na_games^)^]^</name^>
		Echo 				^<systemid^>%%~na^</systemid^>
		Echo 				^<fullname^>%%~nb^</fullname^>
		Echo 				^<systemart^>layouts/%%~na/art/system_art.png^</systemart^>
		Echo 				^<logo^>layouts/%%~na/art/logo.png^</logo^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/direct_launch_emulator.py,1,^)^</onclick^>
		Echo 				^<visible^>Skin.HasSetting^(%%~na_exists^)^</visible^>
		Echo 		^</item^>
	)>>"!output!\%%~na.xml"
	
	if "%%~na"=="ports" (
		Echo 		^<item id^=""^>
		Echo 				^<name^>$INFO^[Skin.String^(%%~na_games^)^]^</name^>
		Echo 				^<systemid^>%%~na^</systemid^>
		Echo 				^<fullname^>%%~nb^</fullname^>
		Echo 				^<systemart^>layouts/%%~na/art/system_art.png^</systemart^>
		Echo 				^<logo^>layouts/%%~na/art/logo.png^</logo^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/menu_loader.py^)^</onclick^>
		Echo 				^<visible^>IntegerGreaterThan^(Skin.String^(ports_games^),0^)^</visible^>
		Echo 		^</item^>
	)>>"!output!\%%~na.xml"

	if "%%~na"=="homebrew" (
		Echo 		^<item id^=""^>
		Echo 				^<name^>$INFO^[Skin.String^(%%~na_games^)^]^</name^>
		Echo 				^<systemid^>%%~na^</systemid^>
		Echo 				^<fullname^>%%~nb^</fullname^>
		Echo 				^<systemart^>layouts/%%~na/art/system_art.png^</systemart^>
		Echo 				^<logo^>layouts/%%~na/art/logo.png^</logo^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/menu_loader.py^)^</onclick^>
		Echo 				^<visible^>IntegerGreaterThan^(Skin.String^(homebrew_games^),0^)^</visible^>
		Echo 		^</item^>
	)>>"!output!\%%~na.xml"

	if "%%~na"=="demos" (
		Echo 		^<item id^=""^>
		Echo 				^<name^>$INFO^[Skin.String^(%%~na_games^)^]^</name^>
		Echo 				^<systemid^>%%~na^</systemid^>
		Echo 				^<fullname^>%%~nb^</fullname^>
		Echo 				^<systemart^>layouts/%%~na/art/system_art.png^</systemart^>
		Echo 				^<logo^>layouts/%%~na/art/logo.png^</logo^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/menu_loader.py^)^</onclick^>
		Echo 				^<visible^>IntegerGreaterThan^(Skin.String^(demos_games^),0^)^</visible^>
		Echo 		^</item^>
	)>>"!output!\%%~na.xml"
	
	if "%%~na"=="xbox" (
		Echo 		^<item id^=""^>
		Echo 				^<name^>$INFO^[Skin.String^(%%~na_games^)^]^</name^>
		Echo 				^<systemid^>%%~na^</systemid^>
		Echo 				^<fullname^>%%~nb^</fullname^>
		Echo 				^<systemart^>layouts/%%~na/art/system_art.png^</systemart^>
		Echo 				^<logo^>layouts/%%~na/art/logo.png^</logo^>
		Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
		Echo 				^<onclick^>RunScript^(special://emustation_scripts/menu_loader.py^)^</onclick^>
		Echo 				^<visible^>IntegerGreaterThan^(Skin.String^(xbox_games^),0^)^</visible^>
		Echo 		^</item^>
	)>>"!output!\%%~na.xml"

	Set /a count+=1
)
Set /a countalt=1
Set /a tmpname=74
:loop
if !countalt! lss 10 Set tmpname2=0!countalt!
if !countalt! gtr 9 Set tmpname2=!countalt!
Echo  Direct Launch !countalt!
(
	Echo 		^<item id^=""^>
	Echo 				^<name^>Direct Launch^</name^>
	Echo 				^<systemid^>customtile^</systemid^>
	Echo 				^<fullname^>Direct Launch^</fullname^>
	Echo 				^<systemart^>^$INFO^[Skin.String^(CustomHomeTile!countalt!SystemArt^)^]^</systemart^>
	Echo 				^<logo^>^$INFO^[Skin.String^(CustomHomeTile!countalt!Logo^)^]^</logo^>
	Echo 				^<onclick^>SetFocus^(9100^)^</onclick^>
	Echo 				^<onclick^>RunScript^(special://emustation_scripts/direct_launch_emulator.py,0,^$INFO^[Skin.String^(CustomHomeTile!countalt!Xbe^)^]^)^</onclick^>
	Echo 				^<visible^>Skin.HasSetting^(CustomHomeTile!countalt!Enabled^)^</visible^>
	Echo 		^</item^>
	Set /a count+=1
	Set /a countalt+=1
	Set /a tmpname+=1
)>>"!output!\direct launch !tmpname2!.xml"
if not "!tmpname!"=="89" goto loop