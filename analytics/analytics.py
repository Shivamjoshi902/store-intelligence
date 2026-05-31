from database.db import get_connection


def get_total_entries():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM events
        WHERE event_type='entry'
        """
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count


def get_total_exits():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM events
        WHERE event_type='exit'
        """
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count


def get_occupancy():

    return get_total_entries() - get_total_exits()


def get_footfall():

    return get_total_entries()