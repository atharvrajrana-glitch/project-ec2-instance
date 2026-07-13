import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

sql_database_url = os.getenv("sql_database_url")
# print("DATABASE URL:",sql_database_url)

engine = create_engine(sql_database_url)

SessionLocal = sessionmaker(autocommit=False,bind=engine)

Base = declarative_base()