def selection_sort(my_list: list):
    list_length = len(my_list)

    for i in range(list_length - 1):
        # Set lowest to the element located at the index i
        lowest = my_list[i]
        index = i
        # Iterate again starting at the next position of i
        for j in range(i + 1, list_length):
            # Compare if the element located at index j is smaller than lowest
            if my_list[j] < lowest:
                lowest = my_list[j]
                index = j
        my_list[i], my_list[index] = my_list[index], my_list[i]

    return my_list


if __name__ == "__main__":
    my_list = [6, 2, 9, 7, 4, 8]
    selection_sort(my_list)
    print(my_list)
