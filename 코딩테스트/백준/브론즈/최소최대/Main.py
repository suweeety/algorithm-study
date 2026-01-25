import sys

# 로직 이해용
n = sys.stdin.readline()

numbers = list(map(int, sys.stdin.readline().split()))

min = numbers[0]
max = numbers[0]

for num in numbers:
    if num < min:
        min = num
    elif num > max:
        max = num

# min, max 사용
# min = min(numbers)
# max = max(numbers)

print(min, max)