for tc in range(1, int(input())+1):
    binary_str = input().strip()

    ans = []

    for i in range(0, 70, 7):
        chunk = binary_str[i : i + 7]
        num = int(chunk, 2)
        ans.append(num)

    print(f'#{tc}', *ans)