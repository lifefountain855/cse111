from mido import MidiFile
import json
from seconds import midi_ticks_to_seconds
import snippets as s

"""
MIDI Note Numbers (0 - 127) By Octave
=====================================================================================================
Octave  |  C  | C# / Db |  D  | D# / Eb |  E  |  F  | F# / Gb |  G  | G# / Ab |  A  | A# / Bb |  B  |
-----------------------------------------------------------------------------------------------------
-1      |  0  |    1    |  2  |    3    |  4  |  5  |    6    |  7  |    8    |  9  |   10    |  11 |
0       | 12  |   13    | 14  |   15    | 16  | 17  |   18    | 19  |   20    | 21  |   22    |  23 |
1       | 24  |   25    | 26  |   27    | 28  | 29  |   30    | 31  |   32    | 33  |   34    |  35 |
2       | 36  |   37    | 38  |   39    | 40  | 41  |   42    | 43  |   44    | 45  |   46    |  47 |
3       | 48  |   49    | 50  |   51    | 52  | 53  |  {54    | 55  |   56    | 57  |   58    |  59 |
4 (Mid) | 60  |   61    | 62  |   63    | 64  | 65  |   66    | 67  |   68    | 69  |   70    |  71 |
5       | 72  |   73    | 74  |   75    | 76  | 77  |   78}   | 79  |   80    | 81  |   82    |  83 |
6       | 84  |   85    | 86  |   87    | 88  | 89  |   90    | 91  |   92    | 93  |   94    |  95 |
7       | 96  |   97    | 98  |   99    | 100 | 101 |   102   | 103 |   104   | 105 |   106   | 107 |
8       | 108 |   109   | 110 |   111   | 112 | 113 |   114   | 115 |   116   | 117 |   118   | 119 |
9       | 120 |   121   | 122 |   123   | 124 | 125 |   126   | 127 |   -     |  -  |    -    |  -  |
=====================================================================================================
"""

NOTETYPES = [
    "bass",
    "snare",
    "hat",
    "bd",
    "bell",
    "flute",
    "chime",
    "guitar",
    "xylophone",
    "iron_xylophone",
    "cow_bell",
    "didgeridoo",
    "bit",
    "banjo",
    "pling",
    "trumpet",
    "trumpet_exposed",
    "trumpet_weathered",
    "trumpet_oxidized",
    "skeleton",
    "witherskeleton",
    "zombie",
    "creeper",
    "piglin",
    "enderdragon",
    "harp",
]

FILENAME='kolob.mid'

def get_file_and_track(filen='',trackx=None,merge=False,instruments=[]):
    """
    Gets input from the user on the file (if not default), if they would like to merge
    all the tracks or what individual track to select.
    
    Parameters:
        None
    Returns:
        list:
            filen: str file name
            trackx: int of track or None
            merge: an int-bool
            instruments: a list of channel-instrument assignments
    """
    print(f"File: {FILENAME}")
    inp=input("Okay (enter)? Or enter file: ")
    if inp: 
        print("ENTERED text")
        if "." not in inp: 
            print("Error processing file. Using default file...")
            filen=FILENAME
        else: 
            print("ENTERED FILE")
            filen=inp
    else:
        filen=FILENAME
    mid = MidiFile(filen, clip=True)
    print(mid.tracks)
    try:
        merge=int(input("Would you like to merge the tracks(1) or pick a single track(0)? "))
        if merge==1:
            instruments=[]
            trackx=None
            skipfirst=0
            for track in mid.tracks:
                if skipfirst==0: skipfirst=1;continue
                instruments.append(input(f"What instrument for {track}? "))
        if merge==0:
            instruments=[]
            trackx=int(input("Which track would you like to do? "))
    except ValueError:
        print("Error: not an integer")
    except: 
        print("Unexpected Error.")

    return [filen,trackx,merge,instruments]

def main():
    filetrack=get_file_and_track()
    seconds=midi_ticks_to_seconds(filetrack[0],filetrack[1],filetrack[2],filetrack[3])
    seconds=json.dumps(seconds,indent=2)
    songs=s.songsjs
    songs=songs.replace("[SONG]",filetrack[0].removesuffix(".mid"))
    songs=songs.replace("[$$$]",seconds)
    allsnippets={"manifest.json":s.manifest,"scripts/index.js":s.jscodesnip,"scripts/songs.js":songs,}
    with open("output.json","w+") as jfile:
        json.dump(allsnippets,jfile,indent=2)

        
if __name__=="__main__":
    main()