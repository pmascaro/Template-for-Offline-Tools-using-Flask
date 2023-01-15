@echo off

echo.
echo ***********************************************************************
echo *                                                                     *
echo * Please wait:                                                        *
echo * Checking if it is the first time you have launched this application *
echo *                                                                     *
echo ***********************************************************************
echo.

rem Check if a folder called 'venv' exists in the Please_Disregard_App directory. 
if exist "Please_Disregard_App\venv\" (

	echo Welcome back!
	echo.

	rem If the folder exists, activate the virtual environment
	call "Please_Disregard_App\venv\Scripts\activate.bat"
	echo Virtual environment activated
	echo.


	echo Running python file. App will open shortly in your browser
	echo.
	python .\Please_Disregard_App\app.py
	echo Python file running 
	echo.

) else (

	rem If the folder does not exist, create a virtual environment
	echo It's the first time you're around. Let us install the App for you.
	echo.
	echo This installation is estimated to take about 3/4 minutes. Time for a coffee/tea?
	echo.

	echo Starting the creation of virtual environment...
	python -m venv .\Please_Disregard_App\venv
	echo Virtual environment created
	echo.


	rem If the folder exists, activate the virtual environment
	call "Please_Disregard_App\venv\Scripts\activate.bat"
	echo Virtual environment activated
	echo.

	
	echo Installing dependencies to virtual environment...
	rem install dependencies from requirements.txt file

	rem it's always best practice tu upgrade pip
	python -m pip install --upgrade pip
	
	rem installing all other dependencies
	pip install -r .\Please_Disregard_App\requirements.txt
	echo All dependencies installed
	echo.

	echo Running python file. App will open shortly in your browser
	echo.
	python .\Please_Disregard_App\app.py

	echo Python file running 
	echo.

)