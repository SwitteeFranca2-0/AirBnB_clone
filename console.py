#!/usr/bin/python3
# This is the entry pont of the command

import cmd
from models.base_model import BaseModel
from models.review import Review
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.city import City
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """This class defines all functons of commands"""

    prompt = '(hbnb) '
    ruler = "="
    doc_header = "Documented commands (type help <topic>)"
    __classes = {
        "BaseModel": BaseModel(),
        "User": User(),
        "Place": Place(),
        "State": State(),
        "City": City(),
        "Amenity": Amenity(),
        "Review": Review()
    }

    def parse_input(self, line: str):
        """Parses the command line arguments"""
        if '"' in line:
            inp = shlex.split(line)
            inp = [o.strip('"') for o in inp]
            return inp
        inp = line.split(" ")
        return inp

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """eof command to exit the program\n"""
        return True

    def emptyline(self):
        """This overides the emptyline command"""
        pass

    def default(self, line):
        """This overrides the default command"""
        cmds = {"all()": self.do_all,
                "count()": self.count
                }
        c2 = {"show": self.do_show,
              "destroy": self.do_destroy,
              "update": self.do_update
              }
        ar = line.split(".")
        if "." not in line:
            print("** Unknown syntax: {} **".format(line))
            return
        if ar[1] not in cmds.keys() and ar[1].split("(")[0] not in c2.keys():
            print("** Unknown syntax: {} **".format(line))
            return
        if ar[1] in cmds:
            cmds[ar[1]]("{}".format(ar[0]))
        else:
            if "update" not in ar[1]:
                id = ar[1].split('(')[1].split(')')[0]
                c2[ar[1].split("(")[0]]("{} {}".format(ar[0], id))
            else:
                if "{" not in ar[1]:
                    id = ar[1].split("(")[1].split(",")[0]
                    atr = ar[1].split("(")[1].split(",")[1]
                    al = ar[1].split("(")[1].split(",")[2].split(")")[0]
                    cmd = ar[1].split("(")[0]
                    c2[cmd]('{} {} {} "{}" '.format(ar[0], id, atr, al))
                else:
                    id = ar[1].split("(")[1].split("{")[0].strip(", ")
                    at_d = '{' + ar[1].split("(")[1].split("{")[1].strip(")")
                    cmd = ar[1].split("(")[0]
                    c2[cmd]('{}.{} {}'.format(ar[0], id, at_d))

    def count(self, line):
        ar = self.parse_input(line)
        print(len([obj for obj in models.storage.all().values()
              if obj.__class__.__name__ == ar[0]]))

    def do_create(self, line):
        """Usage: create <class name>"""
        if line is None:
            print("** class name missing **")
            return
        if line not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
            return
        obj = HBNBCommand.__classes[line]
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Usage: show <class name> <obj id> """
        if len(arg) == 0:
            print("** class name missing **")
            return
        ar = self.parse_input(arg)
        if ar[0] not in HBNBCommand.__classes:
            print("** class doesn't exist ** ")
            return
        if len(ar) == 1:
            print("** instance id missing **")
            return
        id_no = ar[1]
        objs = models.storage.all()
        if any(obj.id == id_no for obj in objs.values()):
            print(objs["{}.{}".format(ar[0], id_no)])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Usage: destroy <class name> <object id>"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        ar = self.parse_input(arg)
        if ar[0] not in HBNBCommand.__classes:
            print("** class doesn't exist ** ")
            return
        if len(ar) == 1:
            print("** instance id missing **")
            return
        id_no = ar[1]
        objs = models.storage.all()
        if any(obj.id == id_no for obj in objs.values()):
            del objs["{}.{}".format(ar[0], id_no)]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Usage: all <class name> or all"""
        ar = self.parse_input(arg)
        if ar[0] and ar[0] not in HBNBCommand.__classes:
            print("** class doesn't exist ** ")
            return
        dict = models.storage.all().values()
        if ar[0]:
            print([str(obj) for obj in dict if
                  obj.__class__.__name__ == ar[0]])
        else:
            print([str(obj) for obj in dict])

    def do_update(self, arg):
        """Usage: update <class name> <id> <attribute name>
            '<attribute value>'"""
        if "{" in arg:
            ar = arg.split(".")
            cls = ar[0]
            id_no = ar[1].split("{")[0].strip(" ")
            at_d = ar[1].split("{")[-1].strip("}")
            at_d = at_d.split(",")
            b = {o.split(":")[0].strip(" '").strip(' "'):
                 o.split(":")[1].strip(" '").strip(' "') for o in at_d}
            objs = models.storage.all()
            if not any(obj.id == id_no for obj in objs.values()
                       if obj.__class__.__name__ == cls):
                print("** no instance found **")
            else:
                obj = objs["{}.{}".format(ar[0], id_no)]
                [setattr(obj, k, v) for k, v in b.items()]
            models.storage.save()
            return
        ar = self.parse_input(arg)
        if len(ar) == 0:
            print("** class name missing **")
            return
        ar = self.parse_input(arg)
        if ar[0] not in HBNBCommand.__classes:
            print("** class doesn't exist ** ")
            return
        if len(ar) == 1:
            print("** instance id missing **")
            return
        else:
            objs = models.storage.all()
            id_no = ar[1]
            if not any(obj.id == id_no for obj in objs.values()
                       if obj.__class__.__name__ == ar[0]):
                print("** no instance found **")
                return
        if len(ar) == 2:
            print("** attribute name missing **")
            return
        if len(ar) == 3:
            print("** value missing **")
            return
        obj = objs["{}.{}".format(ar[0], id_no)]
        if ar[2] not in obj.__class__.__dict__.keys():
            obj.__dict__[ar[2]] = ar[3]
        else:
            ar[3] = type(obj.__class__.__dict__[ar[2]])(ar[3])
            obj.__dict__[ar[2]] = ar[3]
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
