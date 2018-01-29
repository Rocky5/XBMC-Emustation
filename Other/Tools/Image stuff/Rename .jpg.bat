@Echo off
:start
if not exist "%~n1" (
Echo:
Echo Drage the folder onto this bat file.
timeout /t 5 >NUL
Exit
)

Set /p "nameold=Enter Old Name="
Set /p "namenew=Enter New Name="

for /f "Tokens=*" %%a in ('dir /b /s "%~n1\%nameold%.jpg"') do (
	Echo Renaming %nameold%.jpg to %namenew%.jpg
	Ren "%%a" "%namenew%.jpg"
)

timeout /t 5
cls
goto start