from sqlalchemy.exc import IntegrityError, DataError

from instance.db import db

class Goal(db.Model):

	goal_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer)
	title = db.Column(db.String(64))
	current_milliscore = db.Column(db.Integer)
	target_milliscore = db.Column(db.Integer)
	inverted = db.Column(db.Boolean)

	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    	onupdate=db.func.current_timestamp())
	deleted = db.Column(db.Boolean, default=False)

	def __init__(self, user_id, title, target_milliscore, inverted=False):
		self.user_id = user_id
		self.title = title
		self.target_milliscore = target_milliscore
		if inverted:
			self.current_milliscore = target_milliscore
			self.inverted = True
		else:
			self.current_milliscore = 0
			self.inverted = False

	def validate(self):
		try:
			int(self.current_milliscore)
			int(self.target_milliscore)
			int(self.user_id)
			return True, None
		except:
			return False, ["Invalid parameter format"]

	# database interaction functions
	def add(self):
		valid, messages = self.validate()
		if not valid:
			return None, messages
		try:
			db.session.add(self)
			db.session.commit()
			return self.goal_id, "Added new goal successfully."
		except IntegrityError as e:
			db.session.rollback()
			return None, str(e.orig.diag.message_primary)
		except:
			db.session.rollback()
			return None, "An unknown error occurred."

	@staticmethod
	def get_all_from_user_id(user_id):
		return Goal.query.filter_by(user_id=user_id, deleted=False).all()

	@staticmethod
	def get_by_id(goal_id):
		try:
			return_val = Goal.query.filter_by(goal_id=goal_id, deleted=False).first()
			if return_val is None:
				return None, "No active goal with that ID."
			return return_val, "Goal found successfully."
		except DataError as e:
			return None, str(e.orig.diag.message_primary)
		except:
			return None, "An unknown error occurred."

	def edit(self, title=None, current_milliscore=None, target_milliscore=None):
		if self.deleted:
			return None, "Goal previously deleted."

		if current_milliscore is not None:
			self.current_milliscore = current_milliscore
		if target_milliscore is not None:
			self.target_milliscore = target_milliscore
		if title is not None:
			self.title = title
		valid, messages = self.validate()
		if not valid:
			db.session.rollback()
			return None, messages
		try:
			db.session.commit()
			return self, "Goal edited successfully."
		except:
			db.session.rollback()
			return None, "An unknown error occurred."

	def increment_milliscore(self, d_milliscore):
		if self.inverted:
			new_milliscore = self.current_milliscore - d_milliscore
		else:
			new_milliscore = self.current_milliscore + d_milliscore

		# round numbers that are very close to 1/4, 1/2, or whole numbers to account for people counting 1/3 or 1/6 of something
		diff_from_round = new_milliscore%100
		if diff_from_round in [1,2,98,99]: #.167*6=1.002, 1-ans=.998, .333*3=.999, 1-ans=.001
			new_milliscore = round(new_milliscore/100)*100

		return self.edit(current_milliscore=new_milliscore)

	def delete(self):
		if self.deleted:
			return None, "Goal already deleted."
		self.deleted = True
		db.session.commit()
		return self.user_id, "Goal deleted successfully."

	@staticmethod
	def reactivate(goal_id):
		goal = Goal.query.filter_by(goal_id=goal_id).first()
		if goal is not None:
			goal.deleted = False
			db.session.commit()
			return goal, "Goal found and activated."
		else:
			return None, "No goal found with that ID."

