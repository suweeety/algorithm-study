for tc in range(1, int(input())+1):

    N = int(input())
    n = N // 10

    # dp배열 초기화(n이 1인 경우를 대비해 여유있게)
    dp = [0] * (n + 2)

    # 초기값 설정
    dp[1] = 1
    dp[2] = 3

    # 점화식
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + 2 * dp[i-2])

    print(f'#{tc} {dp[n]}')