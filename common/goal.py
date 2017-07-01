from flask import jsonify

import config
from db.database import db

class Goal(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer)
	title = db.Column(db.String(64))

	def __init__(self, user_id, title):
		self.user_id = user_id
		self.title = title

	def to_json(self):
		return jsonify(status=200, id=self.id, user_id=self.user_id, title=self.title)

	def validate(self):
		return True

def goal_from_json(json):
	id = json['id']
	user_id = json['user_id']
	title = json['title']
	ret = Goal(user_id, title)
	ret.id = id
	return ret

def init_goals():
	g1 = Goal(1, 'Make sandwiches')
	g2 = Goal(1, 'Save dolphins')
	g3 = Goal(2, 'Fly')
	g4 = Goal(2, 'Don''t disappear')
	g5 = Goal(3, 'Scan UFOs')
	g6 = Goal(3, 'Write articles')

	db.session.add(g1)
	db.session.add(g2)
	db.session.add(g3)
	db.session.add(g4)
	db.session.add(g5)
	db.session.add(g6)

	db.session.commit()