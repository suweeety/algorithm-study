N, M = map(int, input().split())

l = int(input())
str_v = input()

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

x, y = 0, 0
temp = M

temp -= arr[x][y]
result = True

for s in str_v:
    if temp <= 0:
        result = False
        break

    nx, ny = x, y
    if s == 'U':
        nx = x-1
    elif s == 'L':
        ny = y-1
    elif s == 'R':
        ny = y+1
    elif s == 'D':
        nx = x+1
    
    if 0<=nx<N and 0<=ny<N:
        temp -= arr[nx][ny]
        x, y = nx, ny
if result and temp > 0:
    print('Y')
else:
    print('N')
print(x + 1, y + 1)