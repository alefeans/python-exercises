import pytest
from practice_python.reverse_word_order.reverse_word_order import reverse


@pytest.mark.parametrize(
    "sent, expected",
    [
        ("My name is Alefe", ["Alefe", "is", "name", "My"]),
        ("Alefe", ["Alefe"]),
        ("Alefe is my name", ["name", "my", "is", "Alefe"]),
        ("Alefe is", ["is", "Alefe"]),
    ],
)
def test_the_reverse_word_order(sent, expected):
    # I know the response needs to be a string
    # but for simplicity
    # i"m printing the reverse list with print(*) on the main function
    assert reverse(sent) == expected
