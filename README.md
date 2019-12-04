# Project Title:
    Employee AMS(Attendance Management System)

# Description:
    This project manages the company employees timing with check_in check_out feature
    and generate the report of every employees timing

# Way of download and run project:
    Run this command in terminal
    $ git clone https://github.com/SalmanSaleem1/Employee-AMS.git
        
# Installations:
    Run this command in terminal for install requirments of the project.
    create virtual environment first for the installaion
    $ cd Employee-AMS/
    $ python3 -m venv env 
    $ source env/bin/activate
    $ pip install -r requirements.txt
    
# shell script instructions for database creation
    After installaion if your database is creating issue and showing error there is
    no database then don't wory here is the solution
    Simple run the shell script by using this command:
        1) open terminal any where
           $ cd attendance/ (if you are already in the directory then there is not need
                             to run this command)
           $ chmod +x ListDir.sh
           $ ./ListDir.sh
    Now your database is created and test the app

# python version:
    First install the python3
    With this command
        $ sudo apt-get install python3-venv
        now create the python3 env in the project directory
        with this command:
        $ source env/bin/activate
        
# Run app:
    Run these commands in terminal
        $ cd attendance/
        $ export FLASK_APP=db_shell.py
        $ flask run


