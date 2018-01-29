@Echo off & mode con:cols=110 lines=18 & color 0B & Title parse emulationstation gamelist.xml
Echo:
Echo  Python script and bat file by Rocky5
Echo:
Echo  This is used to parse and extract information from gamelist.xml files so they can
Echo  be used on the xbox as synopsis files for XBMC-Emustation.
Echo:
Echo  Other Info:
Echo  Gamelist.xml is created by EmulationStation or Scraper.exe ( GitHub - sselph/scraper )
Echo  You can combine scraper.exe with fastscraper.bat ( GitHub - paradadf/recaltools )
Echo:
Echo  Gamelist.xml locations:
Echo  If using EmulationStation: ".emulationstation\gamelists\<system name>"
Echo  If using scraper.exe/fastscraper.bat: ".emulationstation\roms\<system name>"
Echo:
Echo:
Echo:
Echo  Press any key to continue.
timeout /t 180 >NUL
cls
if not exist "gamelist.xml" Echo: & Echo  Error! No gamelist.xml found &timeout /t 5 & exit
Echo:
Echo  What System does the gamelist.xml belong to?
Echo:
Set /p "folder=Enter system name now = "
Echo:
python "parser_script.py" "%folder%"
timeout /t 5