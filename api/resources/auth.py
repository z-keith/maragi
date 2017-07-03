from flask import jsonify
from flask_restful import Resource, reqparse, abort

from api.utils.check_permissions import check_password, generate_auth_token, verify_auth_token

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')
parser.add_argument('token')

class RequestToken(Resource):
	def post(self):
		args = parser.parse_args()
		if check_password(args['username'], args['password']):
			token = generate_auth_token(args['username'])
			if token:
				return jsonify(token=token.decode('ascii'), status=200)
		else:
			abort(401, description='invalid username or password')
		
class ValidateToken(Resource):
	def post(self):
		args = parser.parse_args()
		token = args['token']
		user_id = verify_auth_token(token)
		if user_id:
			return jsonify(user_id=user_id, status=200)
		return jsonify(message='invalid token', status=401)