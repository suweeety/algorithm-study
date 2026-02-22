# 십자와 대각선 방향을 정의 (상수화)
cross_dirs = [(0,-1), (1,0), (0,1), (-1,0)]
diag_dirs = [(-1,-1), (-1,1), (1,-1), (1,1)]
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    def get_sum(i, j, dirs):
        # 중앙값 초기화
        total = arr[i][j]
        for di, dj in dirs:
            for dist in range(1, M):
                ni, nj = i + di * dist, j + dj * dist
                # 유효성 검사(범위 초과되지 않도록)
                if 0<=ni<N and 0<=nj<N:
                    total += arr[ni][nj]
                else:
                    break # 범위 벗어나면 해당 방향 중단
        return total

    for i in range(N):
        for j in range(N):
            # 두가지 패턴 중 최대값 찾기
            answer = max(answer, get_sum(i, j, cross_dirs), get_sum(i, j, diag_dirs))
    
    print(f'#{tc} {answer}')