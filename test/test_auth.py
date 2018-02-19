import unittest

from instance.app import create_app
from api.auth import request_token, validate_token

class authTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		#userTest.app = create_app('testing')
		pass

	def setUp(self):
		authTest.app = create_app('testing')

	def tearDown(self):
		pass
	
	def test_auth_request_token(self):
		with authTest.app.app_context():
			id, token=request_token('mustbethursday', 'test')
			self.assertEqual(id, 1, msg='Returned wrong user ID')

			id, token=request_token('Ix_prime', '42')
			self.assertEqual(id, 3, msg='Returned wrong user ID')

			id, token=request_token('mustbethursday', '42')
			self.assertIsNone(id, msg='Returned a user despite wrong password')

			id, token=request_token('mustbetuesday', 'test')
			self.assertIsNone(id, msg='Returned a user despite wrong username')

	def test_auth_validate_token(self):
		with authTest.app.app_context():
			id = 1
			token = 'eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.h6Fc_dET1SBK7aj1RxfrTPfBbWWxFXdDrja5eRD6tOA'
			valid, msg = validate_token(id, token)
			self.assertTrue(valid, msg=msg)

			id = 0
			valid, msg = validate_token(id, token)
			self.assertFalse(valid, msg=msg)

			id = 1
			token = 'ayJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.h6Fc_dET1SBK7aj1RxfrTPfBbWWxFXdDrja5eRD6tOA'
			valid, msg = validate_token(id, token)
			self.assertFalse(valid, msg=msg)