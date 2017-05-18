from person import Staff
from room import Room, Office

class Dojo(object):
	

	def __init__(self):  
		self.fellows_list = []
		self.staff_list = []
		self.office_list = []
		self.living_space_list = []
		self.all_rooms = []
		self.all_persons = []



	def add_person(self, last_name, first_name, person_type, wants_accomodation='N'):
		if type(last_name) != str or type(first_name) != str or type(person_type) != str or not isinstance(wants_accomodation, str):
			raise ValueError("input should be a string")

		else :
			last_name = last_name.lower()
			first_name = first_name.lower()
			person_type = person_type.lower()


		if person_type == "fellow" :
			person = Fellow(last_name, first_name, person_type)
			self.fellows_list.append(person)

			return ('A person called %s has been added') %(last_name+" " + first_name)
		
		elif person_type =="staff" :
			staff = Staff(last_name, first_name)
			self.staff_list.append(staff)

			return ('A person called %s has been created.') %(last_name+" "+first_name)
		




	def create_room(self, room_type, room_name):
		if type(room_name) != str or type(room_type) != str:
			raise ValueError ("input should be strings")

		else: 
			room_name = room_name.lower()
			room_type = room_type.lower()


		if room_type == "office" :
			office = Office(room_name)
			self.office_list.append(office)

			return ('An office called %s has been created.') %(room_name)
		
		elif room_type =="living_space" :
			space = LivingSpace(room_name)
			self.living_space_list.append(space)

			return ('A living space called %s has been created.') %(room_name)
		



