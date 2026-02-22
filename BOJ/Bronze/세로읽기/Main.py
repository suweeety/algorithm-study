# 총 다섯줄의 입력이 주어진다. 각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸 없이 연속으로 주어진다.
lines = []

for i in range(5):
    lines.append(input())

for i in range(15):
    for j in range(5):
        if i < len(lines[j]):
            # 출력 후 마지막 문자 지정
            print(lines[j][i], end="")

# print(lines)

# lines[j][i]

# print(lines[0][0])
# print(lines[1][0])
# print(lines[2][0])

# print(lines, end="")