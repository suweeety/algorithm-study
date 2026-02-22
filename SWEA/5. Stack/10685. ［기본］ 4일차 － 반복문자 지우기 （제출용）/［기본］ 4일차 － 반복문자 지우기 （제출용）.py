for tc in range(1, int(input())+1):
    line = input()
    stack = []
    for i in line:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] != i:
                stack.append(i)
            else:
                stack.pop()
    print(f'#{tc} {len(stack)}')