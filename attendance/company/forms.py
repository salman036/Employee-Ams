from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from flask_wtf.file import *
from attendance.constant.appConstant import *
from attendance.models import Company, User


class RegisterAdminForm(FlaskForm):
    company_name = StringField(FormConstant.NAME, validators=[DataRequired()])
    email = StringField(FormConstant.NAME, validators=[DataRequired(), Email()])
    confirm_email = StringField(FormConstant.CONFIRM_PASSWORD, validators=[DataRequired(), EqualTo('email')])
    full_name = StringField(FormConstant.FULL_NAME, validators=[DataRequired(), Length(min=2, max=40)])
    user_name = StringField(FormConstant.USER_NAME, validators=[DataRequired(), Length(min=2, max=30)])
    password = PasswordField(FormConstant.PASSWORD, validators=[DataRequired(), Length(min=8, max=15),
                                                                Regexp(Constant.REGULAR_EXPRESSION_PASSWORD, message=
                                                                Constant.REGULAR_PASSWORD_EXPRESSION_MESSAGE)])
    confirm_password = PasswordField(FormConstant.CONFIRM_PASSWORD, validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(FormConstant.CREATE)

    def validate_company_name(self, company_name):
        com = Company.query.filter_by(company_name=company_name.data).first()
        if com:
            raise ValidationError(Constant.COMPANY_NAME_ALREADY_EXIST)

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError(Constant.EMAIL_ALREADY_EXIST)


class LoginForm(FlaskForm):
    company_name = StringField(FormConstant.COMPANY)
    user_name = StringField(FormConstant.USER_NAME, validators=[DataRequired()])
    password = PasswordField(FormConstant.PASSWORD, validators=[DataRequired()])
    submit = SubmitField(FormConstant.LOGIN)
