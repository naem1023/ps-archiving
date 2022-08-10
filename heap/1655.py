import sys, heapq

N = int(sys.stdin.readline())

left_heap = []
right_heap = []
answer = []

for i in range(N):
    input_n = int(sys.stdin.readline())

    # 대소관계 비교가 아니라, 양쪽 힙의 길이를 맞춰주기위한 단순한 작업.
    # 힙을 사용했기 때문에 자동으로 요소들 내의 정렬은 된다.

    # 두 힙의 길이가 같다면, 최대힙인 left에 요소를 추가한다.
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-input_n, input_n))
    else:
        heapq.heappush(right_heap, (input_n, input_n))

    # left의 루트가 right의 루트보다 크다 = 중간값이라고 설정한 left의 루트가 right의 루트보다 크다 = 오류
    # -> 둘을 swap해서 해결
    if right_heap and left_heap[0][1] > right_heap[0][1]:
        min_val = heapq.heappop(right_heap)[1]
        max_val = heapq.heappop(left_heap)[1]
        heapq.heappush(left_heap, (-min_val, min_val))
        heapq.heappush(right_heap, (max_val, max_val))

    answer.append(left_heap[0][1])

for a in answer:
    print(a)