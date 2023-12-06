# enter a, b
a, b = map(int, input().split())

# result
if   a > b  : print('>')
elif a < b  : print('<')
elif a == b : print('==')