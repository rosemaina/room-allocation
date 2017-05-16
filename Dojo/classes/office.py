from dojoRoom import Room
class Office(Room):

	def __init__(self,room_name, room_type='office', room_capacity=6):
		super(Office, self).__init__(room_name, room_type, room_capacity)
