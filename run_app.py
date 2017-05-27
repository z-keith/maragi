import os
from flask import Flask, render_template

from db.db_manager import DBManager, WhereClause, OrderClause, LimitClause

app = Flask(__name__)	

@app.route('/')
def index():
	db = DBManager()
	users = db.get_users()
	return render_template('index.html', users=users)
	
@app.errorhandler(404)
def not_found(error):
	return render_template('routing/404.html')

if __name__ == '__main__':
	app.debug = True
	host = os.environ.get('IP', '0.0.0.0')
	port = int(os.environ.get('PORT', 8080))
	app.run(host=host, port=port)
