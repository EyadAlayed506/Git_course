from typing import Any,Annotated
from pydantic import BaseModel

class user(BaseModel):
    name:Annotated[Any,"it can be any type"]
    age:int

user1=user(name="Eyad",age="ahmed")
print(user1)