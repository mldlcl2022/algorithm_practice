# import sys;input = sys.stdin.readline
from collections import deque
n,k = map(int, input().split())
q = deque(list(range(1,n+1)))
result = []
while q :
    q.rotate(-(k-1))
    result.append(str(q.popleft()))
print('<', ', '.join(result)[:], '>', sep='')