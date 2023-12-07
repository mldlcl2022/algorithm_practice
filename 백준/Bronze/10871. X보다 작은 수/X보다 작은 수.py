# enter n, x
n, x = map(int, input().split())

# number list
a = list(map(int, input().split()))[:n]

# result
for i in a :
    if i < x : print(i, end=' ')