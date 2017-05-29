import config
from common.user import User
from common.goal import Goal
from common.action import Action

class DBManager:

	def get_users(self):
		return User.query.all()

	def get_user(self, id=None, username=None):
		if id:
			return User.query.filter_by(id=id).first()
		if username:
			return User.query.filter_by(username=username).first()
		return None

	def get_goals(self):
		pass

	def get_actions(self, where=None, order=None, limit=None):
		pass

	def add_user(self):
		pass

	def add_goal(self):
		pass

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


class WhereClause:
	allowable_operators = ["<", "<=", "=", "!=", ">", ">=", "IS NULL", "IS NOT NULL", "LIKE", "EXISTS"]

	def __init__(self, left, operator, right):
		if operator in self.allowable_operators:
			self.left = left
			self.operator = operator
			self.right = right
		else:
			raise ValueError('Bad operator: {0}'.format(operator))

class OrderClause:
	allowable_orderings = ["ASC", "DESC"]

	def __init__(self, column, direction):
		if direction in self.allowable_orderings:
			self.column = column
			self.direction = direction
		else:
			raise ValueError('Bad orientation: {0}'.format(direction))

class LimitClause:
	def __init__(self, limit):
		if limit > 0:
			self.limit = int(limit)
		else:
			raise ValueError('Bad limit: {0}'.format(limit))

manager = DBManager()