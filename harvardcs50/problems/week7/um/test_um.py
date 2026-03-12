from um import count


def test_single():
    assert count("um") == 1


def test_multiple():
    assert count("Um, thanks, um...") == 2


def test_case_insensitive():
    assert count("UM um Um") == 3


def test_not_substring():
    assert count("yummy album") == 0
