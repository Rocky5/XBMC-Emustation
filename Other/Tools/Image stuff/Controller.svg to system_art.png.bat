@Echo off
Setlocal enabledelayedexpansion

if not exist "%~n1" (
Echo:
Echo Drage the folder onto this bat file.
timeout /t 5 >NUL
Exit
)

for /f "Tokens=*" %%a in ('dir /b /s "%~n1\controller.svg"') do (
	Echo Converting %%~nxa to system_art.png
	convert.exe -background none -filter mitchell -resize 640x320 "%%a" png32:"%%~pa\system_art.png" 2>NUL
	set "line=%%a"
	set "line=!line:%CD%\=!"
	set "line=!line:%~n1\=!"
	set "line=!line:controller.svg=system_art!"
	(echo(!line!)>tmp
	for /f "Tokens=*" %%b in (tmp) do (
		Echo Moving system_art.png
		Echo F | XCopy /S /E "%~n1\%%b.png" "Converted\%%b.png" >NUL
		del /q "%~n1\%%b.png"
		del /q tmp
	)
)
timeout /t 5
