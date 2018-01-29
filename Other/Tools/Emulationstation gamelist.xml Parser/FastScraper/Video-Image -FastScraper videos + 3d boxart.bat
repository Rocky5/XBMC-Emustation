@echo off
color 3f
set releaseDate=15.12.2017
title fastscraper ver. %releaseDate%

rem Set ScreenScraper credentials
set username=""
set password=""

rem Dictionary (auto, es, de, fr, en)
set lang=auto

rem Flags - Static parameters
	rem If true, add roms that are not found as an empty gamelist entry.
		set addNotFound=-add_not_found=false

	rem Comma separated order to prefer images, s=snapshot, b=boxart, f=fanart, a=banner, l=logo, 3b=3D boxart, cart=cartridge, clabel=cartridge label, mix3=Standard 3 mix, mix4=Standard 4 mix. (default "b")
		set consoleImg=-console_img="3b"

	rem Comma seperated order to prefer console sources, ss=screenscraper, ovgdb=OpenVGDB, gdb=theGamesDB (default "gdb")
		set consoleSrc=-console_src="ss,gdb"

	rem If true, convert videos for the Raspberry Pi (e.g. 320x240@30fps) NOTE: This needs ffmpeg installed
		set convertVideo=-convert_videos="true"

	rem If false, don't download any images, instead see if the expected file is stored locally already. (default true)
		set downloadImg=-download_images="true"

	rem If true, download marquees.
		set downloadMarquee=-download_marquees="false"

	rem If true, download videos.
		set downloadVideo=-download_videos="true"

	rem Comma separated list of extensions to also include in the scraper.
		set extraExt=-extra_ext=".scummvm,.ipf,.mx1,.mx2,.exe,.ws,.wsc,.wad,.dsk,.tap,.trd,.tzx,.z80,.p,.a0,.crt,.nib,.do,.po"

	rem jpg or png, the format to write the images. (default "jpg")
		set imgFormat=-img_format="png"

	rem The path to use for images in gamelist.xml. (default "images")
		set imagePath=-image_path="./downloaded_images"

	rem  The suffix added after rom name when creating image files. (default "-image")
		set imageSuffix=-image_suffix=""
		
	rem The order to choose for language if there is more than one for a value. (en, fr, es, de, pt) (default "en")
		set langSS=-lang="en,es,pt,de,fr"

	rem Comma separated order to prefer images, s=snap, t=title, m=marquee, c=cabniet, b=boxart, 3b=3D-boxart, fly=flyer. (default "t,m,s,c")
		set mameImg=-mame_img="b,s,fly,m,t"
		
	rem Comma seperated order to prefer mame sources, ss=screenscraper, adb=arcadeitalia, mamedb=mamedb-mirror, gdb=theGamesDB-neogeo (default "adb,gdb")
		set mameSrc=-mame_src="ss"

	rem jpg or png, the format to write the marquees. (default "png")
		set marqueeFormat=-marquee_format="png"

	rem The path to use for marquees in gamelist.xml. (default "images")
		set marqueePath=-marquee_path="./downloaded_images"

	rem The suffix added after rom name when creating marquee files. (default "-marquee")
		set marqueeSuffix=-marquee_suffix="-marquee"

	rem The max height of images. Larger images will be resized.
		set maxHeight=-max_height=328

	rem The max width of images. Larger images will be resized. (default 400)
		set maxWidth=-max_width=328

	rem Don't add thumbnails to the gamelist.
		set noThumb=-no_thumb=true
		
	rem Download the thumbnail for both the image and thumb (faster). (default "false")
		set thumbOnly=-thumb_only=false

	rem Information will be attempted to be downloaded again but won't remove roms that are not scraped.
		set refreshXML=-refresh=false

	rem The order to choose for region if there is more than one for a value. xx is a special region that will choose any region. (default "us,wor,eu,jp,fr,xx")
		set regionSS=-region="us,wor,eu,jp,fr,xx"

	rem The `username` for registered ScreenScraper users.
		set username=-ss_user=%username%

	rem The `password` for registered ScreenScraper users.
		set password=-ss_password=%password%
	
	rem If true, use the filename minus the extension as the game title in xml.
		set useFilename=-use_filename=false

	rem Use the name in the No-Intro DB instead of the one in the GDB. (default true)
		set useNoIntroName=-use_nointro_name=true

    rem The path to use for videos in gamelist.xml. (default "images")
		set videoPath=-video_path="./downloaded_images"

    rem The suffix added after rom name when creating video files. (default "-video")
		set videoSuffix=-video_suffix=""

	rem Use N worker threads to process roms. (default 1)
		set workersN=-workers=4

rem Create dictionary
	rem Change the code page to Unicode/65001
		chcp 65001 >nul

	rem Get OS's language
		for /F "tokens=3" %%a in ('reg Query "HKCU\Control Panel\Desktop" /V PreferredUILanguages ^| find "PreferredUILanguages"') do set language=%%a
		set language=%language:~0,-3%

	rem Select dictionary
		for %%a in (es de fr en) do (
			if "%%a"=="%lang%" set language=%lang%
		)
				if "%language%"=="es" goto es
				if "%language%"=="de" goto de
				if "%language%"=="fr" goto fr
				goto *
		
		:es
			set "dict=ERROR: Sin conexión a internet. Saliendo...;no es una plataforma soportada.;ERROR: Imposible descargar el scraper. Saliendo...;ERROR: Imposible descomprimir el scraper. Saliendo...;ERROR: Imposible comprobar actualizaciones en GitHub.;Actualizando sselph scraper de;a;, espere por favor...;Descargando sselph scraper;Abriendo Explorador de Carpetas...;Explorador de Carpetas para;aun no implementado, lo siento!;Carpeta de roms seleccionada:;No olvides detener EmulationStation antes de scrapear!;¿Qué sistema(s) desea scrapear? Escribe "all" para todos los sistemas o "cd" para abrir el navegador de carpetas.;Entrada incorrecta!;¿Deseas anexar los gamelists existentes? [Y/N]:;Scrapeando;en progreso. Espere por favor...;Inicio;Fin;Duración;Por favor, seleccione la carpeta de roms; Scrapeado finalizado!" & goto createDict
		:de
			set "dict=FEHLER: Keine Internetverbindung verfügbar. Beenden...;ist kein unterstütztes Betriebssystem.;FEHLER: Scraper konnte nicht heruntergeladet werden. Beenden...;FEHLER: Scraper konnte nicht entpackt werden. Beenden...;FEHLER: Suche nach Updates auf GitHub fehlgeschlagen.;Update sselph scraper von;auf; wird durchgeführt, bitte warten...;Download sselph scraper;Öffne Ordner Browser...;Ordner Browser für;noch nicht implementiert, entschuldige!;Ausgewählter roms Ordner:;Vergiss nicht EmulationStation vor dem Scrapen zu beenden!;Welche(s) System(e) möchtest du scrapen? Tippe "all" für alle Systeme oder "cd", um den Ordner Browser zu öffnen.;Ungültige Eingabe!;Möchtest du die bestehende gamelists erweitern? [Y/N]:;Scrapen;in Arbeit. Bitte warten...;Beginn;Ende;Dauer;Bitte wählen Sie den Ordner roms;Scrapen ist beendet!" & goto createDict
		:fr
			set "dict=ERREUR : Pas de connexion internet disponible. Quitter...;n'est pas une plateforme prise en charge.;ERREUR : Impossible de télécharger le scraper. Quitter...;ERREUR : Impossible de décompresser le scraper. Quitter...;ERREUR : Impossible de rechercher les mises à jour sur GitHub.;La mise à jour de sselph scraper de;à;, veuillez patienter...;Le téléchargement sselph scraper;Ouverture du Navigateur de Dossier...;Navigateur de Dossier pour;pas encore mis en oeuvre, désolé !;Dossier roms sélectionné :;N'oubliez pas d'arrêter de EmulationStation avant de scrapez !;Quel(s) système(s) souhaitez-vous scrapez ? Tapez « all » pour tous les systèmes ou « cd » pour ouvrir le dossier du navigateur.;Entrée incorrecte !;Vous souhaitez ajouter les gamelists ? [Y/N] :;Scrapez;en course. Veuillez patienter...;Démarrer;Terminer;Durée;Veuillez choisir le dossier de roms;Scrapez est terminé !" & goto createDict
		:*
			if not "%language%"=="en" echo Can't get OS's language. English will be used.
			set "dict=ERROR: No internet connection available. Exiting...;is not a supported platform.;ERROR: Unable to download the scraper. Exiting...;ERROR: Couldn't unzip the scraper. Exiting...;ERROR: Unable to check for updates on GitHub.;Updating sselph scraper from;to;, please wait...;Downloading sselph scraper;Opening Folder Browser...;Folder Browser for;not implemented yet, sorry!;Selected roms folder:;Don't forget to stop EmulationStation before scraping!;Which system(s) do you want to scrape? Type "all" for all systems or "cd" to open the folder browser.;Incorrect input!;Would you like to append existing gamelists? [Y/N]:;Scraping;in progress. Please wait...;Start;Finish;Duration;Please choose the roms folder;Scraping has finished!"
		
		:createDict
		set /A count=-1
		call :parseDict "%dict%"

			:parseDict
			set /A count+=1
			for /F "tokens=1* delims=;" %%i in ("%~1") do (
				set dict[%count%]=%%i
				call :parseDict "%%j"
			)

rem Check internet connection
ping 8.8.8.8 -n 1 -w 1000 >nul
if errorlevel 1 echo %dict[0]% & pause >nul & exit

rem Set default roms directory to launch directory
set "romsDir=%cd%"	

:scraperEXE
rem Detect OS architecture
reg Query "HKLM\Hardware\Description\System\CentralProcessor\0" | find /I "x86" >nul && set arch=386 || set arch=amd64

rem Query the API to get the latest tag
set "Uri=https://api.github.com/repos/sselph/scraper/releases/latest"
for /F "delims=" %%a in ('PowerShell Invoke-RestMethod -Method Get -Uri %Uri% ^| find /I "tag_name"') do (
	for /F "tokens=3" %%b in ("%%a") do set scraperVersion=%%b
)

rem Download or update scraper if needed
if exist "scraper.exe" (
	for /F "tokens=* usebackq" %%a in (`scraper.exe -version`) do (
		if "%%a" GEQ "%scraperVersion%" goto systemSelection
		if "%scraperVersion%"=="" echo %dict[4]% & echo. & goto systemSelection
		echo %dict[5]% %%a %dict[6]% %scraperVersion%%dict[7]% & echo.
	)
) else echo %dict[8]% %scraperVersion%%dict[7]% & echo.

rem Build the file name, download url and download the file to the current location
set scraperZip=scraper_windows_%arch%.zip
set scraperURL=https://github.com/sselph/scraper/releases/download/%scraperVersion%/%scraperZip%
PowerShell (New-Object System.Net.WebClient).DownloadFile('%scraperURL%', '%~dp0%scraperZip%')

rem Unzip the scraper and remove unnecessary files
if exist "%scraperZip%" (
	PowerShell Expand-Archive -Path '%scraperZip%' -DestinationPath '.\' -Force
	del LICENSE.txt %scraperZip%	
) else echo %dict[2]% & pause >nul & exit
	
:systemSelection
rem Select the system to scrape (type "all" to scrape all folders)
setlocal EnableDelayedExpansion
echo %dict[14]%
set /P "system="
if "%system%"=="cd" goto SUB_folderBrowser
if "%system%"=="" echo %dict[15]% & goto systemSelection
if /I not "%system%"=="all" goto modeSelection
	set "system="
	for /F "delims=" %%f in ('dir /B /A:D') do set system=!system! %%f

:modeSelection
rem Choose to append an existing (y) or create a new gamelist (n)
if "%refreshXML%"=="-refresh=true" goto fullMode
set /P "appendXML=%dict[16]% "
if /I "%appendXML%"=="y" goto appendMode
if /I "%appendXML%"=="n" goto fullMode
echo %dict[15]% & goto modeSelection

	:appendMode
	set appendMode=-append & goto startTime

	:fullMode
	set "appendMode="

:startTime
rem Save start time
set startTime=%time%

rem ******************** MAIN CODE SECTION

for %%i in (%system%) do (

rem Check if mame device is selected and set corresponding flags
	set "arcade="
	echo %%i | findstr /LIC:"arcade" >nul && set arcade=-mame %mameImg% %mameSrc%
	echo %%i | findstr /LIC:"fba" >nul && set arcade=-mame %mameImg% %mameSrc%
	echo %%i | findstr /LIC:"mame" >nul && set arcade=-mame %mameImg% %mameSrc%
	echo %%i | findstr /LIC:"neogeo" >nul && set arcade=-mame %mameImg% %mameSrc%

rem If mame device, consoleImg not used
	if not "!arcade!"=="" set "consoleImg="

	echo.
	title fastscraper ver. %releaseDate% - %dict[17]% %%i...

rem Scraping roms
	echo %dict[17]% %%i %dict[18]%
	echo.
"%~dp0scraper.exe" %appendMode% !arcade! -rom_dir="%%i" %imagePath% -image_dir="%%i\%imagePath:~15,-1%" %imageSuffix% %marqueePath% -marquee_dir="%%i\%marqueePath:~17,-1%" %marqueeSuffix% %videoPath% -video_dir="%%i\%videoPath:~15,-1%" %videoSuffix% %convertVideo% -output_file="%%i\gamelist.xml" -missing="%%i\_%%i_missing.txt" %addNotFound% !consoleImg! %consoleSrc% %downloadImg% %downloadMarquee% %downloadVideo% %extraExt% %imgFormat% %marqueeFormat% %langSS% %maxHeight% %maxWidth% %noThumb% %thumbOnly% %refreshXML% %regionSS% %username% %password% %useFilename% %useNoIntroName% %workersN%
	echo.
)

rem ******************** END MAIN CODE SECTION

setlocal DisableDelayedExpansion
title fastscraper ver. %releaseDate% - %dict[23]%

rem Save finish time
set endTime=%time%

rem Change formatting for the start and end times
    for /F "tokens=1-4 delims=:.," %%a in ("%startTime%") do (
       set /A "start=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100"
    )

    for /F "tokens=1-4 delims=:.," %%a in ("%endTime%") do (
       set /A "end=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100"
    )

    rem Calculate the duration by subtracting values
    set /A elapsed=end-start
	
	rem Correct if the measurement was in between days (8640000 centisec/day)
	if %end% lss %start% set /A elapsed=end-start+8640000

    rem Format the results for output
    set /A hh=elapsed/(60*60*100), rest=elapsed%%(60*60*100), mm=rest/(60*100), rest%%=60*100, ss=rest/100, cc=rest%%100
    if %hh% lss 10 set hh=0%hh%
    if %mm% lss 10 set mm=0%mm%
    if %ss% lss 10 set ss=0%ss%
    if %cc% lss 10 set cc=0%cc%

    set DURATION=%hh%:%mm%:%ss%,%cc%

    echo %dict[19]%		: %startTime%
    echo %dict[20]%		: %endTime%
    echo          	---------------
    echo %dict[21]%	: %DURATION%
	
popd & pause >nul & exit

:SUB_folderBrowser
setlocal DisableDelayedExpansion
echo.
echo %dict[9]%

rem PowerShell-Subroutine to open a Folder Browser
set "psCommand="(New-Object -COM Shell.Application)^
.BrowseForFolder(0,'%dict[22]%.',0,0).self.path""
for /F "usebackq delims=" %%i in (`PowerShell %psCommand%`) do set "newRoot=%%i"

set "romsDir=%newRoot%"
cls & pushd "%romsDir%" & echo %dict[12]% %romsDir%
rem Check if scraping from network drive and show warning about stopping ES
if not x%romsDir:\\=%==x%romsDir% echo %dict[13]%
echo. & goto systemSelection