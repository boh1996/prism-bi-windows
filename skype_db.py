from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
__author__ = 'Bo'
username = "bo.hans"
path = os.getenv('APPDATA')+'\Skype\{{USERNAME}}\main.db'
path = path.replace("{{USERNAME}}", username)

db_engine = create_engine('sqlite:///main.db')

Session = sessionmaker(bind=db_engine)

# create a Session
session = Session()