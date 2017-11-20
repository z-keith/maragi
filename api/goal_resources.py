from flask_restful import Resource, fields, marshal_with

from api.goal import Goal
from api.parser import parser

goal_fields = {
	'action_id' : fields.Integer,
	'goal_id' : fields.Integer,
	'description' : fields.String
}

class ReadGoal(Resource):
	@marshal_with(goal_fields, envelope='data')
	def post(self, goal_id):
		pass

class ReadGoals(Resource):
	@marshal_with(goal_fields, envelope='data')
	def post(self, user_id):
		pass

class AddGoal(Resource):
	@marshal_with(goal_fields, envelope='data')
	def post(self):
		pass

class EditGoal(Resource):
	@marshal_with(goal_fields, envelope='data')
	def patch(self, goal_id):
		pass

class DeleteGoal(Resource):
	@marshal_with(goal_fields, envelope='data')
	def delete(self, goal_id):
		pass

class ReactivateGoal(Resource):
	@marshal_with(goal_fields, envelope='data')
	def patch(self, goal_id):
		pass