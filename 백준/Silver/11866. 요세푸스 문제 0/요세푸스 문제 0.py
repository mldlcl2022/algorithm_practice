import sys;input = sys.stdin.readline
from collections import deque
n, k = map(int, input().split())
queue = deque(list(range(1,n+1)))
idx = 1
result = []
while queue :
    if idx == k :
        idx = 1
        result.append(str(queue.popleft()))
    else :
        idx += 1
        queue.append(queue.popleft())
print('<',', '.join(result), '>', sep= '')