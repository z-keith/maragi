from flask_restful import Resource, fields, marshal_with

from api.action import Action
from api.parser import parser

action_fields = {
	'action_id' : fields.Integer,
	'goal_id' : fields.Integer,
	'description' : fields.String
}

class ReadAction(Resource):
	@marshal_with(action_fields, envelope='data')
	def post(self, action_id):
		pass

class ReadActions(Resource):
	@marshal_with(action_fields, envelope='data')
	def post(self, goal_id):
		pass

class AddAction(Resource):
	@marshal_with(action_fields, envelope='data')
	def post(self):
		pass
	
class EditAction(Resource):
	@marshal_with(action_fields, envelope='data')
	def patch(self, action_id):
		pass

class DeleteAction(Resource):
	@marshal_with(action_fields, envelope='data')
	def delete(self, action_id):
		pass

class ReactivateAction(Resource):
	@marshal_with(action_fields, envelope='data')
	def patch(self, action_id):
		pass