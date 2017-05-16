import unittest

from dojo import Dojo

class TestDojo(unittest.TestCase):

	def setUp(self):
		self.dojo_instance = Dojo()



	def test_add_person(self):
		new_person = self.dojo_instance.add_person('Maina', 'Rose', 'Staff')
		self.assertEqual(len (self.dojo_instance.staff_list), 1)

	def test_if_name_is_a_string(self):		
		with self.assertRaises(ValueError, msg='input should be a string'):
			self.dojo_instance.add_person("Maina", "Rose", "Staff", 89)

	def test_add_person(self):
		new_person = self.dojo_instance.add_person('Maina', 'Rose', 'Staff', 'wants_accomodation')
		self.assertEqual(len (self.dojo_instance.staff_list), 1)


	def test_add_person_returns_confirmation(self):
		result = self.dojo_instance.add_person( "Maina", "Rose","female", "Staff")
		self.assertEqual(result, "")




unittest.main()