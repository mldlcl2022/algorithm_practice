import sys;input = sys.stdin.readline
from collections import deque
for _ in range(int(input())) :
    n,m = map(int, input().split())
    importance_list = list(map(int, input().split()))
    queue = deque([(importance, order) for order, importance in enumerate(importance_list)])

    cnt = 0
    search_paper = importance_list[m]
    while queue :
        importance, order = queue.popleft()
        if len(queue) == 0 : cnt += 1
        elif importance < max(queue)[0] : queue.append((importance, order))
        elif importance >= max(queue)[0] :
            if importance == search_paper and order == m : cnt += 1;break
            else : cnt += 1
    print(cnt)