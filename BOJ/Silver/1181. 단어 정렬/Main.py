stack = [[] for _ in range(51)]

for i in range(int(input())):
    arr = input()
    if arr not in stack[len(arr)]:
        stack[len(arr)].append(arr)

for i in range(len(stack)):
    if stack[i]:
        stack[i].sort()
        for j in stack[i]:
            print(j)