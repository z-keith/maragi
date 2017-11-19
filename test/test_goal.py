import unittest

from instance.app import create_app
from api.user import User
from api.goal import Goal
from api.action import Action

class goalTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		# goalTest.app = create_app('testing')
		pass

	def setUp(self):
		goalTest.app = create_app('testing')

	def tearDown(self):
		pass
	
	def test_goal_creation(self):
		with goalTest.app.app_context():
			g1 = Goal(1, 'Make 100 unloved children', 100000)
			id, message = g1.add()
			self.assertEqual(id, 7, msg="Goal not created?")

	def test_goal_get_all(self):
		with goalTest.app.app_context():
			all_goals = Goal.get_all_from_user_id(1)
			
			# Should be a list of 2 Goal objects
			self.assertIsInstance(all_goals, list, msg="Did not return a list")
			for goal in all_goals:
				self.assertIsInstance(goal, Goal, msg="Contained a non-Goal object")
			self.assertEqual(len(all_goals), 2, msg="Did not return 2 Goals")

	def test_goal_get_by_ID(self):
		with goalTest.app.app_context():
			# valid IDs
			g1, g1_msg = Goal.get_by_id(1)
			self.assertIsInstance(g1, Goal, msg="Returned a non-Goal object")
			self.assertEqual(g1.title, 'Make 100 sandwiches', msg="Returned the wrong goal")
			g3, g3_msg = Goal.get_by_id(3)
			self.assertIsInstance(g3, Goal, msg="Returned a non-Goal object")
			self.assertEqual(g3.title, 'Fly 6 times', msg="Returned the wrong goal")

			# invalid IDs
			g8, g8_msg = Goal.get_by_id(8)
			self.assertIsNone(g8, msg="Did not return None for a nonexistant ID")
			self.assertEqual(g8_msg, "No active goal with that ID.", msg="Did not properly respond to a nonexistant ID")
			gA, gA_msg = Goal.get_by_id('A')
			self.assertIsNone(gA, msg="Did not return None for an invalid ID")

	def test_goal_edit(self):
		with goalTest.app.app_context():
			g1, g1_msg = Goal.get_by_id(1)
			# 1 valid update
			u, msg = g1.edit(title="SANDWICHES!!!")
			self.assertEqual(g1.title, "SANDWICHES!!!", msg="Did not update this field.")
			# 2 valid updates
			u, msg = g1.edit(title="sandwiches??", target_milliscore=999)
			self.assertEqual(g1.title, "sandwiches??", msg="Did not update this field.")
			self.assertEqual(g1.target_milliscore, 999, msg="Did not update this field.")
			# No updates
			u, msg = g1.edit()
			self.assertEqual(msg, "Goal edited successfully.", msg="Did not handle an empty update operation.")
			# valid and invalid updates
			u, msg = g1.edit(title="nope", target_milliscore="a")
			self.assertIsNone(u, msg="Did not return None when there was an invalid field.")
			self.assertNotEqual(g1.title, "nope", msg="Updated a field with a valid value, when there was an invalid value in the same transaction.")
			self.assertEqual(g1.target_milliscore, 999, msg="Updated a field with an invalid value.")

	def test_goal_increment_score(self):
		with goalTest.app.app_context():
			goal, msg = Goal.get_by_id(1)
			goal.increment_milliscore(333)
			self.assertEqual(goal.current_milliscore, 333, msg="Milliscore not increased")
			goal.increment_milliscore(333)
			self.assertEqual(goal.current_milliscore, 666, msg="Milliscore not increased")
			goal.increment_milliscore(333)
			self.assertEqual(goal.current_milliscore, 1000, msg="Milliscore not increased or rounding incorrect")

			goal4, msg = Goal.get_by_id(4)
			goal4.increment_milliscore(333)
			self.assertEqual(goal4.current_milliscore, 667, msg="Milliscore not decreased")
			goal4.increment_milliscore(333)
			self.assertEqual(goal4.current_milliscore, 334, msg="Milliscore not decreased")
			goal4.increment_milliscore(333)
			self.assertEqual(goal4.current_milliscore, 0, msg="Milliscore not decreased or rounding incorrect")

	def test_goal_delete(self):
		with goalTest.app.app_context():
			# valid delete
			g1, response = Goal.get_by_id(1)
			g1_id, response = g1.delete()
			self.assertEqual(g1_id, 1, msg="Deleted wrong goal or returned wrong value")

			# attempt to modify/delete deleted item
			g1_id, response = g1.delete()
			self.assertIsNone(g1_id, msg="Returned wrong value when deleting a deleted goal")
			self.assertEqual(response, "Goal already deleted.")
			g1, response = g1.edit(title="So much sandwich")
			self.assertIsNone(g1, msg="Returned wrong value when editing a deleted goal")
			self.assertEqual(response, "Goal previously deleted.")

	def test_goal_reactivate(self):
		with goalTest.app.app_context():
			g1, response = Goal.get_by_id(1)
			g1_id, response = g1.delete()
			self.assertEqual(g1_id, 1)

			g1, response = Goal.reactivate(1)
			self.assertFalse(g1.deleted, msg="Deleted attribute still set to false")

			g3, response = Goal.reactivate(3)
			self.assertFalse(g3.deleted, msg="Reactivating active goal deactivates it")

			g7, response = Goal.reactivate(7)
			self.assertIsNone(g7, msg="Wrong response to reactivating nonexistant goal")

			gA, gA_msg = Goal.reactivate('A')
			self.assertIsNone(gA, msg="Wrtong response to reactivating invalid id")

	def test_goal_validate(self):
		with goalTest.app.app_context():
			g = Goal(1, "test", 1000)
			valid, messages = g.validate()
			self.assertTrue(valid, msg="Incorrectly marked as invalid")

			g.user_id = 'a'
			valid, messages = g.validate()
			self.assertFalse(valid, msg="Incorrectly marked as invalid [char user_id]")

			g.current_milliscore = 'a'
			valid, messages = g.validate()
			self.assertFalse(valid, msg="Incorrectly marked as invalid [char current_milliscore]")

			g.target_milliscore = 'a'
			valid, messages = g.validate()
			self.assertFalse(valid, msg="Incorrectly marked as invalid [char target_milliscore]")