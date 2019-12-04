
from datetime import datetime, date
from uuid import uuid4

from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from attendance import db, login, app


@login.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()


class Company(db.Model):
    id = db.Column(db.String(60), primary_key=True, default=uuid4)
    company_name = db.Column(db.String(60), unique=True, primary_key=True)
    create_at = db.Column(db.DateTime(), default=datetime.now)
    users = db.relationship('User', backref='company', lazy=True)
    tim_sheet = db.relationship('Timesheet', backref='company_time', lazy=True)


class User(UserMixin, db.Model):
    id = db.Column(db.String(60), primary_key=True, default=uuid4, unique=True)
    full_name = db.Column(db.String(60))
    user_name = db.Column(db.String(60), primary_key=True)
    email = db.Column(db.String(60), primary_key=True, unique=True)
    department = db.Column(db.String(60), db.ForeignKey('department.id'))
    role = db.Column(db.String(60), default='admin')
    status = db.Column(db.Boolean(), default=True)
    upload_image = db.Column(db.String(100), default='default.png')
    password = db.Column(db.String(60))
    company_name = db.Column(db.String(60), db.ForeignKey('company.id'), primary_key=True)
    user = db.relationship('Company')
    time_sheet = db.relationship('Timesheet', backref='time', lazy=True)

    def get_reset_token(self, expire_time=1800):
        s = Serializer(app.config['SECRET_KEY'], expire_time)
        token = s.dumps({'user_id': self.id}).decode('utf-8')
        return token

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.filter_by(id=user_id).first()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_id(self):
        return self.id


class Department(db.Model):
    id = db.Column(db.String(60), default=uuid4, unique=True)
    department_name = db.Column(db.String(60), primary_key=True)
    company_id = db.Column(db.String(60), db.ForeignKey('company.id'), primary_key=True)
    company = db.relationship('Company')
    users = db.relationship('User', backref='depart', lazy=True)
    create_at = db.Column(db.DateTime(), default=datetime.now)


class Timesheet(db.Model):
    id = db.Column(db.String(60), primary_key=True, default=uuid4)
    user_id = db.Column(db.String(60), db.ForeignKey('user.id'))
    check_in = db.Column(db.DateTime())
    check_out = db.Column(db.DateTime())
    company_id = db.Column(db.String(60), db.ForeignKey('company.id'))
    time_users = db.relationship('User', backref='author', lazy=True)
    date = db.Column(db.String(60), default=date.today)
