import sys;input = sys.stdin.readline
n = int(input())
b = [int(input()) for _ in range(n)]

cnt = 0
stack = []
for f in b :
    while stack and stack[-1] <= f : stack.pop()
    stack.append(f)
    cnt += len(stack)-1
print(cnt)