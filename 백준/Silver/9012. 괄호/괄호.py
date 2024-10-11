import sys;input = sys.stdin.readline
for _ in range(int(input())) :
    s = input().rstrip()
    stack = []
    for p in s :
        if p == '(' : stack.append(p)
        else :
            if len(stack) == 0 : stack.append(p)
            else :
                if stack[-1] == '(' : stack.pop()
                else : stack.append(p)
    if len(stack) == 0 : print('YES')
    else : print('NO')