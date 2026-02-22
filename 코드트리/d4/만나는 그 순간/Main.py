n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(time)

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(time)

# Please write your code here.
count = 0
person1 = []
person2 = []
curr = 0
for i in range(n):
    for j in range(int(t[i])):
        if d[i] == 'R':
            curr += 1
            count += 1
            person1.append(curr)
        elif d[i] == 'L':
            curr -= 1
            count += 1
            person1.append(curr)
count = 0
curr = 0
for i in range(m):
    for j in range(int(t2[i])):
        if d2[i] == 'R':
            curr += 1
            count += 1
            person2.append(curr)
        elif d2[i] == 'L':
            curr -= 1
            count += 1
            person2.append(curr)
result = False
for i in range(len(person1)):
    if person1[i] == person2[i]:
        result = True
        print(i+1)
        break

if not result:
    print(-1)