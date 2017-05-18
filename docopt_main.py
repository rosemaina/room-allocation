"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage: Dojo
    Dojo create_room <room_type> <room_name>... 
    Dojo add_person <last_name> <first_name> <person_type> [<wants_accomodation>]
    Dojo return_non_full_room <room_list> <max_space>
    Dojo (-i| --interactive)
    Dojo (-h| --help)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
# The above usage string shows that docoppt will read and be used
#to determine whether or not the user has passed valid arguements.

import sys
import cmd
# This shows that you are importing the docopt function from the docopt module
# Docopt is library  for parsing command line arguments
from docopt import docopt, DocoptExit
from dojo import Dojo


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to my Interactive Program!' \
        + ' (Type help for a list of commands.)'
    prompt = '(Dojo)'

    dojo = Dojo()
 

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>... """
        room_type = arg["<room_type>"]
        room_name = arg["<room_name>"]

        for room in room_name:
            print(self.dojo.create_room(room_type, room))

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage:  add_person <last_name> <first_name> <person_type> [<wants_accomodation>]
        """
        
        last_name = arg["<last_name>"]
        first_name = arg["<first_name>"]
        person_type = arg["<person_type>"]


        if arg["<wants_accomodation>"] is None:
            wants_accomodation = "N"
        else:
            wants_accomodation = arg["<wants_accomodation>"]

        print (self.dojo.add_person(last_name, first_name, person_type, wants_accomodation))
        print(self.dojo.return_non_full_room(person))
        # print(type(wants_accomodation))
      #   print(arg)

    # @docopt_cmd
    # def return_non_full_room(person):
        
    #     pass

    # @docopt_cmd
    # def do_allocate_room(self, arg):
    #     """Usage:  allocate_room 
    #     """
    #     person = arg["<person>"]

    #     self.dojo.allocate_room(person)
    #     # print(arg)



    def do_quit(self, arg):
        """This quits out of Interactive Mode."""

        print('GOOD BYE!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
