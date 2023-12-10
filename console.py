import cmd

class HBNBCommand(cmd.Cmd):
    
    
    """A Simple command processor

    Args:
        cmd (quit): To exit the program
    """
    prompt = '(hbnb)'
    
    def do_quit(self, arg):
        """This line of code exit the program."""
        return True
    
    def do_EOF(self, arg):
        """This line of code also exit the program.
            with a new line.
        """
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line and the keyword 
            pass is used.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()