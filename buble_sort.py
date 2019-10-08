def bubble_sort(current_list):
    for s in range(len(current_list)):
        for i in range(len(current_list) - 1):
            if current_list[i] > current_list[i+1]:
                current_list[i], current_list[i+1] = current_list[i+1], current_list[i]
            print(i)
            print(current_list)

    print("Sorted list is", current_list)


list_1 = [1, 3, 4, 6, 5, 7, 8, 2, 10, 9]
list_2 = [23, 22, 26, 28, 30, 24, 27, 21, 25, 29]
bubble_sort(list_1)
bubble_sort(list_2)
