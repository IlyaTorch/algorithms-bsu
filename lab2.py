import random

count_binary_search_operations = 0
count_interpolate_search_operations = 0


def binary_search(arr, left_boundary, right_boundary, value):
    global count_binary_search_operations

    if left_boundary <= right_boundary and arr[left_boundary] <= value <= arr[right_boundary]:
        middle = (right_boundary + left_boundary) // 2

        count_binary_search_operations += 1
        if arr[middle] == value:
            return middle

        elif arr[middle] > value:
            return binary_search(arr, left_boundary, middle - 1, value)
        else:
            return binary_search(arr, middle + 1, right_boundary, value)

    else:
        return None


def interpolation_search(arr, value):
    global count_interpolate_search_operations

    left_boundary = 0
    right_boundary = len(arr) - 1

    while left_boundary <= right_boundary and arr[left_boundary] <= value <= arr[right_boundary]:
        if left_boundary == right_boundary:

            count_interpolate_search_operations += 1
            if arr[left_boundary] == value:
                return left_boundary
            return None

        interpolate_coefficient = (value - arr[left_boundary]) / (arr[right_boundary] - arr[left_boundary])
        position = left_boundary + int(interpolate_coefficient * (right_boundary - left_boundary))

        count_interpolate_search_operations += 1
        if arr[position] == value:
            return position

        if value >  arr[position]:
            left_boundary = position + 1
        else:
            right_boundary = position - 1

    return None


if __name__ == '__main__':
    element_to_find = int(input('Enter an element to search '))
    MAX_ELEMENT_IN_ARRAY = int(input('Enter the max element of an array '))
    ARRAY_LENGTH = int(input('Enter the length of an array '))
    array = [random.randint(0, MAX_ELEMENT_IN_ARRAY) for i in range(ARRAY_LENGTH)]
    array.sort()

    binary_search_result = binary_search(array, 0, len(array) - 1, element_to_find)
    interpolate_search_result = interpolation_search(array, element_to_find)

    print(array)
    print('Binary search:')
    if binary_search_result is not None:
        print('Element is present at index ', str(binary_search_result))
    else:
        print('Element is not present in array')
    print('Number of operations in binary search = ', count_binary_search_operations)
    print()
    print('Interpolate search:')
    if binary_search_result is not None:
        print('Element is present at index ', str(interpolate_search_result))
    else:
        print('Element is not present in array')
    print('Number of operations in interpolate search = ', count_interpolate_search_operations)
