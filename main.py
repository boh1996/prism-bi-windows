import classes
import skype_db
__author__ = 'Bo'

results = skype_db.session.query("SELECT FROM SMSes WHERE type=2")

for result in results:
    print result

