from flask import *
from flask_login import login_required, current_user

from attendance.constant.appConstant import *
from attendance import db
from attendance.department.forms import AddDepartmentForm
from attendance.models import Department

department = Blueprint('department', __name__)


@department.route('/add-department', methods=[Constant.GET, Constant.POST])
@login_required
def add_department():
    if current_user.role != StackHolder.ADMIN:
        return redirect(url_for('main.main_menu'))
    form = AddDepartmentForm()
    if form.validate_on_submit():
        try:
            add_department = Department(department_name=form.department_name.data,
                                        company_id=current_user.company_name)
            main_department = Department.query.filter_by(department_name=form.department_name.data).first()
            depart = Department.query.filter_by(company_id=current_user.company_name).all()
            if main_department == depart:
                flash(f'{Constant.DEPARTMENT_ALREADY_EXIST}', f'{Constant.WARNING_FLASH_MESSAGE}')
                return redirect(url_for('department.add_department'))
            else:
                db.session.add(add_department)
                db.session.commit()
                flash(f'{Constant.DEPARTMENT_MESSAGE}', f'{Constant.SUCCESS_FLASH_MESSAGE}')
                return redirect(url_for('detail_department.department_details'))
        except:
            db.session.rollback()
            flash(f"{Constant.DEPARTMENT_ALREADY_EXIST}", f"{Constant.WARNING_FLASH_MESSAGE}")
            return redirect(url_for('department.add_department'))

    fav_icon = url_for('static', filename='RegisterLogin/images/icons/department.png')

    return render_template('add_department.html', form=form, title=FormTitlesConstant.ADD_DEPARTMENT, fav_icon=fav_icon,
                          span='Create Department')
