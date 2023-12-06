# enter a, b, c
A, B, C = map(int, input().split())

# results
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)