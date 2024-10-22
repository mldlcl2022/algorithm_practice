import sys;input = sys.stdin.readline
from collections import deque
n = int(input())
cards = deque(list(range(1,n+1)))

for i in range(len(cards)) :
    pop_card = cards.popleft()
    if len(cards) == 0 : print(pop_card);break
    else :
        cards.append(cards.popleft())