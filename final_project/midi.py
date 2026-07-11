from mido import MidiFile

FILENAME='VampireKillerCV1.mid'

def print_for_key(dict:dict,key:str):
    try:
        print(f"{key.title()}: {dict[key]}")
    except KeyError as err: print(err)
    return

def get_name_and_info(file):
    mid = MidiFile(file, clip=True)
    for msg in mid.tracks[0]:
        md=msg.dict()
        print_for_key(md,"key")
    for msg in mid.tracks[1]:
        print_for_key(md,"track_name")
        print(msg.dict())

def main():
    get_name_and_info(file=FILENAME)


if __name__=="__main__":
    main()