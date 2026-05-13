import random
import timeit


# -------------------------------
# Insertion Sort
# -------------------------------

def insertion_sort(arr):

    arr = arr.copy()

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

    return arr


# -------------------------------
# Merge Sort
# -------------------------------

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:

            result.append(left[i])

            i += 1

        else:

            result.append(right[j])

            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# -------------------------------
# Тестові дані
# -------------------------------

small_data = [random.randint(1, 1000) for _ in range(100)]
medium_data = [random.randint(1, 10000) for _ in range(1000)]
large_data = [random.randint(1, 100000) for _ in range(5000)]


# -------------------------------
# Вимірювання часу
# -------------------------------

print("\n===== SMALL DATA =====")

print(
    "Insertion Sort:",
    timeit.timeit(lambda: insertion_sort(small_data), number=10)
)

print(
    "Merge Sort:",
    timeit.timeit(lambda: merge_sort(small_data), number=10)
)

print(
    "Timsort:",
    timeit.timeit(lambda: sorted(small_data), number=10)
)


print("\n===== MEDIUM DATA =====")

print(
    "Insertion Sort:",
    timeit.timeit(lambda: insertion_sort(medium_data), number=10)
)

print(
    "Merge Sort:",
    timeit.timeit(lambda: merge_sort(medium_data), number=10)
)

print(
    "Timsort:",
    timeit.timeit(lambda: sorted(medium_data), number=10)
)


print("\n===== LARGE DATA =====")

print(
    "Insertion Sort:",
    timeit.timeit(lambda: insertion_sort(large_data), number=10)
)

print(
    "Merge Sort:",
    timeit.timeit(lambda: merge_sort(large_data), number=10)
)

print(
    "Timsort:",
    timeit.timeit(lambda: sorted(large_data), number=10)
)