from flask import jsonify
from flask_restful import Resource, reqparse

from api.utils.db_manager import manager

from common.goal import Goal

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