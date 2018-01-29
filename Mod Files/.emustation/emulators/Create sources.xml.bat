@Echo off
SetLocal EnableDelayedExpansion
:: this batch is used to generate the sources.xml from folders.


(
Echo ^<sources^>
	Echo ^<programs^>
		Echo ^<default pathversion^="1"^/^>
)>>"sources.xml"
		
for ^/f "Tokens=*" %%a in ('dir /b /A:D "*"') do (
	Echo  %%~na
		(
		Echo ^<source^>
			Echo ^<name^>%%~na^<^/name^>
			Echo ^<path pathversion^="1"^>Special:^/^/xbmc^/_cuts^/%%~na^/^<^/path^>
		Echo ^<^/source^>
		)>>"sources.xml"
)
(
		Echo ^<source^>
			Echo ^<name^>Ports^<^/name^>
			Echo ^<path pathversion^="1"^>E:\Homebrew\^<^/path^>
			Echo ^<path pathversion^="1"^>F:\Homebrew\^<^/path^>
			Echo ^<path pathversion^="1"^>G:\Homebrew\^<^/path^>
		Echo ^<^/source^>
		Echo ^<source^>
			Echo ^<name^>Xbox^<^/name^>
			Echo ^<path pathversion^="1"^>E:\Games\^<^/path^>
			Echo ^<path pathversion^="1"^>E:\Games1\^<^/path^>
			Echo ^<path pathversion^="1"^>E:\Games2\^<^/path^>
			Echo ^<path pathversion^="1"^>F:\Games\^<^/path^>
			Echo ^<path pathversion^="1"^>F:\Games1\^<^/path^>
			Echo ^<path pathversion^="1"^>F:\Games2\^<^/path^>
			Echo ^<path pathversion^="1"^>G:\Games\^<^/path^>
			Echo ^<path pathversion^="1"^>G:\Games1\^<^/path^>
			Echo ^<path pathversion^="1"^>G:\Games2\^<^/path^>
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