from flask_restful import Resource, fields, marshal_with

from api.auth import request_token
from api.parser import parser

auth_fields = {
	'user_id' : fields.Integer,
	'token' : fields.String
}

class RequestToken(Resource):
	@marshal_with(auth_fields, envelope='data')
	def post(self):
		pass