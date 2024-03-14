def binary_search(input_list, item):
    """
    Search and return the index of the target item in the given input list

    Args:
        input_list (list): A sorted list
        item (integer): An integer

    Returns:
        index (integer): Index of item in the input_list

    Examples:
        >>> binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
        Returns '7'

        >>> binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -12)
        Returns 'None'
    """
    low = 0
    high = len(input_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = input_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(test_list, 8))
    print(binary_search(test_list, -12))
