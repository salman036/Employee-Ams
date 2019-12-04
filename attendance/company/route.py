from flask import *
from flask_login import login_user, logout_user, current_user

from attendance import *
from attendance.company.forms import RegisterAdminForm, LoginForm
from attendance.constant.appConstant import *
from attendance.models import Company, User

company = Blueprint('company', __name__)


@company.route('/register', methods=[Constant.GET, Constant.POST])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.main_menu'))
    form = RegisterAdminForm()
    if form.validate_on_submit():
        try:
            company = Company(company_name=form.company_name.data)
            db.session.add(company)
            db.session.commit()
        except:
            flash(f'{Constant.COMPANY_NAME_ALREADY_EXIST}', f'{Constant.WARNING_FLASH_MESSAGE}')
            db.session.rollback()
            return redirect(url_for('company.register'))
        try:
            hashed_password = bcrypt.generate_password_hash(form.password.data)
            user = User(email=form.email.data, full_name=form.full_name.data, user_name=form.user_name.data,
                        company_name=company.id,
                        password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash(f'{Constant.REGISTER_SUCCESSFULLY}', f'{Constant.SUCCESS_FLASH_MESSAGE}')
            return redirect(url_for('company.login'))
        except:
            flash(f'{Constant.USERNAME_ALREADY_EXIST}', f'{Constant.WARNING_FLASH_MESSAGE}')
            db.session.rollback()
            com = Company.query.filter_by(company_name=form.company_name.data).first()
            db.session.delete(com)
            db.session.commit()
            return redirect(url_for('company.register'))
    fav_icon = url_for('static', filename='RegisterLogin/images/icons/login.png')
    return render_template('register.html', form=form, title=FormTitlesConstant.REGISTER_COMPANY,
                           fav_icon=fav_icon)


@company.route('/login', methods=[Constant.GET, Constant.POST])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.main_menu'))
    form = LoginForm()
    if form.validate_on_submit():
        company = Company.query.filter_by(company_name=form.company_name.data).first()
        user = User.query.filter_by(user_name=form.user_name.data).first()
        if company is None:
            flash(f'The company name doesnt exit', f'{Constant.INFO_FLASH_MESSAGE}')
        elif company and user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f'{Constant.LOGIN_SUCCESSFULLY}', f'{Constant.SUCCESS_FLASH_MESSAGE}')
            if user.role == StackHolder.EMPLOYEE:
                return redirect(url_for('user.profile'))
            else:
                return redirect(url_for('main.main_menu'))
        else:
            flash(f'{Constant.USER_NAME_OR_PASSWORD_INCORRECT}', f'{Constant.WARNING_FLASH_MESSAGE}')
    fav_icon = url_for('static', filename='RegisterLogin/images/icons/login.png')
    return render_template('login.html', form=form, title=FormTitlesConstant.LOGIN, fav_icon=fav_icon)


@company.route('/logout', methods=[Constant.GET, Constant.POST])
def logout():
    logout_user()
    return redirect(url_for('company.login'))
