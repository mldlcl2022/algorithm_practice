def solution(s):
    stack = []
    result = True
    for i in list(s) :
        if i == '(' : stack.append(i)
        else :
            if len(stack) == 0 and i == ')' : result = False
            else : stack.pop()
    if len(stack) != 0 : result = False
    return result