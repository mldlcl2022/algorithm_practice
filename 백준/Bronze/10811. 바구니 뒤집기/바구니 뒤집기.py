n,m = map(int, input().split())
b = [i+1 for i in range(n)]
for _ in range(m) :
    i,j = map(int, input().split())
    b[i-1:j] = [b[i] for i in range(j-1,i-2,-1)]
for i in b :
    print(i, end= ' ')