n = []

for i in range(9):
    n.append(int(input()))

max = 0
index = 0

for i in range(len(n)):
    if max < n[i]:
        max = n[i]
        index = i + 1

print(max)
print(index)