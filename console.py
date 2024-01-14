#!/usr/bin/python3
"""Module for HBNB command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the program with Ctrl+D"""
        return True

    def do_quit(self, line):
        """Quit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, args):
        """Create a new instance of BaseModel"""
        if not args:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(args)()
                new_instance.save()
                print(new_instance.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, args):
        """Show string representation of an instance"""
        if not args:
            print("** class name missing **")
        else:
            args_list = args.split()
            if len(args_list) == 0:
                print("** class name missing **")
            elif len(args_list) == 1:
                print("** instance id missing **")
            else:
                try:
                    instance = storage.all()[args_list[0] + "." + args_list[1]]
                    print(instance)
                except KeyError:
                    print("** no instance found **")

    def do_destroy(self, args):
        """Delete an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            args_list = args.split()
            if len(args_list) == 0:
                print("** class name missing **")
            elif len(args_list) == 1:
                print("** instance id missing **")
            else:
                try:
                    del storage.all()[args_list[0] + "." + args_list[1]]
                    storage.save()
                except KeyError:
                    print("** no instance found **")

    def do_all(self, args):
        """Print all string representation of all instances"""
        objects = storage.all()
        if args:
            try:
                args_list = args.split()
                objects = [v for k, v in objects.items() if args_list[0]
                           == k.split(".")[0]]
            except:
                print("** class doesn't exist **")
                return
        print(objects)

    def do_update(self, args):
        """Update an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            args_list = args.split()
            if len(args_list) == 0:
                print("** class name missing **")
            elif len(args_list) == 1:
                print("** instance id missing **")
            else:
                key = args_list[0] + "." + args_list[1]
                try:
                    obj = storage.all()[key]
                except KeyError:
                    print("** no instance found **")
                    return

                if len(args_list) == 2:
                    print("** attribute name missing **")
                elif len(args_list) == 3:
                    print("** value missing **")
                else:
                    setattr(obj, args_list[2], eval(args_list[3]))
                    storage.save()

    def do_count(self, args):
        """Count the number of instances of a class"""
        count = sum(1 for obj in storage.all().values()
                    if args == obj.__class__.__name__)
        print(count)

    def default(self, line):
        """Called on an input line when the command prefix is not recognized"""
        class_name = line.split(".")[0]
        if class_name in dir(eval(class_name)):
            command = line.split(".")[1].split("(")[0]
            if command == "all()":
                self.do_all(class_name)
            elif command == "count()":
                self.do_count(class_name)
            elif command == "show(" and line.endswith(")"):
                try:
                    instance_id = line.split("(")[1].split(")")[0]
                    instance_key = "{}.{}".format(class_name, instance_id)
                    instance = storage.all().get(instance_key)
                    if instance:
                        print(instance)
                    else:
                        print("** no instance found **")
                except IndexError:
                    print("** instance id missing **")
            elif command == "destroy(" and line.endswith(")"):
                try:
                    instance_id = line.split("(")[1].split(")")[0]
                    instance_key = "{}.{}".format(class_name, instance_id)
                    del storage.all()[instance_key]
                    storage.save()
                except KeyError:
                    print("** no instance found **")
                except IndexError:
                    print("** instance id missing **")
            else:
                print("** Unknown syntax: {}".format(line))
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
