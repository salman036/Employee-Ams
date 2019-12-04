from flask import *
from flask_login import current_user

from attendance import db
from attendance.constant.appConstant import *
from attendance.department.forms import AddDepartmentForm
from attendance.models import Department

detail_department = Blueprint('detail_department', __name__)


@detail_department.route('/department-detail', methods=[Constant.POST, Constant.GET])
def department_details():
    depart = Department.query.filter_by(company_id=current_user.company_name).all()
    fav_icon = url_for('static', filename='RegisterLogin/images/icons/all_department.png')
    return render_template('department_details.html', depart=depart, fav_icon=fav_icon, title=Constant.DEPARTMENT)


@detail_department.route('/delete-department/<string:id>', methods=[Constant.GET, Constant.POST])
def delete_department(id):
    depart = Department.query.filter_by(id=id).first()
    db.session.delete(depart)
    db.session.commit()
    flash(f'{Constant.DELETE_DEPARTMENT}', f'{Constant.SUCCESS_FLASH_MESSAGE}')
    return redirect(url_for('detail_department.department_details'))


@detail_department.route('/update-department/<string:id>', methods=[Constant.GET, Constant.POST])
def update_department(id):
    depart = Department.query.filter_by(id=id).first()
    form = AddDepartmentForm()
    if form.validate_on_submit():
        depart.department_name = form.department_name.data
        db.session.commit()
        flash(f'{Constant.UPDATE_DEPARTMENT}', f'{Constant.SUCCESS_FLASH_MESSAGE}')
        return redirect(url_for('detail_department.department_details'))
    form.department_name.data = depart.department_name
    fav_icon = url_for('static', filename='RegisterLogin/images/icons/all_department.png')
    return render_template('add_department.html', depart=depart, title=FormTitlesConstant.ALL_DEPARTMENT,
                           fav_icon=fav_icon, form=form, span='Update Department')
