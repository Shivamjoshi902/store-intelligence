EVENTS_TABLE = """
CREATE TABLE IF NOT EXISTS events (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    person_id INTEGER NOT NULL,

    event_type TEXT NOT NULL,

    timestamp TEXT NOT NULL

);
"""