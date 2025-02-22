import json
import time

with open("guitar_events.json", "r") as file:
    events = json.load(file)

timestamp = 0 # In milliseconds

# Simulate playing process
event_index = 0

for event in events:
    string = event["string"]
    fret = event["fret"]
    start = int(event["start"])
    
    if timestamp == start:
        # Do the required cmd
        while :
    
    time.sleep(0.01) # Sleep for 10ms
    timestamp += 10

