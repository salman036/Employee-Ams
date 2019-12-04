from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

from attendance.constant.appConstant import *


class AddDepartmentForm(FlaskForm):
    department_name = StringField(FormConstant.DEPARTMENT, validators=[DataRequired(), Length(min=2, max=25)])
    submit = SubmitField(FormConstant.SUBMIT)
