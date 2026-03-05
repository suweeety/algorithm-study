# 입력받은 긴 16진수 문자열을 한 글자씩 4자리 2진수로 변환
for tc in range(1, int(input()) + 1):
    N = int(input())
    hex_str = input().strip()

    bin_str = ""
    for char in hex_str:
        # 1. 문자를 10진수 정수로 변환 (ex. B -> 11)
        decimal_val = int(char, 16)
        # 2. 10진수를 2진수 문자열로 변환하고 앞에 0b를 제거 (ex. 11 -> '1011')
        binary_val = bin(decimal_val)[2:]
        # 3. 무조건 4자리를 맞추기 위해 빈자리는 0으로 채움 (예: '0' -> '0000')
        binary_val = binary_val.zfill(4)

        bin_str += binary_val # 완성된 4자리 2진수를 붙이기

    # 7자리씩(7-bit) 자르기
    res = []

    for i in range(0, len(bin_str), 7):
        chunk = bin_str[i : i + 7]

        # 마지막에 7-bit를 채울 수 없는 경우의 비트는 버린다
        if len(chunk) == 7:
            # 2진수 -> 10진수로 변환
            decimal_chunk = int(chunk, 2)
            res.append(str(decimal_chunk))

    print(f"#{tc} {' '.join(res)}")