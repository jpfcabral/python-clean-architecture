from typing import List, Optional
from sqlmodel import Field, Relationship
from src.domain.models.users import UserBase


class User(UserBase, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    pets: List['Pet'] = Relationship(back_populates='user')

    def __rep__(self):
        return f"User [name={self.name}, email={self.email}]"
