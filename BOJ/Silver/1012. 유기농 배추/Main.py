from collections import deque

def bfs(si, sj):
    queue = deque()
    queue.append((si, sj))
    green[si][sj] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            r = x + dx[i]
            c = y + dy[i]
            if 0<=r<n and 0<=c<m:
                if green[r][c] == 1:
                    queue.append((r, c))
                    green[r][c] = 0

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    m, n, k = map(int, input().split())
    green = [[0] * m for _ in range(n)]
    cnt = 0

    for i in range(k):
        y, x = map(int, input().split())
        green[x][y] = 1

    for i in range(n):
        for j in range(m):
            if green[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)