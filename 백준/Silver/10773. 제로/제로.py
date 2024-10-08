import sys;input = sys.stdin.readline
s = []
for _ in range(int(input())) :
    num = int(input())
    if num != 0 : s.append(num)
    else :
        if len(s) != 0 : s.pop()
        else : pass
print(sum(s))