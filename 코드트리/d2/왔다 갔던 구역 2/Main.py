n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
checked = [0] * 2000

# # 0의 위치를 배열의 한가운데로 정한다. 이를 OFFSET이라함
# offset = 1000
curr = 0

for i in range(n):
    distance = x[i]
    direction = dir[i]

    if direction == 'R':
        for j in range(curr, curr + distance):
            checked[j] += 1
        curr += distance
    else:
        for j in range(curr - distance, curr):
            checked[j] += 1
        curr -= distance

ans = 0
for i in checked:
    if i >= 2:
        ans += 1

print(ans)