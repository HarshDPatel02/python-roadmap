from plates import is_valid


def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("CS50") == True


def test_start_letters():
    assert is_valid("50CS") == False
    assert is_valid("1ABC") == False
    assert is_valid("CS50") == True


def test_number_placement():
    assert is_valid("CS50") == True
    assert is_valid("CS5A") == False
    assert is_valid("AAA222") == True
    assert is_valid("AA22AA") == False


def test_zero_placement():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True


def test_punctuation():
    assert is_valid("CS50!") == False
    assert is_valid("CS 50") == False


def test_letters_only():
    assert is_valid("HELLO") == True
