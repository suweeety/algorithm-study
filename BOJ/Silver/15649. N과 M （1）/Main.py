import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * (n + 1)
ans = []

def dfs():
    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(1, n+1):
        if i not in ans:
            ans.append(i)      
            dfs()
            ans.pop()
dfs()