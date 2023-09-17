import pytest
from practice_python.odd_or_even.odd_or_even import response, divisible


@pytest.mark.parametrize(
    "number, expected",
    [
        (4, "Multiple of four"),
        (3, "Odd"),
        (2, "Even"),
    ],
)
def test_divisible_responses(number, expected):
    assert response(number) == expected


@pytest.mark.parametrize(
    "num, check, expected",
    [
        (2, 4, "Yes, it's evenly divisible"),
        (2, 3, "No, it's not evenly divisible"),
        (2, 2, "Yes, it's evenly divisible"),
    ],
)
def test_if_number_is_disible_by_check(num, check, expected):
    assert divisible(num, check) == expected
