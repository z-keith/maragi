from wtforms import Form, validators, fields

class NewUserForm(Form):
	username = fields.StringField(u'Username', validators=[validators.input_required()])
	password = fields.StringField(u'Password', validators=[validators.input_required()])
	email = fields.StringField(u'Email', validators=[validators.input_required()])
	firstname = fields.StringField(u'First Name', validators=[validators.input_required()])
	lastname = fields.StringField(u'Last Name', validators=[validators.input_required()])