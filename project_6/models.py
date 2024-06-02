from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(100))
    lastname = Column(String(100))
    joined_at = Column(DateTime, default=datetime.now)
    article = relationship("Article", back_populates="author")


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    content = Column(Text)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="article")


url = "sqlite:///:memory:"
engine = create_engine(url)
Session = sessionmaker(bind=engine)
