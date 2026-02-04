n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = [0] * 101

for i in segments:
    x1, x2 = i
    for j in range(x1, x2+1):
        arr[j] += 1

max_value = max(arr)
print(max_value)