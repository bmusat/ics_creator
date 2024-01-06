import os
import csv
import arrow
import ics
import dotenv

dotenv.load_dotenv()  # take environment variables from .env.

CALENDAR_CSV_FILE = os.getenv('CALENDAR_CSV_FILE')
ICS_FILE          = os.getenv('ICS_FILE')

# read list of holidays from file
with open(CALENDAR_CSV_FILE, newline='', encoding="utf-8") as csvfile:
    eventreader = csv.DictReader(csvfile)
    events = [event for event in eventreader]

# create iCal calendar from holiday events
c = ics.Calendar()
for event in events:
    e = ics.Event()
    e.name = event['Holiday']
    e.begin = arrow.get(event['Date']).replace(tzinfo=ics.utils.gettz())
    if event['DateEnd']:
        e.end = arrow.get(event['DateEnd']).replace(tzinfo=ics.utils.gettz())
    e.make_all_day()
    c.events.add(e)

# save iCal calendar to importable .ics file   
with open(ICS_FILE, 'w', encoding="utf-8") as icsfile:
    icsfile.writelines(c.serialize_iter())
