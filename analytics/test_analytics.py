from analytics.analytics import (
    get_total_entries,
    get_total_exits,
    get_occupancy,
    get_footfall
)

print("Entries:", get_total_entries())

print("Exits:", get_total_exits())

print("Occupancy:", get_occupancy())

print("Footfall:", get_footfall())