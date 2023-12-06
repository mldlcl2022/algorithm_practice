# enter t
t = int(input())

# result
for i in range(t) :
    # enter a, b
    a, b = map(int, input().split())
    # print
    print('Case #{:.0f}: {:.0f}'.format(i+1,a+b))