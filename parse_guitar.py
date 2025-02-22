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
    seen_events = set() # Keep track of seen events to ensure uniqueness
    
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
                            note_start_seconds = current_time
                            # Debugging (can't figure out why it's not reading the fret number):
                            # 0 fret now indicates open string
                            string = note.string
                            fret_temp = note.value
                            start_time = round(note_start_seconds, 3)


                            event_tuple = (string, fret_temp, start_time)

                            if event_tuple not in seen_events:
                                seen_events.add(event_tuple)
                                events.append({
                                    'string': string,
                                    'fret': fret_temp,
                                    'start': start_time
                                })

                        # Update running time after processing the beat.
                        current_time += beat_duration_seconds
    return sorted(events, key=lambda x: x['start'])

if __name__ == '__main__':
    # Replace with the path to your .gpt5 file
    file_path = 'tabs/o-canada.gp5'
    events = parse_gpt5(file_path)
    
    if events:
        with open('guitar_events.json', 'w') as f:
            json.dump(events, f, indent=2)
        print("Parsed events written to guitar_events.json")
    else:
        print("No events parsed.")
