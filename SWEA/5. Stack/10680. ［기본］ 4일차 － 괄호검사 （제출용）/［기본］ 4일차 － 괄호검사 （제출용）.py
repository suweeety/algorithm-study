def check(line):
    mapping = {
        ')':'(',
        '}':'{'
    }
    stack = []

    for char in line:
        if char in mapping.values():
            stack.append(char)

        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return 0
    # 모든 검사 후 스택이 비어있어야 정상. 남아있으면 비정상
    return 1 if not stack else 0

for tc in range(1, int(input())+1):
    line = input()
    print(f'#{tc} {check(line)}')