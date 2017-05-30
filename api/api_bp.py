from flask import Blueprint
from flask_restful import Api, Resource

from api.resources.auth import RequestToken, ValidateToken
from api.resources.user_endpoint import UserEndpoint, UsersEndpoint
from api.resources.goal_endpoint import GoalEndpoint, GoalsEndpoint
from api.resources.action_endpoint import ActionEndpoint, ActionsEndpoint

api_bp = Blueprint('api', __name__, template_folder='templates')
api = Api(api_bp)

api.add_resource(UsersEndpoint, '/users/')
api.add_resource(GoalsEndpoint, '/goals/<int:id>')
api.add_resource(ActionsEndpoint, '/actions/<int:id>')

api.add_resource(UserEndpoint, '/user/<int:id>')
api.add_resource(GoalEndpoint, '/goal/<int:id>')
api.add_resource(ActionEndpoint, '/action/<int:id>')

api.add_resource(RequestToken, '/auth/request_token')
api.add_resource(ValidateToken, '/auth/validate_token')