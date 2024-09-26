import sys;input = sys.stdin.readline
stack = []
for _ in range(int(input())) :
    operation = input().rstrip()
    if int(operation.split()[0]) == 1 : stack.append(int(operation.split()[1]))
    elif int(operation.split()[0]) == 2 :
        try : print(stack.pop())
        except : print(-1)
    elif int(operation.split()[0]) == 3 : print(len(stack))
    elif int(operation.split()[0]) == 4 :
        if len(stack) == 0 : print(1)
        else : print(0)
    elif int(operation.split()[0]) == 5 :
        try : print(stack[-1])
        except : print(-1)