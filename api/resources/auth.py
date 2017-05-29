from flask import jsonify
from flask_restful import Resource, reqparse

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
		return jsonify(message='invalid username or password', status=401)
class ValidateToken(Resource):
	def post(self):
		args = parser.parse_args()
		token = args['token']
		id = verify_auth_token(token)
		if id:
			return jsonify(id=id, status=200)
		return jsonify(message='invalid token', status=401)