from flask import jsonify
from flask_restful import Resource, reqparse, abort

from api.utils.check_permissions import check_password, generate_auth_token, verify_auth_token

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')
parser.add_argument('token')
parser.add_argument('user_id')

class RequestToken(Resource):
	def post(self):
		args = parser.parse_args()
		if check_password(args['username'], args['password']):
			user_id, token = generate_auth_token(args['username'])
			if token:
				return jsonify(user_id= user_id, token=token.decode('ascii'), status=200)
		else:
			abort(401, description='invalid username or password')
		
class ValidateToken(Resource):
	def post(self):
		args = parser.parse_args()
		user_id = args['user_id']
		token = args['token']
		token_as_expected = verify_auth_token(user_id, token)
		if token_as_expected:
			return jsonify(user_id=user_id, status=200)
		abort(401, description='invalid token')