n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
min_sum = []
for i in range(n):
    sum_diff = 0
    for j in range(n):
        sum_diff += arr[j] * abs(i - j)

    min_sum.append(sum_diff)

print(min(min_sum))