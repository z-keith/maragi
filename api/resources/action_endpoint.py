from flask import jsonify
from flask_restful import Resource, reqparse, fields, marshal_with

from api.utils.db_manager import manager

from common.action import Action

parser = reqparse.RequestParser()
parser.add_argument('goal_id')
parser.add_argument('description')

action_fields = {
	'action_id' : fields.Integer,
	'goal_id' : fields.Integer,
	'description' : fields.String
}

class GetActionByActionID(Resource):
	@marshal_with(action_fields, envelope='action')
	def get(self, action_id):
		return manager.get_action(id)

class GetActionsByGoalID(Resource):
	@marshal_with(action_fields, envelope='actions')
	def get(self, goal_id):
		return manager.get_actions(goal_id)
		
class PostNewAction(Resource):
	def post(self):
		args = parser.parse_args()
		goal_id = args['goal_id']
		description = args['description']		

		new_action = Action(goal_id, description)
		if new_action.validate():
			manager.add_action(new_action)

class EditAction(Resource):
	def post(self):
		pass