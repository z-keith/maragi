from flask import jsonify
from flask_restful import Resource, reqparse

from api.utils.db_manager import manager

from common.action import Action

class ActionEndpoint(Resource):
	def get(self, id):
		action = manager.get_action(id)
		if action:
			return action.to_json()
		else:
			return jsonify(message='action not found', status=404)

class ActionsEndpoint(Resource):
	def get(self, id):
		actions = manager.get_action_ids(id)
		if actions:
			return jsonify(actions = actions, status = 200)
		else:
			return jsonify(message='actions for goal not found', status=404)