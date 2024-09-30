import sys;input = sys.stdin.readline
n = int(input())
histogram = []
for _ in range(n) :
    histogram.append(int(input()))
histogram.append(0)

stack = []
result = 0
width, length = 0, 0
for i in range(n+1) :
    if i == 0 : stack.append((i, histogram[i]))
    width = i
    while stack and stack[-1][1] > histogram[i] :
        width, length = stack.pop()
        result = max(result, (i-width)*length)
    stack.append((width, histogram[i]))
print(result)