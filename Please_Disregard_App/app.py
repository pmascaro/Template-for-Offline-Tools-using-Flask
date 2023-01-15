#---
# 
# Read README.md file for instructions on how to run the App
#
#---

#---
# key libraries
#---

from flask import Flask, render_template, request
# import requests
# from requests.auth import HTTPBasicAuth
import json # json it will come in handy when parsing the JSON output of an API
from waitress import serve

import numpy as np
import pandas as pd # <- to install it first you need to upgrade pip by typing 'python -m pip install --upgrade pip --ignore-installed'

import os
from datetime import datetime, timedelta, date, time

#-----
#
# References
#
#-----

# flask app (text preprocessing):https://realpython.com/flask-by-example-part-3-text-processing-with-requests-beautifulsoup-nltk/


#-----
#
# Specifics functions for this project
#
#-----


#-----
#
# Flask app
#
#-----

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
   
   ####
   # your code here
   ####

   return render_template('index.html') # ,start_of_week=start_of_week


if __name__ == '__main__':

   # we use this line of code to serve our app. We are self-hosting it with a standalone container: Waitress
   # The app is running in the browser: simply write http://127.0.0.1:8080/. 
   # Try Chrome if Microsoft Edge doesn't return any results
   serve(app, listen = "127.0.0.1:8080 [::1]:8080")

   # this part of the application is based on a reference that point me to 
   # self-hosted options for Flask Apps ( https://flask.palletsprojects.com/en/2.2.x/deploying/ )
   # I selected Waitress server because it's suitable for Windows. Then, I used
   # link: https://www.youtube.com/watch?v=tovsUQu6kBU 
   # More on Waitress and WSGI: https://betterprogramming.pub/introduction-to-waitress-a-wsgi-server-for-python-2-and-3-c77e20cb292b
   #  Based on the reference above,
   # if you configure waitress 'listen' directive as listen="127.0.0.1:8080 [::1]:8080", only the local machine can access your data.

   # the 0.0.0.0 option makes your application accessible by network IP address so
   #  another machine in the same network can access it. 

   # based on 
   # If you configure waitress 'listen' directive as listen="127.0.0.1:8080 [::1]:8080", only the local machine can access your data.

   # threads = 1 <- The number of threads used to process application logic (integer). The default value is 4.
   # host on specific port -> use 'serve(app, host='0.0.0.0', port=50100, threads=1)' instead
   