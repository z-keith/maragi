from flask import Blueprint
from flask_restful import Api, Resource

from api.resources.auth import RequestToken, ValidateToken
from api.resources.user_endpoint import UserEndpoint

api_bp = Blueprint('api', __name__, template_folder='templates')
api = Api(api_bp)

api.add_resource(UserEndpoint, '/user/<int:id>')
api.add_resource(RequestToken, '/auth/request_token')
api.add_resource(ValidateToken, '/auth/validate_token')