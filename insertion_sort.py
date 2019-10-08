def insertion_sort(current_list):
    for i in range(len(current_list) - 1):
        j = i+1
        while(j > 0) and (current_list[j] < current_list[j-1]):
            current_list[j], current_list[j-1] = current_list[j-1], current_list[j]
            j -= 1
    print(current_list)


list_a = [2, 4, 8, 10, 1, 7, 5, 3, 9, 6]
list_b = [12, 14, 18, 20, 11, 17, 15, 13, 19, 16]
list_c = [22, 24, 28, 30, 21, 27, 25, 23, 29, 26]
insertion_sort(list_a)
insertion_sort(list_b)
insertion_sort(list_c)
