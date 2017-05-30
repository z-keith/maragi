from flask import jsonify

import config
from db.database import db

class Action(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	goal_id = db.Column(db.Integer)
	description = db.Column(db.String(64))

	def __init__(self, id, goal_id, description):
		self.id = id
		self.goal_id = goal_id
		self.description = description

	def to_json(self):
		return jsonify(status=200, id=self.id, goal_id=self.goal_id, description=self.description)

def action_from_json(json):
	id = json['id']
	goal_id = json['goal_id']
	description = json['description']
	return Action(id, goal_id, description)

def init_actions():
	g1 = Action(1, 1, 'Corned beef on rye')
	g2 = Action(2, 1, 'Peanut butter and jelly')
	g3 = Action(3, 2, 'Found fishbowl')
	g4 = Action(4, 3, 'Had sex on wing of commercial airliner')
	g5 = Action(5, 3, 'Had sex on wing of commercial airliner (w/ Walkmen)')
	g6 = Action(6, 4, 'Took interstellar trip')
	g7 = Action(7, 5, 'Red flying saucer')
	g8 = Action(8, 5, 'Green flying saucer')

	db.session.add(g1)
	db.session.add(g2)
	db.session.add(g3)
	db.session.add(g4)
	db.session.add(g5)
	db.session.add(g6)
	db.session.add(g7)
	db.session.add(g8)

	db.session.commit()