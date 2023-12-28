#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
"""
This module hosts class HBNBCommand
"""


class HBNBCommand(cmd.Cmd):
    """
    entry point of the command interpreter
    inherits from Cmd class
    """
    prompt = '(hbnb)'
    __classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }
    operations = ['all', 'count', 'show', 'destroy', 'update']

    def precmd(self, line):
        """
        Hook method executed just before the command line line is
        interpreted, but after the input prompt is generated and issued.
        """
        impurities = ['.', '(', ')']
        for impurity in impurities:
            if impurity in line:
                line_list = line.split(impurity)
                line = ' '.join(line_list)
        line_list = line.split()
        if line_list[0] in HBNBCommand.__classes:
            if line_list[1] in HBNBCommand.operations:
                buffer = line_list[0]
                line_list[0] = line_list[1]
                line_list[1] = buffer
        line = ' '.join(line_list)
        return line

    def do_count(self, arg):
        """
        retrieves the number of instances of a class
        Arguments:
            arg: consists of the class name to count the instances
        """
        arglist = parse(arg)
        if len(arglist) == 0:
            print("** class name missing **")
        else:
            count = 0
            cls = self.verify_class(arglist[0])
            for obj in storage.all().values():
                if type(obj) == cls:
                    count += 1
            print(count)

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        Arguments:
            arg: consists of name of class to create the object
        """
        arglist = parse(arg)
        if len(arglist) == 0:
            print("** class name missing **")
        else:
            cls = self.verify_class(arglist[0])
            if cls:
                my_model = cls()
                my_model.save()
                print(my_model.id)

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name
        Arguments:
            arg: consists of name of class to create the object
        """
        arglist = parse(arg)
        all_list = []
        if len(arglist) > 0:
            cls = self.verify_class(arglist[0])
            if cls:
                for key, value in storage.all().items():
                    if type(value) == cls:
                        str_value = value.__str__()
                        all_list.append(str_value)
                print(all_list)
        else:
            for key, value in storage.all().items():
                str_value = value.__str__()
                all_list.append(str_value)
            print(all_list)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        Arguments:
            arg: consists of name of class where the object resides and
            the object id
        """
        arglist = parse(arg)
        if len(arglist) == 0:
            print("** class name missing **")
        elif len(arglist) == 1:
            print("** instance id missing **")
        else:
            cls = self.verify_class(arglist[0])
            if cls:
                key = arglist[0] + "." + arglist[1]
                objdict = storage.all()
                if key in objdict:
                    print(objdict[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Arguments:
            arg: consists of name of class where the object resides and
            the object id
        """
        arglist = parse(arg)
        if len(arglist) == 0:
            print("** class name missing **")
        elif len(arglist) == 1:
            print("** instance id missing **")
        else:
            cls = self.verify_class(arglist[0])
            if cls:
                key = arglist[0] + "." + arglist[1]
                objdict = storage.all()
                if key in objdict:
                    del (objdict[key])
                    storage.save()
                else:
                    print("** no instance found **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file).
        Arguments:
            arg: consists of name of class where the object resides,
            the object id, attribute name and value
        """
        arglist = parse(arg)
        if len(arglist) == 0:
            print("** class name missing **")
        elif len(arglist) == 1:
            print("** instance id missing **")
        elif len(arglist) == 2:
            print("** attribute name missing **")
        elif len(arglist) == 3:
            key = arglist[0] + "." + arglist[1]
            objdict = storage.all()
            if type(arglist[2]) == dict:
                for k in arglist[2].keys():
                    objdict[key].__dict__[k] = arglist[2][k]
            else:
                print("** value missing **")
        else:
            cls = self.verify_class(arglist[0])
            if cls:
                key = arglist[0] + "." + arglist[1]
                objdict = storage.all()
                if key not in objdict:
                    print("** no instance found **")
                else:
                    objdict[key].__dict__[arglist[2]] = arglist[3]
                    storage.save()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """exits the command interpreter"""
        return True

    def verify_class(self, ClassName):
        """verifies if the class exists"""
        try:
            my_model = eval(ClassName)
            return my_model
        except NameError:
            print("** class doesn't exist **")
            return False


def parse(arg):
    """
    This function splits a string based on delimiters whitespace,
    comma and more
    """
    return arg.split()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
