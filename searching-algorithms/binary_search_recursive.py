def binary_search_recursive(ordered_list, search_value):
    # Define the base case
    ordered_list_length = len(ordered_list)
    if ordered_list_length == 0:
        return False
    else:
        middle = ordered_list_length // 2
        current_index_value = ordered_list[middle]
        # Check whether the search value equals the value in the middle
        if search_value == current_index_value:
            return True
        elif search_value < current_index_value:
            # Call recursively with the left half of the list
            return binary_search_recursive(ordered_list[:middle], search_value)
        else:
            # Call recursively withthe right half of the list
            return binary_search_recursive(ordered_list[middle + 1 :], search_value)

    return False


if __name__ == "__main__":
    print(binary_search_recursive([1, 5, 8, 9, 15, 20, 70, 72], 5))
