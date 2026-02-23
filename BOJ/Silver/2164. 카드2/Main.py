import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

q = deque()
temp = deque()
for i in range(1, n + 1):
    q.append(i)

while len(q) != 1:
    if not temp:
        temp.append(q.popleft())
    else:
        q.append(q.popleft())
        temp.pop()
        
print(q[-1])