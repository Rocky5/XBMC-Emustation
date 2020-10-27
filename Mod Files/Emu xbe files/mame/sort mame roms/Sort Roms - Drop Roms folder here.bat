@echo off
setlocal enableextensions
(
md "Trasnfer to Xbox\working
md "Trasnfer to Xbox\not working"
md "Trasnfer to Xbox\roms with problems\bad colours"
md "Trasnfer to Xbox\roms with problems\bad colours no sound"
md "Trasnfer to Xbox\roms with problems\close colours"
md "Trasnfer to Xbox\roms with problems\partial sound"
md "Trasnfer to Xbox\roms with problems\need samples"
md "Trasnfer to Xbox\roms with problems\no sound"
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

for /f "tokens=*" %%a in (..\txt_files\working-colours_bad.txt) do (
	title Processing Bad Colour Roms.
	set "tilename=%%a"
	if exist "%%a" Echo   %%a
	SetLocal EnableDelayedExpansion 
		move "!tilename!" "..\Trasnfer to Xbox\roms with problems\bad colours\!tilename!" >NUL 2> NUL
	endlocal
	title Processing Bad Colour Roms....
)

for /f "tokens=*" %%a in (..\txt_files\working-colours_bad-no_sound.txt) do (
	title Processing Bad Colour No Sound Roms.
	set "tilename=%%a"
	if exist "%%a" Echo   %%a
	SetLocal EnableDelayedExpansion 
		move "!tilename!" "..\Trasnfer to Xbox\roms with problems\bad colours no sound\!tilename!" >NUL 2> NUL
	endlocal
	title Processing Bad Colour No Sound Roms....
)

for /f "tokens=*" %%a in (..\txt_files\working-colours_close.txt) do (
	title Processing Close Colours Roms.
	set "tilename=%%a"
	if exist "%%a" Echo   %%a
	SetLocal EnableDelayedExpansion 
		move "!tilename!" "..\Trasnfer to Xbox\roms with problems\close colours\!tilename!" >NUL 2> NUL
	endlocal
	title Processing Close Colours Roms....
)

for /f "tokens=*" %%a in (..\txt_files\working-partial_sound.txt) do (
	title Processing Partial Sound Roms.
	set "tilename=%%a"
	if exist "%%a" Echo   %%a
	SetLocal EnableDelayedExpansion 
		move "!tilename!" "..\Trasnfer to Xbox\roms with problems\partial sound\!tilename!" >NUL 2> NUL
	endlocal
	title Processing Partial Sound Roms....
)

for /f "tokens=*" %%a in (..\txt_files\working-partial-needs_samples.txt) do (
	title Processing Need Samples Roms.
	set "tilename=%%a"
	if exist "%%a" Echo   %%a
	SetLocal EnableDelayedExpansion 
		move "!tilename!" "..\Trasnfer to Xbox\roms with problems\need samples\!tilename!" >NUL 2> NUL
	endlocal
	title Processing Need Samples Roms....
)

for /f "tokens=*" %%a in (..\txt_files\working-partial-no_sound.txt) do (
	title Processing No Sound Roms.
	set "tilename=%%a"
	if exist "%%a" Echo   %%a
	SetLocal EnableDelayedExpansion 
		move "!tilename!" "..\Trasnfer to Xbox\roms with problems\no sound\!tilename!" >NUL 2> NUL
	endlocal
	title Processing No Sound Roms....
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

pause