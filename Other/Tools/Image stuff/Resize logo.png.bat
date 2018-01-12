@Echo off
Setlocal enabledelayedexpansion

if not exist "%~n1" (
Echo:
Echo Drage the folder onto this bat file.
timeout /t 5 >NUL
Exit
)

for /f "Tokens=*" %%a in ('dir /b /s /A:-D "%~n1\logo.png"') do (
	Echo Converting %%~na to logo.png
	convert.exe -filter mitchell -resize 480x98 "%%a" png32:"%%~pna..png" 2>NUL
	set "line=%%a"
	set "line=!line:%CD%\=!"
	set "line=!line:%~n1\=!"
	set "line=!line:\art\%%~nxa=!"
	md "converted\!line!\art" 2>NUL
	move "%%~pna..png" "%CD%\converted\!line!\art\logo.png" >NUL
)
timeout /t 5
