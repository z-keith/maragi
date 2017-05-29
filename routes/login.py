from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from passlib.hash import sha512_crypt
import requests

from api.utils.db_manager import DBManager, WhereClause, OrderClause, LimitClause
from forms.login_form import LoginForm

from common.user import user_from_json

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login', methods=['POST'])
def login():
	if not current_user.get_id():
		username = request.form['username']
		password = request.form['password']
		
		token_response = requests.post(url_for('api.requesttoken', _external=True), data={'username' : username, 'password' : password})
		response_code = token_response.json()['status']

		if response_code == 200:
			token = token_response.json()['token']
			validate_response = requests.post(url_for('api.validatetoken', _external=True), data={'token' : token})
			user_id = validate_response.json()['id']
			# get user json
			user_json = requests.get(url_for('api.user', id=user_id, _external=True)).json()
			# build user object from json
			user = user_from_json(user_json)
			# login user object 	
			login_user(user, remember=True)
			user.token = token
		else:
			pass
			# login error
			return redirect(url_for('home.index'))
			
	return redirect(url_for('dash.dashboard'))

@auth.route("/logout")
def logout():
	if current_user.get_id():
		logout_user()
	return redirect(url_for('home.index'))

