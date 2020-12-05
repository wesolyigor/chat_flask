from flask import Blueprint, render_template, url_for, session
from werkzeug.utils import redirect

from chat.forms import UserForm

bp_main = Blueprint('main', __name__, url_prefix='/')


@bp_main.route('/', methods=["GET", "POST"])
def home():
    form = UserForm()

    if form.validate_on_submit():
        session['room'] = form.room.data
        session['name'] = form.name.data
        return redirect(url_for('ws.chat'))

    return render_template('home.html', form=form)

