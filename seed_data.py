from incident_memory import *

init_db()

clear_incidents()

add_incident(
    "Rate Shopping stuck in Processing",
    "Queue Service Down",
    "Restart Queue Processor Service"
)

add_incident(
    "Hilton GRO Sync Failure",
    "API Authentication Timeout",
    "Refresh API Token"
)

add_incident(
    "Rate Push Failure",
    "PMS Connectivity Issue",
    "Reconnect PMS"
)
print("Sample incidents added successfully!")

print(get_incidents())