from flask import jsonify
from flask_restful import Resource, reqparse, fields, marshal_with

from api.utils.db_manager import manager

from common.user import User

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('firstname')
parser.add_argument('lastname')
parser.add_argument('email')
parser.add_argument('password')

user_fields = {
	'user_id' : fields.Integer,
	'username' : fields.String,
	'firstname' : fields.String,
	'lastname' : fields.String,
	'email' : fields.String,
	'goals_url' : fields.Url('api.getgoalsbyuserid', absolute=True)
}

class GetUserByUserID(Resource):
	@marshal_with(user_fields, envelope='user')
	def get(self, user_id):
		return manager.get_user(user_id=user_id)
		
class GetAllUsers(Resource):
	@marshal_with(user_fields, envelope='users')
	def get(self):
		return manager.get_users()

class PostNewUser(Resource):
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

class EditUser(Resource):
	def post(self):
		pass