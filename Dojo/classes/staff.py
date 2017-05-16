from dojoPerson import Person 
class Staff(Person):

	def __init__(self, last_name, first_name , person_type='staff', wants_accomodation='N'):
		super(Staff, self).__init__(last_name, first_name, person_type, wants_accomodation)