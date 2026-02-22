n, m = map(int, input().split())
arr_a = [list(map(int, input().split())) for _ in range(n)]
arr_b = [list(map(int, input().split())) for _ in range(m)]

max_v = -float('inf')

# 세로 이동 반복
for i in range(m-n+1):
    # 가로 이동 반복
    for j in range(m-n+1):
        sum_v = 0
        for r in range(n):
            for c in range(n):
                sum_v += arr_a[r][c] * arr_b[i+r][j+c]
        if max_v < sum_v:
            max_v = sum_v
print(max_v)