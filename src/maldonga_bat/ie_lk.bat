@echo off
echo Setting up log file...

for /f "tokens=1-4 delims=/ " %%i in ("%date%") do (
     set dow=%%h
     set month=%%i
     set day=%%j
     set year=%%k
   )
SET datestr=%month%_%day%_%year%
SET path=./Log/
SET filename=%path%log-%datestr%.txt

echo ==LOG FILE %datestr% == > %filename%

goto main

main:
    shutdown -c Just reminder, don't fuck up. -s -t 000