import sqlite3

import config
from model.user import User
from model.goal import Goal
from model.action import Action

class DBManager:

	def __init__(self):
		self.db = sqlite3.connect(config.DATABASE_NAME)

	def get_results(self, table, where=None, order=None, limit=None):
		wherestring = ""
		orderstring = "" 
		limitstring = ""
		params = list()
		
		if where:
			wherestring = "WHERE"
			for clause in where:
				wherestring +=  " {0} {1} ? AND".format(clause.left, clause.operator)
				params.append(clause.right)
			wherestring = wherestring[:-3]
		
		if order:
			orderstring = " ORDER BY {0} {1} ".format(order.column, order.direction)
		
		if limit:
			limitstring = " LIMIT {0} ".format(limit.value)

		select_string = "SELECT * FROM {0} {1}{2}{3};".format(table, wherestring, orderstring, limitstring)
		param_tuple = tuple(params)
		cursor = self.db.execute(select_string, param_tuple)
		return cursor.fetchall()		

	def get_users(self, where=None, order=None, limit=None):
		users = self.get_results("user", where, order, limit)

		return_list = list()
		for row in users:
			return_list.append(User(row))
		return return_list		

	def get_goals(self, where=None, order=None, limit=None):
		goals = self.get_results("goal", where, order, limit)

		return_list = list()
		for row in goals:
			return_list.append(Goal(row))
		return return_list

	def get_actions(self, where=None, order=None, limit=None):
		actions = self.get_results("action", where, order, limit)

		return_list = list()
		for row in actions:
			return_list.append(Action(row))
		return return_list

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