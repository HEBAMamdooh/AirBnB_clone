#!/usr/bin/python3
"""
Command interpreter module
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exits the program with EOF"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Handles empty lines"""
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(args[0])()
                new_instance.save()
                print(new_instance.id)
            except Exception as e:
                print(f"** {e.__class__.__name__}: {str(e)} **")

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                obj_key = args[0] + "." + args[1]
                obj = storage.all().get(obj_key)
                if obj is not None:
                    print(obj)
                else:
                    print(f"** no instance found **")
            except Exception as e:
                print(f"** {e.__class__.__name__}: {str(e)} **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                obj_key = args[0] + "." + args[1]
                obj = storage.all().get(obj_key)
                if obj is not None:
                    del storage.all()[obj_key]
                    storage.save()
                else:
                    print(f"** no instance found **")
            except Exception as e:
                print(f"** {e.__class__.__name__}: {str(e)} **")

    def do_all(self, line):
        """Prints all string representations of all instances"""
        args = line.split()
        obj_list = []
        if len(args) == 0:
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
        elif args[0] not in globals():
            print("** class doesn't exist **")
        else:
            for key, obj in storage.all().items():
                if args[0] in key:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            try:
                obj_key = args[0] + "." + args[1]
                obj = storage.all().get(obj_key)
                if obj is not None:
                    attr_name = args[2]
                    attr_value = args[3]
                    setattr(obj, attr_name, attr_value)
                    storage.save()
                else:
                    print(f"** no instance found **")
            except Exception as e:
                print(f"** {e.__class__.__name__}: {str(e)} **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
