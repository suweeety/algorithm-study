import sys

input = sys.stdin.readline
n = int(input())
n_list = [int(input()) for _ in range(n)]

# 산술평균
avg = round(sum(n_list) / n)
print(avg)

# 중앙값
n_list.sort()
print(n_list[n // 2])

# 최빈값
counts = {}
for i in n_list:
    counts[i] = counts.get(i, 0) + 1

max_v = 0
for i in counts.values():
    if i > max_v:
        max_v = i

max_list = []
for i in counts:
    if counts[i] == max_v:
        max_list.append(i)

if len(max_list) > 1:
    print(max_list[1])
else:
    print(max_list[0])

# 범위
print(n_list[-1] - n_list[0])