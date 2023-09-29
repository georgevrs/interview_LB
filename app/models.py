# app/models.py
from sqlalchemy import Column, Integer, String, Date, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "mysql+mysqlconnector://root@localhost/interview_LB"

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL)


# Use this for future session creations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
metadata = MetaData()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    gemh_number = Column(String, unique=True, index=True)
    website = Column(String)
    registration_date = Column(Date)
