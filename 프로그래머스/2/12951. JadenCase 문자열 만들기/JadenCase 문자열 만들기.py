def solution(s):
    stack = []
    word = str()
    for i in list(s) :
        if i != ' ' : word = word + i
        elif i == ' ' :
            stack.append(word)
            stack.append(' ')
            word = str()
    stack.append(word)
    return ''.join([i.upper()[:1]+i[1:].lower() for i in stack])