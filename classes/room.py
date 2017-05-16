class Room(object):


	def __init__(self, room_name, room_type, room_capacity):
		self.room_name = room_name
		self.room_type = room_type
		self.room_capacity = room_capacity
		self.room_occupants = []


	def room_capacity(self, room_type):
		capacity = self.room_capacity
		print (capacity, " ")


	def add_room_occupant(self, room_type, room_name):
		occupant =self.room_type + "" + self.room_name
		print (occupant, 'office', 'blue')