import sys
N = int(input())
arr = [int(sys.stdin.readline()) for _ in range(N)]
sys.setrecursionlimit(10**5)
# arr.sort()

def partition(arr, left, right):
    pivot = arr[left]
    left_idx = left
    right_idx = right
    
    while left_idx < right_idx:
        while pivot < arr[right_idx]:
           right_idx -= 1

        while left_idx < right_idx and pivot >= arr[left_idx]:
           left_idx += 1

        temp = arr[left_idx]
        arr[left_idx] = arr[right_idx]
        arr[right_idx] = temp

    arr[left] = arr[left_idx]
    arr[left_idx] = pivot

    return left_idx


def quicksort(arr, left, right):
    if left >= right:
        return
    pivot = partition(arr, left, right)
    quicksort(arr, left, pivot - 1)
    quicksort(arr, pivot + 1, right)

quicksort(arr, 0, len(arr) - 1)

for i in arr:
    sys.stdout.write(str(i)+'\n')