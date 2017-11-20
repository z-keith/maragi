from flask_restful import reqparse

def generate_parser():
	parser = reqparse.RequestParser()
	parser.add_argument('user_id')
	parser.add_argument('goal_id')
	parser.add_argument('action_id')

	parser.add_argument('username')
	parser.add_argument('email')
	parser.add_argument('firstname')
	parser.add_argument('lastname')

	parser.add_argument('title')
	parser.add_argument('target_milliscore')
	parser.add_argument('current_milliscore')
	parser.add_argument('inverted')

	parser.add_argument('description')
	parser.add_argument('milli_value')

	parser.add_argument('token')

	return parser

parser = generate_parser()