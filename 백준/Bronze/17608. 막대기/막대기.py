# 시간 초과과
import sys;input = sys.stdin.readline
n = int(input())
bars = []
for i in range(n) :
    h = int(input())
    bars.append(h)

cnt = 0
current = 0
for _ in range(len(bars)) :
    pop_h = bars.pop()
    if current < pop_h :
        current = pop_h
        cnt += 1
print(cnt)