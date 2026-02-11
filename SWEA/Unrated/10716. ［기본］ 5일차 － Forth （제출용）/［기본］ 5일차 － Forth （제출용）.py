for tc in range(1, int(input())+1):
    line = list(map(str, input().split()))
    stack = []
    error = False
    result = 0
    for token in line:
        if token == '.':
            if len(stack) == 1:
                print(f'#{tc} {stack.pop()}')
            else:
                print(f'#{tc} error')
            break

        elif token not in '*/+-':
            stack.append(int(token))
        else:
            if len(stack) < 2:
                error = True
                break

            num2 = stack.pop()
            num1 = stack.pop()
            result = 0
            if token == '+':
                result = num1 + num2
            elif token == '-':
                result = num1 - num2
            elif token == '*':
                result = num1 * num2
            elif token == '/':
                result = int(num1 / num2)
            stack.append(result)

    if error:
        print(f'#{tc} error')