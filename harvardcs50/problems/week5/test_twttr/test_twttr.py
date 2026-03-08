from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"

def test_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("AEIOU") == ""

def test_mixed():
    assert shorten("cs50") == "cs50"
    assert shorten("Python") == "Pythn"

def test_numbers():
    assert shorten("12345") == "12345"

def test_punctuation():
    assert shorten("hello!") == "hll!"
