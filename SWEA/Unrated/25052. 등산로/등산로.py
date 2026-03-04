for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_v = 0 # 등산로 총개수

    for i in range(n):
        for j in range(n):
            si, sj, cnt = i, j, 1
            while True:
                temp = []
                dx = [-1, 1, 0, 0]
                dy = [0, 0, -1, 1]
                for k in range(4):
                    r = si + dx[k]
                    c = sj + dy[k]
                    # 주변에 작은게 있으면 넣어.
                    if 0 <= r < n and 0 <= c < n and arr[si][sj] > arr[r][c]:
                        temp.append((arr[r][c], r, c))
                if not temp:
                    break
                _, si, sj = min(temp)
                cnt += 1

            if cnt > max_v:
                max_v = cnt
    print(f'#{tc} {max_v}')