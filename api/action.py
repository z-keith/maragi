from sqlalchemy.exc import IntegrityError, DataError

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
		from api.goal import Goal
		try:
			int(self.milli_value)
			int(self.goal_id)
			g, msg = Goal.get_by_id(self.goal_id)
			if g is None:
				return False, ["User ID does not exist"]
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
			return self.action_id, "Added new action successfully."
		except IntegrityError as e:
			db.session.rollback()
			return None, str(e.orig.diag.message_primary)
		except:
			db.session.rollback()
			return None, "An unknown error occurred."

	@staticmethod
	def get_all_from_goal_id(goal_id):
		try:
			return Action.query.filter_by(goal_id=goal_id, deleted=False).all()
		except DataError as e:
			return None, str(e.orig.diag.message_primary)

	@staticmethod
	def get_by_id(action_id):
		try:
			return_val = Action.query.filter_by(action_id=action_id, deleted=False).first()
			if return_val is None:
				return None, "No active action with that ID."
			return return_val, "Action found successfully."
		except DataError as e:
			return None, str(e.orig.diag.message_primary)
		except:
			return None, "An unknown error occurred."

	def edit(self, description=None, milli_value=None):
		if self.deleted:
			return None, "Action previously deleted."

		if description is not None:
			self.description = description
		if milli_value is not None:
			self.milli_value = milli_value

		valid, messages = self.validate()
		if not valid:
			db.session.rollback()
			return None, messages
		try:
			db.session.commit()
			return self, "Action edited successfully."
		except:
			db.session.rollback()
			return None, "An unknown error occurred."

	def delete(self):
		if self.deleted:
			return None, "Action already deleted."
		self.deleted = True
		db.session.commit()
		return self.action_id, "Action deleted successfully."

	@staticmethod
	def reactivate(id):
		try:
			action = Action.query.filter_by(action_id=id).first()
			if action is not None:
				action.deleted = False
				db.session.commit()
				return action, "Action found and activated."
			else:
				return None, "No action found with that ID."
		except DataError as e:
			return None, str(e.orig.diag.message_primary)
		except:
			return None, "An unknown error occurred."

