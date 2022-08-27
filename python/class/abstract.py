from abc import ABC, abstractmethod


class Animal(ABC):
  @abstractmethod
  def move(self, position: str):
    pass


class Dog(Animal):
  def __init__(self, name):
    self.name = name

  def move(self):
    print("I can move")


dog = Dog('Arlo')
print(dog.move())
