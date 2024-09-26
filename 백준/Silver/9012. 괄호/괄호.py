import sys;input = sys.stdin.readline
for _ in range(int(input())) :
    ps = input().rstrip()
    s = []
    for p in ps :
        if p == '(' : s.append(1)
        elif p == ')' : s.append(-1)
        if sum(s) < 0 : break
    if sum(s) == 0 : print('YES')
    else : print('NO')