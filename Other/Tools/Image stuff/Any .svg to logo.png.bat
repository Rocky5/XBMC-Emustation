@Echo off
Setlocal enabledelayedexpansion

if not exist "%~n1" (
Echo:
Echo Drage the folder onto this bat file.
timeout /t 5 >NUL
Exit
)

for /f "Tokens=*" %%a in ('dir /b /s "%~n1\*.svg"') do (
	Echo Converting %%~nxa to %%~na.png
	convert.exe -background none -filter mitchell -resize 480x98 "%%a" png32:"%%~pna.png" 2>NUL
	set "line=%%a"
	set "line=!line:%CD%\=!"
	set "line=!line:%~n1\=!"
	set "line=!line:.svg=.png!"
	(echo(!line!)>tmp
	for /f "Tokens=*" %%b in (tmp) do (
		Echo Moving %%~nb.png
		Echo F | XCopy /S /E "%%~dpna.png" "Converted\%%b" >NUL
		Echo Renaming %%~nb.png to logo.png
		Ren "Converted\%%b" "logo.png"
		del /q "%~n1\%%b"
		del /q tmp
	)
)
timeout /t 5
