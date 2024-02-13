#!/usr/bin/python3
"""defines the HBnB console"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """defines the HBnB command line interpreter"""
    prompt = "(hbnb)"
    accepted_classes = ["BaseModel", "User"]

    def do_quit(self, arg):
        """for exiting the program"""
        return True

    def help_quit(self, arg):
        """displays how to end the program"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """EOF signal to end the program"""
        print()
        return True

    def emptyline(self):
        """do nothing when an emptyline is entered"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.accepted_classes:
            print("** class doesn't exist **")
        else:
            new_inst = eval(f"{commands[0]}()")
            storage.save()
            print(new_inst.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.accepted_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.accepted_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name
        """
        objects = storage.all()
        commands = shlex.split(arg)
        if len(commands) == 0:
            for k, v in objects.items():
                print(str(v))
        elif commands[0] not in self.accepted_classes:
            print("** class doesn't exist **")
        else:
            for k, v in objects.items():
                if k.split('.')[0] == commands[0]:
                    print(str(v))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.accepted_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                objt = objects[key]
                attr_name = commands[2]
                attr_value = commands[3]
                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(objt, attr_name, attr_value)
                objt.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
