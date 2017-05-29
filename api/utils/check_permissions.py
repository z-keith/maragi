from itsdangerous import (JSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from passlib.hash import sha512_crypt

from api.utils.db_manager import DBManager, WhereClause
from config import SERIALIZER_KEY

def check_password(username, password):
	where = [WhereClause('username', '=', username)]
	db = DBManager()
	users = db.get_users(where)
	if len(users) != 1:
		return False
	user = users[0]

	return sha512_crypt.verify(password, user.hashed_password)

def generate_auth_token(username):
	where = [WhereClause('username', '=', username)]
	db = DBManager()
	users = db.get_users(where)
	if len(users) != 1:
		return None
	user = users[0]

	s = Serializer(SERIALIZER_KEY)
	return s.dumps({ 'id': user.id })

def verify_auth_token(token):
	s = Serializer(SERIALIZER_KEY)
	try:
		data = s.loads(token)
	except BadSignature:
		return None

	return data['id']

