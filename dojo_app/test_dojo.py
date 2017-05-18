import unittest

from dojo import Dojo 
from person import Person 
from room import Room, Office 

class TestDojo(unittest.TestCase):

	def setUp(self):
		self.dojo_instance = Dojo()


	def test_add_person(self):
		self.dojo_instance.add_person("Maina", "Rose", "staff")
		self.assertEqual(len (self.dojo_instance.staff_list), 1)


	def test_if_name_is_a_string(self):		  
		with self.assertRaises(ValueError, msg="input should be a string"):
			self.dojo_instance.add_person("Maina", 9, "Staff")


	def test_create_room(self):
		self.dojo_instance.create_room( 'office', 'Aberdare')
		self.assertEqual(len (self.dojo_instance.office_list), 1)


	def test_add_person_returns_confirmation(self):
		result = self.dojo_instance.add_person( "Maina", "Rose", "Staff", "N")
		self.assertEqual(result, "A person called maina rose has been created.")


unittest.main()