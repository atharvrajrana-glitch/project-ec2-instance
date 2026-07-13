from sqlalchemy import Column, Integer, String, Boolean,create_engine
from app.database import Base

class User(Base):
    __tablename__="users"

    id = Column(Integer,primary_key=True)
    username = Column(String(50),unique=True,nullable=False)
    email = Column(String(100),nullable=False)
    height = Column(Integer,index=True,nullable=True)
    
