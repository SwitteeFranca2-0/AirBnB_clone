#!/usr/bin/python3
#This is the entry pont of the command

import cmd
from models.base_model import BaseModel
import models
import json
import shlex

class HBNBCommand(cmd.Cmd):
    """This class defines all functons of commands"""

    prompt = '(hbnb) '
    ruler = "="
    doc_header = "Documented commands (type help <topic>)"

    def parse_input(self, line: str):
        """Overrides the parseline command"""
        #if '""' in line:
            #inp = shlex.split(line)
            #return inp
        inp = line.split(" ")
        return inp
    def do_quit(self, line):
        """Quit command to exit the program\n"""
        exit();
    
    def do_EOF(self, line):
        """eof command to exit the program\n"""
        exit();
    
    def emptyline(self):
        """This overides the emptyline command"""
        pass;
    
    def do_create(self, line):
        """Usage: create <class name>"""
        if line is None:
            print("** class name missing **")
            return;
        if line != "BaseModel":
            print("** class name doesn't exist **")
            return
        obj = BaseModel()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Usage: show <class name> <obj id> """
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = self.parse_input(arg)
        if args[0] != "BaseModel":
            print("** class doesn't exist ** ")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return;
        id_no = args[1]
        objs = models.storage.all()
        if any(obj.id == id_no for obj in objs.values()):
            print (objs["BaseModel.{}".format(id_no)])
        else:
            print("** no instance id found **")
        
    def do_destroy(self, arg):
        """Usage: destroy <class name> <object id>"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = self.parse_input(arg)
        if args[0] != "BaseModel":
            print("** class doesn't exist ** ")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return;
        id_no = args[1]
        objs = models.storage.all()
        if any(obj.id == id_no for obj in objs.values()):
            del objs["BaseModel.{}".format(id_no)]
            models.storage.save()
        else:
            print("** no instance id found **")
        
    def do_all(self, arg):
        """Usage: all <class name> or all"""
        args = self.parse_input(arg)
        if args[0] and args[0] != "BaseModel":
            print("** class doesn't exist ** ")
            return
        print([str(obj) for obj in models.storage.all().values()])
    
    def do_update(self, arg):
        """Usage: update <class name> <id> <attribute name> '<attribute value>'"""
        args = self.parse_input(arg)
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = self.parse_input(arg)
        if args[0] != "BaseModel":
            print("** class doesn't exist ** ")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return;
        else:
            objs = models.storage.all()
            id_no = arg[1]
            if any(obj.id == id_no for obj in objs.values()):
                print("** no instance id found **")
                return;
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj = objs["BaseModel.{}".format(id_no)]
        obj.arg[2] = arg[3]
        models.storage.save()
        
        

    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
