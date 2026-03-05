for tc in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    ans = 0
    for i in range(N-1):
        for j in range(N-1):
            for k in range(i+1, N):
                for l in range(j+1, N):
                    if board[i][j] == board[k][l]:
                        temp = ((i - k) * (j - l)) * 2
                        if cnt < temp:
                            cnt = temp
                            ans = 1
                        elif cnt == temp:
                            ans += 1
                    # 만약 모든 원소의 숫자가 다르면 싸피부분배열의 면적은 1이고, 개수는 NxN개가 된다.

    if ans == 0:
        ans = N * N

    print(f'#{tc} {ans}')