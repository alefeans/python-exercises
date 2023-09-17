import pytest
from practice_python.list_less_then_five.list_less_then_five import check_list


@pytest.mark.parametrize("sent, expected", [([1, 2, 5, 6], [1, 2]), ([6, 7], []), ([1], [1])])
def test_check_itens_less_then_five(sent, expected):
    assert check_list(sent) == expected
