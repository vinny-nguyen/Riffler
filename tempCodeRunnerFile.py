import json
import time

def precise_sleep(duration_ms):
    start = time.perf_counter_ns()
    while (time.perf_counter_ns() - start < (duration_ms * 1e6)):
        pass

with open("guitar_events.json", "r") as file:
    events = json.load(file)

timestamp = 0 # In milliseconds

# Simulate playing process
event_index = 0
total_events = len(events)

while event_index < total_events:
    # For all events with same timestamp
    while event_index < total_events and events[event_index]["start"] == timestamp:
        event = events[event_index]
        print(f"At {event["start"]}ms: Play string {event["string"]} at fret {event["fret"]}")
        event_index += 1

    timestamp += 10
    precise_sleep(10)
