for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    sum_v = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                r = i + dx[k]
                c = j + dy[k]
                if 0 <= r < N and 0 <= c < N:
                    sum_v += abs(arr[i][j] - arr[r][c])
    print(f'#{tc} {sum_v}')