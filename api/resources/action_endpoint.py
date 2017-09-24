from flask import jsonify
from flask_restful import Resource, reqparse, fields, marshal_with

from api.utils.db_manager import manager
from api.utils.check_permissions import verify_auth_token

from common.action import Action

parser = reqparse.RequestParser()
parser.add_argument('goal_id')
parser.add_argument('description')
parser.add_argument('user_id')
parser.add_argument('token')

action_fields = {
	'action_id' : fields.Integer,
	'goal_id' : fields.Integer,
	'description' : fields.String
}

class GetActionByActionID(Resource):
	@marshal_with(action_fields, envelope='action')
	def post(self, action_id):
		token = parser.parse_args()['token']
		user_id = parser.parse_args()['user_id']
		if not verify_auth_token(user_id, token):
			abort(403, description='token does not match the user requested')
		return manager.get_action(id)

class GetActionsByGoalID(Resource):
	@marshal_with(action_fields, envelope='actions')
	def post(self, goal_id):
		token = parser.parse_args()['token']
		user_id = parser.parse_args()['user_id']
		if not verify_auth_token(user_id, token):
			abort(403, description='token does not match the user requested')
		return manager.get_actions(goal_id)
		
class PostNewAction(Resource):
	@marshal_with(action_fields, envelope='action')
	def post(self):
		args = parser.parse_args()
		goal_id = args['goal_id']
		description = args['description']		

		new_action = Action(goal_id, description)
		validate_action_success, validate_action_reason = manager.validate_action(new_action)
		if validate_action_success:
			manager.add_action(new_action)
			return new_action
		else:
			abort(403, description=validate_action_reason)

class EditAction(Resource):
	def post(self, action_id):
		token = parser.parse_args()['token']
		user_id = parser.parse_args()['user_id']
		if not verify_auth_token(user_id, token):
			abort(403, description='token does not match the user requested')

class DeleteAction(Resource):
	def post(self, action_id):
		token = parser.parse_args()['token']
		user_id = parser.parse_args()['user_id']
		if not verify_auth_token(user_id, token):
			abort(403, description='token does not match the user requested')