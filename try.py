from dataclasses import dataclass


from dataclasses import dataclass

# @dataclass
class ClassA:
  def __init__(self):
    self()
    print('init')

  def __call__(self):
    print('call')

foo = ClassA()
