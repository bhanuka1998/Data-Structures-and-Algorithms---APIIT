def mergesort(list):
    if len(list) > 1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        mergesort(left)
        mergesort(right)
        i = j = k = 0
        while (len(left) > i) and (len(right) > j):
            if left[i] > right[j]:
                list[k] = right[j]
                j += 1
                k += 1
            else:
                list[k] = left[i]
                i += 1
                k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
    return list


list_1 = [2, 6, 8, 1, 3, 5, 7, 4, 9]
print(mergesort(list_1))