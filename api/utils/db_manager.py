from sqlalchemy import func

import config
from db.database import db
from common.user import User
from common.goal import Goal
from common.action import Action

class DBManager:

	def get_users(self):
		return User.query.all()

	def get_user(self, user_id=None, username=None):
		if user_id:
			return User.query.filter_by(user_id=user_id).first()
		if username:
			return User.query.filter(func.lower(User.username)==func.lower(username)).first()
		return None

	def get_goals(self, user_id):
		return Goal.query.filter_by(user_id=user_id).all()

	def get_goal(self, goal_id):
		if goal_id:
			return Goal.query.filter_by(goal_id=goal_id).first()
		return None

	def get_actions(self, goal_id):
		return Action.query.filter_by(goal_id=goal_id).all()

	def get_action(self, action_id):
		if action_id:
			return Action.query.filter_by(action_id=action_id).first()
		return None

	def add_user(self, user):
		db.session.add(user)
		db.session.commit()

	def add_goal(self, goal):
		db.session.add(goal)
		db.session.commit()

	def add_action(self):
		pass

	def edit_user(self):
		pass

	def edit_goal(self):
		pass

	def edit_action(self):
		pass

	def delete_user(self):
		pass

	def delete_goal(self):
		pass

	def delete_action(self):
		pass

manager = DBManager()