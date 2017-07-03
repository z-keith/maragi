from flask import jsonify
from flask_restful import Resource, reqparse, fields, marshal_with

from api.utils.db_manager import manager

from common.goal import Goal

parser = reqparse.RequestParser()
parser.add_argument('user_id')
parser.add_argument('title')

goal_fields = {
	'goal_id' : fields.Integer,
	'user_id' : fields.Integer,
	'title' : fields.String,
	'actions_url' : fields.Url('api.getactionsbygoalid', absolute=True)
}

class GetGoalByGoalID(Resource):
	@marshal_with(goal_fields, envelope='goal')
	def get(self, goal_id):
		return manager.get_goal(goal_id)

class GetGoalsByUserID(Resource):
	@marshal_with(goal_fields, envelope='goals')
	def get(self, user_id):
		return manager.get_goals(user_id)

class PostNewGoal(Resource):
	def post(self):
		args = parser.parse_args()
		user_id = args['user_id']
		title = args['title']		

		new_goal = Goal(user_id, title)
		if new_goal.validate():
			manager.add_goal(new_goal)

class EditGoal(Resource):
	def post(self):
		pass