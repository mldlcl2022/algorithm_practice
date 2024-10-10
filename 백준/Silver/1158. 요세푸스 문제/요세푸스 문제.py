from collections import deque

n,k = map(int, input().split())
queue = deque(range(1,n+1))
result = deque()
print('<', end= '')
while True :
    if len(queue) == 1 : print(f'{queue.popleft()}>');break
    else :
        queue.rotate(-(k-1))
        print(f'{queue.popleft()}, ', end= '')