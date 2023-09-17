import pytest
from practice_python.list_ends.list_ends import cut


@pytest.mark.parametrize(
    "sent, expected",
    [([1, 2, 3, 4], [1, 4]), ([1], [1]), ([1, 2], [1, 2]), ([2, 3, 5], [2, 5]), ([], [])],
)
def test_if_new_list_contains_first_and_last_numbers(sent, expected):
    assert cut(sent) == expected
