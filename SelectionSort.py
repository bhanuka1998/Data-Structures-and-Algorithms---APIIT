def insertion_sort(current_list):
    for i in range(len(current_list)):
        smallest_index = i
        for j in range(i+1, len(current_list)):
            if(current_list[smallest_index] > current_list[j]):
                smallest_index = j
        current_list[smallest_index], current_list[i] = current_list[i], current_list[smallest_index]
        print(current_list)


list_a = [2, 4, 8, 10, 1, 7, 5, 3, 9, 6]
insertion_sort(list_a)
