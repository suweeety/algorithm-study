n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
x, y = 0, 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    if dir[i] == 'E':
        x += dx[0] * dist[i]
        y += dy[0] * dist[i]
    elif dir[i] == 'W':
        x += dx[1] * dist[i]
        y += dy[1] * dist[i]
    elif dir[i] == 'N':
        x += dx[2] * dist[i]
        y += dy[2] * dist[i]
    elif dir[i] == 'S':
        x += dx[3] * dist[i]
        y += dy[3] * dist[i]

print(x, y)