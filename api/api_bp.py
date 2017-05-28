from flask import Blueprint
from flask_restful import Api, Resource

api_bp = Blueprint('api', __name__, template_folder='templates')
api = Api(api_bp)

class User(Resource):
	def get(self, id):
		# go out to database and build representation of user, and return it
		return {'id' : id}

api.add_resource(User, '/user/<int:id>')