import mido

def convert_note(note_num):
    #
    minecraft_notes = [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]
    minecraft_pitches = [0.5,0.529732,0.561231,0.594604,0.629961,0.66742,0.707107,0.749154,0.793701,0.840896,0.890899,0.943874,1,1.059463,1.122462,1.189207,1.259921,1.33484,1.414214,1.498307,1.587401,1.681793,1.781797,1.887749,2,]
    if note_num in minecraft_notes:
        # print(minecraft_notes.index(note_num))
        # print(minecraft_pitches[minecraft_notes.index(note_num)])
        return minecraft_pitches[minecraft_notes.index(note_num)]
    else:
        print("Error: not a number in minecraft notes.")
        return "Error"

def midi_ticks_to_seconds(file_path,track):
    """
    Parses a MIDI file, calculates absolute seconds for every message, 
    and highlights performance notes when applicable.
    """
    mid = mido.MidiFile(file_path)
    ticks_per_beat = mid.ticks_per_beat
    current_tempo = 500000  # Default 120 BPM
    
    # Merge parallel tracks into one chronological sequence
    # merged_messages = mido.merge_tracks(mid.tracks)
    merged_messages = mid.tracks[track]
    
    absolute_time_seconds = 0.0
    timeline = []

        # Print Header for Scannability
    print(f"{'Event Type':<16} | {'Note Name (Num)':<16} | {'Delta Ticks':<12} | {'Abs Seconds':<12}")
    print("-" * 65)
    for msg in merged_messages:
        # 1. Calculate time delta in seconds
        delta_seconds = (msg.time * current_tempo) / (ticks_per_beat * 1_000_000)
        absolute_time_seconds += delta_seconds
        
        # 2. Extract note data if the message is a performance event
        note_display = "-"
        if msg.type in ['note_on', 'note_off']:
            # note_name = mido.note_to_name(msg.note)
            note_display = f"({msg.note})"
            
            # A note_on with velocity 0 is functionally a note_off
            if msg.type == 'note_on' and msg.velocity == 0:
                note_display += " [OFF]"
        
        # 3. Store the data structured
        timeline.append({
            "message": msg.type,
            "absolute_seconds": absolute_time_seconds,
            "delta_seconds": msg.time,
            "note_name": note_display if note_display != "-" else None,
            "minecraft_pitch": convert_note(msg.note) if note_display != "-" else None
        })
        
        # 4. Print visual tracking
        print(f"{msg.type:<16} | {note_display:<16} | {msg.time:<12} | {absolute_time_seconds:<12.4f}")

        # 5. Dynamically handle tempo shifts
        if msg.type == 'set_tempo':
            current_tempo = msg.tempo
            print(f" >>> [Tempo Change] New Tempo: {current_tempo} ms/beat")

    return timeline