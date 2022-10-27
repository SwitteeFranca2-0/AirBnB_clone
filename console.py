#!/usr/bin/python3
#This is the entry pont of the command

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """This class defines all functons of commands"""

    prompt = '(hbnb) '
    ruler = "="
    doc_header = "Documented commands (type help <topic>)"

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        exit();
    
    def do_EOF(self, line):
        """eof command to exit the program\n"""
        exit();
    
    def emptyline(self):
        """This overides the emptyline command"""
        pass;
    
    def create(self, line):
        """This creates a new instance of BaseModel"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
