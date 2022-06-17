from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from config import Config
from sqlalchemy.orm import sessionmaker

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread': False})

Base = declarative_base()
metadata = Base.metadata
Session = sessionmaker(bind=engine)
session = Session()
