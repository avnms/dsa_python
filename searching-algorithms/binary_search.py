def binary_search(ordered_list, search_value):
    first = 0
    last = len(ordered_list) - 1

    while first <= last:
        middle = (first + last) // 2
        current_index_value = ordered_list[middle]
        # Check whether the search value equals the value in the middle
        if search_value == current_index_value:
            return True
        # Check whether the search value is less than the value in the middle
        elif search_value < current_index_value:
            last = middle - 1
        else:
            first = middle + 1

    return False


if __name__ == "__main__":
    print(binary_search([1, 5, 8, 9, 15, 20, 70, 72], 5))
