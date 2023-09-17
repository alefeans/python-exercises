import pytest
from practice_python.list_comprehensions.list_comprehensions import even_numbers


@pytest.mark.parametrize(
    "input_list, even_list",
    [
        ([1, 2, 3], [1, 3]),
        ([1], [1]),
        ([2, 4], []),
        ([2, 3, 4, 5], [3, 5]),
        ([5, 5, 5], [5, 5, 5]),
    ],
)
def test_if_received_numbers_are_even(input_list, even_list):
    assert even_numbers(input_list) == even_list
