from flask import jsonify
from flask_restful import Resource, reqparse

from api.utils.db_manager import manager

from common.user import User

class UserEndpoint(Resource):
	def get(self, id):
		user = manager.get_user(id=id)
		if user:
			return user.to_json()
		else:
			return jsonify(message='user not found', status=404)

class UsersEndpoint(Resource):
	def get(self):
		users = manager.get_user_ids()
		if users:
			return jsonify(users = users, status = 200)
		else:
			return jsonify(message='users not found', status=404)