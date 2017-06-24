from flask import jsonify
from flask_restful import Resource, reqparse

from api.utils.db_manager import manager

from common.user import User

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('firstname')
parser.add_argument('lastname')
parser.add_argument('email')
parser.add_argument('password')

class UserEndpoint(Resource):
	def get(self, id):
		user = manager.get_user(id=id)
		if user:
			return user.to_json()
		else:
			return jsonify(message='user not found', status=404)

class UsersEndpoint(Resource):
	def get(self):
		users = manager.get_user_ids()
		if users:
			return jsonify(users = users, status = 200)
		else:
			return jsonify(message='users not found', status=404)

	def post(self):
		args = parser.parse_args()
		username = args['username']
		firstname = args['firstname']
		lastname = args['lastname']
		email = args['email']
		password = args['password'] 

		new_user = User(username, firstname, lastname, email)
		new_user.hash_password(password)
		if new_user.validate():
			manager.add_user(new_user)