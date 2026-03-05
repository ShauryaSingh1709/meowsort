from typing import List, TypeVar

T = TypeVar("T")


def bubble_sort(data: List[T]) -> List[T]:
    arr = data.copy()
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


def quick_sort(data: List[T]) -> List[T]:
    if len(data) <= 1:
        return data.copy()

    pivot = data[len(data) // 2]

    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)