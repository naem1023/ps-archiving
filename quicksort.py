def partition(array, start, end):
    if start >= end:
        return start
    else:
        pivot = start
        for idx in range(start + 1, end + 1):
            if array[idx] <= array[start]:
                pivot += 1
                array[idx], array[pivot] = array[pivot], array[idx]
        array[start], array[pivot] = array[pivot], array[start]
        return pivot

def quicksort(array):
    def _quicksort(array, start, end):
        if start >= end:
            return
        else:
            pivot = partition(array, start, end)
            _quicksort(array, start, pivot - 1)
            _quicksort(array, pivot + 1, end)
    return _quicksort(array, 0, len(array) - 1)

import random
a = [random.randrange(1, 100) for _ in range(20)]

print(a)
quicksort(a)
print(a)

