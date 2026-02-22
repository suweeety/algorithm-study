x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
offset = 1001
arr = [[0] * 2001 for _ in range(2001)]

# 첫번째 - 1채우기
for i in range(x1[0] + offset, x2[0] + offset):
    for j in range(y1[0] + offset, y2[0] + offset):
        arr[i][j] = 1
# 두번째 - 0지우기
for i in range(x1[1] + offset, x2[1] + offset):
    for j in range(y1[1] + offset, y2[1] + offset):
        arr[i][j] = 0
# 남아있는 거
min_x, max_x = 2001, 0
min_y, max_y = 2001, 0
result = False

for i in range(x1[0] + offset, x2[0] + offset):
    for j in range(y1[0] + offset, y2[0] + offset):
        if arr[i][j] == 1:
            result = True
            if i < min_x: min_x = i
            if i > max_x: max_x = i
            if j < min_y: min_y = j
            if j > max_y: max_y = j

# 5. 결과 출력
if not result:
    print(0)
else:
    # (max_x - min_x + 1)은 칸의 개수이므로 직사각형의 한 변의 길이가 됩니다.
    width = (max_x - min_x + 1)
    height = (max_y - min_y + 1)
    print(width * height)