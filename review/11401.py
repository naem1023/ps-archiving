N, K = map(int, input().split())
p = 1000000007

def factorial(n):
    e = 1
    for i in range(1, n + 1):
        e = (e * i) % p
    return e

def square(n, k):
    if k == 1:
        return n
    elif k == 0:
        return 1
    
    tmp = square(n, k // 2)
    if k % 2:
        return tmp * tmp * n % p
    else:
        return tmp * tmp % p


top = factorial(N)
bot = square(factorial(N - K) * factorial(K) % p , p - 2)

print(top * bot % p)