# Python typing Classes as types and Pydantic models

class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "John doe"
    signup_date: datetime | None = None
    friends: list[str] = []

    def get_name(self):
        return self.name


data = {
    "id": 1,
    "signup_ts": "2017-06-01 12:22",
    "friends": ["Alice", "Bob"],
}

user = User(**data)
print(user) # id=1 name='John doe' signup_date=None friends=['Alice', 'Bob']
print(user.friends)
print(user.get_name())
