import unittest
from person import Person 


class TestPerson(unittest.TestCase):	

	def test_name_sequence(self):
		state = Person('Maina', 'Rose', 'F','fellow', 'Y')
		self.assertEqual(state.get_full_name(), 'Maina Rose')



unittest.main()
