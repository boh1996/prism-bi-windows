from sqlalchemy import create_engine
import os
import sys
__author__ = 'Bo'
username = "bo.hans"
skype_path = os.getenv('APPDATA')+'\Skype\{{USERNAME}}\main.db'
skype_path = skype_path.replace("{{USERNAME}}", username)

print skype_path
skype_db_engine = create_engine('sqlite:////'+skype_path)
skype_db_connection = skype_db_engine.connect()

