from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

def bfs(x, y):
    # 초기값 넣어주기
    queue = deque()
    queue.append((x, y))
    
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            r = x + dx[i]
            c = y + dy[i]
            if 0<=r<n and 0<=c<m:
                if maze[r][c] == 1:
                    maze[r][c] = maze[x][y] + 1
                    queue.append((r, c))
    return maze[n-1][m-1]

print(bfs(0, 0))