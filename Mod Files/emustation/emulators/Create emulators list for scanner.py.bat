@Echo off
SetLocal EnableDelayedExpansion
:: this batch is used to generate.

Echo EMU_Directories			^= ^[ >"test.xml"
for /f "Tokens=*" %%a in ('dir /b /A:D "*"') do (
	Echo "%%a",
)>>"test.xml"
Echo  ^] ## used to create folders of the supported emulators.>>"test.xml"