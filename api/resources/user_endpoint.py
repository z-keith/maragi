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