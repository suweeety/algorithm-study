for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
 
    max_len = 0
 
    # 1. 가로 방향 직선 구조물 찾기
    for i in range(n):
        cnt = 0
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt >= 2:  # 길이가 2 이상일 때만 구조물로 인정
                    max_len = max(max_len, cnt)
                cnt = 0
        if cnt >= 2:  # 줄이 끝났을 때 남은 cnt 체크
            max_len = max(max_len, cnt)
 
    # 2. 세로 방향 직선 구조물 찾기
    for j in range(m):
        cnt = 0
        for i in range(n):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt >= 2:
                    max_len = max(max_len, cnt)
                cnt = 0
        if cnt >= 2:
            max_len = max(max_len, cnt)
 
    print(f'#{tc} {max_len}')