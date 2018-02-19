from itsdangerous import (JSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

from api.user import User
from instance.config import Config

def request_token(username, password):
	serializer = Serializer(Config.SERIALIZER_KEY)

	user, msg = User.get_by_username(username)
	if user is None:
		return None, msg
	elif user.verify_password(password):
		token = serializer.dumps({'user_id': user.user_id})
		return user.user_id, token
	else:
		return None, "Invalid password"

def validate_token(user_id, token):
	serializer = Serializer(Config.SERIALIZER_KEY)
	
	try:
		data = serializer.loads(token)
		if data['user_id'] == user_id:
			return True, None
		else:
			return False, "Mismatched token"
	except SignatureExpired:
		return False, "Signature expired"
	except BadSignature:
		return False, "Bad signature"