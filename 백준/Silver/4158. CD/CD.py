import sys;input = sys.stdin.readline
from bisect import bisect_left
while True :
    n,m = map(int, input().split())
    if n == 0 and m == 0 : break
    sg = [];sy = []
    for _ in range(n) :
        sg.append(int(input()))
    for _ in range(m) :
        sy.append(int(input()))

    cnt = 0
    sg.sort();sy.sort()
    for i in range(n) :
        if sg[i] == sy[bisect_left(sy, sg[i])] : cnt += 1
        else : continue
    print(cnt)