@echo off
setlocal enableextensions
(
md "Trasnfer to Xbox\working
md "Trasnfer to Xbox\not working"
md "Trasnfer to Xbox\roms with problems"
md "Trasnfer to Xbox\demos"
md "Trasnfer to Xbox\bios"
) 2> NUL

CD %1

for /f "tokens=*" %%a in (..\txt_files\working.txt) do (
	title Processing Working Roms.
	set "tilename=%%a"
	if exist "%%a" Echo   %%a
	SetLocal EnableDelayedExpansion 
		move "!tilename!" "..\Trasnfer to Xbox\working\!tilename!" >NUL 2> NUL
	endlocal
	title Processing Working Roms....
)

for /f "tokens=*" %%a in (..\txt_files\not_working.txt) do (
	title Processing Not Working Roms.
	set "tilename=%%a"
	if exist "%%a" Echo   %%a
	SetLocal EnableDelayedExpansion 
		move "!tilename!" "..\Trasnfer to Xbox\not working\!tilename!" >NUL 2> NUL
	endlocal
	title Processing Not Working Roms....
)

for /f "tokens=*" %%a in (..\txt_files\imperfect.txt) do (
	title Processing Not Imperfect Roms.
	set "tilename=%%a"
	if exist "%%a" Echo   %%a
	SetLocal EnableDelayedExpansion 
		move "!tilename!" "..\Trasnfer to Xbox\roms with problems\!tilename!" >NUL 2> NUL
	endlocal
	title Processing Not Imperfect Roms....
)

for /f "tokens=*" %%a in (..\txt_files\demo_files.txt) do (
	title Processing Demos.
	set "tilename=%%a"
	if exist "%%a" Echo   %%a
	SetLocal EnableDelayedExpansion 
		move "!tilename!" "..\Trasnfer to Xbox\demos\!tilename!" >NUL 2> NUL
	endlocal
	title Processing Demos....
)

for /f "tokens=*" %%a in (..\txt_files\bios_files.txt) do (
	title Processing Bios.
	set "tilename=%%a"
	if exist "%%a" Echo   %%a
	SetLocal EnableDelayedExpansion 
		move "!tilename!" "..\Trasnfer to Xbox\bios\!tilename!" >NUL 2> NUL
	endlocal
	title Processing Bios....
)

pause