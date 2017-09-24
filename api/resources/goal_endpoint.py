from flask import jsonify
from flask_restful import Resource, reqparse, fields, marshal_with, abort

from api.utils.db_manager import manager
from api.utils.check_permissions import verify_auth_token

from common.goal import Goal

parser = reqparse.RequestParser()
parser.add_argument('user_id')
parser.add_argument('title')
parser.add_argument('token')

goal_fields = {
	'goal_id' : fields.Integer,
	'user_id' : fields.Integer,
	'title' : fields.String,
	'actions_url' : fields.Url('api.getactionsbygoalid', absolute=True)
}

class GetGoalByGoalID(Resource):
	@marshal_with(goal_fields, envelope='goal')
	def post(self, goal_id):
		token = parser.parse_args()['token']
		user_id = parser.parse_args()['user_id']
		if not verify_auth_token(user_id, token):
			abort(403, description='token does not match the user requested')
		goal = manager.get_goal(goal_id)
		if goal:
			return goal
		else:
			abort(404, description='goal not found')

class GetGoalsByUserID(Resource):
	@marshal_with(goal_fields, envelope='goals')
	def post(self, user_id):
		token = parser.parse_args()['token']
		if not verify_auth_token(user_id, token):
			abort(403, description='token does not match the user requested')
		goals = manager.get_goals(user_id)
		return goals

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
	def post(self, goal_id):
		token = parser.parse_args()['token']
		user_id = parser.parse_args()['user_id']
		if not verify_auth_token(user_id, token):
			abort(403, description='token does not match the user requested')
		

class DeleteGoal(Resource):
	def post(self, goal_id):
		token = parser.parse_args()['token']
		user_id = parser.parse_args()['user_id']
		if not verify_auth_token(user_id, token):
			abort(403, description='token does not match the user requested')