import random

def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def partition_random(my_list, left, right):

    random_index = random.randint(left, right)
    swap(my_list, random_index, right)

    pivot = my_list[right]

    i = left - 1

    for j in range(left, right):

        if my_list[j] <= pivot:
            i += 1
            swap(my_list, i, j)

    swap(my_list, i + 1, right)

    return i + 1


def quick_sort_random_helper(my_list, left, right):

    if left < right:

        pivot_index = partition_random(my_list, left, right)

        quick_sort_random_helper(my_list, left, pivot_index - 1)

        quick_sort_random_helper(my_list, pivot_index + 1, right)

    return my_list


def random_quick_sort(my_list):

    quick_sort_random_helper(my_list, 0, len(my_list) - 1)


data = [4, 6, 1, 7, 3, 2, 5]

random_quick_sort(data)

print(data)