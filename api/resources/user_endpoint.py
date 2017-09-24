from flask import jsonify
from flask_restful import Resource, reqparse, fields, marshal_with, abort

from api.utils.db_manager import manager
from api.utils.check_permissions import verify_auth_token

from common.user import User

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('firstname')
parser.add_argument('lastname')
parser.add_argument('email')
parser.add_argument('password')
parser.add_argument('user_id')
parser.add_argument('token')

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
	def post(self, user_id):
		token = parser.parse_args()['token']
		if not verify_auth_token(user_id, token):
			abort(403, description='token does not match the user requested')
		user = manager.get_user(user_id=user_id)
		if user:
			return user
		else:
			abort(404, description='user not found')
		
class GetAllUsers(Resource):
	@marshal_with(user_fields, envelope='users')
	def get(self):
		return manager.get_users()

class PostNewUser(Resource):
	@marshal_with(user_fields, envelope='user')
	def post(self):
		args = parser.parse_args()
		username = args['username']
		firstname = args['firstname']
		lastname = args['lastname']
		email = args['email']
		password = args['password'] 

		new_user = User(username, firstname, lastname, email)
		new_user.hash_password(password)

		validate_user_success, validate_user_reason = manager.validate_user(new_user)
		if validate_user_success:
			manager.add_user(new_user)
			return new_user
		else:
			abort(403, description=validate_user_reason)

class EditUser(Resource):
	@marshal_with(user_fields, envelope='user')
	def post(self, user_id):
		token = parser.parse_args()['token']
		if not verify_auth_token(user_id, token):
			abort(403, description='token does not match the user requested')