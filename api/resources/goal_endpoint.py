from flask import jsonify
from flask_restful import Resource, reqparse, fields, marshal_with, abort

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
		goal = manager.get_goal(goal_id)
		if goal:
			return goal
		else:
			abort(404, description='goal not found')

class GetGoalsByUserID(Resource):
	@marshal_with(goal_fields, envelope='goals')
	def get(self, user_id):
		goals = manager.get_goals(user_id)
		if goals:
			return goals
		else:
			abort(404, description='no goals for this user id')

class PostNewGoal(Resource):
	@marshal_with(goal_fields, envelope='goal')
	def post(self):
		args = parser.parse_args()
		user_id = args['user_id']
		title = args['title']		

		new_goal = Goal(user_id, title)
		validate_goal_success, validate_goal_reason = manager.validate_goal(new_goal)
		if validate_goal_success:
			manager.add_goal(new_goal)
			return new_goal
		else:
			abort(403, description=validate_goal_reason)

class EditGoal(Resource):
	@marshal_with(goal_fields, envelope='goal')
	def post(self):
		pass