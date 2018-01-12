@Echo off

if not exist "layouts" md layouts
for /f "tokens=*" %%a in (systems.txt) do (
	if "%%a"=="dreamcast" (
		move "%%a" "layouts"
		ren "layouts\%%a" "dreamcastvmu"
	)
	if "%%a"=="auto-allgames" (
		move "%%a" "layouts"
		ren "layouts\%%a" "allgames"
	)
	if "%%a"=="auto-favorites" (
		move "%%a" "layouts"
		ren "layouts\%%a" "favourites"
	)
	if "%%a"=="auto-lastplayed" (
		move "%%a" "layouts"
		ren "layouts\%%a" "lastplayed
	)
	move "%%a" "layouts"
)

pause