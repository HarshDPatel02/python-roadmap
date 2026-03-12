from numb3rs import validate

def test_valid_ips():
    assert validate("127.0.0.1") ==  True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True

def test_invalid_rangea():
    assert validate("512.512.512.512") == False
    assert validate("256.100.100.100") == False
    assert validate("1.2.3.1000") == False

def test_invalid_format():
    assert validate("cat") ==  False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False

def test_leading_zero():
    assert validate("192.168.001.1") == False

