import secrets
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Session
from sqlalchemy.sql import func


if TYPE_CHECKING:
    from .user import User 


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    slug = Column(String(255), unique=True, nullable=False)
    is_published = Column(Boolean, default=False, nullable=False, server_default="False")
    author_id = Column(Integer, ForeignKey("users.id", ondelete= "CASCADE"), nullable=False)

    published_on = Column(Datetime(timezone=True), nullable=True)
    created_at = Column(Datetime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(Datetime(timezone=True), onupdate=func.now(), nullable=False)

    author = relationship("User", back_populates="posts", lazy="joined")


    # Methods
    def __init__(self, **kwargs):
        """ Add slug for SEO """
        super().__init__(**kwargs)
        if not self.slug and self.title:
            self.slug = self.generate_slug


    def generate_slug(self, title: str) -> str:
        """ Generate URL-friendly slug from title """
        suffix = secrets.token_urlsafe(6)
        slug = f"{title.lower().replace(" ", "-")}-{suffix}"
        return slug


    def publish(self):
        if not self.is_published and self.title:
            self.is_published = True
            self.published_on = datetime.utcnow()


    def unpublish(self):
        if self.is_published:
            self.is_published = False
            self.published_on = None


    @property
    def is_draft(self):
        return not self.is_published
