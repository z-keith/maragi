import unittest

from instance.app import create_app
from api.user import User
from api.action import Action

class actionTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		# actionTest.app = create_app('testing')
		pass

	def setUp(self):
		actionTest.app = create_app('testing')

	def tearDown(self):
		pass
	
	def test_action_creation(self):
		with actionTest.app.app_context():
			a1 = Action(1, 'Tuna', 1000)
			id, message = a1.add()
			self.assertEqual(id, 9, msg="Action not created?")

			a1 = Action(9, 'Tuna', 1000)
			id, message = a1.add()
			self.assertIsNone(id, msg="Created action with invalid goal id")

	def test_action_get_all_by_goal(self):
		with actionTest.app.app_context():
			all_actions = Action.get_all_from_goal_id(1)
			
			# Should be a list of 2 Action objects
			self.assertIsInstance(all_actions, list, msg="Did not return a list")
			for action in all_actions:
				self.assertIsInstance(action, Action, msg="Contained a non-Action object")
			self.assertEqual(len(all_actions), 2, msg="Did not return 2 Actions")

	def test_action_get_by_ID(self):
		with actionTest.app.app_context():
			# valid IDs
			a1, a1_msg = Action.get_by_id(1)
			self.assertIsInstance(a1, Action, msg="Returned a non-Action object")
			self.assertEqual(a1.description, 'Corned beef on rye', msg="Returned the wrong action")
			a3, a3_msg = Action.get_by_id(3)
			self.assertIsInstance(a3, Action, msg="Returned a non-Action object")
			self.assertEqual(a3.description, 'Found fishbowl', msg="Returned the wrong action")

			# invalid IDs
			a9, a9_msg = Action.get_by_id(9)
			self.assertIsNone(a9, msg="Did not return None for a nonexistant ID")
			self.assertEqual(a9_msg, "No active action with that ID.", msg="Did not properly respond to a nonexistant ID")
			aA, aA_msg = Action.get_by_id('A')
			self.assertIsNone(aA, msg="Did not return None for an invalid ID")

	def test_action_edit(self):
		with actionTest.app.app_context():
			a1, a1_msg = Action.get_by_id(1)
			# 1 valid update
			u, msg = a1.edit(description="SANDWICHES!!!")
			self.assertEqual(a1.description, "SANDWICHES!!!", msg="Did not update this field.")
			# 2 valid updates
			u, msg = a1.edit(description="sandwiches??", milli_value=999)
			self.assertEqual(a1.description, "sandwiches??", msg="Did not update this field.")
			self.assertEqual(a1.milli_value, 999, msg="Did not update this field.")
			# No updates
			u, msg = a1.edit()
			self.assertEqual(msg, "Action edited successfully.", msg="Did not handle an empty update operation.")
			# valid and invalid updates
			u, msg = a1.edit(description="nope", milli_value="a")
			self.assertIsNone(u, msg="Did not return None when there was an invalid field.")
			self.assertNotEqual(a1.description, "nope", msg="Updated a field with a valid value, when there was an invalid value in the same transaction.")
			self.assertEqual(a1.milli_value, 999, msg="Updated a field with an invalid value.")

	def test_action_delete(self):
		with actionTest.app.app_context():
			# valid delete
			a1, response = Action.get_by_id(1)
			a1_id, response = a1.delete()
			self.assertEqual(a1_id, 1, msg="Deleted wrong action or returned wrong value")

			# attempt to modify/delete deleted item
			a1_id, response = a1.delete()
			self.assertIsNone(a1_id, msg="Returned wrong value when deleting a deleted action")
			self.assertEqual(response, "Action already deleted.")
			a1, response = a1.edit(description="So much sandwich")
			self.assertIsNone(a1, msg="Returned wrong value when editing a deleted action")
			self.assertEqual(response, "Action previously deleted.")

	def test_action_reactivate(self):
		with actionTest.app.app_context():
			a1, response = Action.get_by_id(1)
			a1_id, response = a1.delete()
			self.assertEqual(a1_id, 1)

			a1, response = Action.reactivate(1)
			self.assertFalse(a1.deleted, msg="Deleted attribute still set to false")

			a3, response = Action.reactivate(3)
			self.assertFalse(a3.deleted, msg="Reactivating active action deactivates it")

			a9, response = Action.reactivate(9)
			self.assertIsNone(a9, msg="Wrong response to reactivating nonexistant action")

			aA, aA_msg = Action.reactivate('A')
			self.assertIsNone(aA, msg="Wrong response to reactivating invalid id")

	def test_action_validate(self):
		with actionTest.app.app_context():
			a1 = Action(1, "test", 1000)
			valid, messages = a1.validate()
			self.assertTrue(valid, msg="Incorrectly marked as invalid")

			a1.goal_id = 0
			valid, messages = a1.validate()
			self.assertFalse(valid, msg="Incorrectly marked as valid [nonexistantgoal_id]")

			a1.goal_id = 'a'
			valid, messages = a1.validate()
			self.assertFalse(valid, msg="Incorrectly marked as valid [char goal_id]")

			a1.current_milliscore = 'a'
			valid, messages = a1.validate()
			self.assertFalse(valid, msg="Incorrectly marked as valid [char current_milliscore]")

			a1.target_milliscore = 'a'
			valid, messages = a1.validate()
			self.assertFalse(valid, msg="Incorrectly marked as valid [char target_milliscore]")