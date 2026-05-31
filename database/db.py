import sqlite3

from database.models import EVENTS_TABLE

DB_NAME = "store.db"


def get_connection():

    return sqlite3.connect(DB_NAME)


def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(EVENTS_TABLE)

    conn.commit()

    conn.close()

    print("Database initialized successfully.")