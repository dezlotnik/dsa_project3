def find_rotation_point(input_list):
    # This method uses binary search to find the rotation index. The rotation
    # index is the index for the largest value in the array. The sublist to the
    # right (exlusive) and left (inclusive) of the rotation index are sorted in
    # ascending order.
    start = 0
    end = len(input_list) - 1
    while start <= end:
        mid = start + (end - start)//2
        # Check if the next value in the array is lower than mid. If so, then
        # mid is the rotation index.
        if (input_list[mid] > input_list[mid + 1]):
            return mid
        if (input_list[mid] > input_list[-1]):
            # rotation point is to the right
            start = mid + 1
        else:
            # rotation point is to the left
            end = mid - 1
    # List is already sorted. Return last index.
    return len(input_list) - 1

def binary_search(array, target, start, end):
    # Binary search to find the target value in the array.
    while end >= start:
        mid = start + (end - start)//2
        if (array[mid] == target):
            return mid
        if (array[mid] < target):
            start = mid + 1
        else:
            end = mid - 1
    return -1

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # First, find the rotation index. This is the index with the largest value
    # in the rotated array and splits the array into two sorted lists.
    rotation_index = find_rotation_point(input_list)
    # Check if the target number is to the left or right of the rotation index.
    in_left_sublist = (input_list[0] <= number
                       and number <= input_list[rotation_index])
    if (in_left_sublist):
        # Search the left sublist from 0 to rotation index.
        return binary_search(input_list, number, 0, rotation_index)
    else:
        # Search the right sublist from rotation index + 1 to the end of the
        # list.
        return binary_search(input_list, number, rotation_index + 1, len(input_list) - 1)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
    
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[1, 2, 3, 4, 5, 6], 6])
