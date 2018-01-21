from api.user import User

u = User('a','b','c','d@e')
print(('test->'))
print(u.hash_password('test'))
print('42 ->')
print(u.hash_password('42'))