# FeatureRequests
Homework assignment for BriteCore

Project Uses the following Tech Stack:

OS: Ubuntu 

Python Version: Python 2.7.10

SimpleHTTPServer

JavaScript: KnockoutJS 3.4.2

ORM: Sql-Alchemy

NOTE: This project has been deployed to an Amazon EC2 Ubuntu Server.

SET UP DATABASE:
------------------------------------------
Open a terminal window:

    1.) cd to FeatureRequests
    
    2.) Run the following command: python database.py
    
This script (database.py) sets up the sqlite database.

How to run project?
------------------------------------------
You must set up the database before you can begin to submit new feature requests!

Open a terminal window:

    1.) cd to FeatureRequests
    
    2.) Run the following command: python feature_requests.py -m
    
    3.) Open a web browser to add a new feature: http://127.0.0.1:8000/ or http://localhost:8000/
    
To view data of all clients, open a web browser to: http://127.0.0.1:8000/view_all.html or http://localhost:8000/view_all.html
    
How to run test cases?
------------------------------------------
Requirements: Python Nose and Python Requests

Open a termianl window:

    1.) cd to FeatureRequests
    
    2.) Run the following command to install nose: sudo easy_install nose
    
    3.) Run the following command to install requests: sudo easy_install requests
    
    4.) Run test cases:  nosetests --verbosity=2 test_feature_requests.py
    
    NOTE: The python script MUST be running for the tests to pass!

Viewing the Database manually:
------------------------------------------
1.) Download phpLiteAdmin

2.) In the phpliteadmin.php config file, set the directory value to 'YOUR_PATH/FeatureRequests'

3.) Move the phpliteadmin.php config file to your web server's directory

4.) In a web browser, go to: localhost/phpliteadmin.php

