from flask import *
from flask_login import current_user

from attendance import db, bcrypt
from attendance.constant.appConstant import *
from attendance.user.forms import AddUserForm, RequestResetForm, ResetPasswordForm, ProfileForm
from attendance.models import User, Department, Timesheet

from attendance.user.utils import send_reset_email

from attendance.user.utils import save_pic

from flask_weasyprint import HTML, render_pdf

user = Blueprint('user', __name__)


@user.route('/add-user', methods=[Constant.GET, Constant.POST])
def add_user():
    if request.method == Constant.POST:
        depart = request.form['depart_name']
    else:
        depart = None
    department = Department.query.filter_by(company_id=current_user.company_name).all()
    for one_depat in department:

        if depart == one_depat.id:
            depart_id = one_depat.id
            print(depart_id)
    if current_user.role != StackHolder.ADMIN:
        return redirect(url_for('main.main_menu'))

    form = AddUserForm()
    update_user = User.query.all()
    if form.validate_on_submit():
        # try:
        role = request.form['select_value']
        hashed_passord = bcrypt.generate_password_hash(form.password.data)
        if depart == 'Departments':
            user = User(full_name=form.full_name.data, user_name=form.user_name.data, email=form.email.data,
                        role=role.lower(), password=hashed_passord
                        , company_name=current_user.company_name)
        else:
            user = User(full_name=form.full_name.data, user_name=form.user_name.data, email=form.email.data,
                        department=depart_id, role=role.lower(), password=hashed_passord
                        , company_name=current_user.company_name)
        mail_user = User.query.filter_by(email=form.email.data).first()
        main_user = User.query.filter_by(user_name=form.user_name.data).first()
        current_company = User.query.filter_by(company_name=current_user.company_name).all()
        if main_user in current_company:
            flash(f'{Constant.USERNAME_ALREADY_EXIST}', f'{Constant.WARNING_FLASH_MESSAGE}')
            return redirect(url_for('user.add_user'))
        elif mail_user:
            flash(f'{Constant.EMAIL_ALREADY_EXIST}', f'{Constant.INFO_FLASH_MESSAGE}')
        else:
            db.session.add(user)
            db.session.commit()
            flash(f'{Constant.USER_ADDED_SUCCESSFULLY}', f'{Constant.SUCCESS_FLASH_MESSAGE}')
            return redirect(url_for('main.main_menu'))
            # except:
            # db.session.rollback()
            return redirect(url_for('user.add_user'))

    fav_icon = url_for('static', filename='RegisterLogin/images/icons/user.png')
    return render_template('add_user.html', form=form, span=FormTitlesConstant.ADD_USER, fav_icon=fav_icon
                           , department=department, title=FormTitlesConstant.ADD_USER, update_user=update_user)


@user.route('/reset_password', methods=[Constant.POST, Constant.GET])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.main_menu'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        return redirect(url_for('company.login'))
    return render_template('request_reset.html', title=Constant.RESET_REQUEST, form=form)


@user.route('/reset_password/<token>', methods=[Constant.POST, Constant.GET])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.main_menu'))
    user = User.verify_reset_token(token)
    if user is None:
        flash(f'{Constant.INVALID_TOKEN}', f'{Constant.INFO_FLASH_MESSAGE}')
        return redirect(url_for('user.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hased_password = bcrypt.generate_password_hash(form.password.data)
        user.password = hased_password
        db.session.commit()
        flash(f'{Constant.PASSWORD_UPDATE}', f'{Constant.SUCCESS_FLASH_MESSAGE}')
        return redirect(url_for('company.login'))
    return render_template('reset_password.html', title=Constant.RESET_PASSWORD, form=form)


@user.route('/delete-user/<string:id>', methods=[Constant.POST, Constant.GET])
def delete_user(id):
    user_delete = User.query.filter_by(id=id).first()
    record_in_time_sheet = Timesheet.query.filter_by(user_id=id).all()
    db.session.delete(user_delete)
    for delete_selected_user in record_in_time_sheet:
        db.session.delete(delete_selected_user)
        db.session.commit()
    db.session.commit()
    return redirect(url_for('main.main_menu'))


@user.route('/update-user/<string:id>', methods=[Constant.POST, Constant.GET])
def update_user(id):
    update_user = User.query.filter_by(id=id).first()
    if request.method == Constant.POST:
        depart = request.form.get('depart_name')
    else:
        depart = None
    department = Department.query.filter_by(company_id=current_user.company_name).all()

    for one_depat in department:
        if depart == one_depat.id:
            depart_id = one_depat.id
            print(depart_id)
    form = AddUserForm()
    try:
        if request.method == Constant.POST:
            role = request.form['select_value']
            update_user.full_name = form.full_name.data
            update_user.user_name = form.user_name.data
            update_user.email = form.email.data
            update_user.email = form.confirm_email.data
            update_user.department = depart_id
            update_user.role = role.lower()
            db.session.commit()
            flash(f'{Constant.UPDATE_USER_SUCCESSFULLY}', f'{Constant.SUCCESS_FLASH_MESSAGE}')
            return redirect(url_for('user.update_user', id=id))
        elif request.method == Constant.GET:
            form.full_name.data = update_user.full_name
            form.user_name.data = update_user.user_name
            form.email.data = update_user.email
            form.confirm_email.data = update_user.email
    except:
        db.session.rollback()
        flash(f'{Constant.SELECT_DEPARTMENT}', f'{Constant.INFO_FLASH_MESSAGE}')
    fav_icon = url_for('static', filename='RegisterLogin/images/icons/user.png')
    return render_template('add_user.html', form=form, department=department, title=FormTitlesConstant.UPDATE_USER
                           , span=FormTitlesConstant.UPDATE_USER, fav_icon=fav_icon, update_user=update_user)


@user.route('/profile', methods=[Constant.GET, Constant.POST])
def profile():
    user = User.query.filter_by(company_name=current_user.company_name).all()
    form = ProfileForm()
    if form.validate_on_submit():
        if form.upload_image.data:
            profile_pic = save_pic(form.upload_image.data)
            current_user.upload_image = profile_pic
        current_user.full_name = form.full_name.data
        current_user.user_name = form.user_name.data
        current_user.email = form.email.data
        if current_user.department == None:
            form.department.data = 'None'
        else:
            current_user.depart.department_name = form.department.data
        db.session.commit()
        redirect(url_for('user.profile'))
    elif request.method == Constant.GET:
        form.full_name.data = current_user.full_name
        form.user_name.data = current_user.user_name
        form.email.data = current_user.email
        if current_user.department == None:
            form.department.data = 'None'
        else:
            form.department.data = current_user.depart.department_name
    image_upload = url_for('static', filename='images/' + current_user.upload_image)
    return render_template('profile.html', form=form, user=user, image_upload=image_upload,
                           title=current_user.user_name)


@user.route('/pdf', methods=[Constant.GET, Constant.POST])
def pdf_file():
    attendance_record = Timesheet.query.filter_by(company_id=current_user.company_name).all()
    current_user_record = Timesheet.query.filter_by(user_id=current_user.id).all()
    html = render_template('pdf.html', attendance_record=attendance_record, current_user_record=current_user_record,
                           title='PDF')
    return render_pdf(HTML(string=html))
