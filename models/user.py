from sqlalchemy import Integer, Column, String, DateTime
from db import Base, session
from sqlalchemy.sql import func
import re


# class User(Base):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), nullable=False)
#     phone = db.Column(db.String(50), nullable=False)
#     password = db.Column(db.String(500), nullable=False)
#     description = db.Column(db.String(1000), nullable=False)
#     created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
#     updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())
#
#     # phone_valid(phone:str) -> bool
#     @staticmethod
#     def phone_valid(phone: str) -> bool:
#         regular = r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'
#         return bool(re.match(regular, phone))
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    password = Column(String(500), nullable=False)
    description = Column(String(1000), nullable=False)
    created_at = Column(DateTime(), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(), nullable=False, server_default=func.now(), onupdate=func.now())

    @staticmethod
    def phone_valid(phone: str) -> bool:
        regular = r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'
        return bool(re.match(regular, phone))

    def save(self):
        session.add(self)
        session.commit()
