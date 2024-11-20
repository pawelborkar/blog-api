from typing import Annotated

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    fullname: Annotated[str, "Enter your full name"]