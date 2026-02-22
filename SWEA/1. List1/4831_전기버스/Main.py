for tc in range(1, int(input())+1):
    k, n, m = map(int, input().split())
    chargers = list(map(int, input().split()))
    
    bus_stop = [0] * (n+1)
    
    for i in chargers:
        bus_stop[i] += 1
    
    start = 0 # 현재 버스 위치
    cnt = 0 # 충전 횟수

    while start + k < n:
        for i in range(k, 0, -1):
            if bus_stop[start + i] == 1:
                start = i
                cnt += 1
                break
            else:
                count = 0
                break
    
    print(f'#{tc} {cnt}')