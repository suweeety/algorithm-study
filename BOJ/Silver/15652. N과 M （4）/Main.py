import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = []

def dfs():
    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(1, n+1):
        if len(ans) == 0:
            ans.append(i)
            dfs()
            ans.pop()
        else:
            if i >= ans[-1]:
                ans.append(i)
                dfs()
                ans.pop()

dfs()