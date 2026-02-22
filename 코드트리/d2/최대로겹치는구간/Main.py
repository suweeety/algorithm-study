n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# offset을 100으로 잡기
arr = [0] * 201

for i in segments:
    x1, x2 = i
    for j in range(x1+101, x2+101):
        arr[j] += 1

max_value = max(arr)
print(max_value)