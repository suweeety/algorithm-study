arr = input()
cnt = 0
total_cnt = 0

for i in range(len(arr)):
    if arr[i] == '(':
        cnt += 1
    else:
        cnt -= 1
        if arr[i-1] == '(':
            total_cnt += cnt
        else:
            total_cnt += 1

print(total_cnt)