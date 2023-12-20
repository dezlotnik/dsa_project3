def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    out_list = input_list
    next_two_index = len(out_list) - 1
    next_zero_index = 0
    curr_index = 0
    while curr_index <= next_two_index:
        # Stop iterating when the current index passes the next expected
        # placement of a two. In that case, all the remaining elements should
        # already be 2, and don't need to be sorted.
        if (out_list[curr_index] == 2):
            # If the value at the current index is a two, swap the current 2
            # value with the value at the next two spot. Then, decrement
            # next_two_index.
            out_list[curr_index] = input_list[next_two_index]
            out_list[next_two_index] = 2
            next_two_index -= 1
        elif (out_list[curr_index] == 0):
            # If the value at the current index is a zero, swap the current 0
            # value with the value at the next zero spot. Then, decrement
            # next_zero_index. We also need to increment the current index. 
            out_list[curr_index] = input_list[next_zero_index]
            out_list[next_zero_index] = 0
            next_zero_index += 1
            curr_index += 1
        else:
            # Value is a one. Leave it and move on.
            curr_index += 1
    return out_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Test Cases
# Nominal Test case
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Edge case 1:
# Already sorted
test_function([0, 1, 1, 1, 1, 2])

# Edge case 2:
# No 1s
test_function([2, 0])

# Edge case 3:
# Single number
test_function([0])
