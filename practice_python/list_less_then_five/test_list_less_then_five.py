from list_less_then_five import check_list

def test_check_itens_less_then_five():
    test_list = [1, 2, 5, 6]
    assert check_list(test_list) == [1, 2]
