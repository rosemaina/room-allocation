import unittest
from room import Room

class TestRoom(unittest.TestCase):
	def setUp(self):
		self.room_instance = Room('blue', 'office', 6)


	def test_get_room_capacity(self):
		office_size = self.room_instance.get_room_capacity()
		self.assertEqual(office_size, 'Capacity is 6')
		

unittest.main()
