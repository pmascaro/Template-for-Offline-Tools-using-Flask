### Creating the project

#### 1. Creating venv

This sections is based on the following youtube tutorial: https://www.youtube.com/watch?v=brJR5Qjp4SM

and https://bobbyhadz.com/blog/source-is-not-recognized-as-internal-or-external-command

To create virtual environment, in the project terminal, use `python -m venv venv`, where 'venv' is the name of the virtual environment. A `venv` folder will appear in the project directory.

#### 2. Using venv

This creates the virtual environment. We now need to activate it. To do so, use:

- if you use windows use the following: `venv\Scripts\activate.bat`, where 'venv' is the name of the virtual environment. A `venv` folder will appear in the project directory.

_Aside note:_ remember that 'chdir' command prints the path in the terminal

To deactivate it, type: `deactivate`

_Note:_ To check for interpreter, use `python`

Now it's time to install all your required libraries, which you can do as you require them. Also, you can check (here)[https://towardsdatascience.com/how-to-use-bash-to-automate-the-boring-stuff-for-data-science-d447cd23fffe] if you want to install them in one go

At the end of the process, use this in the terminal:

`pip freeze > requirements.txt`

You can always create another virtual environment, you can always copy all the requirements from the requirements.txt file:

`pip install -r requirements.txt`

### Running Flask app

#### Development mode

Flask has its own built test server, we will use it to see what we are doing to do that in the project terminal type:

`set FLASK_DEBUG=1`

`python -m flask run`

Finally, open `http://127.0.0.1:5000/`

The above opens a localhost, press Ctrl+C to close it.

### Sharing Flask app with non-technical stakeholders

#### Production mode

Prerequisites: 
- Python installed in your laptop
- Access to GitLab to be able to install the cadspy library


Step 1) In the Windows Command prompt App (Go to Search box and type 'Command Prompt'), go to the project directory by typing this:

`cd /d <path>`

For example, to access this project directory you would type:

`cd /d O:\HO - Ground Ops\HO - Baggage\Live\Demand Based Build - ST\03 Seasonal plan - PMM\00 template`


Step 2) Create virtual environment

in the Command Prompt App, use:

`python -m venv venv`

where 'venv' is the name of the virtual environment. A `venv` folder will appear in the project directory. You don't need to know the details, but basically this is needed for you to be able to run the App.


Step 3) Activate virtual environment. We need to use Python to run the app. For that we need to connect to it and we do so by activating our virtual environment. It doesn't take long, just type the below in the Command Prompt App:

`venv\Scripts\activate.bat`


Step 4) ONLY the first time you run app in production mode, you need to install any code dependencies. That is, anything needed for you to run the App. Go to Step 4 if you have already run the app at least once.

`pip install -r requirements.txt`

_Expected time for this step: about 15 minutes (time to go for a coffee/tea/lunch maybe? :) )_



Step 5) Run the app by typing the below in the Command Prompt App:

`python app.py`

_Expected time until you can jumpt to Step 5: about 30 seconds_


Step 6) Some output text will appear in the Command Prompt App. Follow instructions there. The app should be running on this direction on any browser: http://127.0.0.1:8080/
