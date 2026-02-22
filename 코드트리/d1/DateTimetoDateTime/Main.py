a, b, c = map(int, input().split())

# Please write your code here.
time = 0
day = 11
h = 11
m = 11

while True:
    if a < 11:
        time = -1
        break
    elif a == 11:
        if b < 11:
            time = -1
            break
        elif b == 11:
            if c < 11:
                time = -1
                break

    if day == a and h == b and m == c:
        break
    
    time += 1
    m += 1

    if m == 60:
        h += 1
        m = 0
    elif h == 24:
        day += 1
        h = 0

print(time)