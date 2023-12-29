:: Copyright of John Conn (Rocky5 Forums & JCRocky5 Twitter) 2016
:: Please don't re-release this as your own, if you make a better tool then I don't mind :-)

@Echo off & SetLocal EnableDelayedExpansion & Mode con:cols=100 lines=10 & Color 0B
title XBMC-Emustation Builder

REM Set d=%DATE:~3,2%/%DATE:~0,2%/%DATE:~6,4%
REM Set t=%TIME:~0,2%:%TIME:~3,2%
REM Set d=%d: =0%

REM Echo timestamp=%d% %t%>"%USERPROFILE%\Desktop\New Downloader Builder\Downloader Builder\emustat_r_timestamp"

if exist "XBMC" Set "foldername=XBMC"
if exist "Build" Set "foldername=Build"
if not exist "%foldername%" (
	Echo Error, place a fresh copy of XBMC next to this batch file and try again.
	timeout /t 5
	Exit
)
:Start
Set /p "version="<version.txt
REM Set "fromDate=23/06/2022"
for /F "usebackq tokens=1,2 delims==" %%i in (`wmic os get LocalDateTime /VALUE 2^>NUL`) do if '.%%i.'=='.LocalDateTime.' set dateformat=%%j
Set toDate=%dateformat:~6,2%^/%dateformat:~4,2%^/%dateformat:~0,4%
REM if exist "..\other\build for release.bin" (
	REM (
	REM echo fromDate^=CDate^("%fromDate%"^)
	REM echo toDate^=CDate^("%toDate%"^)
	REM echo WScript.Echo DateDiff^("d",fromDate,toDate,vbMonday^)
	REM )>tmp.vbs
	REM for /f %%a in ('cscript /nologo tmp.vbs') do (
	REM if %%a GEQ 100 Set "daytotal=%%a"
	REM if %%a LSS 100 Set "daytotal=0%%a"
	REM if %%a LSS 10 Set "daytotal=00%%a"
	REM )
	REM del tmp.vbs
REM ) else (
	REM Set daytotal=123
REM )
title XBMC-Emustation Builder - %version%
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

for /f "tokens=*" %%a in ('dir /b "%foldername%\emustation\themes\simple\language"') do (
	Call Other\Tools\repl.bat "xbmc-emustation 0.0.000" "Xbmc-Emustation Stable Build %version%" L < "%foldername%\emustation\themes\simple\language\%%a\strings.po" >"%foldername%\emustation\themes\simple\language\%%a\strings.tmp"
	Del "%foldername%\emustation\themes\simple\language\%%a\strings.po"
	rename "%foldername%\emustation\themes\simple\language\%%a\strings.tmp" "strings.po"
	
	Call Other\Tools\repl.bat "xbmc-emustation datetime" "[CR]Stable Build %version%: %d% - %t%" L < "%foldername%\emustation\themes\simple\language\%%a\strings.po" >"%foldername%\emustation\themes\simple\language\%%a\strings.tmp"
	Del "%foldername%\emustation\themes\simple\language\%%a\strings.po"
	rename "%foldername%\emustation\themes\simple\language\%%a\strings.tmp" "strings.po"

	Call Other\Tools\repl.bat "build type" "Stable_Build" L < "%foldername%\emustation\themes\simple\language\%%a\strings.po" >"%foldername%\emustation\themes\simple\language\%%a\strings.tmp"
	Del "%foldername%\emustation\themes\simple\language\%%a\strings.po"
	rename "%foldername%\emustation\themes\simple\language\%%a\strings.tmp" "strings.po"
)

MD "%foldername%\system\SystemInfo"
Call Other\Tools\repl.bat "	" "" L < "changes.txt" >"%foldername%\system\SystemInfo\changes.txt"
copy /y "Source\default.xbe" "%foldername%\default.xbe"
ren "%foldername%" "XBMC-Emustation"
)>nul 2>&1

cls
Echo: & Echo: & Echo: & Echo   Done...
timeout /t 3 >NUL