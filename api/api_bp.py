from flask import Blueprint
from flask_restful import Api, Resource

from api.resources.auth import RequestToken, ValidateToken

api_bp = Blueprint('api', __name__, template_folder='templates')
api = Api(api_bp)

class User(Resource):
	def get(self, id):
		# go out to database and build representation of user, and return it
		return {'id' : id}

api.add_resource(User, '/user/<int:id>')
api.add_resource(RequestToken, '/auth/request_token')
api.add_resource(ValidateToken, '/auth/validate_token')