from odd_or_even import response, divisible

class TestClass(object):

    def test_if_number_is_multiple_of_four(self):
        assert response(4) == "Multiple of four", "The value is not a multiple of four"    
        
    def test_if_number_is_odd(self):
        assert response(3) == "Odd", "The value was even, should be odd"
    
    def test_if_number_is_even(self):
        assert response(2) == "Even", "The value was odd, should be even"

    def test_if_number_is_disible_by_check(self):
        assert divisible(2, 4) == "Yes, it's evenly divisible"

