from flask import jsonify

import config
from db.database import db

class Goal(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer)
	title = db.Column(db.String(64))

	def __init__(self, id, user_id, title):
		self.id = id
		self.user_id = user_id
		self.title = title

	def to_json(self):
		return jsonify(status=200, id=self.id, user_id=self.user_id, title=self.title)

def goal_from_json(json):
	id = json['id']
	user_id = json['user_id']
	title = json['title']
	return Goal(id, user_id, title)

def init_goals():
	g1 = Goal(1, 1, 'Make sandwiches')
	g2 = Goal(2, 1, 'Save dolphins')
	g3 = Goal(3, 2, 'Fly')
	g4 = Goal(4, 2, 'Don''t disappear')
	g5 = Goal(5, 3, 'Scan UFOs')
	g6 = Goal(6, 3, 'Write articles')

	db.session.add(g1)
	db.session.add(g2)
	db.session.add(g3)
	db.session.add(g4)
	db.session.add(g5)
	db.session.add(g6)

	db.session.commit()