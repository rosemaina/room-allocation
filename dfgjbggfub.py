"""
Dojo rom assignment
	Usage: 
        create_room <room_type> <room_name>... 
        add_person <last_name> <first_name>  <job_type> <wants accomodation>

"""
        
from docopt import docopt

@docopt_cmd
def do_create_room(self, arg):
	"""Usage: create_room <room_name>..."""
	room = Room()
	rooms = arg['<room_name>']
	for Rm in rooms:
		#can i use print or Dojo.create_room(room_name(Rm))
		print = room.create_room(Rm)


@docopt_cmd
def do_create_roomType(self, arg):
	"""Usage: create_room <room_type>..."""
	room = Room()
	room_name = arg['<room_name>']
	room_type = arg['<room_type>']
	ROOM = room.create_roomType(room_name, room_type)
	print(ROOM)

@docopt_cmd
def do_add_person(self, arg):
	"""Usage: add_person <last_name> <first_name> <fellow|staff > [wants_accomodation]"""
	person = Person()
	last_name = arg['<last_name>']
	first_name = arg['<first_name>']
	person_type = arg['<person_type>']

	if arg["--wants_accomodation"] is None:
		wants_accomodation = "None"
	else:
		wants_accomodation = arg["--wants_accomodation"]

		# print(type(wants_accomodation))
		#person.add_person(last_name, first_name, person_type, accomodation, wants_accomodation)
		person.add_person( last_name=last_name,
			             first_name=first_name,
						 person_type=person_type,
						 accomodation=accomodation,
						 wants_accomodation=wants_accomodation
						  )
		
