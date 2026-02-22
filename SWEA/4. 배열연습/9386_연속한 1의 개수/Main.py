T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
 
 
    max_v = 0
    count = 0
    for i in range(0, N):
        if arr[i] == 1:
            count += 1
        elif arr[i] == 0:
            if max_v < count:
                max_v = count
            count = 0 # 초기화
    if max_v < count:
        max_v = count
 
    print(f'#{tc} {max_v}')