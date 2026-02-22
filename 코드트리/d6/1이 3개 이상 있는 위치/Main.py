n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0

for i in range(n):
    for j in range(n):
        count = 0
        
        # 현재 칸 (i, j)의 인접한 4방향을 확인
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]

            if 0<=ni<n and 0<=nj<n:
                if arr[ni][nj] == 1:
                    count += 1

        if count >= 3:
            ans += 1
print(ans)