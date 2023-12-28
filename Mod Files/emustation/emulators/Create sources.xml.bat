@Echo off
SetLocal EnableDelayedExpansion
:: this batch is used to generate the sources.xml from folders.


(
Echo ^<sources^>
	Echo ^<programs^>
		REM Echo ^<default pathversion^="1"^/^>
)>>"sources.xml"
		
REM for ^/f "Tokens=*" %%a in ('dir /b /A:D "*"') do (
	REM Echo  %%~na
		REM (
		REM Echo ^<source^>
			REM Echo ^<name^>%%~na^<^/name^>
			REM Echo ^<path pathversion^="1"^>Special:^/^/xbmc^/_cuts^/%%~na^/^<^/path^>
		REM Echo ^<^/source^>
		REM )>>"sources.xml"
REM )
(
		Echo ^<source^>
			Echo ^<name^>Static_Menu^<^/name^>
			Echo ^<path pathversion^="1"^>X:\^<^/path^>
		Echo ^<^/source^>
		Echo ^<source^>
			Echo ^<name^>Apps^<^/name^>
			Echo ^<path pathversion^="1"^>E:\Applications\^<^/path^>
			Echo ^<path pathversion^="1"^>F:\Applications\^<^/path^>
			Echo ^<path pathversion^="1"^>G:\Applications\^<^/path^>
			Echo ^<path pathversion^="1"^>E:\Apps\^<^/path^>
			Echo ^<path pathversion^="1"^>F:\Apps\^<^/path^>
			Echo ^<path pathversion^="1"^>G:\Apps\^<^/path^>
		Echo ^<^/source^>
		Echo ^<source^>
			Echo ^<name^>Homebrew^<^/name^>
			Echo ^<path pathversion^="1"^>E:\Homebrew\^<^/path^>
			Echo ^<path pathversion^="1"^>F:\Homebrew\^<^/path^>
			Echo ^<path pathversion^="1"^>G:\Homebrew\^<^/path^>
		Echo ^<^/source^>
		Echo ^<source^>
			Echo ^<name^>Ports^<^/name^>
			Echo ^<path pathversion^="1"^>E:\Ports\^<^/path^>
			Echo ^<path pathversion^="1"^>F:\Ports\^<^/path^>
			Echo ^<path pathversion^="1"^>G:\Ports\^<^/path^>
		Echo ^<^/source^>
		Echo ^<source^>
			Echo ^<name^>Xbox^<^/name^>
			Echo ^<path pathversion^="1"^>E:\Games\^<^/path^>
			Echo ^<path pathversion^="1"^>F:\Games\^<^/path^>
			Echo ^<path pathversion^="1"^>G:\Games\^<^/path^>
		Echo ^<^/source^>
	Echo ^<^/programs^>
	Echo ^<video^>
		Echo ^<default pathversion^="1"^/^>
	Echo ^<^/video^>
	Echo ^<music^>
		Echo ^<default pathversion^="1"^/^>
	Echo ^<^/music^>
	Echo ^<pictures^>
		Echo ^<default pathversion^="1"^/^>
	Echo ^<^/pictures^>
	Echo ^<files^>
		Echo ^<default pathversion^="1"^/^>
	Echo ^<^/files^>
Echo ^<^/sources^>
)>>"sources.xml"

pause