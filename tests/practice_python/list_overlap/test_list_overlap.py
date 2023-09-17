import pytest

from practice_python.list_overlap.list_overlap import common_numbers


@pytest.mark.parametrize(
    "list_one, list_two, expected",
    [([1, 2, 3, 5], [2, 5], {2, 5}), ([1, 2], [1], {1}), ([1, 2], [3], set())],
)
def test_which_numbers_are_commons(list_one, list_two, expected):
    assert common_numbers(list_one, list_two) == expected
