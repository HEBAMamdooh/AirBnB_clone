#!/usr/bin/python3
"""Command interpreter module"""
import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage

classes = {
    'BaseModel': BaseModel,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review,
    'User': User
}


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line handling"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to JSON, and prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in FileStorage._FileStorage__objects:
                print(FileStorage._FileStorage__objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id, and saves the changes to JSON"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in FileStorage._FileStorage__objects:
                del FileStorage._FileStorage__objects[key]
                FileStorage.save(FileStorage)
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances based on the class name"""
        args = arg.split()
        objects_list = []
        if not args:
            for key, value in FileStorage._FileStorage__objects.items():
                objects_list.append(str(value))
            print(objects_list)
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            for key, value in FileStorage._FileStorage__objects.items():
                if key.startswith(args[0]):
                    objects_list.append(str(value))
            print(objects_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id and saves the changes to JSON"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            key = "{}.{}".format(args[0], args[1])
            if key not in FileStorage._FileStorage__objects:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in FileStorage._FileStorage__objects:
                print("** no instance found **")
            else:
                obj = FileStorage._FileStorage__objects[key]
                setattr(obj, args[2], args[3])
                FileStorage.save(FileStorage)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
