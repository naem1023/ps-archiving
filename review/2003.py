import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

sub_sum = arr[0]

start, end = 0, 0
count = 0

while True:
    if sub_sum < M:
        # end를 늘려서 수를 늘린다
        end += 1
        if end == N:
            break
        sub_sum += arr[end]
    elif sub_sum == M:
        # 답
        count += 1
        # sub_sum -= arr[start]
        # start += 1
        # start, end 중 뭘 늘리든 상관없다.
        # 인덱스 검사, 값 증감만 잘 신경쓰자.
        end += 1
        if end >= N:
            break
        sub_sum += arr[end]
    else:
        # start를 늘려서 수를 줄인다
        sub_sum -= arr[start]
        start += 1
    
print(count)