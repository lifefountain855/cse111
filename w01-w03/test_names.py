from names import make_full_name, \
    extract_family_name, extract_given_name, extract_city, extract_zip, extract_state
import pytest

def test_make_full_name():
    assert type(make_full_name("", "")) == str
    assert make_full_name("", "") == ";"
    assert make_full_name("", "sapp") == "sapp;"
    assert make_full_name("kevin", "") == ";kevin"
    assert make_full_name("kevin", "sapp") == "sapp;kevin"
    assert make_full_name("Joseph", "Smith") == "Smith;Joseph"

def test_extract_family_name():
    assert type(extract_family_name(" ; ")) == str
    assert extract_family_name(" ; ") == ' '
    assert extract_family_name("sapp; ") == 'sapp'
    assert extract_family_name("sapp; kevin") == 'sapp'
    assert extract_family_name("smith; joseph") == 'smith'
    assert extract_family_name("brown; john") == 'brown'

def test_extract_given_name():
    assert type(extract_given_name(" ; ")) == str
    assert extract_given_name(" ; ") == ''
    assert extract_given_name("sapp; ") == ''
    assert extract_given_name("sapp; kevin") == 'kevin'
    assert extract_given_name("smith; joseph") == 'joseph'
    assert extract_given_name("brown; john") == 'john'

def test_extract_address():
    assert extract_state("525 S Center St, Rexburg, ID 83460") == '83460'
    assert extract_zip("525 S Center St, Rexburg, ID 83460") == 'ID'
    assert extract_city("525 S Center St, Rexburg, ID 83460") == 'Rexburg'

pytest.main(["-v", "--tb=line", "-rN", __file__])