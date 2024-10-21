import sys;input = sys.stdin.readline
from collections import deque
n = int(input())
cards = deque([i for i in range(1,n+1)])
result = []
while cards :
    result.append(cards.popleft())
    if len(cards) == 0 : break
    else : cards.append(cards.popleft())
print(' '.join(map(str, result)))