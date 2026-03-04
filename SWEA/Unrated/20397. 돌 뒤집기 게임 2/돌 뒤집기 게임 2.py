for tc in range(1, int(input())+1):
    # 돌의 수 N, 뒤집기 횟수 M
    n, m = map(int, input().split())
    # N개 돌의 초기상태
    stone = list(map(int, input().split()))
    # M개의 줄에 걸쳐 i, j가 주어진다.
    for _ in range(m):
        i, j = map(int, input().split())
        for k in range(1, j+1):
            l = (i-1) - k
            r = (i-1) + k
            if 0<=l<n and 0<=r<n:
                if stone[l] == stone[r]:
                    if stone[l] == 1:
                        stone[l], stone[r] = 0, 0
                    elif stone[l] == 0:
                        stone[l], stone[r] = 1, 1
            else:
                break

    print(f'#{tc}', *stone)