from flask import Blueprint, render_template, url_for
from flask_login import current_user
import requests

from api.utils.db_manager import manager
from forms.login_form import LoginForm
from forms.new_user_form import NewUserForm
from common.user import user_from_json
from common.goal import goal_from_json
from common.action import action_from_json

home = Blueprint('home', __name__, template_folder='templates')

@home.route('/')
def index():
	user_id_list = requests.get(url_for('api.usersendpoint', _external=True)).json()
	if not user_id_list['status'] == 200:
		return 'nope'
	user_id_list = user_id_list['users']
	user_list = list()
	for user_id in user_id_list:
		user_json = requests.get(url_for('api.userendpoint', id=user_id, _external=True)).json()
		if not user_json['status'] == 200:
			continue
		user = user_from_json(user_json)
		user_list.append(user)
		
		user.goals = list()
		goal_id_list = requests.get(url_for('api.goalsendpoint', id=user_id, _external=True)).json()
		if not goal_id_list['status'] == 200:
			continue
		goal_id_list = goal_id_list['goals']

		for goal_id in goal_id_list:
			goal_json = requests.get(url_for('api.goalendpoint', id=goal_id, _external=True)).json()
			if not goal_json['status'] == 200:
				continue
			goal = goal_from_json(goal_json)
			user.goals.append(goal)

			goal.actions = list()
			action_id_list = requests.get(url_for('api.actionsendpoint', id=goal_id, _external=True)).json()
			if not action_id_list['status'] == 200:
				continue
			action_id_list = action_id_list['actions']

			for action_id in action_id_list:
				action_json = requests.get(url_for('api.actionendpoint', id=action_id, _external=True)).json()
				action = action_from_json(action_json)
				goal.actions.append(action)

	return render_template('index.html', users=user_list, loginform=LoginForm(), newuserform = NewUserForm())