from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Genshin_Item(Base):
    __tablename__ = "genshin"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    element = Column(String, index=True)
    level = Column(Integer, index=True)
