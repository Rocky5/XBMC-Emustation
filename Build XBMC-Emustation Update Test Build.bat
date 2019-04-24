:: Copyright of John Conn (Rocky5 Forums & JCRocky5 Twitter) 2016
:: Please don't re-release this as your own, if you make a better tool then I don't mind :-)

@Echo off & SetLocal EnableDelayedExpansion & Mode con:cols=100 lines=10 & Color 0B
title XBMC-Emustation Builder

Attrib /s -r -h -s "Thumbs.db" >NUL
Del /Q /S "Thumbs.db" 2>NUL
for /F "usebackq tokens=1,2 delims==" %%i in (`wmic os get LocalDateTime /VALUE 2^>NUL`) do if '.%%i.'=='.LocalDateTime.' set dateformat=%%j

cls

:Start
Set "foldername=update-files"
Set "version=1.2"
Set "fromDate=20/12/2018"
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
cls
Echo: & Echo: & Echo: & Echo   Please wait...

(
XCopy /s /e /i /h /r /y "Mod Files" "%foldername%"
XCopy /s /i /h /r /y "Emu xbe files" "%foldername%\.emustation\emulators"
del /q /s "%foldername%\.emustation\emulators\*.bat"
del /q /s "%foldername%\.emustation\emulators\place emulators files in here"
del /q "%foldername%\.emustation\emulators\*.info"
rd /q /s "%foldername%\.emustation\scripts\not used"
copy /y "New XBMC xbe\default.xbe" "%foldername%\default.xbe"
del /q /s "%foldername%\system\userdata\guisettings.xml"
rd /q /s "%foldername%\.emustation\roms"
rd /q /s "%foldername%\.emustation\media"
rd /q /s "%foldername%\.emustation\themes\simple\media\Use for custom home layouts"
)
copy /y "Changes.txt" "%foldername%"
Call Other\Tools\repl.bat "XBMC-Emustation 0.0.000" "XBMC-Emustation Test Build 1.1.%daytotal%" L < "%foldername%\.emustation\themes\simple\language\English\strings.po" >"%foldername%\.emustation\themes\simple\language\English\strings.tmp"
Del "%foldername%\.emustation\themes\simple\language\English\strings.po"
rename "%foldername%\.emustation\themes\simple\language\English\strings.tmp" "strings.po"
Call Other\Tools\repl.bat "	" "" L < "%foldername%\changes.txt" >"%foldername%\changes.tmp"
copy /b "Other\Tools\Changes\Changes_Header.xml"+"%foldername%\changes.tmp"+"Other\Tools\Changes\Changes_Footer.xml" "%foldername%\.emustation\themes\simple\720p\Custom_Changes.xml"
del /q "%foldername%\changes.tmp"
CD %foldername%\
del /Q "Changes.txt"
"C:\Program Files\7-Zip\7z.exe" a "..\Other\update build\updater\Update Files\%foldername%.zip" "*" -mx=7 -r -y
"C:\Program Files\7-Zip\7z.exe" a "..\XBMC-Emustation-test-build.zip" "..\Other\update build\*" -mx=0 -r -y
del /Q "..\Other\update build\updater\Update Files\%foldername%.zip"
cls
Echo: & Echo:
Echo  Just overwrite your existing install of XBMC-Emustation
Echo  None of your scanned content or settings will be lost.
timeout /t 15 >NUL