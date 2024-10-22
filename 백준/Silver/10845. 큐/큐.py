import sys;input = sys.stdin.readline
n = int(input())
queue = []
for _ in range(n) :
    order = input().rstrip()
    if order.split()[0] == 'push' : queue.append(int(order.split()[1]))
    elif order == 'pop' :
        if len(queue) == 0 : print(-1)
        else : print(queue.pop(0))
    elif order == 'size' : print(len(queue))
    elif order == 'empty' :
        if len(queue) == 0 : print(1)
        else : print(0)
    elif order == 'front' :
        if len(queue) == 0 : print(-1)
        else : print(queue[0])
    elif order == 'back' :
        if len(queue) == 0 : print(-1)
        else : print(queue[-1])