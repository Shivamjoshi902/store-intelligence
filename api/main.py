from fastapi import FastAPI
from database.db import get_events
from analytics.analytics import get_occupancy
from analytics.analytics import (
    get_total_entries,
    get_total_exits,
    get_occupancy,
    get_footfall
)

app = FastAPI(
    title="Store Intelligence API",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "message": "Store Intelligence System Running"
    }

@app.get("/events")
def events():

    rows = get_events()

    result = []

    for row in rows:

        result.append(
            {
                "id": row[0],
                "person_id": row[1],
                "event_type": row[2],
                "timestamp": row[3]
            }
        )

    return result

@app.get("/occupancy")
def occupancy():

    return {
        "occupancy": get_occupancy()
    }

@app.get("/analytics")
def analytics():

    return {

        "entries": get_total_entries(),

        "exits": get_total_exits(),

        "occupancy": get_occupancy(),

        "footfall": get_footfall()
    }