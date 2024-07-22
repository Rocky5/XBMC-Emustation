:: Copyright of John Conn (Rocky5 Forums & JCRocky5 Twitter) 2016
:: Please don't re-release this as your own, if you make a better tool then I don't mind :-)

@Echo off & SetLocal EnableDelayedExpansion & Mode con:cols=100 lines=10 & Color 0B
title XBMC-Emustation Builder

Set d=%DATE:~0,2%/%DATE:~3,2%/%DATE:~6,4%
Set t=%TIME:~0,2%:%TIME:~3,2%
Set d=%d: =0%
Set t=%t: =0%

:Start
Set "foldername=update-files"
Set "output_zip=XBMC-Emustation-update-files.zip"
Set /p "version="<version.txt

REM Set "fromDate=23/06/2022"
REM for /F "usebackq tokens=1,2 delims==" %%i in (`wmic os get LocalDateTime /VALUE 2^>NUL`) do if '.%%i.'=='.LocalDateTime.' set dateformat=%%j
REM Set toDate=%dateformat:~6,2%^/%dateformat:~4,2%^/%dateformat:~0,4%
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
	REM Set daytotal=0
REM )

title XBMC-Emustation Update Builder ^(Test^) - %version%

Set /p "buildTSV="<RC.txt
if "%buildTSV%"=="true" (
	title XBMC-Emustation Update Builder ^(Release^) - %version%
	Echo timestamp=%d% %t%>"%USERPROFILE%\Desktop\New Downloader Builder\Downloader Builder\emustat_u_timestamp"
	Echo version=%version%>"%USERPROFILE%\Desktop\New Downloader Builder\Downloader Builder\emustat_u_version"
)

cls
Echo: & Echo: & Echo: & Echo   Preping files & Echo   Please wait...
(
Attrib /s -r -h -s "desktop.ini"
Attrib /s -r -h -s "Thumbs.db"
Del /Q /S "desktop.ini"
Del /Q /S "Thumbs.db"
XCopy /s /e /i /h /r /y "Mod Files" "%foldername%"
move "%foldername%\emustation\emulators" "Other\"
del /q /s "Other\emulators\*.bat"
del /q "Other\emulators\system_list.txt"
XCopy /s /i /h /r /y "Mod Files\Emu xbe files" "Other\emulators"
del /q /s "Other\emulators\place emulators files in here"
del /q "Other\emulators\*.info"
del /q /s "Other\emulators\xspectrum.ini"
del /q /s "Other\emulators\virtualboyx.ini"
del /q /s "Other\emulators\mednafenx_pce.ini"
del /q /s "Other\emulators\snes9xbox.ini"
del /q /s "Other\emulators\neogensplusgx.ini"
del /q /s "Other\emulators\pcsx.ini"
del /q /s "Other\emulators\neopopx.ini"
del /q /s "Other\emulators\mednafenx_nes.ini"
del /q /s "Other\emulators\xboyadvance.ini"
rd /q /s "%foldername%\emustation\scripts\not used"
rd /q /s "%foldername%\Emu xbe files"
copy /y "Source\default.xbe" "%foldername%\default.xbe"
del /q /s "%foldername%\system\userdata\guisettings.xml"
del /q /s "%foldername%\system\userdata\advancedsettings.xml"
rd /q /s "%foldername%\emustation\roms"
rd /q /s "%foldername%\emustation\media"																			   
)>nul 2>&1

cls
Echo: & Echo: & Echo: & Echo   Creating archives & Echo   Please wait...
(

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
CD %foldername%\
del /Q "Changes.txt"
"C:\Program Files\7-Zip\7z.exe" a "..\Other\update build\updater\Update Files\%foldername%-emus.zip" "..\Other\emulators\*" -mx=7 -r -y
"C:\Program Files\7-Zip\7z.exe" a "..\Other\update build\updater\Update Files\%foldername%.zip" "*" -mx=7 -r -y
"C:\Program Files\7-Zip\7z.exe" a "..\%output_zip%" "..\Other\update build\*" -mx=7 -r -y
cd ..\
del /Q "Other\update build\updater\Update Files\%foldername%-emus.zip"
del /Q "Other\update build\updater\Update Files\%foldername%.zip"
rd /q /s "Other\emulators"
rd /q /s "update-files"																			   
)>nul 2>&1

cls
Echo: & Echo: & Echo: & Echo:
Echo  Current version: xbmc-emustation Stable Build %version%
timeout /t 15 >NUL