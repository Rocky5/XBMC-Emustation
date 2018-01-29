@Echo off
Setlocal enabledelayedexpansion

if not exist "%~n1" (
Echo:
Echo Drage the folder onto this bat file.
timeout /t 5 >NUL
Exit
)

Set /p "nameold=Enter .SVG Name="
Set "namenew=system_art"

for /f "Tokens=*" %%a in ('dir /b /s "%~n1\%nameold%.svg"') do (
	Echo Converting %%~nxa to %namenew%.png
	convert.exe -background none -filter mitchell -resize 640x320 "%%a" png32:"%%a.png" 2>NUL
	set "line=%%~dpa"
	set "line=!line:%CD%\=!"
	set "line=!line:%~n1\=!"
	set "line=!line:.svg=!"
	(echo(!line!)>tmp
	for /f "Tokens=*" %%b in (tmp) do (
		Echo Moving %namenew%.png
		Echo F | XCopy /S /E "%%a.png" "Converted\%%b\%namenew%.png" >NUL
		del /q "%%a.png"
		del /q tmp
	)
)
timeout /t 5
