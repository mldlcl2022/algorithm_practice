for i in range(int(input())) :
    stack = list(input().split())
    print(f'Case #{i+1}: ', end= '')
    while len(stack) > 1 :
        print(stack.pop(), end= ' ')
    print(stack.pop())