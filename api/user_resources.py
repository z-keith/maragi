from flask_restful import Resource, fields, marshal_with

from api.user import User
from api.parser import parser

user_fields = {
	'user_id'  : fields.Integer,
	'username' : fields.String,
	'email' : fields.String,
	'firstname' : fields.String,
	'lastname' : fields.String
}

class ReadUser(Resource):
	@marshal_with(user_fields, envelope='data')
	def post(self, user_id):
		name = parser.parse_args()['firstname']

class ReadUsers(Resource):
	@marshal_with(user_fields, envelope='data')
	def post(self):
		pass

class AddUser(Resource):
	@marshal_with(user_fields, envelope='data')
	def post(self):
		pass

class EditUser(Resource):
	@marshal_with(user_fields, envelope='data')
	def patch(self, user_id):
		pass
	
class DeleteUser(Resource):
	@marshal_with(user_fields, envelope='data')
	def delete(self, user_id):
		pass

class ReactivateUser(Resource):
	@marshal_with(user_fields, envelope='data')
	def patch(self, user_id):
		pass