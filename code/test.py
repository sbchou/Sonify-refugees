from miditime.miditime import MIDITime

# Instantiate the class with a tempo (120bpm is the default) and an output file destination. 
#the number of seconds you want to represent a year in the final song (default is 5 sec/year), the base octave (C5 is middle C, so the default is 5, and how many octaves you want your output to range over (default is 1).
mymidi = MIDITime(120, 'myfile.mid', 5, 5, 1)

# Create a list of notes. Each note is a list: [time, pitch, velocity, duration]
midinotes = [
    [0, 60, 127, 3],  #At 0 beats (the start), Middle C with velocity 127, for 3 beats
    [10, 61, 127, 4]  #At 10 beats (12 seconds from start), C#5 with velocity 127, for 4 beats
]

# Add a track with those notes
mymidi.add_track(midinotes)

# Output the .mid file
mymidi.save_midi()
