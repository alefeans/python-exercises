import pytest
from epi.chapter_2 import even_first


@pytest.mark.parametrize(
    "input, expected",
    [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [2, 3, 1]),
        ([1, 2, 3, 4], [4, 2, 3, 1]),
        ([1, 5, 3, 4], [4, 3, 5, 1]),
        ([1, 2, 4, 4], [4, 2, 4, 1]),
    ],
)
def test_if_reorders_list_with_even_numbers_in_the_beginning(input, expected):
    assert even_first(input) == expected
