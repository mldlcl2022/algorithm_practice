import sys;input = sys.stdin.readline
s = []
for _ in range(int(input())) :
    n = int(input())
    if n != 0 : s.append(n)
    else : s.pop()
print(sum(s))