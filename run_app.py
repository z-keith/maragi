import os
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, current_user
from passlib.hash import sha512_crypt

from db.db_manager import DBManager, WhereClause, OrderClause, LimitClause
from forms.login_form import LoginForm
import config

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
	db = DBManager()
	users = db.get_users([WhereClause('id', '=', user_id)])
	if len(users) == 1:
		return users[0]
	else:
		return None

@app.route('/')
def index():
	return render_template('index.html', users=users)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		db = DBManager()
		users = db.get_users([WhereClause('username', '=', request.form['username'])])
		if len(users) == 1:
			if sha512_crypt.verify(request.form['password'], users[0].hashed_password):
				login_user(users[0])
				return redirect(url_for('index'))
	return render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(flask.url_for('index'))
	
@app.errorhandler(404)
def not_found(error):
	return render_template('routing/404.html')

if __name__ == '__main__':
	app.debug = True
	app.secret_key = config.SECRET_KEY

	host = os.environ.get('IP', '0.0.0.0')
	port = int(os.environ.get('PORT', 8080))
	app.run(host=host, port=port)
