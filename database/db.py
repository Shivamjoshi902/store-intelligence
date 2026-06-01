import sqlite3

from database.models import EVENTS_TABLE

DB_NAME = "demo_store.db"


def get_connection():

    return sqlite3.connect(DB_NAME)


def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(EVENTS_TABLE)

    conn.commit()

    conn.close()

    print("Database initialized successfully.")

def save_event(event):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO events
        (
            person_id,
            event_type,
            timestamp
        )
        VALUES (?, ?, ?)
        """,
        (
            event["person_id"],
            event["event_type"],
            event["timestamp"]
        )
    )

    conn.commit()

    conn.close()


def get_events():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            person_id,
            event_type,
            timestamp
        FROM events
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows