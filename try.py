from dataclasses import dataclass


from dataclasses import dataclass

# @dataclass
class ClassA:
  def __init__(self, name, age):
    self.name = name
    self.age = age

foo = ClassA(age=10, name='ark zeki')
print(foo.__dict__)
