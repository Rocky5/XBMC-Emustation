@echo off
if not exist "output" md output
for /f "tokens=*" %%a in ('dir /b /A:D "*"') do (
	Echo Name: %%~na
	for /f "tokens=*" %%b in ('dir /b "%%~na\*.txt"') do (
		if not exist "output\%%~na" md "output\%%~na"
		echo %%b
		echo|set /p="Name: ">"output\%%~na\%%b"
		type "%%~na\%%b">>"output\%%~na\%%b"
	)
)