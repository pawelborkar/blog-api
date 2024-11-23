from pydantic import BaseModel, HttpUrl


class Image(BaseModel):
    file_name: str | None = None
    url: HttpUrl
