"""
배열에서 중복되지 않는 요소들 찾기

i = 2
j = 5
[1, 2, 2, 3, 3, 4]
[1, 2, 4, 2, 3, 4]

"""
def count(arr):
    arr.sort()
    
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1

            # 이전에 다르다고 판단된 값을 저장하기 위한 용도.
            arr[i] = arr[j]

    return i