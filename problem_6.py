def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return None, None
    min = float('inf')
    max = float('-inf')
    for value in ints:
        if (value < min):
            min = value
        if (value > max):
            max = value
    return min, max

# Test Cases
# Nominal test case
import random
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Edge case 1: empty input
l = []
print ("Pass" if ((None, None) == get_min_max(l)) else "Fail")

# Edge case 2: Large values
l = [-1000000,1000000]
print ("Pass" if ((-1000000, 1000000) == get_min_max(l)) else "Fail")
