for tc in range(1, 11):
    n = int(input())
    line = input()

    stack = []
    new_line = ''

    for token in line:
        # 피연산자면 붙여
        if token not in '+*':
            new_line += token
        # 연산자면
        else:
            # 스택이 있으면
            if token == '*':
                # 곱센은 나보다 우선순위가 낮은 +는 건들지 않고
                # 같은 *이 있을때만 꺼내서 출력
                while stack and stack[-1] == '*':
                    new_line += stack.pop()
                stack.append(token)
            elif token == '+':
                # 덧셈은 나보다 우선순위 높거나 같은 *,+ 모두 꺼냄
                while stack:
                    new_line += stack.pop()
                stack.append(token)
    while stack:
        new_line += stack.pop()

    for char in new_line:
        if char not in '*+':
            stack.append(int(char))
        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            result = 0
            if char == '+':
                result = num1 + num2
            elif char == '*':
                result = num1 * num2
            stack.append(result)

    print(f'#{tc} {stack.pop()}')
