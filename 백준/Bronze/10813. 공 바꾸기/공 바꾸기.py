n,m = map(int, input().split())
b = [i+1 for i in range(n)]
for _ in range(m) :
    i,j = map(int, input().split())
    tmp = b[i-1]
    b[i-1] = b[j-1]
    b[j-1] = tmp
for c in b :
    print(c, end= ' ')