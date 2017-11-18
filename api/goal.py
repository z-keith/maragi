from sqlalchemy.exc import IntegrityError

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

	# database interaction functions
	def add(self):
		try:
			db.session.add(self)
			db.session.commit()
			return self.goal_id, "Added new goal successfully."
		except IntegrityError as e:
			return None, str(e.orig.diag.message_primary)
		except:
			return None, "An unknown error occurred."

	@staticmethod
	def get_all_from_user_ID(user_id):
		pass

	@staticmethod
	def get_by_id(goal_id):
		pass

	def edit(self):
		pass

	def delete(self):
		pass

