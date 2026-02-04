import sys
input = sys.stdin.readline

n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
arr = [0] * (n+1)

for i in commands:
    A, B = i
    for j in range(A, B+1):
        arr[j] += 1

max_num = max(arr)
print(max_num)