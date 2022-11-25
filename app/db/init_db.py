from .database import Base, engine


def initialize_db():
    # create database with tables
    Base.metadata.create_all(bind=engine)
