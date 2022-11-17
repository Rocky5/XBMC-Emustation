:: Copyright of John Conn (Rocky5 Forums & JCRocky5 Twitter) 2016
:: Please don't re-release this as your own, if you make a better tool then I don't mind :-)

@Echo off & SetLocal EnableDelayedExpansion & Mode con:cols=100 lines=10 & Color 0B
title XBMC-Emustation Builder

if exist "XBMC" Set "foldername=XBMC"
if exist "Build" Set "foldername=Build"
if not exist "%foldername%" (
	Echo Error, place a fresh copy of XBMC next to this batch file and try again.
	timeout /t 5
	Exit
)
:Start
Set "version=1.4"
Set "fromDate=23/06/2022"
for /F "usebackq tokens=1,2 delims==" %%i in (`wmic os get LocalDateTime /VALUE 2^>NUL`) do if '.%%i.'=='.LocalDateTime.' set dateformat=%%j
Set toDate=%dateformat:~6,2%^/%dateformat:~4,2%^/%dateformat:~0,4%
if exist "..\other\build for release.bin" (
	(
	echo fromDate^=CDate^("%fromDate%"^)
	echo toDate^=CDate^("%toDate%"^)
	echo WScript.Echo DateDiff^("d",fromDate,toDate,vbMonday^)
	)>tmp.vbs
	for /f %%a in ('cscript /nologo tmp.vbs') do (
	if %%a GEQ 100 Set "daytotal=%%a"
	if %%a LSS 100 Set "daytotal=0%%a"
	if %%a LSS 10 Set "daytotal=00%%a"
	)
	del tmp.vbs
) else (
	Set daytotal=123
)
Set "daytotal=001"
title XBMC-Emustation Builder - %version%.%daytotal%
cls
Echo: & Echo: & Echo: & Echo   Preping files & Echo   Please wait...
(
Attrib /s -r -h -s "desktop.ini"
Attrib /s -r -h -s "Thumbs.db"
Del /Q /S "desktop.ini"
Del /Q /S "Thumbs.db"
rd /q /s "%foldername%\plugins"
rd /q /s "%foldername%\sounds"
rd /q /s "%foldername%\userdata"
rd /q /s "%foldername%\visualisations"
rd /q /s "%foldername%\web"
rd /q /s "%foldername%\system\keymaps"
rd /q /s "%foldername%\system\cdrip"
rd /q /s "%foldername%\system\scrapers"
rd /q /s "%foldername%\system\players\mplayer\codecs"
rd /q /s "%foldername%\skin"
rd /q /s "%foldername%\scripts"
rd /q /s "%foldername%\screensavers"
del /q "%foldername%\system\filezilla server.xml"
del /q "%foldername%\copying.txt"
del /q "%foldername%\keymapping.txt"
del /q "%foldername%\media\icon.png"
del /q "%foldername%\media\Splash_2007.png"
del /q "%foldername%\media\Splash_2008.png"
del /q "%foldername%\media\weather.rar"
move "%foldername%\media" "%foldername%\system\"
move "%foldername%\language" "%foldername%\system\"
move "%foldername%\media" "%foldername%\system\"
move "%foldername%\screenshots" "%foldername%\system\"
move "%foldername%\UserData" "%foldername%\system\"
XCopy /s /e /i /h /r /y "Mod Files" "%foldername%"
XCopy /s /i /h /r /y "Other\update images" "%foldername%\system\media\update\"
XCopy /s /i /h /r /y "Mod Files\Emu xbe files" "%foldername%\emustation\emulators"
del /q /s "%foldername%\emustation\emulators\*.bat"
del /q "%foldername%\emustation\emulators\system_list.txt"
del /q /s "%foldername%\emustation\emulators\place emulators files in here"
del /q "%foldername%\emustation\emulators\*.info"
del /q /s "%foldername%\emustation\roms\roms go here"
del /q /s "%foldername%\emustation\media\media goes here"
rd /q /s "%foldername%\emustation\scripts\not used"
rd /q /s "%foldername%\Emu xbe files"
copy /y "Changes.txt" "%foldername%"
Call Other\Tools\repl.bat "xbmc-emustation 0.0.000" "xbmc-emustation %version%.%daytotal%" L < "%foldername%\emustation\themes\simple\language\English\strings.po" >"%foldername%\emustation\themes\simple\language\English\strings.tmp"
Del "%foldername%\emustation\themes\simple\language\English\strings.po"
rename "%foldername%\emustation\themes\simple\language\English\strings.tmp" "strings.po"
Call Other\Tools\repl.bat "	" "" L < "%foldername%\changes.txt" >"%foldername%\changes.tmp"
copy /b "Other\Tools\Changes\Changes_Header.xml"+"%foldername%\changes.tmp"+"Other\Tools\Changes\Changes_Footer.xml" "%foldername%\emustation\themes\simple\xml\Custom_Changes.xml"
del /q "%foldername%\changes.tmp"
del /Q "%foldername%\Changes.txt"
copy /y "Source\default.xbe" "%foldername%\default.xbe"
ren "%foldername%" "XBMC-Emustation"
)>nul 2>&1

cls
Echo: & Echo: & Echo: & Echo   Done...
timeout /t 3 >NUL