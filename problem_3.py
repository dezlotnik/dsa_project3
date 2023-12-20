def divide(items):
    mid = len(items)//2
    return items[:mid], items[mid:]
    
def merge(left, right):
    left_index = 0
    right_index = 0
    merged = []
    while left_index < len(left) and right_index < len(right):
        if (left[left_index] < right[right_index]):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    # We've gone through all of left or all or right.
    # Append the remainder onto the merged list.
    # left_index = len(left) or right_index = len(right)
    merged += left[left_index:]
    merged += right[right_index:]
    return merged
    
def mergesort(items):
    # Step 1: (base case)
    if len(items) <= 1:
        return items
    
    # Step 2: divide items
    list1, list2 = divide(items)
    
    # Step 3: Merge sort
    left = mergesort(list1)
    right = mergesort(list2)
    
    return merge(left, right)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Step 1, sort the unsorted input list.
    sorted = mergesort(input_list)
    
    # Step 2, iterate through the sorted list in reverse. We need to grab the
    # largest available integer and place it at the largest available digit 
    # of the two output numbers.
    digit_idx = len(sorted) - 1
    num1 = ""
    num2 = ""
    while digit_idx >= 0:
        if (len(num1) <= len(num2)):
            # The length of the number indicates how many digits we've filled.
            # If the length of num1 is lower than num2 then num1 has a higher
            # value digit available.
            num1 += str(sorted[digit_idx])
        else:
            # num2 has the largest available digit that hasn't been set yet.
            num2 += str(sorted[digit_idx])
        digit_idx -= 1
    # Convert strings to integers and return the two numbers.
    return [int(num1), int(num2)]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1,1], [1, 1]])
