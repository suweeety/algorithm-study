import sys
input = sys.stdin.readline

left_arr = list(input().strip())
right_arr = []

idx = 0
cnt = 0

for _ in range(int(input())):
    arr = input().split()
    if arr[0] == 'L' and left_arr:
        right_arr.append(left_arr.pop())
    elif arr[0] == 'D' and right_arr:
        left_arr.append(right_arr.pop())
    elif arr[0] == 'B' and left_arr:
        left_arr.pop()
    elif arr[0] == 'P':
        left_arr.append(arr[1])

print(''.join(left_arr) + ''.join(reversed(right_arr)))