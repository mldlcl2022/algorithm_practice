import sys;input = sys.stdin.readline
from collections import deque
n = int(input())
cards = deque(list(range(1,n+1)))

for i in range(len(cards)-1) :
    cards.popleft()
    cards.append(cards.popleft())
print(cards[0])