import sys
N = int(sys.stdin.readline())

pibo = []
b = 'Messi Gimossi'
q = 5
w = 13
pibo.append(q)
pibo.append(w)

while w < 1073741824:
    e = w
    w = w + q + 1
    q = e
    pibo.append(w)

i = 0
while pibo[i] < N:
    i += 1

'''
String Order
F(M) = F(M-1) + F(M-2)
'''
while i >= 2:
    # Detect space, exit immediately
    if N == pibo[i - 1] + 1:
        N = -1
        break
    # If target is located on F(M - 2)
    elif N > pibo[i - 1]:
        # Decrease counter
        i -= 2
        # Decrease N with F(M - 1)
        N -= pibo[i + 1] + 1
    # If target is located on F(M - 1)
    else:
        i -= 1

if N == -1 or N == 6:
    print('Messi Messi Gimossi')
else:
    print(b[N - 1])


# 5 = 5
# 5 7 = 12
# 5 7 / 5 = 17  = 2 + 1
# 5 7 5 / 5 7 = 29 = 3 + 2
# 5 7 5 5 7 / 5 7 5 = 46 = 5 + 3
# 5 7 5 5 7 5 7 5 / 5 7 5 5 7 = 75 = 8 + 5
