n = int(input())
data = [int(input()) for _ in range(n)]

stack = []
result = []
count = 0

for i in range(1, n+1):
    stack.append(i)
    result.append('+')

    while stack and stack[-1] == data[count]:
        stack.pop()
        result.append('-')
        count += 1
         
if count == n:
    for i in result:
         print(i)
else:
    print('NO')