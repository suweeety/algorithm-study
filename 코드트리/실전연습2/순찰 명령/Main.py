N, K = map(int, input().split())

arr = input()

forbidden = set()

for _ in range(K):
    fx, fy = map(int, input().split())
    forbidden.add((fx, fy))

x, y = 0, 0

for i in arr:
    nx, ny = x, y

    if i == 'W':
        nx = x-1
    elif i == 'A':
        ny = y-1
    elif i == 'S':
        nx = x+1
    elif i == 'D':
        ny = y+1
    
    if 0<=nx<30000 and 0<=ny<30000:
        if (nx, ny) not in forbidden:
            x, y = nx, ny

print(x, y)