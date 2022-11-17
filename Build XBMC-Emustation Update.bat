:: Copyright of John Conn (Rocky5 Forums & JCRocky5 Twitter) 2016
:: Please don't re-release this as your own, if you make a better tool then I don't mind :-)

@Echo off & SetLocal EnableDelayedExpansion & Mode con:cols=100 lines=10 & Color 0B
title XBMC-Emustation Builder

:Start
Set "foldername=update-files"
Set "output_zip=XBMC-Emustation-update-files.zip"
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
	Set daytotal=0
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
XCopy /s /e /i /h /r /y "Mod Files" "%foldername%"
XCopy /s /i /h /r /y "Other\update images" "%foldername%\system\media\update\"
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
copy /y "Changes.txt" "%foldername%"
Call Other\Tools\repl.bat "xbmc-emustation 0.0.000" "xbmc-emustation %version%.%daytotal%" L < "%foldername%\emustation\themes\simple\language\English\strings.po" >"%foldername%\emustation\themes\simple\language\English\strings.tmp"
Del "%foldername%\emustation\themes\simple\language\English\strings.po"
rename "%foldername%\emustation\themes\simple\language\English\strings.tmp" "strings.po"
Call Other\Tools\repl.bat "	" "" L < "%foldername%\changes.txt" >"%foldername%\changes.tmp"
copy /b "Other\Tools\Changes\Changes_Header.xml"+"%foldername%\changes.tmp"+"Other\Tools\Changes\Changes_Footer.xml" "%foldername%\emustation\themes\simple\xml\Custom_Changes.xml"
del /q "%foldername%\changes.tmp"
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
Echo  Current version: xbmc-emustation test build %version%.%daytotal%
timeout /t 15 >NUL