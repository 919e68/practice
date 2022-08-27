from dataclasses import dataclass, field
from typing import Optional, List


class MongoCollection:
  def save(self):
    print('save')
    print('self', self)


@dataclass
class Field:
  name: str
  alias: Optional[str] = None


@dataclass
class Schema:
  collection: str
  # fields: list[Field]


  # @classmethod
  # def get_collection_name(cls):
  #   return cls.collection

# result = Schema(
#   collection='projects',
#   fields=['Hello World']
# )

class Project(Schema):
  collection = 'Hello'



project = Project()

print(project)
print(dir(project))


