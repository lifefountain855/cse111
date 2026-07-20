import main as m
import seconds as s
import pytest
from unittest.mock import MagicMock

class MockMidiFile:
    # 1. Define the inner child class inside the parent
    class MockTrack:
        def __init__(self, name):
            self.name = name
            
        def __str__(self):
            return self.name

    def __init__(self, filename, clip=False):
        self.filename = filename
        
        # 2. Instantiate using the parent scope (self.MockTrack)
        self.tracks = [
            self.MockTrack("Meta Track"), 
            self.MockTrack("Track 1"), 
            self.MockTrack("Track 2"),
            self.MockTrack("Track 3")
        ]

@pytest.fixture
def mock_midi(monkeypatch):
    """Mocks the MidiFile class so it doesn't look for real files."""
    monkeypatch.setattr(m, "MidiFile", MockMidiFile)

def test_convert_note():
    assert s.convert_note(0) == 'Error'
    assert s.convert_note(53) == 'Error'
    assert s.convert_note(True) == 'Error'
    assert s.convert_note(79) == 'Error'
    assert s.convert_note(54) == 0.5
def test_convert_note2():
    notes = [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]
    pitches = [0.5,0.529732,0.561231,0.594604,0.629961,0.66742,0.707107,0.749154,0.793701,0.840896,0.890899,0.943874,1,1.059463,1.122462,1.189207,1.259921,1.33484,1.414214,1.498307,1.587401,1.681793,1.781797,1.887749,2]
    assert s.convert_note(78) == 2
    for i in range(0,len(notes)):
        assert s.convert_note(notes[i]) == pitches[i]

def test_midi_ticks_to_seconds():
    output=s.midi_ticks_to_seconds('kolob.mid',0,True,["flute","gutiar","bass"])
    assert type(output) == type([])
    assert type(output[0]) == type({}) # type: ignore
    assert type(output[0]["message"]) == type("") # type: ignore

    assert s.midi_ticks_to_seconds('kolob.m',0,True,["flute","gutiar","bass"]) == FileNotFoundError
    assert s.midi_ticks_to_seconds('kolob.mid',10,False,[]) == IndexError
    assert s.midi_ticks_to_seconds('kolob.mid',0,True,[]) == IndexError

def test_get_file_and_track(monkeypatch,mock_midi):
    inputs = iter(["", "1", "Piano", "Guitar"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = m.get_file_and_track()

    assert result == ["kolob.mid", None, 1, ["Piano", "Guitar"]]

    inputs1 = iter(["custom1.mid", "0", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs1))

    result1 = m.get_file_and_track()

    assert result1 == ["custom1.mid", 2, 0, []]

    inputs2 = iter(["badfilename", "0", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs2))

    result2 = m.get_file_and_track()

    assert result2 == ["kolob.mid", 1, 0, []]

def test_get_file_and_track2(monkeypatch,mock_midi):
    inputs = iter(["", "0", "notanint"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = m.get_file_and_track()

    assert result == ["kolob.mid", None, 0, []]

    inputs2 = iter(["", "notanint", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs2))

    result2 = m.get_file_and_track()

    assert result2 == ["kolob.mid", None, 0, []]



# test_convert_note2()
pytest.main(["-v", "--tb=line", "-rN", __file__])