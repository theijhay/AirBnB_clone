## 0x00. AirBnB clone - The console

## The description of the project.
 - The Airbnb Clone project is a recreation platform. The goal is to replicate core functionalities, allowing users to list their properties for short-term rentals and enabling guests to discover their properties. The project prioritizes a seamless and user-friendly experience for both hosts and guests.It includes a command-line interface (CLI) to interact with the system.

## The description of the command interpreter.
 - The command interpreter is a text-based interface that enables users to interact with the Airbnb clone system. It supports various commands to perform actions such as creating properties,and handling user information.

## how to start it
 - Create a repository
 - Clone the repository, for example (git clone https://github.com/your-username/airbnb-clone.git)
 - cd into the repository. ( cd AirBnB_clone )

## How to Use the Command Interpreter.
 - Once the command interpreter is running, you can enter commands to perform various actions within the Airbnb clone.

## Execution
Your shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

```
But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash