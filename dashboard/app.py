import sys
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import streamlit as st
from database.db import get_events
from analytics.analytics import (
    get_total_entries,
    get_total_exits,
    get_occupancy,
    get_footfall
)
import pandas as pd
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="Store Intelligence Dashboard",
    layout="wide"
)

st_autorefresh(
    interval=5000,
    key="dashboard_refresh"
)

st.title("🏪 Store Intelligence Dashboard")
st.caption(
    "Real-time retail analytics powered by YOLOv8, ByteTrack and FastAPI"
)

entries = get_total_entries()
exits = get_total_exits()
occupancy = get_occupancy()
footfall = get_footfall()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Entries",
        entries
    )

with col2:
    st.metric(
        "Exits",
        exits
    )

with col3:
    st.metric(
        "Occupancy",
        occupancy
    )

with col4:
    st.metric(
        "Footfall",
        footfall
    )

st.divider()

st.subheader("Recent Events")

events = get_events()

table_data = []

for event in reversed(events[-10:]):

    table_data.append(
        {
            "ID": event[0],
            "Person ID": event[1],
            "Event Type": event[2],
            "Timestamp": event[3]
        }
    )

st.table(table_data)

st.divider()

st.subheader("Event Distribution")

chart_data = pd.DataFrame(
    {
        "Event Type": ["Entry", "Exit"],
        "Count": [entries, exits]
    }
)

st.bar_chart(
    chart_data.set_index("Event Type")
)

# Analytics Summary Section
st.divider()

st.subheader("Store Insights")

st.success(
    f"Total Footfall Today: {footfall}"
)

st.info(
    f"Current Occupancy: {occupancy}"
)