import sys;input = sys.stdin.readline
from collections import deque
for _ in range(int(input())) :
    n,m = map(int, input().split())
    queue = deque([(importance, idx) for idx, importance in enumerate(list(map(int, input().split())))])
    paper = queue[m][0]
    order = 0
    while True :
        if queue[0][0] < max(queue)[0] :
            queue.append(queue.popleft())
        else :
            importance, idx = queue.popleft()
            if idx == m : order += 1;break
            else : order += 1
    print(order)