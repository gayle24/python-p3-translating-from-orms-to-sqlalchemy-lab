from models import Dog

from sqlalchemy import (create_engine,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def create_table(base):
    __tablename__ = 'dogs'
    __table_args__ = (
        PrimaryKeyConstraint(
            'id',
            name='id_pk'),
        UniqueConstraint(
            'email',
            name='unique_email'),
        CheckConstraint(
            'grade BETWEEN 1 AND 12',
            name='grade_between_1_and_12')
    )

    Index('index_name', 'name')

    id = Column(Integer())
    name = Column(String())
    email = Column(String(55))

def save(session, dog):
    pass

def get_all(session):
    pass

def find_by_name(session, name):
    pass

def find_by_id(session, id):
    pass

def find_by_name_and_breed(session, name, breed):
    pass

def update_breed(session, dog, breed):
    pass