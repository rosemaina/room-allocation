import unittest

class TestRoom(unittest.TestCase):
	def setUp(self):
		self.room_instance = Room()


	def test_get_room_capacity(self):
		space = Room()
		size = space.get_room_capacity('office')
		self.assertEqual(size, 6)
		size = space.get_room_capacity('living')
		self.assertEqual(size, 4)

	def test_add_room_occupant(self):
		occupant = self.room_instance.add_room_occupant('Rose', 1)

















def reallocate_person(self):

		pass
		self.person = []
		

		

		
		
	


unittest.main()






