from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user
import requests

from api.utils.db_manager import manager
from common.user import user_from_json
from common.goal import goal_from_json
from common.action import action_from_json
from forms.new_goal_form import NewGoalForm

dash = Blueprint('dash', __name__, template_folder='templates')

@dash.route('/dashboard')
@login_required
def dashboard():
	user_json = requests.get(url_for('api.getuserbyuserid', user_id=current_user.user_id, _external=True)).json()['user']
	user = user_from_json(user_json)
		
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

	ngf = NewGoalForm(user_id=current_user.user_id)

	return render_template('dashboard.html', user=user, newgoalform=ngf)

@dash.route('/settings')
@login_required
def settings():
	return render_template('settings.html')