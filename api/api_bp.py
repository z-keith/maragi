from flask import Blueprint
from flask_restful import Api, Resource

from api.resources.auth import RequestToken, ValidateToken
from api.resources.user_endpoint import GetUserByUserID, GetAllUsers, PostNewUser, EditUser
from api.resources.goal_endpoint import GetGoalByGoalID, GetGoalsByUserID, PostNewGoal, EditGoal, DeleteGoal
from api.resources.action_endpoint import GetActionByActionID, GetActionsByGoalID, PostNewAction, EditAction, DeleteAction

api_bp = Blueprint('api', __name__, template_folder='templates')
api = Api(api_bp)

#api.add_resource(GetAllUsers, '/users')
api.add_resource(GetGoalsByUserID, '/user/<int:user_id>/goals')
api.add_resource(GetActionsByGoalID, '/goal/<int:goal_id>/actions')

api.add_resource(GetUserByUserID, '/user/<int:user_id>')
api.add_resource(GetGoalByGoalID, '/goal/<int:goal_id>')
api.add_resource(GetActionByActionID, '/action/<int:action_id>')

api.add_resource(PostNewUser,'/add_user')
api.add_resource(PostNewGoal, '/add_goal')
api.add_resource(PostNewAction, '/add_action')

api.add_resource(EditUser, '/user/<int:user_id>/edit')
api.add_resource(EditGoal, '/goal/<int:goal_id>/edit')
api.add_resource(EditAction, '/action/<int:action_id>/edit')

api.add_resource(DeleteGoal, '/goal<int:goal_id>/delete')
api.add_resource(DeleteAction, '/action/<int:action_id>/delete')

api.add_resource(RequestToken, '/auth/request_token')
api.add_resource(ValidateToken, '/auth/validate_token')