
from project import calculate_summary


def test_single_category():
    data = [
        {"amount": 10, "category": "food"},
        {"amount": 5, "category": "food"}
    ]

    result = calculate_summary(data)

    assert result["food"] == 15


def test_multiple_categories():
    data = [
        {"amount": 10, "category": "food"},
        {"amount": 20, "category": "travel"},
        {"amount": 5, "category": "food"}
    ]

    result = calculate_summary(data)

    assert result["food"] == 15
    assert result["travel"] == 20


def test_empty_data():
    result = calculate_summary([])
    assert result == {}
