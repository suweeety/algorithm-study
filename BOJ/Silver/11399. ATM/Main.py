n = int(input())
arr = list(map(int, input().split()))

arr.sort()

total = 0
sum_time = 0

for i in arr:
    sum_time += i
    total += sum_time

print(total)