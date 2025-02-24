import os


def greet(name):
    print(f"Hello, {name}")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hi, my name is " + self.name)


p = Person("Alice", 30)

p.say_hello()

greet("Bob")


if os.environ.get("DEBUG"):
    print("Debug mode is on")