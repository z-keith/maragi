
from flask import Blueprint
from flask_restful import Api

from api.resources import *

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(ReadUser, '/user/<int:user_id>')
api.add_resource(ReadUsers, '/users')
api.add_resource(ReadGoal, '/goal/<int:goal_id>')
api.add_resource(ReadGoals, '/goals/<int:user_id>')
api.add_resource(ReadAction, '/action/<int:action_id>')
api.add_resource(ReadActions, '/actions/<int:goal_id>')

api.add_resource(AddUser, '/user')
api.add_resource(AddGoal, '/goal')
api.add_resource(AddAction, '/action')

api.add_resource(EditUser, '/user/<int:user_id>/edit')
api.add_resource(EditGoal, '/goal/<int:goal_id>/edit')
api.add_resource(EditAction, '/action/<int:action_id>/edit')

api.add_resource(DeleteUser, '/user/<int:user_id>/delete')
api.add_resource(DeleteGoal, '/goal/<int:goal_id>/delete')
api.add_resource(DeleteAction, '/action/<int:action_id>/delete')

api.add_resource(ReactivateUser, '/user/<int:user_id>/reactivate')
api.add_resource(ReactivateGoal, '/goal/<int:goal_id>/reactivate')
api.add_resource(ReactivateAction, '/action/<int:action_id>/reactivate')

api.add_resource(RequestToken, '/login')
api.add_resource(ValidateToken, '/validate')