def count_bits(x):
    """Counts any bit that is set to 1 in a number

    Steps:
    - Verifies every bit of the number starting from the least significant bit
    - Initializes a counter and performs the loop until x becomes equal to 0
    - Increments the num_of_bits counter with the result of x & 1 operation. This operation
    will only return 1 if the least significant bit is set to 1 and 0 if not, because the &
      operator only returns 1 if both bits are sets to 1 at the same places (truth table)
    Another way of seeing it, is that it works like a multiplication. For instance, the number
    3 is 11 in binary. If multiplied by 01 (the binary representation of 1 with a 0 padding),
    returns 1, so it can be used to increment the counter. The number two which is 10 in binary
    with 01 returns 0, so it won't increment the counter
    - After that, performs a shift-right operation and assigns it to x, so now
    the binary 11 becomes 1, the binary 10110 becomes 1011 and so on and so forth
    """
    num_of_bits = 0
    while x:
        num_of_bits += x & 1
        x >>= 1
    return num_of_bits


def right_propagate_bit(x):
    """Right propagate the rightmost set bit in x, e.g., turns (01010000)2 to (01011111)2"""
    return x | (x - 1)


def is_power_of_two(n):
    """Test if x is a power of 2
    Evaluates to true for x = 1, 2, 4, 8..., and false for other values"""
    return n & (n - 1) == 0
