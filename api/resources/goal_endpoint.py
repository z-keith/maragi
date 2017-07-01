from flask import jsonify
from flask_restful import Resource, reqparse

from api.utils.db_manager import manager

from common.goal import Goal

parser = reqparse.RequestParser()
parser.add_argument('user_id')
parser.add_argument('title')

class GoalEndpoint(Resource):
	def get(self, id):
		goal = manager.get_goal(id)
		if goal:
			return goal.to_json()
		else:
			return jsonify(message='goal not found', status=404)

class GoalsEndpoint(Resource):
	def get(self, id):
		goals = manager.get_goal_ids(id)
		if goals:
			return jsonify(goals = goals, status = 200)
		else:
			return jsonify(message='goals for user not found', status=404)

	def post(self):
		args = parser.parse_args()
		user_id = args['user_id']
		title = args['title']		

		new_goal = Goal(user_id, title)
		if new_goal.validate():
			manager.add_goal(new_goal)