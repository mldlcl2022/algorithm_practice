m = []
for _ in range(5) :
    m.append(list(input()))
for i in range(max([len(m[i]) for i in range(len(m))])) :
    for j in range(len(m)) :
        try : print(m[j][i], end= '')
        except : pass