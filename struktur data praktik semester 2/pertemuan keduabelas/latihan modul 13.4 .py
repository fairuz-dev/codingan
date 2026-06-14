# DESCENDING MERGE SORT DAN QUICK SORT

# =========================
# MERGE SORT DESCENDING
# =========================

def descend_merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list

    mid = len(my_list) // 2

    left = descend_merge_sort(my_list[:mid])
    right = descend_merge_sort(my_list[mid:])

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# =========================
# QUICK SORT DESCENDING
# =========================

def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot_desc(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] > my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)

    swap(my_list, pivot_index, swap_index)

    return swap_index


def quick_sort_helper_desc(my_list, left, right):
    if left < right:
        pivot_index = pivot_desc(my_list, left, right)

        quick_sort_helper_desc(my_list, left, pivot_index - 1)
        quick_sort_helper_desc(my_list, pivot_index + 1, right)

    return my_list


def descend_quick_sort(my_list):
    return quick_sort_helper_desc(my_list, 0, len(my_list) - 1)

data1 = [4, 6, 1, 7, 3, 2, 5]
data2 = [4, 6, 1, 7, 3, 2, 5]

hasil_merge = descend_merge_sort(data1)

descend_quick_sort(data2)

print("Hasil Descending Merge Sort =", hasil_merge)
print("Hasil Descending Quick Sort =", data2)