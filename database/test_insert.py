from database.db import (
    initialize_database,
    save_event,
    get_events
)

initialize_database()

sample_event = {
    "person_id": 999,
    "event_type": "entry",
    "timestamp": "2026-05-31T15:30:00"
}

save_event(sample_event)

events = get_events()

for event in events:
    print(event)