@Echo off
Setlocal enabledelayedexpansion

if not exist "%~n1" (
Echo:
Echo Drage the folder onto this bat file.
timeout /t 5 >NUL
Exit
)

for /f "Tokens=*" %%a in ('dir /b /s "%~n1\controller.svg"') do (
	Echo Converting %%~nxa to system_art.png ^& system_art_small.png
	convert.exe -background none -filter mitchell -resize 720x405 "%%a" png32:"%%~pa\system_art.png" 2>NUL
	convert.exe -background none -filter mitchell -resize 190x110 "%%a" png32:"%%~pa\system_art_small.png" 2>NUL
	set "line=%%a"
	set "line=!line:%CD%\=!"
	set "line=!line:%~n1\=!"
	set "line=!line:controller.svg=system_art!"
	(echo(!line!)>tmp
	for /f "Tokens=*" %%b in (tmp) do (
		Echo Moving system_art.png
		Echo Moving system_art_small.png
		Echo F | XCopy /S /E "%~n1\%%b.png" "Converted\%%b.png" >NUL
		Echo F | XCopy /S /E "%~n1\%%b_small.png" "Converted\%%b_small.png" >NUL
		del /q "%~n1\%%b.png"
		del /q "%~n1\%%b_small.png"
		del /q tmp
	)
)
timeout /t 5
