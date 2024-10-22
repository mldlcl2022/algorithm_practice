import sys;input = sys.stdin.readline
from collections import deque
t = int(input())
for _ in range(t) :
    n,m = map(int, input().split())
    importances = deque([(importance, index) for index, importance in enumerate(list(map(int, input().split())))])
    
    cnt = 0
    paper = importances[m][0]
    while importances :
        pop = importances.popleft()
        if len(importances) == 0 : cnt += 1
        elif pop[0] >= max(importances)[0] :
            if pop[0] == paper and pop[1] == m : cnt += 1;break
            else : cnt += 1
        elif pop[0] < max(importances)[0] : importances.append(pop)
    print(cnt)