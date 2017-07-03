from flask import jsonify

import config
from db.database import db

class Action(db.Model):
	action_id = db.Column(db.Integer, primary_key=True)
	goal_id = db.Column(db.Integer)
	description = db.Column(db.String(64))

	def __init__(self, goal_id, description):
		self.goal_id = goal_id
		self.description = description

	def to_json(self):
		return jsonify(status=200, action_id=self.action_id, goal_id=self.goal_id, description=self.description)

def action_from_json(json):
	action_id = json['action_id']
	goal_id = json['goal_id']
	description = json['description']

	ret = Action(goal_id, description)
	ret.action_id = action_id
	return ret

def init_actions():
	g1 = Action(1, 'Corned beef on rye')
	g2 = Action(1, 'Peanut butter and jelly')
	g3 = Action(2, 'Found fishbowl')
	g4 = Action(3, 'Had sex on wing of commercial airliner')
	g5 = Action(3, 'Had sex on wing of commercial airliner (w/ Walkmen)')
	g6 = Action(4, 'Took interstellar trip')
	g7 = Action(5, 'Red flying saucer')
	g8 = Action(5, 'Green flying saucer')

	db.session.add(g1)
	db.session.add(g2)
	db.session.add(g3)
	db.session.add(g4)
	db.session.add(g5)
	db.session.add(g6)
	db.session.add(g7)
	db.session.add(g8)

	db.session.commit()