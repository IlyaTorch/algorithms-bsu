import time
import random

K = 8


def find_position_to_separate_array(array: list, left_index: int, pivot_index: int):
    right_index = pivot_index - 1

    while True:
        while array[left_index] < array[pivot_index]:
            left_index += 1
        while array[right_index] > array[pivot_index] and right_index > 0:
            right_index -= 1

        if left_index >= right_index:
            break
        else:
            array[left_index], array[right_index] = array[right_index], array[left_index]
            left_index += 1
            right_index -= 1

    array[left_index], array[pivot_index] = array[pivot_index], array[left_index]
    return left_index


def quick_sort(array: list, left_index: int, pivot_index: int):

    if pivot_index <= left_index:
        return
    if len(array) > K:
        index_to_separate = find_position_to_separate_array(array, left_index, pivot_index)
        quick_sort(array, left_index, index_to_separate - 1)
        quick_sort(array, index_to_separate + 1, pivot_index)
    else:
        insertion_sort(array)


def insertion_sort(array: list):
    for i in range(1, len(array)):
        item = array[i]
        j = i - 1
        while item < array[j] and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = item


size = int(input("Enter size of the array:\n"))
max_value = int(input("Enter the max value of the array:\n"))
min_value = int(input("Enter the min value of the array:\n"))
numbers = [random.randint(min_value, max_value) for i in range(size)]
# numbers = [random.randint(1, 500000) for i in range(550000)]

sorted_numbers = numbers.copy()
sorted_numbers.sort()

print(numbers)

t = time.time()
# quick_sort(numbers, 0, 549999)
quick_sort(numbers, 0, size - 1)
print(sorted_numbers)
print()
print(f'time of sorting: {time.time() - t}')
print(sorted_numbers == numbers)
