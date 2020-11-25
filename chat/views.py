from flask import Blueprint, render_template

bp_main = Blueprint('main', __name__, url_prefix='/')


@bp_main.route('/')
def home():
    text = 'textext'
    return render_template('home.html', text=text)