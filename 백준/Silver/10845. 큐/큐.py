from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
dq = deque()

for _ in range(n):
    command = list(input().split())
    if command[0] == 'push':
        dq.append(command[1])
    elif command[0] == 'pop':
        try:
            print(dq.popleft())
        except:
            print(-1)
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if len(dq) > 0:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        try:
            print(dq[0])
        except:
            print(-1)
    elif command[0] == 'back':
        try:
            print(dq[-1])
        except:
            print(-1)
