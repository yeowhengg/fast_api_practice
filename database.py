# Uncomment me to run it locally!
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123@localhost/test"

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# # it is an instance of a db session. This specific instance will be the actual db session.
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # this is the db model maker. This returns a class of the database structure
# Base = declarative_base()




# # I am for docker env!
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

engine = create_engine("postgresql://postgres:postgres@db:5432/postgres", echo=True)
if not database_exists(engine.url):
    create_database(engine.url)

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db/postgres"

meta = MetaData()

genshin = Table(
    'genshin', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('element', String),
    Column('level', Integer)
)

meta.create_all(engine)

# it is an instance of a db session. This specific instance will be the actual db session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# this is the db model maker. This returns a class of the database structure
Base = declarative_base()