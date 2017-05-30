from flask import Blueprint, render_template
from flask_login import login_required, current_user

dash = Blueprint('dash', __name__, template_folder='templates')

@dash.route('/dashboard')
@login_required #this isn't working
def dashboard():
	return 'dashboard'