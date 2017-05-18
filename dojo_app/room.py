class Room(object):


	def __init__(self, room_name, room_type, room_capacity):
		self.room_name = room_name
		self.room_type = room_type
		self.room_capacity = room_capacity   
		self.occupants = []


	def get_room_capacity(self):

		return ("Capacity is " + str(self.room_capacity))


	# def add_room_occupant(self, person_type, last_name, first_name):
	# 	self.room_occupants.append([person_type, last_name, first_name])
	# 	print(person_type +" " + last_name + " " + first_name + " has been allocated " + self.room_type + " " + self.room_name)
		

class LivingSpace(Room):
	def __init__(self,room_name, room_type, room_capacity):
		super(LivingSpace, self).__init__(room_name, room_type='living_space', room_capacity=4)

class Office(Room):
	def __init__(self,room_name, room_type, room_capacity):
		super(Office, self).__init__(room_name, room_type='office', room_capacity=4)

