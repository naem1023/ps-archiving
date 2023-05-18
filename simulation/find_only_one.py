"""
배열에서 중복되지 않는 요소 찾기
- 중복되지 않는 요소들 외에는 모두 2개씩 있음.
"""

def find_one(arr):
    arr.sort()
    for i in range(0, len(arr), 2):
        if arr[i] != arr[i + 1]:
            return arr[i]
        

            