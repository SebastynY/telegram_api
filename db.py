from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine
from config import Config
from sqlalchemy.orm import sessionmaker

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)

Base = declarative_base()
metadata = Base.metadata
Session = sessionmaker(bind=engine)
session = Session()
