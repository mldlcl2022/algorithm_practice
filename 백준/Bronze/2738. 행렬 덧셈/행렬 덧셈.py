n,m = map(int, input().split())
m1 = [];m2 = []
result = []
for i in range(n*2) :
    if i < n : m1.append(list(map(int, input().split()))[:m])
    else : m2.append(list(map(int, input().split()))[:m])
for i in range(n) :
    for j in range(m) :
        print(m1[i][j]+m2[i][j], end= ' ')
    print()