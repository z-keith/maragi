from flask import Blueprint, render_template
from flask_login import login_required, current_user

dash = Blueprint('dash', __name__, template_folder='templates')

@dash.route('/dashboard')
@login_required
def dashboard():
	return render_template('dashboard.html')