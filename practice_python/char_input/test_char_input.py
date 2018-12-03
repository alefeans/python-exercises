import pytest
from char_input import years


@pytest.mark.parametrize("name, age, expected", [
    ("John", 2, "John will be 100 years old in 2116")
])
def test_when_user_will_be_100_years_old(name, age, expected):
    assert years(name, age) == expected
