@echo off
setlocal enableextensions

md "bios"

CD %1

for /f "tokens=*" %%a in (..\txt_files\bios_list.txt) do (
	title Processing Bios Files.
	set "tilename=%%a"
	if exist "%%a" Echo   %%a
	SetLocal EnableDelayedExpansion 
		move "!tilename!" "..\bios\!tilename!" >NUL 2> NUL
	endlocal
	title Processing Bios Files....
)
pause