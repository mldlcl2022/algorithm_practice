# enter total_price
x = int(input())

# enter n
n = int(input())

# price
p = 0

# calculate price
for i in range(n) :
    # enter a, b
    a, b = map(int, input().split())
    # price
    p += (a*b)

# check
if x == p : print('Yes')
else : print('No')