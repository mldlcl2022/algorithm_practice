import sys;input = sys.stdin.readline
buildings = []
for _ in range(int(input())) :
    buildings.append(int(input()))

stack = []
result = 0
for floor in buildings : 
    while stack and stack[-1] <= floor :
        stack.pop()
    stack.append(floor)
    result += len(stack) - 1
print(result)