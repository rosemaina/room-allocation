import unittest
import sys 
from os import path 
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from room import Room

class TestRoom(unittest.TestCase):
	def setUp(self):
		self.room_instance = Room('blue', 'office', 6)


	def test_get_room_capacity(self):
		office_size = self.room_instance.get_room_capacity()
		self.assertEqual(office_size, 'Capacity is 6')
		

	def test_add_room_occupant(self):
		occupant = self.room_instance.add_room_occupant('fellow', 'Maina', 'Rose')
		self.assertEqual(len(self.room_instance.room_occupants), 1)



if __name__ == '__main__':
	unittest.main()


