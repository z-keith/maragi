from flask import Blueprint, render_template, url_for
from flask_login import current_user
import requests

from forms.login_form import LoginForm
from forms.new_user_form import NewUserForm

home = Blueprint('home', __name__, template_folder='templates')

@home.route('/')
def index():
	if current_user.get_id():
		lgf = None
		nuf = None
	else:
		lgf = LoginForm(next=url_for('dash.dashboard'))
		nuf = NewUserForm()

	return render_template('index.html', loginform=lgf, newuserform=nuf)