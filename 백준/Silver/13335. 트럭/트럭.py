import sys;input = sys.stdin.readline
from collections import deque
n,w,l = map(int, input().split())
trucks = deque(list(map(int, input().split())))

cnt = 0
on = deque([0]*w)
while on :
    cnt += 1
    on.popleft()
    if trucks :
        if sum(on)+trucks[0] > l : on.append(0)
        else : on.append(trucks.popleft())
print(cnt)