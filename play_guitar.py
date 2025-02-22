import json
import time
import numpy as np
import sounddevice as sd

from parse_guitar import file_name

def precise_sleep(duration_ms):
    start = time.perf_counter_ns()
    while (time.perf_counter_ns() - start < (duration_ms * 1e6)):
        pass

def play_tone(frequency=440, duration=0.01, sample_rate=44100):
    """Generates and plays a sine wave at a given frequency and duration."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # Amplitude 0.5 to avoid clipping
    sd.play(wave, samplerate=sample_rate)

with open(f"{file_name}.json", "r") as file:
    events = json.load(file)

timestamp = 0 # In milliseconds

# Simulate playing process
event_index = 0
total_events = len(events)

while event_index < total_events:
    # For all events with same timestamp
    played = False
    while event_index < total_events and events[event_index]["start"] == timestamp:
        if not played:
            play_tone()
            played = True
        event = events[event_index]
        print(f"At {event["start"]}ms: Play string {event["string"]} at fret {event["fret"]}")
        event_index += 1

    timestamp += 1
    precise_sleep(1)
time.sleep(1)