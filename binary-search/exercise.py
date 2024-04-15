def binary_search_steps_counter(input_list, item):
    """
    Return the number of steps it takes to search the target item in the given input list

    Args:
        input_list (list): A sorted list
        item (integer): An integer

    Returns:
        steps_counter (integer): Maximum number of search steps

    Examples:
        >>> test_list_1 = [i + 1 for i in range(128)]
        >>> binary_search_steps_counter(test_list_1, 128)
        Returns 'The maximum number of steps to search for an item in a list of 128 values is: 8'

        >>> test_list_2 = [i + 1 for i in range(256)]
        >>> binary_search_steps_counter(test_list_2, 256)
        Returns 'The maximum number of steps to search for an item in a list of 256 values is: 9'
    """
    steps_counter = 0
    low = 0
    high = len(input_list) - 1

    while low <= high:
        steps_counter += 1
        mid = (low + high) // 2
        guess = input_list[mid]
        if guess == item:
            return steps_counter
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


# 1
# What's the maximum number of steps it would take to search
# the target item in a sorted list containing 128 values
test_list_1 = [i + 1 for i in range(128)]
result_1 = binary_search_steps_counter(test_list_1, 128)
print(
    f"The maximum number of steps to search for an item in a list of {len(test_list_1)} values is: {result_1}"
)


# 2
# What's the maximum number of steps it would take to search
# the target item in a sorted list containing 256 values
test_list_2 = [i + 1 for i in range(256)]
result_2 = binary_search_steps_counter(test_list_2, 256)
print(
    f"The maximum number of steps to search for an item in a list of {len(test_list_2)} values is: {result_2}"
)
