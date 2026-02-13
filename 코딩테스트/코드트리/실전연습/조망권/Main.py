n, m = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
# i가 현재 내 위치. 앞뒤로 k개씩 공간이 있어야 함

for i in range(n):
    view = True
    for k in range(1, m+1):
        if 0 <= (i-k) < n:
            if arr[i] < arr[i-k]:
                view = False
                break
        if 0 <= (i+k) < n:
            if arr[i] < arr[i+k]:
                view = False
                break
    if view:
        count += 1

print(count)