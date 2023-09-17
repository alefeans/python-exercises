import pytest
from epi.chapter_1 import right_propagate_bit, is_power_of_two


@pytest.mark.parametrize(
    "input, expected",
    [
        (1, 1),
        (2, 3),
        (80, 95),
        (32, 63),
    ],
)
def test_if_righ_propagates_rightmost_bit(input, expected):
    assert right_propagate_bit(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (1, True),
        (2, True),
        (3, False),
        (4, True),
        (5, False),
        (6, False),
        (8, True),
        (1024, True),
    ],
)
def test_if_is_power_of_two(input, expected):
    assert is_power_of_two(input) == expected
