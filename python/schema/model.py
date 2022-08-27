from dataclasses import dataclass
from bson import ObjectId
from typing import Any, Callable, Dict, List, Optional, Union

EXCLUDED_ATTRIBUTES = [
  'aliases',
  'fields',
]

def rename_keys(aliases: dict[str, str], data: Union[Dict, List[Dict]]):
  if isinstance(data, Dict):
    return {
      aliases.get(key, key): value
      for key, value in data.items()
    }

  if isinstance(data, List):
    return [
      rename_keys(aliases, item)
      for item in data
    ]

def exclude_keys(excluded_keys: list, data: Union[Dict, List[Dict]]):
  if isinstance(data, Dict):
    return {
      key: data[key]
      for key in data
      if key not in excluded_keys
    }

  if isinstance(data, List):
    return [
      exclude_keys(excluded_keys, item)
      for item in data
    ]

@dataclass
class Field:
  default: Optional[Any] = None
  name: Optional[Any] = None
  alias: Optional[str] = None
  type: Optional[Any] = None
  parser: Optional[Callable] = None

class Model:
  def __init__(self, **kwargs):
    self.aliases: dict[str, str] = {}
    self.fields: list[Field] = []
    self.init(kwargs)

  def init(self, attributes):
    self.set_attributes(attributes)
    self.get_aliases()

  def set_attribute(self, name: str, type: Any, value: Any, field: Field):
    field.name = name
    field.type = type
    self.fields.append(field)
    if callable(field.parser):
      value = field.parser(value)
    setattr(self, name, value)

  def set_attributes(self, attrs):
    attributes = self.get_attributes()
    for field_name, field_type in attributes.items():
      field = getattr(self, field_name, None)
      if isinstance(field, Field):
        set_name = field.alias or field_name
        value = attrs.get(set_name, field.default)
        self.set_attribute(field_name, field_type, value, field)

  def get_attributes(self):
    return self.__annotations__

  def get_aliases(self):
    if not self.aliases:
      for field in self.fields:
        if field.alias:
          self.aliases[field.name] = field.alias
    return self.aliases

  def dict(self, alias: bool = False):
    result = exclude_keys(self.excluded_fields(), self.__dict__)
    return rename_keys(self.aliases(), result) if alias else result

  def excluded_fields(self):
    return EXCLUDED_ATTRIBUTES

  def __str__(self):
    return f'<{type(self).__name__} {self.dict()}>'


class Project(Model):
  collection: str

  # fields
  id: ObjectId = Field(parser=ObjectId)
  user_id: str = Field(alias='userId')
  title: str = Field()
  problem_type: str = Field(alias='userId')
  description: str = Field()
  is_copied: bool = Field(default=False, alias='isCopied')
  created_at: str = Field(alias='createdAt')
  updated_at: str = Field(alias='updatedAt')


project = Project(userId=123)
print(project)