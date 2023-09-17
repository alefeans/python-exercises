import pytest
from datetime import datetime
from practice_python.char_input.char_input import years


@pytest.mark.parametrize(
    "name, age, expected",
    [("John", 2, "John will be 100 years old in {}".format(datetime.now().year + 98))],
)
def test_when_user_will_be_100_years_old(name, age, expected):
    assert years(name, age) == expected
