:: Copyright of John Conn (Rocky5 Forums & JCRocky5 Twitter) 2016
:: Please don't re-release this as your own, if you make a better tool then I don't mind :-)

:Start
@Echo off & SetLocal EnableDelayedExpansion & Mode con:cols=100 lines=10 & Color 0B
title XBMC-Emustation Builder

if exist "XBMC" Set "foldername=XBMC"
if exist "Build" Set "foldername=Build"
if not exist "%foldername%" Exit

cls
Echo: & Echo: & Echo: & Echo   Please wait...

(
rd /q /s "%foldername%\plugins"
rd /q /s "%foldername%\sounds"
rd /q /s "%foldername%\userdata"
rd /q /s "%foldername%\visualisations"
rd /q /s "%foldername%\web"
rd /q /s "%foldername%\system\keymaps"
rd /q /s "%foldername%\system\cdrip"
rd /q /s "%foldername%\system\scrapers"
rd /q /s "%foldername%\system\players\mplayer\codecs"
del /q /s "%foldername%\copying.txt"
del /q /s "%foldername%\keymapping.txt"
del /q /s "%foldername%\media\icon.png"
del /q /s "%foldername%\media\Splash_2007.png"
del /q /s "%foldername%\media\Splash_2008.png"
del /q /s "%foldername%\media\weather.rar"
rd /q /s "%foldername%\skin"
rd /q /s "%foldername%\scripts"
rd /q /s "%foldername%\screensavers"
move "%foldername%\media" "%foldername%\system\"
md "%foldername%\skin"
XCopy /s /e /i /h /r /y "Mod Files" "%foldername%"
copy /y "New XBMC xbe\default.xbe" "%foldername%\default.xbe"
Echo:>"%foldername%\system\Faster_Game_Loading.bin"
move "%foldername%\language" "%foldername%\system\"
move "%foldername%\media" "%foldername%\system\"
move "%foldername%\screenshots" "%foldername%\system\"
move "%foldername%\UserData" "%foldername%\system\"
rd /q /s "%foldername%\Apps\FTP"
rd /q /s "%foldername%\Updater"
rd /q /s "%foldername%\skin"
del /q /s "%foldername%\_emulators\*.bat"
XCopy /s /i /h /r /y "Emu xbe files" "%foldername%\_emulators"
del /q "%foldername%\_emulators\*.info"
ren "%foldername%" "XBMC-Emustation"
)
cls
Echo:
Echo: & Echo: & Echo: & Echo   Done...
timeout /t 3 >NUL