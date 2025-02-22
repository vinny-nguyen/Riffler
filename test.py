import guitarpro
import json

TICKS_PER_BEAT = 480  # Guitar Pro's default tick resolution per quarter note

def get_tempo(measure):
    """Attempts to retrieve the tempo (BPM) for a measure. Defaults to 120 BPM if not found."""
    if hasattr(measure.header, 'tempo'):
        tempo = getattr(measure.header, 'tempo', None)
        if tempo is not None:
            try:
                return tempo.value  # if tempo is an object
            except AttributeError:
                return tempo       # if tempo is already a number

    if hasattr(measure.header, 'events'):
        for event in measure.header.events:
            if hasattr(event, 'type') and event.type == 'Tempo':
                return event.value

    return 120  # Default BPM if no tempo is found

def parse_gpt5(file_path):
    """Parses a Guitar Pro (.gp5) file and extracts note events with timing, fret, and string."""
    try:
        song = guitarpro.parse(file_path)
    except Exception as e:
        print(f"Error parsing file: {e}")
        return []

    events = []
    seen_events = set()  # To ensure unique entries

    for track in song.tracks:
        if not track.isPercussionTrack:
            current_time = 0.0  # Running time in seconds
            for measure in track.measures:
                bpm = get_tempo(measure)
                seconds_per_beat = 60.0 / bpm  # Convert BPM to seconds per beat

                for voice in measure.voices:
                    for beat in voice.beats:
                        # Skip empty beats (rests or beats with no notes)
                        if not beat.notes:
                            continue

                        beat_duration_ticks = beat.duration.time  # This might be in ticks
                        beat_duration_beats = beat_duration_ticks / TICKS_PER_BEAT  # Convert to beats
                        beat_duration_seconds = beat_duration_beats * seconds_per_beat  # Convert to seconds
                        print(f"Beat duration (seconds): {beat_duration_seconds}")

                        # Use the current time before incrementing
                        for note in beat.notes:
                            string = note.string
                            fret = note.value
                            start_time = round(current_time, 3)

                            event_tuple = (string, fret, start_time)
                            if event_tuple not in seen_events:
                                seen_events.add(event_tuple)
                                events.append({
                                    'string': string,
                                    'fret': fret,
                                    'start': start_time * 1000
                                })

                        # Now update the running time **after** processing this beat
                        current_time += beat_duration_seconds
                        print(f"Updated current time: {current_time}")
                        print("END BEAT")

    return sorted(events, key=lambda x: x['start'])

parse_gpt5("tabs/test.gp5")
