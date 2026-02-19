n = int(input())
arr = list(map(int, input().split()))

dp = [999999] * n

dp[0] = 0

for i in range(n):
    if arr[i] == 0 or dp[i] == 999999:
        continue

    if i + 1 < n and arr[i + 1] == 1:
        if dp[i + 1] > dp[i] + 1:
            dp[i + 1] = dp[i] + 1
            
    if i + 3 < n and arr[i + 3] == 1:
        if dp[i + 3] > dp[i] + 1:
            dp[i + 3] = dp[i] + 1

if dp[n - 1] == 999999:
    print(-1)
else:
    print(dp[n - 1])