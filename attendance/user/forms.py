from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import *
from wtforms.validators import *

from attendance.constant.appConstant import *
from attendance.models import User


class AddUserForm(FlaskForm):
    full_name = StringField(FormConstant.FULL_NAME, validators=[DataRequired(), Length(min=2, max=30)])
    user_name = StringField(FormConstant.USER_NAME, validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField(FormConstant.EMAIL, validators=[DataRequired(), Length(min=2, max=35), Email()])
    confirm_email = StringField(FormConstant.EMAIL, validators=[DataRequired(), Email(), EqualTo('email')])
    upload_image = FileField(FormConstant.UPLOAD_IMAGE, validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    password = PasswordField(FormConstant.PASSWORD,
                             validators=[DataRequired(), Length(min=8, max=15),
                                         Length(min=2, max=35), Regexp(Constant.REGULAR_EXPRESSION_PASSWORD,
                                                                       message=Constant.REGULAR_PASSWORD_EXPRESSION_MESSAGE)])
    confirm_password = PasswordField(FormConstant.CONFIRM_PASSWORD, validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(FormConstant.SUBMIT)


class RequestResetForm(FlaskForm):
    email = StringField(FormConstant.EMAIL, validators=[DataRequired(), Length(min=2, max=35), Email()])
    submit = SubmitField('Send')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValueError(f'{Constant.EMAIL_DOES_NOT_EXIST}', f'{Constant.INFO_FLASH_MESSAGE}')


class ResetPasswordForm(FlaskForm):
    password = PasswordField(FormConstant.PASSWORD, validators=[DataRequired()])
    confirm_password = PasswordField(FormConstant.CONFIRM_PASSWORD,
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(Constant.RESET_PASSWORD)


class ProfileForm(FlaskForm):
    full_name = StringField(FormConstant.FULL_NAME)
    user_name = StringField(FormConstant.USER_NAME)
    email = StringField(FormConstant.EMAIL)
    department = StringField(FormConstant.DEPARTMENT)
    upload_image = FileField(FormConstant.UPLOAD_IMAGE, validators=[FileAllowed(['jpg', 'jpeg', 'png'])])

    update = SubmitField(FormConstant.UPDATE)
