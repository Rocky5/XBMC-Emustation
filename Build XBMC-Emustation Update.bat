:: Copyright of John Conn (Rocky5 Forums & JCRocky5 Twitter) 2016
:: Please don't re-release this as your own, if you make a better tool then I don't mind :-)

:Start
@Echo off & SetLocal EnableDelayedExpansion & Mode con:cols=100 lines=10 & Color 0B
title XBMC-Emustation Builder

Set "foldername=XBMC-Emustation-update-files"

cls
Echo: & Echo: & Echo: & Echo   Please wait...

(
XCopy /s /e /i /h /r /y "Mod Files" "%foldername%"
XCopy /s /i /h /r /y "Emu xbe files" "%foldername%\_emulators"
Echo:>"%foldername%\system\Faster_Game_Loading.bin"
del /q /s "%foldername%\_emulators\*.bat"
del /q "%foldername%\_emulators\*.info"
copy /y "New XBMC xbe\default.xbe" "%foldername%\default.xbe"
del /q /s "%foldername%\userdata.xml"
rd /q /s "%foldername%\_cuts"
rd /q /s "%foldername%\_roms"
rd /q /s "%foldername%\_tbns"
)
cls
Echo: & Echo:
Echo  Just overwrite your existing install of XBMC-Emustation
Echo  None of your scanned content or settings will be lost.
timeout /t 15 >NUL