l = []
for _ in range(10) :
    l.append(int(input()))
print(len(set([num%42 for num in l])))