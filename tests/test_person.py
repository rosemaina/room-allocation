import unittest
import sys 
from os import path 
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from person import Person 


class TestPerson(unittest.TestCase):	


	def test_name_sequence(self):
		state = Person('Maina', 'Rose', 'F','fellow', 'Y')
		self.assertEqual(state.get_full_name(), 'Maina Rose', 
			msg='persons full name does not match')

if __name__ == '__main__':
	unittest.main()
