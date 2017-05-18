class Person(object):
	
	def __init__(self, last_name, first_name, person_type, wants_accomodation='N'):
		self.last_name = last_name
		self.first_name = first_name
		self.person_type = person_type
		self.wants_accomodation = wants_accomodation

	#this function return the perso's full name
	def get_full_name(self):
		
		full_name = self.last_name + " " + self.first_name
		return full_name


	@abstractmethod 
	def istype(self):
		pass





#state = Person('Maina', 'Rose', 'F','fellow', 'Y')
#print (state.get_full_name())


class Fellow(Person):

	def __init__(self, last_name, first_name, gender,):
		super(Fellow, self).__init__(last_name, first_name, gender, person_type='fellow', wants_accomodation='N')

	def istype(self):
		return "fellow"



class Staff(Person):
	def __init__(self, last_name, first_name , person_type='staff', wants_accomodation='N'):
		super(Staff, self).__init__(last_name, first_name, person_type, wants_accomodation)

	def istype(self):
		return "staff"
	

	
	