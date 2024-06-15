m = []
for _ in range(9) :
    m.append(list(map(int, input().split()))[:9])
row, col = 0, 0
value = 0
for i in range(9) :
    for j in range(9) :
        if value <= m[i][j] :
            row = i+1;col = j+1
            value = m[i][j]
        else : pass
print(value)
print(row, col)