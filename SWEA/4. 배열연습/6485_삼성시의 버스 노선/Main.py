T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    P = int(input())
    arr_bus = []
    for _ in range(P):
        arr_bus.append(int(input()))
 
    bus = [0] * 5001
    for i in range(N):
        for j in range(arr[i][0], arr[i][1] + 1):
            bus[j] += 1
 
    print(f'#{tc}', end=' ')
    for stop_num in arr_bus:
        # arr_bus에 들어있는 정류장 번호의 카운트만 순서대로 출력
        print(bus[stop_num], end=' ')
    print()  # 다음 테스트 케이스를 위해 줄바꿈