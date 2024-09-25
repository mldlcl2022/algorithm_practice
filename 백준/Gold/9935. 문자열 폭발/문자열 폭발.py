import sys;input = sys.stdin.readline
s1 = input().rstrip()
s2 = input().rstrip()

stack = []
for i in range(len(s1)) :
    stack.append(s1[i])
    if ''.join(stack[-len(s2):]) == s2 :
        for _ in range(len(s2)) :
            stack.pop()
if stack : print(''.join(stack))
else : print('FRULA')