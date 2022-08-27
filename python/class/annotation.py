class Demo:
  ok: bool = False
  data: dict
  errors: list[dict] = None
  # def __init__(self, ok=False, data=None):
  #   self.ok = ok
  #   self.data = data
  #   self.errors = []

demo = Demo()
print('demo.__dict__', demo.__dict__)
print('demo.__annotations__', demo.__annotations__)
