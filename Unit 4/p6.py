#Write a program to demonstrate method overriding and polymorphism.

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    # Method overriding
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    # Method overriding
    def sound(self):
        print("Cat meows")


# Polymorphism
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.sound()
