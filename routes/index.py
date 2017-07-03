from flask import Blueprint, render_template, url_for
from flask_login import current_user
import requests

from api.utils.db_manager import manager
from forms.login_form import LoginForm
from forms.new_user_form import NewUserForm
from forms.new_goal_form import NewGoalForm
from common.user import user_from_json
from common.goal import goal_from_json
from common.action import action_from_json

home = Blueprint('home', __name__, template_folder='templates')

@home.route('/')
def index():
	user_json_list = requests.get(url_for('api.getallusers', _external=True)).json()['users']

	user_list = list()

	for user_json in user_json_list:

		user = user_from_json(user_json)
		user_list.append(user)
		
		user.goals = list()
		goal_json_list = requests.get(user_json['goals_url']).json()['goals']

		for goal_json in goal_json_list:
			
			goal = goal_from_json(goal_json)
			user.goals.append(goal)

			goal.actions = list()
			action_json_list = requests.get(goal_json['actions_url']).json()['actions']

			for action_json in action_json_list:
				action = action_from_json(action_json)
				goal.actions.append(action)

	if current_user.get_id():
		ngf = NewGoalForm(user_id=current_user.user_id)
	else:
		ngf = None

	return render_template('index.html', users=user_list, loginform=LoginForm(), newuserform = NewUserForm(), newgoalform = ngf)