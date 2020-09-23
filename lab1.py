import time
import random

# K_QUICK = 10
# K_MERGE = 12


def find_optimal_k_quick(min_value, max_value, size):
    k_quick_time_list = []
    for k_quick in list(range(3, 25)):
        numbers = [random.randint(min_value, max_value) for i in range(size)]
        print(numbers)
        t = time.time()

        quick_sort(numbers, start_num, size - 1, k_quick)

        time_of_sorting = time.time() - t
        print(f'time of sorting: {time_of_sorting}')
        k_quick_time_list.append((k_quick, time_of_sorting))

    print(k_quick_time_list)
    print(f'K_QUICK_OPTIMAL = {min(k_quick_time_list, key=lambda x: x[1])}')


def find_optimal_k_merge(min_value, max_value, size):
    k_merge_time_list = []
    for k_merge in list(range(3, 35)):
        numbers = [random.randint(min_value, max_value) for i in range(size)]
        print(numbers)
        t = time.time()
        merge_sort(numbers, k_merge)
        time_of_sorting = time.time() - t
        print(f'time of sorting: {time_of_sorting}')
        k_merge_time_list.append((k_merge, time_of_sorting))

    print(k_merge_time_list)
    print('K_MERGE_OPTIMAL = {0}, Minimal time = {1}'.format(*min(k_merge_time_list, key=lambda x: x[1])))


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


def quick_sort(array: list, left_index: int, pivot_index: int, k_quick: int):

    if pivot_index <= left_index:
        return
    if len(array) > k_quick:
        index_to_separate = find_position_to_separate_array(array, left_index, pivot_index)
        quick_sort(array, left_index, index_to_separate - 1, k_quick)
        quick_sort(array, index_to_separate + 1, pivot_index, k_quick)
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


def merge_sort(arr, k_merge):
    if len(arr) < k_merge:
        insertion_sort(arr)
    elif len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        left = merge_sort(left, k_merge)
        right = merge_sort(right, k_merge)

        arr = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                arr.append(left[0])
                left.pop(0)
            else:
                arr.append(right[0])
                right.pop(0)

        for i in left:
            arr.append(i)
        for i in right:
            arr.append(i)

    return arr


size = int(input("Enter size of the array:\n"))
max_value = int(input("Enter the max value of the array:\n"))
min_value = int(input("Enter the min value of the array:\n"))
start_num = 0

# numbers = [random.randint(1, 500000) for i in range(550000)]

# find_optimal_k_quick(min_value, max_value, size)
find_optimal_k_merge(min_value, max_value, size)
