def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
       ints(list): list of integers containing one or more integers
    """
    min = float('inf')
    max = float('-inf')
    for value in ints:
        if (value < min):
            min = value
        if (value > max):
            max = value
    return min, max

### Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [0,0]
print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail")

l = [-2,-1]
print ("Pass" if ((-2, -1) == get_min_max(l)) else "Fail")
