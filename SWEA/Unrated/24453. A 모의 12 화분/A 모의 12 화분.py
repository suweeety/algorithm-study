for tc in range(1, int(input())+1):
    n, p = map(int, input().split())
    ai = list(map(int, input().split()))
    bi = list(map(int, input().split()))
 
    dp = [[0,0] for _ in range(n)]
 
    # 첫째날
    dp[0][0] = ai[0] # a 선택
    dp[0][1] = bi[0] # b 선택
    
    for i in range(1, n):
        #(i+1)번째 날 a선택
        dp[i][0] = max(dp[i-1][0] + ai[i] - p, dp[i-1][1] + ai[i])
        #(i+1)번째 날 b 선택
        dp[i][1] = max(dp[i-1][1] + bi[i] - p, dp[i-1][0] + bi[i])
 
    print(f"#{tc} {max(dp[n-1])}")