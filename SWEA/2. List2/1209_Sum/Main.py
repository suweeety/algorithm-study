for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    max_v = 0

    for i in range(100):
        row_sum = 0
        col_sum = 0
        dir1_sum = 0
        dir2_sum = 0
        # 가로 구하기
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
            if i == j:
                dir1_sum += arr[i][j]
            elif i+j == 99:
                dir2_sum += arr[i][j]
        if max_v < row_sum:
            max_v = row_sum
        elif max_v < col_sum:
            max_v = col_sum
    
    if max_v < dir1_sum:
        max_v = dir1_sum
    elif max_v < dir2_sum:
        max_v = dir2_sum

    print(f'#{tc} {max_v}')