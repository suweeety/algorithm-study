for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
 
    max_v = 0
     
    # 행 한줄씩 계산
    for row in arr:
        s = sum(row)
        if max_v < s:
            max_v = s
    same1 = 0
    same2 = 0
    for j in range(100):
        col_some = 0
        # 열 한줄씩 계산
        for i in range(100):
            col_some += arr[i][j]
            # 대각선(->) 계산
            if i == j:
                same1 += arr[i][j]
            # 대각선(<-) 계산
            if 99 == (i+j):
                same2 += arr[i][j]
        if max_v < col_some:
            max_v = col_some
    # 모든 루프가 끝난 후 대각선 최댓값 최종 비교
    if max_v < same1:
        max_v = same1
    if max_v < same2:
        max_v = same2
 
    print(f'#{tc} {max_v}')