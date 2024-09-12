from collections import deque

n,k = map(int, input().split())
queue = deque([i for i in range(1,n+1)])    

idx = 0
result = deque()
while True :
    idx += 1
    pop_num = queue.popleft()
    if idx % k == 0 :
        result.append(pop_num)
    else :
        queue.append(pop_num)
    if len(queue) == 0 :
        break
for i,r in enumerate(result) :
    if i == 0 : print('<', end= '')
    print(r, end= '')
    if (i+1) == len(result) : print('>', end= '')
    else : print(', ', end= '')