import sys;input = sys.stdin.readline
while True :
    s = input().rstrip()
    if s == '.' : break
    stack = []
    for a in s :
        if a == '(' or a == '[' : stack.append(a)
        elif a == ')' :
            if len(stack) != 0 and stack[-1] != '[' : stack.pop()
            else : stack.append(')');break
        elif a == ']' :
            if len(stack) != 0 and stack[-1] != '(' : stack.pop()
            else : stack.append(']');break
    if len(stack) == 0 : print('yes')
    else : print('no')