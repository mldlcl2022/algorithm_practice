import sys;input = sys.stdin.readline
from collections import deque
q = deque([])
for _ in range(int(input())) :
    operation = list(input().split())
    if operation[0] == 'push' : q.append(int(operation[1]))
    elif operation[0] == 'pop' :
        if len(q) == 0 : print(-1)
        else : print(q.popleft())
    elif operation[0] == 'size' : print(len(q))
    elif operation[0] == 'empty' :
        if len(q) == 0 : print(1)
        else : print(0)
    elif operation[0] == 'front' :
        if len(q) == 0 : print(-1)
        else : print(q[0])
    elif operation[0] == 'back' :
        if len(q) == 0 : print(-1)
        else : print(q[-1])