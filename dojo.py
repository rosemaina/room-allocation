#import sys 
#from os import path 
#sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from person import Staff, Fellow
from room import  Office, LivingSpace
import random

class Dojo(object):
	

	def __init__(self):  
		self.fellows_list = []
		self.staff_list = []
		self.office_list = []
		self.living_space_list = []
		self.all_rooms = []
		self.all_persons = []



	def add_person(self, last_name, first_name, person_type, wants_accomodation='N'):

		
		last_name = last_name.lower()
		first_name = first_name.lower()
		person_type = person_type.lower()


		if person_type == "fellow" :
			person = Fellow(last_name, first_name, person_type)
			self.fellows_list.append(person)
			self.allocate_room(person, "y")

			return ('A person called %s has been added') %(last_name+" " + first_name)
		
		elif person_type =="staff" :
			person = Staff(last_name, first_name)
			self.staff_list.append(person)
			self.allocate_room(person)

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
			self.all_rooms.append(office)

			return ('An office called %s has been created.') %(room_name)
		
		elif room_type =="living_space" :
			space = LivingSpace(room_name)
			self.living_space_list.append(space)
			self.all_rooms.append(space)

			return ('A living space called %s has been created.') %(room_name)

	def return_non_full_room(self, room_list, max_space):
		non_full_list = []

		for room in room_list:
			if len(room.occupants) < max_space:
				non_full_list.append(room)
		return non_full_list


	def allocate_room(self, person, accommodate = 'N'):
		#this checks whether an office or a living space exixts and is actually in the all_rooms list.
		
			# if room_name not in self.all_rooms:
			# 	return "Room does not exist!"

			try:
				ran_office = random.choice(self.return_non_full_room(self.office_list, 6))
				ran_living_space = random.choice(self.return_non_full_room(self.living_space_list, 4))
			except IndexError:
				return "No room created or room is full"
			if person.istype() == "fellow" and accommodate == 'y':
				ran_office.occupants.append(person)
				ran_living_space.occupants.append(person)
				print(person.name, "person has been assigned an office and living space", ran_office, ran_living_space)
			else:
				ran_office.occupants.append(person)
				print(person.name, "person has been assigned an office", ran_office)

			# room = ran_room
			# #this adds a room to living space list if the type defined is an office
			# if room.room_type == 'office'and room.room_occupants == 6:
			# 		return 'Room is full'
			# elif room.room_type == 'office' and room.room_occupants < 6:
			# 	room.room_occupants.append(person)
			# 	for room_occupants in room:
			# 		room_occupants += 1
			

			# # this adds a room to living space list if type defined is a livingspace
			# if room.room_type == 'living_space' and room.room_occupants == 4:
			# 	return 'Room is full'

			# elif room.room_type == 'living_space' and room.room_occupants < 4:
			# 	room.room_occupants.append(person)
			# 	for room_occupants in room:
			# 		room_occupants += 1


	def print_allocations(self,*args):
		print ("Room Allocation Data:")
		print ('**********************')
		print (" ID ----- Person Name")
		print 
		for room in self.all_rooms:

			if room in self.office_list and self.living_space_list:
				print('---------- office occupants ----------')(room)
			else:
				print('-----------living space occupants-------------')(room)

	# def check(self):
	# 	pass





		



