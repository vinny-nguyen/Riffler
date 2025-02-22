import guitarpro
import json

def get_tempo(measure):
    """
    Attempts to retrieve the tempo (BPM) for a measure.
    Checks if 'tempo' exists directly on the header, then in header events.
    Defaults to 120 BPM if not found.
    """
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

    return 120

def parse_gpt5(file_path):
    """
    Parses a Guitar Pro (.gpt5) file and extracts note events with timing, fret, string, and velocity.
    Returns a list of events.
    """
    try:
        song = guitarpro.parse(file_path)
    except Exception as e:
        print(f"Error parsing file: {e}")
        return []

    events = []
    
    # Loop through each track that is not a percussion track.
    for track in song.tracks:
        if not track.isPercussionTrack:
            current_time = 0.0  # Running time in seconds
            for measure in track.measures:
                bpm = get_tempo(measure)
                seconds_per_beat = 60.0 / bpm
                
                for voice in measure.voices:
                    for beat in voice.beats:
                        beat_duration_beats = beat.duration.time
                        beat_duration_seconds = beat_duration_beats * seconds_per_beat
                        
                        # For each note in the beat, assume it starts at current_time
                        for note in beat.notes:
                            note_start_seconds = current_time  # No per-note offset available
                            event = {
                                'string': note.string,          # Guitar string number (typically 1 to 6)
                                'fret': getattr(note, 'fret', -1), # Fret number (-1 indicates open string) -- Fix this
                                'start': round(note_start_seconds, 3),  # Start time in seconds
                                'duration': round(beat_duration_seconds, 3),  # Duration in seconds
                                'velocity': note.velocity       # Dynamic level, if available
                            }
                            events.append(event)
                        # Update running time after processing the beat.
                        current_time += beat_duration_seconds
    return events

if __name__ == '__main__':
    # Replace with the path to your .gpt5 file
    file_path = 'tabs\god-save-the-queen.gp5'
    events = parse_gpt5(file_path)
    
    if events:
        with open('guitar_events.json', 'w') as f:
            json.dump(events, f, indent=2)
        print("Parsed events written to guitar_events.json")
    else:
        print("No events parsed.")
