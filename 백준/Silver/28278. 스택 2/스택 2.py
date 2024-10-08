import sys;input = sys.stdin.readline
stack = []
for _ in range(int(input())) :
    o = input().rstrip()
    
    if o.split()[0] == '1' : stack.append(int(o.split()[1]))
    elif o == '2' :
        if len(stack) != 0 : print(stack.pop())
        else : print(-1)
    elif o == '3' : print(len(stack))
    elif o == '4' :
        if len(stack) == 0 : print(1)
        else : print(0)
    elif o == '5' :
        if len(stack) != 0 : print(stack[-1])
        else : print(-1)