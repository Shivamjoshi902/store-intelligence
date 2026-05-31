from database.db import get_events

events = get_events()

for event in events:
    print(event)