Project Title: Employee AMS(Attendance Management System)

Description: This project manage the company employees timing with check_in check_out time
    and generate the report of every employee timing performance

Way of download and run project:
    These instruction will get you copy of a project and running on your local machine for
     development and testing purpose


Run app:
    if you want to run app then simply run this command in terminal
    $ cd attendance/
    $ export FLASK_APP=db_shell.py
    $ flask run
    if your app is creating some issues and want to install some modules
    then check the requirement file and install requirement file module which are written in this file

python version:
    if you want to run this app with python 3.6 then first install the python3
    whit this command
    $ sudo apt-get install python3-venv
    now create the python3 env in the project directory
    with this command:
    $ python3 -m venv env
    $ source env/bin/activate
    and then run the command mention in the 'Run app' blog
