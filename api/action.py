from sqlalchemy.exc import IntegrityError

from instance.db import db

class Action(db.Model):

	action_id = db.Column(db.Integer, primary_key=True)
	goal_id = db.Column(db.Integer)
	description = db.Column(db.String(64))
	milli_value = db.Column(db.Integer) # 1 point is stored as 1000, etc

	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    	onupdate=db.func.current_timestamp())
	deleted = db.Column(db.Boolean, default=False)

	def __init__(self, goal_id, description, milli_value):
		self.goal_id = goal_id
		self.description = description
		self.milli_value = milli_value

	def validate(self):
		return True, None

	# database interaction functions
	def add(self):
		valid, messages = self.validate()
		if not valid:
			return None, messages
		try:
			db.session.add(self)
			db.session.commit()
			return self.goal_id, "Added new action successfully."
		except IntegrityError as e:
			db.session.rollback()
			return None, str(e.orig.diag.message_primary)
		except:
			db.session.rollback()
			return None, "An unknown error occurred."

	@staticmethod
	def get_all_from_goal_id(goal_id):
		pass

	@staticmethod
	def get_by_id(action_id):
		pass

	def edit(self):
		pass

	def delete(self):
		pass

	@staticmethod
	def reactivate(id):
		pass

