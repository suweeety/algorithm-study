n = int(input())
member_list = []
for i in range(n):
    age, name = input().split()
    member_list.append((int(age), i, name))

member_list.sort()

for member in member_list:
    print(member[0], member[2])