import sys;input = sys.stdin.readline
n = int(input())
p = list(map(int, input().split()))
stack = []
current = 1
for i in range(n) :
    stack.append(p[i])
    while stack and stack[-1] == current :
        stack.pop()
        current += 1
if stack : print('Sad')
else : print('Nice')