from flask import Blueprint, render_template

errors = Blueprint('errors', __name__, template_folder='templates')

@errors.errorhandler(404)
def not_found(error):
	return render_template('routing/404.html')