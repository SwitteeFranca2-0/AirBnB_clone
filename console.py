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
    
    def do_create(self, obj=None):
        """This creates a new instance of BaseModel"""
        if obj is None:
            print("** class name missing **")
            return;
        if obj != "BaseModel":
            print("** class name doesn't exist **")
            return
        obj = BaseModel()
        obj.save()
        print(obj.id)

    def do_show(self, className=None, id=None):
        """This displays information about a """
        if className is None:
            print("** class name missing **")
            return
        if className != "BaseModel":
            print("** class name doesn't exist ** ")
            return
        if id is None:
            print("** instance id missing **")
        ###not done
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
