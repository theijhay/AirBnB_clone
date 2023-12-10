#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import json
import shlex
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

# The Do Quit
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

# The Do EOF
    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print()  # Add a newline before exiting
        return True

# The Emptyline
    def emptyline(self):
        """Do nothing while receiving an empty line."""
        pass
    
    
    """Create a new instance of the base model"""
    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)
    
    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        storage = BaseModel._FileStorage__objects
        if key not in storage:
            print("** no instance found **")
        else:
            print(storage[key])       
            
            
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        storage = BaseModel._FileStorage__objects
        if key not in storage:
            print("** no instance found **")
        else:
            del storage[key]
            BaseModel.save_to_file()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = shlex.split(arg)
        storage = BaseModel._FileStorage__objects
        if not args:
            print([str(storage[key]) for key in storage])
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            print([str(storage[key]) for key in storage if args[0] in key])

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        storage = BaseModel._FileStorage__objects
        if key not in storage:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attr_value = args[3]
        instance = storage[key]
        setattr(instance, attr_name, attr_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
