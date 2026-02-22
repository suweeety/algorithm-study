# 1. 색종이의 개수 N을 입력받습니다.
n = int(input())

# 2. N개의 좌표 쌍을 입력받아 리스트에 튜플 형태로 저장합니다.
# 예: [(0, 0), (4, 0), (0, 4)]
points = [tuple(map(int, input().split())) for _ in range(n)]

# 3. zip(*)을 사용하여 (x, y) 튜플 묶음을 x끼리, y끼리 분리합니다.
# points가 [(0, 0), (4, 0)] 이라면, zip의 결과는 (0, 4)와 (0, 0)이 됩니다.
x, y = zip(*points)

# 4. 튜플 형태인 x, y 데이터를 수정하기 편하도록 리스트로 변환합니다.
x, y = list(x), list(y)

# --- 여기서부터 추가된 코드입니다 ---

# 5. 도화지 역할을 할 2차원 리스트를 만듭니다. (가로 200, 세로 200 크기)
# 모든 칸을 0으로 초기화합니다.
paper = [[0] * 200 for _ in range(200)]

# 6. 각 색종이의 좌표를 하나씩 꺼내어 도화지에 표시합니다.
for i in range(n):
    # 배열의 인덱스는 음수가 될 수 없으므로, -100~100 범위를 0~200으로 변환하기 위해 100을 더합니다.
    start_x = x[i] + 100
    start_y = y[i] + 100
    
    # 색종이 크기인 8x8 영역을 순회하며 1을 채웁니다.
    for dx in range(8):
        for dy in range(8):
            # 이미 1이 써져 있는 곳(중복 영역)에 다시 1을 써도 
            # 값은 그대로 1이기 때문에 중복 계산이 자동으로 방지됩니다.
            paper[start_x + dx][start_y + dy] = 1

# 7. 도화지 전체에서 1이 적힌 칸의 개수를 모두 더해 총 넓이를 구합니다.
total_area = 0
for row in paper:
    total_area += sum(row)

# 8. 최종 넓이를 출력합니다.
print(total_area)