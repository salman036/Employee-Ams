from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

from attendance.config import Config

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
app.secret_key = '12343423345'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
mail = Mail(app)

login = LoginManager(app)
login.login_view = 'company.login'
login.login_message_category = 'info'

# Blue print imports

from attendance.company.route import company
from attendance.main.route import main
from attendance.department.route import department
from attendance.department_detail.route import detail_department
from attendance.user.route import user
from attendance.add_attendance.route import user_attendance

app.register_blueprint(company)
app.register_blueprint(main)
app.register_blueprint(department)
app.register_blueprint(detail_department)
app.register_blueprint(user)
app.register_blueprint(user_attendance)
