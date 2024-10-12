import sys;input = sys.stdin.readline
from collections import deque
n = int(input())
meeting = list()
for _ in range(n) :
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting.sort(key= lambda x: (x[1], x[0]))
meeting = deque(meeting)
cnt = 0
last_end = 0
while meeting :
    start, end = meeting.popleft()
    if last_end <= start :
        cnt += 1
        last_end = end
print(cnt)