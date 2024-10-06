import sys;input = sys.stdin.readline
from collections import deque
m = []
for _ in range(int(input())) :
    s, e = map(int, input().split())
    m.append((s,e))

tmp = 0
total = 0
sorted_m = sorted(m, key= lambda x: (x[1], x[0]))
for start, end in sorted_m :
    if tmp <= start :
        total += 1
        tmp = end
print(total)