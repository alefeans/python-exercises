from list_overlap import common_numbers

def test_which_numbers_are_commons():
    a = [1, 2, 3, 5]
    b = [2, 5]
    assert common_numbers(a, b) == {2, 5}
