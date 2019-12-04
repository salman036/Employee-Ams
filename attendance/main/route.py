from flask import *
from flask_login import login_required, current_user

from attendance.constant.appConstant import *
from attendance.models import User, Department
from attendance.user.forms import ProfileForm

main = Blueprint('main', __name__)


@main.route('/', methods=[Constant.GET, Constant.POST])
@login_required
def main_menu():
    if current_user.role == StackHolder.EMPLOYEE:
        return redirect(url_for('user.profile'))
    form = ProfileForm()
    user = User.query.filter_by(company_name=current_user.company_name).all()
    department = Department.query.filter_by(company_id=current_user.company_name)
    return render_template('front_end.html', user=user, title=FormTitlesConstant.HOME, department=department,
                           form=form)
