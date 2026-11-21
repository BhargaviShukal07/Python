from abc import ABC, abstractmethod

# Abstraction
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Encapsulation
class Dog(Animal):
    def __init__(self, name):
        self.__name = name

    def sound(self):
        print(self.__name, "barks")

# Object creation
d = Dog("Tommy")
d.sound()
