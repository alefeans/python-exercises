import pytest
from odd_or_even import response, divisible

class TestClass(object):

    @pytest.mark.parametrize("number, expected", [
        (4, "Multiple of four"),
        (3, "Odd"),
        (2, "Even"),
    ])
    def test_divisible_responses(self, number, expected):
        assert response(number) == expected

    def test_if_number_is_disible_by_check(self):
        assert divisible(2, 4) == "Yes, it's evenly divisible"

    def test_if_number_is_not_divisible_by_check(self):
        assert divisible(2, 3) != "Yes, it's evenly divisible"
