from flask import render_template, flash
from flask_mail import Message

from attendance import mail, app
from attendance.constant.appConstant import *

import secrets
import os
from PIL import Image


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset message', sender='noreply@gmail.com', recipients=[user.email])
    msg.html = render_template('include/SentEmail.html', token=token, _external=True)
    flash(f'{Constant.RESET_PASSWORD_EMAIL_SEND}', f'{Constant.INFO_FLASH_MESSAGE}')
    mail.send(msg)
    return "Send"


def save_pic(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)
    form_picture.save(picture_path)
    out_out_size = (100, 100)
    i = Image.open(form_picture)
    i.thumbnail(out_out_size)
    i.save(picture_path)
    return picture_fn

