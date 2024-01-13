#!/usr/bin/python3
"""
Command interpreter module.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models import storage
from shlex import split
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Do nothing on empty input line.
        """
        pass

    def do_quit(self, arg):
        """ 
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, saves it to JSON file, and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on class name and id.
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        all_objs = storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and id (save the change into the JSON file).
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        all_objs = storage.all()
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representations of all instances based or not on the class name.
        """
        all_objs = storage.all()
        if not arg:
            print([str(all_objs[obj]) for obj in all_objs])
        else:
            args = arg.split()
            if args[0] not in globals():
                print("** class doesn't exist **")
            else:
                print([str(all_objs[obj])
                      for obj in all_objs if args[0] in obj])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        setattr(all_objs[key], args[2], eval(args[3]))
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
