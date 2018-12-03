import pytest
from string_lists import is_palindrome


@pytest.mark.parametrize("received, expected", [
    ("radar", "Is palindrome"),
    ("bla", "Is not a palindrome")
])
def test_if_is_palindrome_returns_right(received, expected):
    assert is_palindrome(received) == expected
