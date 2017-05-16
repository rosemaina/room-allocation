from dojoPerson import Person
class Fellow(Person):


    def __init__(self, last_name, first_name, gender, person_type='fellow', wants_accomodation='N'):
        super(Fellow, self).__init__(last_name, first_name,gender, person_type, wants_accomodation)