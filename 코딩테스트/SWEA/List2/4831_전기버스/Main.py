T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split()) # 최대한 이동할 수 있는 정류장 수 K, 종점인 N, 충전기가 설치된 정류장 M
    
    arr = [0] + list(map(int, input().split())) + [N]
    last = 0 # 마지막 충전 위치
    cnt = 0 # 충전횟수

    for i in range(1, M+2): # 종점까지 갈 수 있는지
        if arr[i] - arr[i-1] <= K: # 두 충전기 사이가 K이내
            if arr[i] - last > K: # 마지막 충전기에서 너무 멀면
                last = arr[i-1]
                cnt += 1
        else: # 두 충전기 사이가 K보다 크면 운행불가
            cnt = 0
            break

print(f'#{tc} {cnt}')