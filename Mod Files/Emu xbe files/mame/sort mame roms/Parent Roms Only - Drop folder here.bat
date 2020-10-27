@echo off
setlocal enableextensions
(
md "Trasnfer to Xbox\
) 2> NUL

CD %1

for /f "tokens=*" %%a in (..\txt_files\parent_roms.txt) do (
	title Processing Parent Roms.
	set "tilename=%%a"
	if exist "%%a" Echo   %%a
	SetLocal EnableDelayedExpansion 
		move "!tilename!" "..\Trasnfer to Xbox\!tilename!" >NUL 2> NUL
	endlocal
	title Processing Parent Roms....
)
pause