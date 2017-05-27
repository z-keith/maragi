from wtforms import Form, validators, fields

class LoginForm(Form):
	username = fields.StringField(u'Username', validators=[validators.input_required()])
	password = fields.StringField(u'Password', validators=[validators.input_required()])