from wtforms import Form, validators, fields

class NewGoalForm(Form):
	user_id = fields.HiddenField(u'', validators=[validators.input_required()])
	title = fields.StringField(u'Goal Title', validators=[validators.input_required()])