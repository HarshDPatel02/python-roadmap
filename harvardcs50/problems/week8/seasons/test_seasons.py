from seasons import minutes_since_birth, number_to_words
from datetime import date


def test_minutes_one_year():
    today = date.today()
    birth = f"{today.year - 1}-{today.month:02}-{today.day:02}"
    assert minutes_since_birth(birth) in [525600, 527040]


def test_minutes_two_years():
    today = date.today()
    birth = f"{today.year - 2}-{today.month:02}-{today.day:02}"
    assert minutes_since_birth(birth) >= 1051200


def test_words():
    assert number_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
