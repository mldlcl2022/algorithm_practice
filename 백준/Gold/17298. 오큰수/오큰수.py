import sys;input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

result = [-1]*n
stack = [0]
for i in range(1,n) :
    while stack and a[stack[-1]] < a[i] :
        result[stack.pop()] = a[i]
    stack.append(i)
print(*result)