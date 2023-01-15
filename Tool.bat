@echo off

rem Store the current working directory in a variable
set "current_dir=%cd%"

echo.
echo -------------------------------------------
echo.
rem Log the current working directory
echo Current working directory is: %current_dir%
echo.
echo -------------------------------------------
echo.

rem Set title of the new command prompt window
title Please wait until the tool is launched in your browser. Close this window once finished with the tool.

rem set the current directory to the directory we are in
cd %current_dir%

rem Open a new command prompt window, and run functions batch file
rem title Please Wait until the tool is launched in your browser & 
start cmd /c call Please_Disregard_App\functions.bat