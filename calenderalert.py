import datetime
import os

from icalevents.icalevents import events

url = os.environ["BLMR_ICAL_URL"]
es = events(url, start=datetime.datetime.now(), end=datetime.date.today() + datetime.timedelta(days=1))
for e in es:
    print(e)
