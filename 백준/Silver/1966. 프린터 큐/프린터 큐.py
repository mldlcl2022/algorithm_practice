# try 1 : fail
from collections import deque

for _ in range(int(input())) :
    n,m = map(int, input().split())
    importance = [[j,i] for i,j in enumerate(list(map(int, input().split())))]
    queue = deque(importance)
    num = importance[m][0]
    th = 0
    while True :
        if queue[0][0] < max(queue)[0] :
            pop_num = queue.popleft()
            queue.append(pop_num)
        else :
            pop_num = queue.popleft()
            th += 1
            if len(queue) == 0 : print(th);break
            else :
                if pop_num[0] == num and pop_num[1] == m : print(th);break
                else : continue