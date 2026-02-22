import sys

input = sys.stdin.readline

N, K = map(int, input().split())


# factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# K * (N-K) // N
print(factorial(N) // (factorial(K) * factorial(N-K)))