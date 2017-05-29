from flask import jsonify
from flask_restful import Resource, reqparse

from api.utils.db_manager import DBManager, WhereClause

from common.user import User

class User(Resource):
	def get(self, id):
		db = DBManager()
		user = db.get_user_by_ID(id)
		if user:
			return user.to_json()
		else:
			return jsonify(message='user not found', status=404)