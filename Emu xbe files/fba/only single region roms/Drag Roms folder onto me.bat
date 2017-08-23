@echo off
setlocal DisableDelayedExpansion enableextensions

md "Trasnfer to Xbox"

CD %1

for /f "tokens=*" %%a in (..\game_list.txt) do (
	set "tilename=%%~na"

	SetLocal EnableDelayedExpansion 
		move "!tilename!.zip" "..\Trasnfer to Xbox\!tilename!.zip"
	endlocal
)
pause