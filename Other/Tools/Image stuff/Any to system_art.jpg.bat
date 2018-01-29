@Echo off
Setlocal enabledelayedexpansion

if not exist "%~n1" (
Echo:
Echo Drage the folder onto this bat file.
timeout /t 5 >NUL
Exit
)

for /f "Tokens=*" %%a in ('dir /b /s /A:-D "%~n1\*.*"') do (
	Echo Converting %%~na to system_art.jpg
	convert.exe "%%a" -filter mitchell -resize 640x320 "%%~pna..jpg" 2>NUL
	set "line=%%a"
	set "line=!line:%CD%\=!"
	set "line=!line:%~n1\=!"
	set "line=!line:\art\%%~nxa=!"
	md "converted\!line!\art" 2>NUL
	move "%%~pna..jpg" "%CD%\converted\!line!\art\system_art.jpg" >NUL
)
timeout /t 5
