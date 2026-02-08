import sys
import math

input = sys.stdin.readline

a, b, v = map(int, input().split())

# 공식 : (v-b) / (a-b)
# 반올림~!
r = math.ceil((v-b) / (a-b))

print(r)