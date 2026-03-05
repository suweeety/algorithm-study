for tc in range(1, int(input())+1):
    r_si, r_ei, r_sj, r_ej = list(map(int, input().split()))
    b_si, b_ei, b_sj, b_ej = list(map(int, input().split()))

    sum_board = [[0] * 10 for _ in range(10)]

    for i in range(r_si, r_sj+1):
        for j in range(r_ei, r_ej+1):
            sum_board[i][j] += 1

    for i in range(b_si, b_sj+1):
        for j in range(b_ei, b_ej+1):
            sum_board[i][j] += 1

    temp_arr = []
    for i in range(10):
        for j in range(10):
            if sum_board[i][j] >= 2:
                temp_arr.append((i, j))
    if not temp_arr:
        print(f'#{tc} 0 0')
    else:
        a, b = min(temp_arr)
        c, d = max(temp_arr)
        print(f'#{tc} {d-b+1} {c-a+1}')