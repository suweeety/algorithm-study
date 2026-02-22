n, m = map(int, input().split())

board = []

for _ in range(n):
    board.append(input())

cnts = []

# 범위 초과하지 않게
for i in range(n-7):
    for j in range(m-7):
        w = 0
        b = 0
        # 전체 탐색
        for row in range(i, i+8):
            for col in range(j, j+8):
                if (row + col) % 2 == 0:
                    if board[row][col] != 'B':
                        b += 1
                    if board[row][col] != 'W':
                        w += 1
                else:
                    if board[row][col] != 'W':
                        b += 1
                    if board[row][col] != 'B':
                        w += 1
        cnts.append(w)
        cnts.append(b)

print(min(cnts))