from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Password(Base):
	__tablename__ = 'users'

	id = Column('id', Integer, primary_key=True, autoincrement=True)
	label = Column('label', String)
	password = Column('password', String)

engine = create_engine('sqlite:///password_generator.db')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)