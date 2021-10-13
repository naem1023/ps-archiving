import sys

V, E = list(map(int, sys.stdin.readline().strip().split() ))

G = [ list(map(int, sys.stdin.readline().strip().split() )) for _ in range(E)]

print(G)