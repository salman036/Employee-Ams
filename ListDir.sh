source venv/bin/activate
MYSQL_USER="root"
MYSQL_PASSWORD="your_password"

mysql -u $MYSQL_USER -p -e "CREATE DATABASE attendance"
use mysql
cd attendance/
export FLASK_APP=db_shell.py
flask db init
flask db migrate -m "initial commit"
flask db upgrade

