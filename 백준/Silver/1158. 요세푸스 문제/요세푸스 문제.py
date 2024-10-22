import sys;input = sys.stdin.readline
from collections import deque
n,k = map(int, input().split())
l = deque(list(range(1,n+1)))
result = []
while l :
    l.rotate(-(k-1))
    result.append(str(l.popleft()))
print('<'+', '.join(result)+'>')