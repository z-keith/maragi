from itsdangerous import (JSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from passlib.hash import sha512_crypt

from api.utils.db_manager import manager
from config import SERIALIZER_KEY

def check_password(username, password):
	user = manager.get_user(username=username)
	if user:
		return sha512_crypt.verify(password, user.hashed_password)
	return None

def generate_auth_token(username):
	user = manager.get_user(username=username)

	s = Serializer(SERIALIZER_KEY)
	return user.user_id, s.dumps({ 'user_id': user.user_id })

def verify_auth_token(user_id, token):
	s = Serializer(SERIALIZER_KEY)
	try:
		data = s.loads(token)
	except BadSignature:
		return False

	return data['user_id'] == int(user_id)