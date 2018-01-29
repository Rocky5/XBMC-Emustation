@Echo off
SetLocal EnableDelayedExpansion

For /f "Tokens=*" %%a in ('dir /b /a:d "*"') do Echo default.xbe >"%%a\default.xbe"