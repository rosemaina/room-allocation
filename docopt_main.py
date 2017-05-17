#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    create_room <room_type> <room_name>... 
    add_person <last_name> <first_name> <gender> <person_type> <wants accomodation>

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
        + ' (type help for a list of commands.)'
    prompt = '(my_program) '
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>... """
        room_type = arg["<room_type>"]
        rooms = arg["<room_name>"]

        print(arg)

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage:  add_person <last_name> <first_name> <gender>  <person_type> <wants accomodation>
        """
        
        last_name = arg["<last_name>"]
        first_name = arg["<first_name>"]
        person_type = arg["<person_type"]


        if arg["--wants_accomodation"] is None:
            wants_accomodation = "N"
        else:
            wants_accomodation = arg["--wants_accomodation"]
      
      # print(type(wants_accomodation))
        print(arg)

     @docopt_cmd
    def do_a(self, arg):
        """Usage: """

    def do_quit(self, arg):
        """This quits out of Interactive Mode."""

        print('GOOD BYE!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
