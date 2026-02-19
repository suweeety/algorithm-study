n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
# 1. A의 매 초 시점 위치 기록
pos_a = [0]
curr_a = 0
for i in range(n):
    # 방향에 따라 이동 수치 결정
    move_val = 0
    if d[i] == 'R':
        move_val = 1
    else:
        move_val = -1
    
    # 시간(t)만큼 반복하며 위치 저장
    for _ in range(t[i]):
        curr_a += move_val
        pos_a.append(curr_a)

# 2. B의 매 초 시점 위치 기록
pos_b = [0]
curr_b = 0
for i in range(m):
    # 방향에 따라 이동 수치 결정
    move_val_b = 0
    if d_b[i] == 'R':
        move_val_b = 1
    else:
        move_val_b = -1
        
    for _ in range(t_b[i]):
        curr_b += move_val_b
        pos_b.append(curr_b)

# 3. 움직임이 끝난 후에도 자리에 머물도록 리스트 길이 맞추기
len_a = len(pos_a)
len_b = len(pos_b)

if len_a < len_b:
    for _ in range(len_b - len_a):
        pos_a.append(pos_a[-1])
elif len_b < len_a:
    for _ in range(len_a - len_b):
        pos_b.append(pos_b[-1])

# 4. "직전에는 다르고, 현재는 같은" 횟수 카운트
ans = 0
total_time = len(pos_a)
for i in range(1, total_time):
    # i-1초(직전)와 i초(현재)를 비교
    if pos_a[i-1] != pos_b[i-1]:
        if pos_a[i] == pos_b[i]:
            ans += 1

print(ans)