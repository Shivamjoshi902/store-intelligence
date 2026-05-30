from datetime import datetime


def create_event(person_id, event_type):

    return {
        "person_id": person_id,
        "event_type": event_type,
        "timestamp": datetime.now().isoformat()
    }