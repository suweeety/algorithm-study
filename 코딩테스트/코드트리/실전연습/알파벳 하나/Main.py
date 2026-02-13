N = int(input())
arr = {}

max_v = 0
max_char = ''
# 알파벳 개수 세기
for i in range(N):
    line = input()
    for char in line:
        if char in arr:
            arr[char] += 1
        else:
            arr[char] = 1
# print(arr)
for i in sorted(arr.keys()):
    if arr[i] > max_v:
        max_v = arr[i]
        max_char = i

result = (N * N) - max_v
print(result, max_char)