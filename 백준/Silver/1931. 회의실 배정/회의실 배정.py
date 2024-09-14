l = []
for _ in range(int(input())) :
    l.append(list(map(int, input().split())))

tmp = 0
total = 0
sorted_l = sorted(l, key= lambda x: (x[1], x[0]))
for start, end in sorted_l :
    if tmp <= start : 
        total += 1
        tmp = end
print(total)