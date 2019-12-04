from datetime import datetime, date

from flask import *
from flask_login import login_required, current_user

from attendance import db
from attendance.constant.appConstant import *
from attendance.models import User, Timesheet

user_attendance = Blueprint('user_attendance', __name__)


@user_attendance.route('/attendance/<string:user_id>', methods=[Constant.GET, Constant.POST])
@login_required
def attendance(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    return render_template('user_attendance.html', user=user, title=Constant.ATTENDANCE)


@user_attendance.route('/check-in/<string:user_id>', methods=[Constant.GET, Constant.POST])
def check_in(user_id):
    if request.method == Constant.GET:
        try:
            check_in_user = Timesheet.query.filter_by(user_id=user_id, date=Constant.date).first()
            if check_in_user is not None or check_in_user.date == Constant.date:
                flash(f'{Constant.ALREADY_CHECK_IN}', f'{Constant.INFO_FLASH_MESSAGE}')
                return redirect(url_for('user_attendance.attendance', user_id=user_id))
            else:
                flash(f'{Constant.CHECK_IN_SUCCESSFULLY}', f'{Constant.SUCCESS_FLASH_MESSAGE}')
                user = Timesheet(user_id=user_id, check_in=datetime.now(), company_id=current_user.company_name)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('user_attendance.attendance', user_id=user_id))
        except:
            flash(f'{Constant.CHECK_IN_SUCCESSFULLY}', f'{Constant.SUCCESS_FLASH_MESSAGE}')
            user = Timesheet(user_id=user_id, check_in=datetime.now(), company_id=current_user.company_name)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user_attendance.attendance', user_id=user_id))
    return redirect(url_for('main.main_menu'))


@user_attendance.route('/check-out/<string:user_id>', methods=[Constant.GET, Constant.POST])
def check_out(user_id):
    if request.method == Constant.GET:
        check_out_user = Timesheet.query.filter_by(user_id=user_id, date=Constant.date).first()
        try:
            if check_out_user.check_out is None:
                check_out_user.check_out = datetime.utcnow()
                db.session.commit()
                flash(f'{Constant.CHECK_OUT_SUCCESSFULLY}', f'{Constant.SUCCESS_FLASH_MESSAGE}')
                return redirect(url_for('user_attendance.attendance', user_id=user_id))
            elif check_out_user.date == check_out_user.date:
                flash(f'{Constant.ALREADY_CHECK_OUT}', f'{Constant.INFO_FLASH_MESSAGE}')
                return redirect(url_for('user_attendance.attendance', user_id=user_id))
        except:
            db.session.rollback()
            flash(f'{Constant.FIRST_CHECK_IN_PLEASE}', f'{Constant.INFO_FLASH_MESSAGE}')
            return redirect(url_for('user_attendance.attendance', user_id=user_id))
    return redirect(url_for('main.main_menu'))


@user_attendance.route('/attendance-record', methods=[Constant.GET, Constant.POST])
def all_attendance_record():
    if current_user.is_authenticated == False:
        return redirect(url_for('main.main_menu'))
    attendance_record = Timesheet.query.filter_by(company_id=current_user.company_name).all()
    current_user_record = Timesheet.query.filter_by(user_id=current_user.id).all()
    return render_template('attendance_record.html', attendance_record=attendance_record,
                           current_user_record=current_user_record,
                           title=Constant.ATTENDANCE_RECORD)
