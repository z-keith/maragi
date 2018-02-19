from itsdangerous import JSONWebSignatureSerializer as Serializer
from instance.config import Config
from api.auth import validate_token

serializer = Serializer(Config.SERIALIZER_KEY)
token = serializer.dumps({'user_id': 1})
print('userid = 1')
print(token)
print (validate_token(1, token)[0])
token = serializer.dumps({'user_id': 2})
print('\nuserid = 2')
print(token)
print (validate_token(2, token)[0])
token = serializer.dumps({'user_id': 3})
print('\nuserid = 3')
print(token)
print (validate_token(3, token)[0])