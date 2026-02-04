# 테스트 케이스
T = int(input())
 
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N * N 배열 입력
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0 # 파리채 내부 합
            for r in range(M):
                for c in range(M):
                    s += arr[i+r][j+c]
 
            if max < s:
                max = s
 
    print(f'#{tc} {max}')