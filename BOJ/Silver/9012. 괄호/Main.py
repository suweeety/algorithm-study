n = int(input())
stack = []
status = False
for k in range(n):
    stack.clear()
    arr = input()
    for i in arr:
        if i == '(':
            stack.append(i)
        else:
            if '(' in stack:
                stack.pop()
            else:
                status = False
                stack.append(i)
                continue
    if stack:
        status = False
    else:
        status = True
    if status:
        print('YES')
    else:
        print('NO')