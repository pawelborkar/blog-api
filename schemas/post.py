from pydantic import BaseModel
from datetime import datetime
from .image import Image
from .user import User


class PostBase(BaseModel):
    title: str
    content: str
    author_id: int # Requires authentication
    isPublished: bool
    images: list[Image] | None = None
    tags: set[str] | None = None
    

class PostIn(PostBase):
    pass


class PostOut(PostBase):
    id: int


class Post(PostBase):
    id: int
    published_on: datetime | None = None
    created_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True
