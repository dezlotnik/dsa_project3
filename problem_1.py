def sqrt_recursive(number, start, end):
    mid = start + (end - start)//2
    # Check if the floored square root is in [mid, mid+1]. If so, check if
    # mid + 1 is exactly the square root. Otherwise, return mid.
    if (mid*mid <= number and (mid+1)*(mid+1) >= number):
        if (mid+1)*(mid+1) == number:
            return mid + 1
        else:
            return mid
    if (mid*mid > number):
        # If mid*mid is greater than number, then we know mid isn't the floored
        # square root and the correct value is less than mid.
        return sqrt_recursive(number, start, mid - 1)
    else:
        # The floored square is less than or equal to mid. mid may still be the
        # floored square root, keep it in the next iteration.
        return sqrt_recursive(number, mid, end)

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # Needed time complexity is O(log(n)).
    # Use binary search
    # Only need to search integers up to number // 2 + 1
    return sqrt_recursive(number, 0, number//2 + 1)

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
