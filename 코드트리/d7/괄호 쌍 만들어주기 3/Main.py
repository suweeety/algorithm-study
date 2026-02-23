arr = input()

# Please write your code here.
open = 0
sum_v = 0
for char in arr:
    if char == '(':
        open += 1
    elif char == ')':
        sum_v += open
print(sum_v)