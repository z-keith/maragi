from flask_restful import Resource, reqparse, fields, marshal_with

from api.user import User
from api.goal import Goal
from api.action import Action
from api.auth import request_token, validate_token

parser = reqparse.RequestParser()
parser.add_argument('user_id')
parser.add_argument('goal_id')
parser.add_argument('action_id')

parser.add_argument('username')
parser.add_argument('email')
parser.add_argument('firstname')
parser.add_argument('lastname')

parser.add_argument('title')
parser.add_argument('target_milliscore')
parser.add_argument('current_milliscore')
parser.add_argument('inverted')

parser.add_argument('description')
parser.add_argument('milli_value')

parser.add_argument('token')

user_fields = {
	'action_id' : fields.Integer,
	'goal_id' : fields.Integer,
	'description' : fields.String
}

goal_fields = {
	'action_id' : fields.Integer,
	'goal_id' : fields.Integer,
	'description' : fields.String
}

action_fields = {
	'action_id' : fields.Integer,
	'goal_id' : fields.Integer,
	'description' : fields.String
}

auth_fields = {
	'user_id' : fields.Integer,
	'token' : fields.String
}

class ReadUser(Resource):
	@marshal_with(user_fields, envelope='data')
	def post(self, user_id):
		pass

class ReadUsers(Resource):
	@marshal_with(user_fields, envelope='data')
	def post(self):
		pass

class ReadGoal(Resource):
	@marshal_with(goal_fields, envelope='data')
	def post(self, goal_id):
		pass

class ReadGoals(Resource):
	@marshal_with(goal_fields, envelope='data')
	def post(self, user_id):
		pass

class ReadAction(Resource):
	@marshal_with(action_fields, envelope='data')
	def post(self, action_id):
		pass

class ReadActions(Resource):
	@marshal_with(action_fields, envelope='data')
	def post(self, goal_id):
		pass

class AddUser(Resource):
	@marshal_with(user_fields, envelope='data')
	def post(self):
		pass

class AddGoal(Resource):
	@marshal_with(goal_fields, envelope='data')
	def post(self):
		pass

class AddAction(Resource):
	@marshal_with(action_fields, envelope='data')
	def post(self):
		pass

class EditUser(Resource):
	@marshal_with(user_fields, envelope='data')
	def patch(self, user_id):
		pass
	
class EditGoal(Resource):
	@marshal_with(goal_fields, envelope='data')
	def patch(self, goal_id):
		pass
	
class EditAction(Resource):
	@marshal_with(action_fields, envelope='data')
	def patch(self, action_id):
		pass

class DeleteUser(Resource):
	@marshal_with(user_fields, envelope='data')
	def delete(self, user_id):
		pass
	
class DeleteGoal(Resource):
	@marshal_with(goal_fields, envelope='data')
	def delete(self, goal_id):
		pass

class DeleteAction(Resource):
	@marshal_with(action_fields, envelope='data')
	def delete(self, action_id):
		pass

class ReactivateUser(Resource):
	@marshal_with(user_fields, envelope='data')
	def patch(self, user_id):
		pass

class ReactivateGoal(Resource):
	@marshal_with(goal_fields, envelope='data')
	def patch(self, goal_id):
		pass

class ReactivateAction(Resource):
	@marshal_with(action_fields, envelope='data')
	def patch(self, action_id):
		pass

class RequestToken(Resource):
	@marshal_with(auth_fields, envelope='data')
	def post(self):
		pass