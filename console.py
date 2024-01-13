#!/usr/bin/python3
"""
Module for the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Empty line doesn't do anything
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it, and prints the id
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                cls_name = args[0]
                obj_id = args[1]
                key = "{}.{}".format(cls_name, obj_id)
                obj = storage.all().get(key)
                if not obj:
                    print("** no instance found **")
                else:
                    print(obj)
            except Exception:
                print(
                    "** class doesn't exist **" if args[0] not in globals() else "** instance id missing **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                cls_name = args[0]
                obj_id = args[1]
                key = "{}.{}".format(cls_name, obj_id)
                obj = storage.all().get(key)
                if not obj:
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()
            except Exception:
                print(
                    "** class doesn't exist **" if args[0] not in globals() else "** instance id missing **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name
        """
        args = arg.split()
        objs = []
        if not args:
            objs = [str(obj) for obj in storage.all().values()]
        else:
            try:
                cls_name = args[0]
                if cls_name not in globals():
                    print("** class doesn't exist **")
                    return
                objs = [str(obj) for key, obj in storage.all().items()
                        if key.startswith(cls_name)]
            except Exception:
                print("** class doesn't exist **")
        print(objs)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                cls_name = args[0]
                obj_id = args[1]
                key = "{}.{}".format(cls_name, obj_id)
                obj = storage.all().get(key)
                if not obj:
                    print("** no instance found **")
                else:
                    if len(args) < 3:
                        print("** attribute name missing **")
                    elif len(args) < 4:
                        print("** value missing **")
                    else:
                        attr_name = args[2]
                        value = args[3]
                        try:
                            value = eval(value)
                        except:
                            pass
                        setattr(obj, attr_name, value)
                        obj.save()
            except Exception:
                print(
                    "** class doesn't exist **" if args[0] not in globals() else "** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
