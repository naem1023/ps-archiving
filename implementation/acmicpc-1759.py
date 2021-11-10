import sys


L, C = list(map(int, sys.stdin.readline().split()))

char_list = sys.stdin.readline().split()

from itertools import combinations

char_list.sort()

answer = list(combinations(char_list, L))
answer = list(map(lambda x: ''.join(x), answer))

m = ['a', 'e', 'i', 'o', 'u']
for a in answer:
    m_count = 0
    j_count = 0
    
    for c in a:
        if c in m:
            m_count += 1
        else:
            j_count += 1
    
    if m_count >= 1 and j_count >= 2:
        print(a)