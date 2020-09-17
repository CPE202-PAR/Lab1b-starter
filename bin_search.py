# CPE 202 Lab 1b

# Python List, number -> number or None
def bin_search_iter(int_list, target):  # Binary Search using iteration
    """ searches for target in int_list and returns associated index if found, otherwise returns None
        int_list must be in ascending order for Binary Search to return proper result
        if int_list is None, raise ValueError"""
    if int_list is None:
        raise ValueError
    low = 0
    high = len(int_list) - 1
    while low < high:
        mid = (high + low) // 2
        if int_list[mid] < target:  # If mid value is less than target, ignore left half
            low = mid + 1
        elif int_list[mid] > target:  # If mid value is greater than target, ignore right half
            high = mid - 1
        else:  # mid value must equal target
            return mid
    # If we reach here, target not present
    return None

# Python List, number -> number or None
def bin_search_rec(int_list, target):   # Binary Search using recursion
    """ searches for target in int_list and returns associated index if found, otherwise returns None
        int_list must be in ascending order for Binary Search to return proper result
        if int_list is None, raise ValueError"""
    if int_list is None:
        raise ValueError
    return bin_search_rec_helper(int_list, target, 0, len(int_list)-1)

# Python List, number, number, number -> number or None
def bin_search_rec_helper(int_list, target, low, high):  # Recursive helper function
    """ searches for target in int_list[low..high] and returns index if found"""

