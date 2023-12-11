#!/usr/bin/python3
class ExampleClass:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"Hello, {self.name}!")


def main():
    example_instance = ExampleClass("World")
    example_instance.print_name()


if __name__ == "__main__":
    main()
