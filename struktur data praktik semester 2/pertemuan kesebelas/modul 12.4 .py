# Bubble Sort
def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):

            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp

    return my_list


# Selection Sort
def selection_sort(my_list):
    for i in range(len(my_list) - 1):

        min_index = i

        for j in range(i + 1, len(my_list)):

            if my_list[j] < my_list[min_index]:
                min_index = j

        if i != min_index:
            temp = my_list[min_index]
            my_list[min_index] = my_list[i]
            my_list[i] = temp

    return my_list


# Insertion Sort
def insertion_sort(my_list):

    for i in range(1, len(my_list)):

        temp = my_list[i]
        j = i - 1

        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1

    return my_list


# Menampilkan hasil
print("Sebelum diurutkan :", [15, 9, 27, 4, 18, 11])

print()

print("Bubble Sort")
print(bubble_sort([15, 9, 27, 4, 18, 11]))

print()

print("Selection Sort")
print(selection_sort([15, 9, 27, 4, 18, 11]))

print()

print("Insertion Sort")
print(insertion_sort([15, 9, 27, 4, 18, 11]))
