@echo off
setlocal DisableDelayedExpansion enableextensions

md "Trasnfer to Xbox\roms"
md "Trasnfer to Xbox\videos"

CD %1

for /f "tokens=*" %%a in (..\game_list.txt) do (
	set "tilename=%%~na"

	SetLocal EnableDelayedExpansion 
		move "!tilename!.zip" "..\Trasnfer to Xbox\roms\!tilename!.zip"
		move "!tilename!.xmv" "..\Trasnfer to Xbox\videos\!tilename!.xmv"
	endlocal
)
pause