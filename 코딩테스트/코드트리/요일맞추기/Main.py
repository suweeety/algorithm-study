m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_total_days(m, d):
    pass
    total = 0
    for i in range(1, m):
        total += num_of_days[i]
    total += d
    return total

diff = get_total_days(m2, d2) - get_total_days(m1, d1)

week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print(week[diff % 7])