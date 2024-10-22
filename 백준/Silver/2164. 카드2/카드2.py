import sys;input = sys.stdin.readline
from collections import deque
n = int(input())
cards = deque(list(range(1,n+1)))

while cards :
    pop_card = cards.popleft()
    if len(cards) == 0 : print(pop_card)
    else :
        cards.append(cards.popleft())